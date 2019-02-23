#author: hujinbin
#date:2018/01/01
#description: create a topology

#!/usr/bin/python

import thread

from mininet.topo import Topo

from mininet.net import Mininet

from mininet.node import CPULimitedHost

from mininet.link import TCLink

from mininet.util import dumpNodeConnections

from mininet.log import setLogLevel

from mininet.node import Controller 

from mininet.cli import CLI

from functools import partial

from mininet.node import RemoteController

import os

import threadpool
 
import time,threading

from multiprocessing import Pool

flag=1

class MyTopo(Topo):

    "Single switch connected to n hosts."

    def __init__(self):

        Topo.__init__(self)
		
		#add switch

        s1=self.addSwitch('s1')

        s2=self.addSwitch('s2')

        s3=self.addSwitch('s3')

        s4=self.addSwitch('s4')

        s5=self.addSwitch('s5')

        s6=self.addSwitch('s6')

        s7=self.addSwitch('s7')

        s8 = self.addSwitch('s8')

        s9 = self.addSwitch('s9')

        s10 = self.addSwitch('s10')

        s11 = self.addSwitch('s11')

        s12 = self.addSwitch('s12')

        s13 = self.addSwitch('s13')

        s14 = self.addSwitch('s14')

        s15 = self.addSwitch('s15')

        s16 = self.addSwitch('s16')

        s17 = self.addSwitch('s17')

        s18 = self.addSwitch('s18')

        s19 = self.addSwitch('s19')

        s20 = self.addSwitch('s20')

        s21 = self.addSwitch('s21')

        s22 = self.addSwitch('s22')
		
		#add host

        h1=self.addHost('h1')

        h2=self.addHost('h2')

        h3=self.addHost('h3')

        h4=self.addHost('h4')

        h5=self.addHost('h5')

        h6=self.addHost('h6')

        h7 = self.addHost('h7')

        h8 = self.addHost('h8')

        h9 = self.addHost('h9')

        h10 = self.addHost('h10')

        h11 = self.addHost('h11')

        h12 = self.addHost('h12')

        h13 = self.addHost('h13')

        h14 = self.addHost('h14')

        h15 = self.addHost('h15')

        h16 = self.addHost('h16')

        h17 = self.addHost('h17')

        h18 = self.addHost('h18')

        h19 = self.addHost('h19')

        h20 = self.addHost('h20')

        h21=self.addHost('h21')

        h22=self.addHost('h22')

        h23=self.addHost('h23')

        h24=self.addHost('h24')

        h25=self.addHost('h25')

        h26=self.addHost('h26')

        h27 = self.addHost('h27')

        h28 = self.addHost('h28')

        h29 = self.addHost('h29')

        h30 = self.addHost('h30')

        h31 = self.addHost('h31')

        h32 = self.addHost('h32')

        h33 = self.addHost('h33')

        h34 = self.addHost('h34')

        h35 = self.addHost('h35')

        h36 = self.addHost('h36')

        h37 = self.addHost('h37')

        h38 = self.addHost('h38')

        h39 = self.addHost('h39')

        h40 = self.addHost('h40')

        b=300
        b1=20
        b2=20
        d='0.1ms'
		
		#add link
        self.addLink(h1, s1, bw=b2, delay=d, loss=0, max_queue_size=b, use_htb=True)

        self.addLink(h2, s1, bw=b2, delay=d, loss=0, max_queue_size=b, use_htb=True)

        self.addLink(h3, s1, bw=b2, delay=d, loss=0, max_queue_size=b, use_htb=True)

        self.addLink(h4, s1, bw=b2, delay=d, loss=0, max_queue_size=b, use_htb=True)

        self.addLink(h5, s1, bw=b2, delay=d, loss=0, max_queue_size=b, use_htb=True)

        self.addLink(h6, s1, bw=b2, delay=d, loss=0, max_queue_size=b, use_htb=True)

        self.addLink(h7, s1, bw=b2, delay=d, loss=0, max_queue_size=b, use_htb=True)

        self.addLink(h8, s1, bw=b2, delay=d, loss=0, max_queue_size=b, use_htb=True)

        self.addLink(h9, s1, bw=b2, delay=d, loss=0, max_queue_size=b, use_htb=True)

        self.addLink(h10, s1, bw=b2, delay=d, loss=0, max_queue_size=b, use_htb=True)

        self.addLink(h11, s1, bw=b2, delay=d, loss=0, max_queue_size=b, use_htb=True)

        self.addLink(h12, s1, bw=b2, delay=d, loss=0, max_queue_size=b, use_htb=True)

        self.addLink(h13, s1, bw=b2, delay=d, loss=0, max_queue_size=b, use_htb=True)

        self.addLink(h14, s1, bw=b2, delay=d, loss=0, max_queue_size=b, use_htb=True)

        self.addLink(h15, s1, bw=b2, delay=d, loss=0, max_queue_size=b, use_htb=True)

        self.addLink(h16, s1, bw=b2, delay=d, loss=0, max_queue_size=b, use_htb=True)

        self.addLink(h17, s1, bw=b2, delay=d, loss=0, max_queue_size=b, use_htb=True)

        self.addLink(h18, s1, bw=b2, delay=d, loss=0, max_queue_size=b, use_htb=True)

        self.addLink(h19, s1, bw=b2, delay=d, loss=0, max_queue_size=b, use_htb=True)

        self.addLink(h20, s1, bw=b2, delay=d, loss=0, max_queue_size=b, use_htb=True)

        self.addLink(s1, s2, bw=b1, delay=d, loss=0, max_queue_size=b, use_htb=True)

        self.addLink(s1, s3, bw=b1, delay=d, loss=0, max_queue_size=b, use_htb=True)

        self.addLink(s1, s4, bw=b1, delay=d, loss=0, max_queue_size=b, use_htb=True)

        self.addLink(s1, s5, bw=b1, delay=d, loss=0, max_queue_size=b, use_htb=True)

        self.addLink(s1, s6, bw=b1, delay=d, loss=0, max_queue_size=b, use_htb=True)

        self.addLink(s1, s7, bw=b1, delay=d, loss=0, max_queue_size=b, use_htb=True)

        self.addLink(s1, s8, bw=b1, delay=d, loss=0, max_queue_size=b, use_htb=True)

        self.addLink(s1, s9, bw=b1, delay=d, loss=0, max_queue_size=b, use_htb=True)

        self.addLink(s1, s10, bw=b1, delay=d, loss=0, max_queue_size=b, use_htb=True)

        self.addLink(s1, s11, bw=b1, delay=d, loss=0, max_queue_size=b, use_htb=True)

        self.addLink(s1, s12, bw=b1, delay=d, loss=0, max_queue_size=b, use_htb=True)

        self.addLink(s1, s13, bw=b1, delay=d, loss=0, max_queue_size=b, use_htb=True)

        self.addLink(s1, s15, bw=b1, delay=d, loss=0, max_queue_size=b, use_htb=True)

        self.addLink(s1, s16, bw=b1, delay=d, loss=0, max_queue_size=b, use_htb=True)

        self.addLink(s1, s17, bw=b1, delay=d, loss=0, max_queue_size=b, use_htb=True)

        self.addLink(s1, s18, bw=b1, delay=d, loss=0, max_queue_size=b, use_htb=True)

        self.addLink(s1, s19, bw=b1, delay=d, loss=0, max_queue_size=b, use_htb=True)

        self.addLink(s1, s20, bw=b1, delay=d, loss=0, max_queue_size=b, use_htb=True)

        self.addLink(s1, s21, bw=b1, delay=d, loss=0, max_queue_size=b, use_htb=True)

        self.addLink(s1, s22, bw=b1, delay=d, loss=0, max_queue_size=b, use_htb=True)

        self.addLink(s2, s14, bw=b1, delay=d, loss=0, max_queue_size=b, use_htb=True)

        self.addLink(s3, s14, bw=b1, delay=d, loss=0, max_queue_size=b, use_htb=True)

        self.addLink(s4, s14, bw=b1, delay=d, loss=0, max_queue_size=b, use_htb=True)

        self.addLink(s5, s14, bw=b1, delay=d, loss=0, max_queue_size=b, use_htb=True)

        self.addLink(s6, s14, bw=b1, delay=d, loss=0, max_queue_size=b, use_htb=True)

        self.addLink(s7, s14, bw=b1, delay=d, loss=0, max_queue_size=b, use_htb=True)

        self.addLink(s8, s14, bw=b1, delay=d, loss=0, max_queue_size=b, use_htb=True)

        self.addLink(s9, s14, bw=b1, delay=d, loss=0, max_queue_size=b, use_htb=True)

        self.addLink(s10, s14, bw=b1, delay=d, loss=0, max_queue_size=b, use_htb=True)

        self.addLink(s11, s14, bw=b1, delay=d, loss=0, max_queue_size=b, use_htb=True)

        self.addLink(s12, s14, bw=b1, delay=d, loss=0, max_queue_size=b, use_htb=True)

        self.addLink(s13, s14, bw=b1, delay=d, loss=0, max_queue_size=b, use_htb=True)

        self.addLink(s15, s14, bw=b1, delay=d, loss=0, max_queue_size=b, use_htb=True)

        self.addLink(s16, s14, bw=b1, delay=d, loss=0, max_queue_size=b, use_htb=True)

        self.addLink(s17, s14, bw=b1, delay=d, loss=0, max_queue_size=b, use_htb=True)

        self.addLink(s18, s14, bw=b1, delay=d, loss=0, max_queue_size=b, use_htb=True)

        self.addLink(s19, s14, bw=b1, delay=d, loss=0, max_queue_size=b, use_htb=True)

        self.addLink(s20, s14, bw=b1, delay=d, loss=0, max_queue_size=b, use_htb=True)

        self.addLink(s21, s14, bw=b1, delay=d, loss=0, max_queue_size=b, use_htb=True)

        self.addLink(s22, s14, bw=b1, delay=d, loss=0, max_queue_size=b, use_htb=True)

        self.addLink(s14, h21, bw=b1, delay=d, loss=0, max_queue_size=b, use_htb=True)

        self.addLink(s14, h22, bw=b1, delay=d, loss=0, max_queue_size=b, use_htb=True)

        self.addLink(s14, h23, bw=b1, delay=d, loss=0, max_queue_size=b, use_htb=True)

        self.addLink(s14, h24, bw=b1, delay=d, loss=0, max_queue_size=b, use_htb=True)

        self.addLink(s14, h25, bw=b1, delay=d, loss=0, max_queue_size=b, use_htb=True)

        self.addLink(s14, h26, bw=b1, delay=d, loss=0, max_queue_size=b, use_htb=True)

        self.addLink(s14, h27, bw=b1, delay=d, loss=0, max_queue_size=b, use_htb=True)

        self.addLink(s14, h28, bw=b1, delay=d, loss=0, max_queue_size=b, use_htb=True)

        self.addLink(s14, h29, bw=b1, delay=d, loss=0, max_queue_size=b, use_htb=True)

        self.addLink(s14, h30, bw=b1, delay=d, loss=0, max_queue_size=b, use_htb=True)

        self.addLink(s14, h31, bw=b1, delay=d, loss=0, max_queue_size=b, use_htb=True)

        self.addLink(s14, h32, bw=b1, delay=d, loss=0, max_queue_size=b, use_htb=True)

        self.addLink(s14, h33, bw=b1, delay=d, loss=0, max_queue_size=b, use_htb=True)

        self.addLink(s14, h34, bw=b1, delay=d, loss=0, max_queue_size=b, use_htb=True)

        self.addLink(s14, h35, bw=b1, delay=d, loss=0, max_queue_size=b, use_htb=True)

        self.addLink(s14, h36, bw=b1, delay=d, loss=0, max_queue_size=b, use_htb=True)

        self.addLink(s14, h37, bw=b1, delay=d, loss=0, max_queue_size=b, use_htb=True)

        self.addLink(s14, h38, bw=b1, delay=d, loss=0, max_queue_size=b, use_htb=True)

        self.addLink(s14, h39, bw=b1, delay=d, loss=0, max_queue_size=b, use_htb=True)

        self.addLink(s14, h40, bw=b1, delay=d, loss=0, max_queue_size=b, use_htb=True)


