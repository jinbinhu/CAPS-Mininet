/*
Author: Lizhaoyi
Date:2018/01/01
Description: The kernel module at the sender.
*/


#include <linux/init.h>
#include <linux/module.h>
#include <linux/netfilter.h>
#include <linux/socket.h> /*PF_INET*/
#include <linux/netfilter_ipv4.h> /*NF_IP_PRE_FIRST*/
#include <linux/skbuff.h>
#include <linux/netdevice.h>
#include <linux/inet.h> /*in_aton()*/
#include <net/ip.h>
#include <net/tcp.h>
#include <linux/kernel.h>

#include <linux/if_ether.h>
#include <linux/if_packet.h>
#include <net/tcp.h>
#include <net/udp.h>
#include <net/icmp.h>

#define ETH "eth0"
#define ORG_PACK 8
#define MAX_DATA_BUFFER 1460
#define DST_PORT 23456
#define DST_IP "192.168.188.133"

unsigned char SMAC[ETH_ALEN] = {0x00,0x0C,0x29,0x7E,0xB1,0x35};
unsigned char DMAC[ETH_ALEN] = {0x00,0x0C,0x29,0x18,0xE7,0x78};
unsigned char DATA_BUFFER1[MAX_DATA_BUFFER];
unsigned char DATA_BUFFER2[MAX_DATA_BUFFER];
unsigned int  count = 0;
struct sk_buff* cpskb = NULL;

MODULE_LICENSE("GPL");
MODULE_AUTHOR("lzy");


int copy_send_nskb(struct sk_buff* skb,unsigned int label)
{
	struct net_device *dev;
	struct sk_buff* nskb;
   	struct iphdr* nip_hdr, *cpip_hdr, *oip_hdr;
	unsigned int nip_hdr_off, cpip_hdr_off, oip_hdr_off;
	struct tcphdr* ntcp_hdr, *cptcp_hdr, *otcp_hdr;
	unsigned int ntcp_hdr_off, cptcp_hdr_off, otcp_hdr_off;
	struct ethhdr* neth_hdr;
	int ret = 0;
	int buffer_len = 0;
	int odata_len = 0;
	int cpdata_len = 0;
	
	if(cpskb == NULL) return 0;


	oip_hdr = ip_hdr(skb);
	oip_hdr_off = oip_hdr->ihl << 2;
	otcp_hdr = (struct tcphdr *)((void *)oip_hdr + oip_hdr_off);
	otcp_hdr_off = otcp_hdr->doff << 2;

	cpip_hdr= ip_hdr(cpskb);
	cpip_hdr_off= cpip_hdr->ihl << 2;
	cptcp_hdr = (struct tcphdr *)((void *)cpip_hdr + cpip_hdr_off);
	cptcp_hdr_off = cptcp_hdr->doff << 2;

	if(cpskb->len > skb->len){
		buffer_len = cpskb->len - cpip_hdr_off - cptcp_hdr_off;
		nskb = skb_copy(cpskb,GFP_ATOMIC);
	}else{
		buffer_len = skb->len - oip_hdr_off - otcp_hdr_off;
		nskb = skb_copy(skb,GFP_ATOMIC);
	}

	nip_hdr = ip_hdr(nskb);
	nip_hdr_off = nip_hdr->ihl << 2;
	ntcp_hdr = (struct tcphdr *)((void *)nip_hdr + nip_hdr_off);
	ntcp_hdr_off = ntcp_hdr->doff << 2;

//code
	memset(DATA_BUFFER1,0,sizeof(DATA_BUFFER1));
	memset(DATA_BUFFER2,0,sizeof(DATA_BUFFER2));

	memcpy(DATA_BUFFER1, (unsigned char*)((void *)otcp_hdr+otcp_hdr_off), skb->len - oip_hdr_off - otcp_hdr_off);
	memcpy(DATA_BUFFER2, (unsigned char*)((void *)cptcp_hdr+cptcp_hdr_off), cpskb->len - cpip_hdr_off - cptcp_hdr_off);

	int i=0;
	for(i=0; i<buffer_len; i++){
		DATA_BUFFER2[i] = DATA_BUFFER1[i]^DATA_BUFFER2[i];
	}



//modify nskb

	ntcp_hdr->res1 = (label>>1) + ORG_PACK;
	memcpy((unsigned char*)((void*)ntcp_hdr+ntcp_hdr_off), DATA_BUFFER2, buffer_len);

	nip_hdr->check = 0;
	nip_hdr->check = ip_fast_csum((unsigned char *)nip_hdr, nip_hdr->ihl);
	
	nskb->csum = 0;
	nskb->csum = csum_partial((unsigned char *)(ntcp_hdr + ntcp_hdr_off),
    	ntohs(nip_hdr->tot_len) - nip_hdr_off - ntcp_hdr_off, 0);

	ntcp_hdr->check = 0;
	ntcp_hdr->check = csum_tcpudp_magic(nip_hdr->saddr, nip_hdr->daddr,
    	ntohs(nip_hdr->tot_len) - nip_hdr_off, nip_hdr->protocol,
    	csum_partial((unsigned char *)ntcp_hdr, ntcp_hdr_off, nskb->csum));


	nskb->ip_summed = CHECKSUM_NONE;
	nskb->pkt_type  = PACKET_OTHERHOST;


	dev = dev_get_by_name(&init_net,ETH);
	nskb->dev = dev;
	if(nskb->dev==NULL){
       		kfree_skb(nskb);
        	return 0;
   	}

//eth headeri
	neth_hdr = (struct ethhdr *)skb_push (nskb, ETH_HLEN);
	memcpy (neth_hdr->h_dest, DMAC, ETH_ALEN);
	memcpy (neth_hdr->h_source, SMAC, ETH_ALEN);
	neth_hdr->h_proto = __constant_htons (ETH_P_IP);
	skb_reset_mac_header(nskb);

	dev_put(dev);
	ret = dev_queue_xmit(nskb);

	dev_put(dev);

	return 1;
}

