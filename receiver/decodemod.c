/*
author: Lizhaoyi
date:2018/01/01
description: The kernel module at the receiver.
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
#define TOT_PACK 12
#define MAX_DATA_BUFFER 1460
#define TOT_DATA_BUFFER 14600
#define DST_PORT 23456
#define SRC_IP "192.168.188.136"
#define DST_IP "192.168.188.133"


unsigned char SMAC[ETH_ALEN] = {0x00,0x0C,0x29,0x7E,0xB1,0x35};
unsigned char DMAC[ETH_ALEN] = {0x00,0x0C,0x29,0x18,0xE7,0x78};
unsigned char FLAG_MAP[TOT_PACK+1];
unsigned char TMP_BUFFER[TOT_DATA_BUFFER];
unsigned int  count = 0;
unsigned int seqn = 0;

int syph = 0;

struct tempdata{
	unsigned char DATA_BUFFER[MAX_DATA_BUFFER];
	unsigned int lenth;
}TEMPDATA[TOT_PACK+1];

MODULE_LICENSE("GPL");
MODULE_AUTHOR("lzy");


int deal_skb(struct sk_buff* skb)
{
	syph = 1;
	struct ethhdr* omac_hdr;
    	struct iphdr* oip_hdr;
    	unsigned int oip_hdr_off;
	struct tcphdr* otcp_hdr;
    	unsigned int otcp_hdr_off;
	unsigned int label;
	unsigned char* opayload;
	unsigned int opayload_len;

	omac_hdr = (struct ethhdr*)skb_mac_header(skb);
	oip_hdr = (struct iphdr*)((void *)omac_hdr+ETH_HLEN);
	oip_hdr_off = oip_hdr->ihl << 2;
	otcp_hdr = (struct tcphdr *)((void *)oip_hdr + oip_hdr_off);
	otcp_hdr_off = otcp_hdr->doff << 2;
	opayload = (unsigned char*)((void *)otcp_hdr+otcp_hdr_off);
	opayload_len = skb->len - oip_hdr_off - otcp_hdr_off;

	label = otcp_hdr->res1;
	if(label == 0) return 1;
	if(label == 1){
		seqn = otcp_hdr->seq;
		printk("flow start \n");
	}

	if(label <= ORG_PACK){ //if recv original pack
		if(FLAG_MAP[label] == 0){
			memcpy(TEMPDATA[label].DATA_BUFFER,opayload,opayload_len);
			TEMPDATA[label].lenth = opayload_len;
			FLAG_MAP[label] = 1;
			count++;

			int orgpack = label%2 ? label+1 : label-1;
    		int codepack = (label+1)>>1 + ORG_PACK;
    		if(FLAG_MAP[codepack] && !FLAG_MAP[orgpack]){
    			//decode
				int tmp_len = TEMPDATA[codepack].lenth;
				int i=0;
				printk("decode begin\n");
    			for(i=0; i<tmp_len; i++){
    				TEMPDATA[orgpack].DATA_BUFFER[i] = TEMPDATA[codepack].DATA_BUFFER[i] ^ TEMPDATA[label].DATA_BUFFER[i];
    			}
				TEMPDATA[orgpack].lenth = tmp_len;
   		 		FLAG_MAP[orgpack] = 1;
    			count++;
				printk("decode end\n");
        	}
		}else{  //update pack length
			TEMPDATA[label].lenth = opayload_len;
			return 1;
		}
	}else{
		int orgp2 = (label-ORG_PACK)<<1;
		int orgp1 = orgp2-1;
		if(FLAG_MAP[orgp1] && FLAG_MAP[orgp2]){
			;
		}else{
			memcpy(TEMPDATA[label].DATA_BUFFER,opayload,opayload_len);
			TEMPDATA[label].lenth = opayload_len;
			FLAG_MAP[label] = 1;
			//decode
			printk("decode begin\n");
			if(FLAG_MAP[orgp1] && !FLAG_MAP[orgp2]){ //recv orgp1 and not recv orgp2
				int i=0;
            	for(i=0; i<TEMPDATA[label].lenth; i++){
            		TEMPDATA[orgp2].DATA_BUFFER[i] = TEMPDATA[label].DATA_BUFFER[i] ^ TEMPDATA[orgp1].DATA_BUFFER[i];
            	}
				TEMPDATA[orgp2].lenth = TEMPDATA[label].lenth;
                FLAG_MAP[orgp2] = 1;
                count++;
			}
			if(!FLAG_MAP[orgp1] && FLAG_MAP[orgp2]){ //not recv orgp1 and recb orgp1
                //decode
				int i=0;
				for(i=0; i<TEMPDATA[label].lenth; i++){
					TEMPDATA[orgp1].DATA_BUFFER[i] = TEMPDATA[label].DATA_BUFFER[i] ^ TEMPDATA[orgp2].DATA_BUFFER[i];
				}
				TEMPDATA[orgp1].lenth = TEMPDATA[label].lenth;
                FLAG_MAP[orgp1] = 1;
                count++;
			}
			printk("decode end\n");
		}

	}

	syph = 0;
	return 0;
}

int modify_expand_skb(struct sk_buff* skb)
{

	struct ethhdr* nmac_hdr;
    	struct iphdr* nip_hdr;
    	unsigned int nip_hdr_off;
    	struct tcphdr* ntcp_hdr;
    	unsigned int ntcp_hdr_off;
	unsigned int label;
    	unsigned char* npayload;
	unsigned int npayload_len;

//get TMP_BUFFER
	int i=0;
	int j=0;
	int last_p = 0;
	for(i=1; i<=ORG_PACK; i++){
		memcpy(TMP_BUFFER+last_p, TEMPDATA[i].DATA_BUFFER, TEMPDATA[i].lenth);
		last_p += TEMPDATA[i].lenth;
	}


//expand packet
	pskb_expand_head(skb,0,last_p,GFP_ATOMIC);

	nmac_hdr = (struct ethhdr*)skb_mac_header(skb);
	nip_hdr = (struct iphdr*)((void *)nmac_hdr+ETH_HLEN);
	nip_hdr_off = nip_hdr->ihl << 2;
	ntcp_hdr = (struct tcphdr *)((void *)nip_hdr + nip_hdr_off);
	ntcp_hdr_off = ntcp_hdr->doff << 2;
	npayload = (unsigned char*)((void *)ntcp_hdr+ntcp_hdr_off);
	npayload_len = skb->len - nip_hdr_off - ntcp_hdr_off;


	unsigned char* tmp_p = (void *)skb_put(skb,last_p-npayload_len) - npayload_len;

	memcpy(tmp_p,TMP_BUFFER,last_p);

	ntcp_hdr->res1 = 0;
//modify seq number
	if(seqn) ntcp_hdr->seq = seqn;

//update check csum
	ntcp_hdr->check = 0;
    	skb->csum = csum_partial((unsigned char *)ntcp_hdr,  ntohs(nip_hdr->tot_len) +last_p-npayload_len- nip_hdr_off,0);
    	ntcp_hdr->check = csum_tcpudp_magic(nip_hdr->saddr,
                        nip_hdr->daddr,
                        ntohs(nip_hdr->tot_len)+last_p-npayload_len - nip_hdr_off,nip_hdr->protocol,
                        skb->csum);
    	nip_hdr->check = 0;
    	nip_hdr->check = ip_fast_csum(nip_hdr,nip_hdr->ihl);

	return 1;
}


bool check_pack(struct sk_buff* skb)
{
	if(skb == NULL){ return 0; }
	struct ethhdr* omac_hdr;
	struct iphdr* oip_hdr;
    	unsigned int oip_hdr_off;
    	struct tcphdr* otcp_hdr;
    	unsigned int otcp_hdr_off;

	omac_hdr = (struct ethhdr*)skb_mac_header(skb);

	oip_hdr = (struct iphdr*)((void *)omac_hdr+ETH_HLEN);
    	oip_hdr_off = oip_hdr->ihl << 2;

	otcp_hdr = (struct tcphdr *)((void *)oip_hdr + oip_hdr_off);
	otcp_hdr_off = otcp_hdr->doff << 2;

	if(oip_hdr->protocol != IPPROTO_TCP){
	//	printk("not TCP \n");
		return 0;
	}
	if(oip_hdr->saddr != in_aton(SRC_IP)){
		printk("not SRC_IP \n");
		return 0;
	}
	if(otcp_hdr->dest != htons(DST_PORT)){
		printk("not DST_PORT \n");
		return 0;
	}

	if(otcp_hdr->syn || otcp_hdr->fin || otcp_hdr->rst || otcp_hdr->urg){
		printk("is SYN or FIN or RST or or URG \n");
		return 0;
	}

	if(skb->len - otcp_hdr_off - oip_hdr_off <=0 || otcp_hdr->res1 == 0){
		//printk("no payload,payload_len: %d \n",skb->len - otcp_hdr_off - oip_hdr_off);
		return 0;
	}

	return 1;
}

unsigned int decodemod(unsigned int hooknum,
	struct sk_buff* skb,
    	const struct net_device *in,
    	const struct net_device *out,
    	int (*okfn)(struct sk_buff*))
{


    if(check_pack(skb) && count < ORG_PACK){
		if(deal_skb(skb)){
			return NF_DROP;
		}
		if(count >= ORG_PACK){

			modify_expand_skb(skb);
			printk("flow finish \n");
		//clear var
			seqn = 0;
			count = 0;
			memset(TEMPDATA,0,sizeof(TEMPDATA));
			memset(FLAG_MAP,0,sizeof(FLAG_MAP));
			memset(TMP_BUFFER,0,sizeof(TMP_BUFFER));

			return NF_ACCEPT;
		}

	}else{
		return NF_ACCEPT;
	//	printk("check_pack false \n");
	}

	return NF_DROP;


}


static struct nf_hook_ops decode_ops = {
                .hook                = decodemod,
                .owner               = THIS_MODULE,
                .pf                  = PF_INET,
                .hooknum             = NF_INET_LOCAL_IN,
                .priority            = NF_IP_PRI_FIRST,
};

static int __init init(void)
{
    	int ret;
    	ret = nf_register_hook(&decode_ops);
    	if (ret < 0) {
        	printk("http detect:can't register mac_ops detect hook!\n");
        	return ret;
    	}
    	printk("insmod mac_ops detect module\n");
    	return 0;
}

static void __exit fini(void)
{
    	nf_unregister_hook(&decode_ops);
    	printk("remove mac_ops detect module.\n");
}

module_init(init);
module_exit(fini);