def perfTest():

    "Create network and run simple performance test"

    global flag
    topo = MyTopo()


    net = Mininet(topo=topo, host=CPULimitedHost, link=TCLink, controller=partial(RemoteController,ip='127.0.0.1',port=6633))


    net.start()

    print "Dumping host connections"

    dumpNodeConnections(net.hosts)

    h1,h2,h3,h4,h5,h6,h7,h8,h9,h10=net.get('h1','h2','h3','h4','h5','h6','h7','h8','h9','h10')

    h21, h22, h23, h24, h25, h26, h27, h28, h29, h30 = net.get('h21', 'h22', 'h23', 'h24', 'h25', 'h26', 'h27', 'h28', 'h29', 'h30')

    h11,h12,h13, h14, h15, h16, h17, h18, h19, h20 = net.get('h11', 'h12', 'h13', 'h14', 'h15', 'h16', 'h17', 'h18', 'h19', 'h20')

    h31, h32, h33, h34, h35, h36, h37, h38, h39, h40 = net.get('h31', 'h32', 'h33', 'h34', 'h35', 'h36', 'h37', 'h38',
                                                               'h39', 'h40')

    h1.setMAC("0:0:0:0:0:1")

    h2.setMAC("0:0:0:0:0:2")

    h3.setMAC("0:0:0:0:0:3")

    h4.setMAC("0:0:0:0:0:4")

    h5.setMAC("0:0:0:0:0:5")

    h6.setMAC("0:0:0:0:0:6")

    h7.setMAC("0:0:0:0:0:7")

    h8.setMAC("0:0:0:0:0:8")

    h9.setMAC("0:0:0:0:0:9")

    h10.setMAC("0:0:0:0:0:10")

    h11.setMAC("0:0:0:0:0:11")

    h12.setMAC("0:0:0:0:0:12")

    h13.setMAC("0:0:0:0:0:13")

    h14.setMAC("0:0:0:0:0:14")

    h15.setMAC("0:0:0:0:0:15")

    h16.setMAC("0:0:0:0:0:16")

    h17.setMAC("0:0:0:0:0:17")

    h18.setMAC("0:0:0:0:0:18")

    h19.setMAC("0:0:0:0:0:19")

    h20.setMAC("0:0:0:0:0:20")

    h21.setMAC("0:0:0:0:0:21")

    h22.setMAC("0:0:0:0:0:22")

    h23.setMAC("0:0:0:0:0:23")

    h24.setMAC("0:0:0:0:0:24")

    h25.setMAC("0:0:0:0:0:25")

    h26.setMAC("0:0:0:0:0:26")

    h27.setMAC("0:0:0:0:0:27")

    h28.setMAC("0:0:0:0:0:28")

    h29.setMAC("0:0:0:0:0:29")

    h30.setMAC("0:0:0:0:0:30")

    h31.setMAC("0:0:0:0:0:31")

    h32.setMAC("0:0:0:0:0:32")

    h33.setMAC("0:0:0:0:0:33")

    h34.setMAC("0:0:0:0:0:34")

    h35.setMAC("0:0:0:0:0:35")

    h36.setMAC("0:0:0:0:0:36")

    h37.setMAC("0:0:0:0:0:37")

    h38.setMAC("0:0:0:0:0:38")

    h39.setMAC("0:0:0:0:0:39")

    h40.setMAC("0:0:0:0:0:40")



    time.sleep(150)

    #iperf Server
    h21.popen('iperf -s ', shell=True)

    #iperf Server
    h22.popen('iperf -s ', shell=True)
    h23.popen('iperf -s ', shell=True)
    h24.popen('iperf -s ', shell=True)
    h25.popen('iperf -s ', shell=True)
    h26.popen('iperf -s ', shell=True)
    h27.popen('iperf -s ', shell=True)
    h28.popen('iperf -s ', shell=True)
    h29.popen('iperf -s ', shell=True)
    h30.popen('iperf -s ', shell=True)

    h31.popen('iperf -s ', shell=True)

    # iperf Server
    h32.popen('iperf -s ', shell=True)
    h33.popen('iperf -s ', shell=True)
    h34.popen('iperf -s ', shell=True)
    h35.popen('iperf -s ', shell=True)
    h36.popen('iperf -s ', shell=True)
    h37.popen('iperf -s ', shell=True)
    h38.popen('iperf -s ', shell=True)
    h39.popen('iperf -s ', shell=True)
    h40.popen('iperf -s ', shell=True)

    h=[h1,h2,h3,h4,h5,h6,h7,h8,h9,h10,h11,h12,h13,h14,h15,h16,h17,h18,h19,h20,h21,h22,h23,h24,h25,h26,h27,h28,h29,h30,h31,h32,h33,h34,h35,h36,h37,h38,h39,h40]
    num_list=[19,18,17,16,15,14,13,12,11,10,9,8,7,6,5,4,3,2,1,0]

    def loop(n):
        if n==19 :
            print 'lf10:'
            h20.cmdPrint('iperf -c ' + h40.IP() + ' -l 7240000 -n 1 ')
        elif n==18:
            h19.cmdPrint('iperf -c ' + h39.IP() + ' -l 7240000 -n 1 ')
        elif n == 17:
            h18.cmdPrint('iperf -c ' + h38.IP() + ' -l 7240000 -n 1 ')
        elif n == 16:
            h17.cmdPrint('iperf -c ' + h37.IP() + ' -l 7240000 -n 1 ')
        else:
            h[n].cmdPrint('iperf -c '+ h[n+20].IP()+' -l 579200 -n 1 ')
    pool = threadpool.ThreadPool(20)
    requests = threadpool.makeRequests(loop,num_list)
    [pool.putRequest(req) for req in requests]
    pool.wait()

    CLI(net)

    net.stop()

if __name__ == '__main__':

    setLogLevel('info')

    perfTest()