void modify_skb(struct sk_buff* skb,unsigned int seqn)
{
	struct iphdr* oip_hdr;
	unsigned int oip_hdr_off;
	struct tcphdr* otcp_hdr;
	unsigned int otcp_hdr_off;



	oip_hdr = ip_hdr(skb);
	oip_hdr_off = oip_hdr->ihl << 2;

	otcp_hdr = (struct tcphdr *)((void *)oip_hdr + oip_hdr_off);
	otcp_hdr_off = otcp_hdr->doff << 2;

//modify_tcphd
	otcp_hdr->res1 = seqn;

	skb->csum = 0;
	skb->csum = csum_partial((unsigned char *)(otcp_hdr + otcp_hdr_off),
    	ntohs(oip_hdr->tot_len) - oip_hdr_off - otcp_hdr_off, 0);

	otcp_hdr->check = 0;
	otcp_hdr->check = csum_tcpudp_magic(oip_hdr->saddr, oip_hdr->daddr,
    	ntohs(oip_hdr->tot_len) - oip_hdr_off, oip_hdr->protocol,
    	csum_partial((unsigned char *)otcp_hdr, otcp_hdr_off, skb->csum));

	skb->ip_summed = CHECKSUM_NONE;

}

	bool check_pack(struct sk_buff* skb)
{
	if(skb == NULL){ return 0; }
	struct iphdr* oip_hdr;
	unsigned int oip_hdr_off;
	struct tcphdr* otcp_hdr;
	unsigned int otcp_hdr_off;


	oip_hdr = ip_hdr(skb);
	oip_hdr_off = oip_hdr->ihl << 2;

	otcp_hdr = (struct tcphdr *)((void *)oip_hdr + oip_hdr_off);
	otcp_hdr_off = otcp_hdr->doff << 2;

	if(oip_hdr->protocol != IPPROTO_TCP){
	//	printk("not TCP \n");
		return 0;
	}
	if(oip_hdr->daddr != in_aton(DST_IP)){
	//	printk("not DST_IP \n");
		return 0;
	}
	if(otcp_hdr->dest != htons(DST_PORT)){
	//	printk("not DST_PORT \n");
		return 0;
	}


	if(otcp_hdr->syn || otcp_hdr->fin || otcp_hdr->rst ||otcp_hdr->urg){
	//	printk("is SYN or FIN or RST or URG \n");
		return 0;
	}

	if(skb->len - oip_hdr_off - otcp_hdr_off <= 0){
	//	printk("no payload \n");
		return 0;
	}

	return 1;
}

unsigned int codemod(unsigned int hooknum,
	struct sk_buff* skb,
	const struct net_device *in,
	const struct net_device *out,
	int (*okfn)(struct sk_buff*))
{


	if(check_pack(skb)){
		if(count >= ORG_PACK) return NF_DROP;
	//	printk("check_pack true \n");
		count++;
		modify_skb(skb,count);
		if(count%2 == 0){
			copy_send_nskb(skb,count);
		}else{
			if(cpskb!=NULL) kfree_skb(cpskb);
			cpskb = skb_copy(skb,GFP_ATOMIC);
		}
		if(count >= ORG_PACK){
			if(cpskb!=NULL) kfree_skb(cpskb);
			count = 0;
	//		printk("send a flow success \n");
		}
	}else{
	//	printk("check_pack false \n");
	}


	return NF_ACCEPT;

}


static struct nf_hook_ops code_ops = {
                .hook                = codemod,
                .owner               = THIS_MODULE,
                .pf                  = PF_INET,
                .hooknum             = NF_INET_LOCAL_OUT,
                .priority            = NF_IP_PRI_FIRST,
};

static int __init init(void)
{
	int ret;
	ret = nf_register_hook(&code_ops);
	if (ret < 0) {
        	printk("http detect:can't register mac_ops detect hook!\n");
        	return ret;
    	}
    	printk("insmod mac_ops detect module\n");
    	return 0;
}

static void __exit fini(void)
{
    	nf_unregister_hook(&code_ops);
    	printk("remove mac_ops detect module.\n");
}

module_init(init);
module_exit(fini);

