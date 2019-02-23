#author: hujinbin
#date:2018/01/01
#description: controller

from pox.core import core

import pox.openflow.libopenflow_01 as of

from pox.lib.util import dpidToStr

from pox.lib.addresses import IPAddr, EthAddr

from pox.lib.packet.arp import arp

from pox.lib.packet.ethernet import ethernet, ETHER_BROADCAST

from pox.lib.packet.packet_base import packet_base

from pox.lib.packet.packet_utils import *

import pox.lib.packet as pkt

from pox.lib.recoco import Timer

import time

a=0.00001

log = core.getLogger()

s1_dpid=0

s2_dpid=0

s3_dpid=0

s4_dpid=0

s5_dpid=0

s6_dpid=0

s7_dpid=0

s8_dpid=0

s9_dpid=0

s10_dpid=0

s11_dpid=0

s12_dpid=0

s13_dpid=0

s14_dpid=0

s15_dpid=0

s16_dpid=0

s17_dpid=0

s18_dpid=0

s19_dpid=0

s20_dpid=0

s21_dpid=0

s22_dpid=0

s1_p1=0

s1_p11=0

s1_p12=0

s1_p13=0

s1_p14=0

s1_p15=0

s1_p16=0

s1_p17=0

s1_p18=0

s1_p19=0

s1_p20=0

s1_p21=0

s1_p22=0

s1_p23=0

s1_p24=0

s1_p25=0

s1_p26=0

s1_p27=0

s1_p28=0

s1_p29=0

s1_p30=0

s2_p1=0

s3_p1=0

s4_p1=0

s5_p1=0

s6_p1=0

s7_p1=0

s8_p1=0

s9_p1=0

s10_p1=0

s11_p1=0

s12_p1=0

s13_p1=0

s15_p1=0

s16_p1=0

s17_p1=0

s18_p1=0

s19_p1=0

s20_p1=0

s21_p1=0

s22_p1=0

pre_s1_p1=0

pre_s1_p11=0

pre_s1_p12=0

pre_s1_p13=0

pre_s1_p14=0

pre_s1_p15=0

pre_s1_p16=0

pre_s1_p17=0

pre_s1_p18=0

pre_s1_p19=0

pre_s1_p20=0

pre_s1_p21=0

pre_s1_p22=0

pre_s1_p23=0

pre_s1_p24=0

pre_s1_p25=0

pre_s1_p26=0

pre_s1_p27=0

pre_s1_p28=0

pre_s1_p29=0

pre_s1_p30=0

pre_s2_p1=0

pre_s3_p1=0

pre_s4_p1=0

pre_s5_p1=0

pre_s6_p1=0

pre_s7_p1=0

pre_s8_p1=0

pre_s9_p1=0

pre_s10_p1=0

pre_s11_p1=0

pre_s12_p1=0

pre_s13_p1=0

pre_s15_p1=0

pre_s16_p1=0

pre_s17_p1=0

pre_s18_p1=0

pre_s19_p1=0

pre_s20_p1=0

pre_s21_p1=0

pre_s22_p1=0


turn1=0
turn2=0
turn3=0
turn4=0
turn5=0
turn6=0
turn7=0
turn8=0
turn9=0

#add
s1_p2=0

s1_p3=0

s1_p4=0

s1_p5=0

s1_p6=0

s1_p7=0

s1_p8=0

s1_p9=0

pre_s1_p2=0

pre_s1_p3=0

pre_s1_p4=0

pre_s1_p5=0

pre_s1_p6=0

pre_s1_p7=0

pre_s1_p8=0

pre_s1_p9=0

turn10=0

count=0

def getTheTime():  #fuction to create a timestamp

  flock = time.localtime()

  then = "[%s-%s-%s" %(str(flock.tm_year),str(flock.tm_mon),str(flock.tm_mday))

  if int(flock.tm_hour)<10:

    hrs = "0%s" % (str(flock.tm_hour))

  else:

    hrs = str(flock.tm_hour)

  if int(flock.tm_min)<10:

    mins = str(flock.tm_min)

    secs = "0%s" % (str(flock.tm_sec))

  else:

    secs = str(flock.tm_sec)

  then +="]%s.%s.%s" % (hrs,mins,secs)

  return then



def _timer_func1 ():

  global s1_dpid, s2_dpid, s3_dpid, s4_dpid, s5_dpid,s6_dpid,s7_dpid, s8_dpid, s9_dpid, s10_dpid, s11_dpid,s12_dpid,s13_dpid, s14_dpid
  global s15_dpid,s16_dpid,s17_dpid, s18_dpid, s19_dpid, s20_dpid, s21_dpid, s22_dpid
  global turn1,turn2,turn3,turn4,turn5,turn6,turn7,turn8,turn9,turn10,count

  if turn1==0 :

      msg = of.ofp_flow_mod()

      msg.command=of.OFPFC_MODIFY_STRICT

      msg.priority =100

      msg.idle_timeout = 0

      msg.hard_timeout = 0

      msg.match.dl_type = 0x0800

      msg.match.nw_dst = "10.0.0.11"

      msg.actions.append(of.ofp_action_output(port = 11))

      core.openflow.getConnection(s1_dpid).send(msg)

      turn1=1

      count=count+1

      return



  if turn1==1:

      msg = of.ofp_flow_mod()

      msg.command=of.OFPFC_MODIFY_STRICT

      msg.priority =100

      msg.idle_timeout = 0

      msg.hard_timeout = 0

      msg.match.dl_type = 0x0800

      msg.match.nw_dst = "10.0.0.11"

      msg.actions.append(of.ofp_action_output(port = 12))

      core.openflow.getConnection(s1_dpid).send(msg)

      turn1=2

      return



  if turn1==2 :

      msg = of.ofp_flow_mod()

      msg.command=of.OFPFC_MODIFY_STRICT

      msg.priority =100

      msg.idle_timeout = 0

      msg.hard_timeout = 0

      msg.match.dl_type = 0x0800

      msg.match.nw_dst = "10.0.0.11"

      msg.actions.append(of.ofp_action_output(port = 13))

      core.openflow.getConnection(s1_dpid).send(msg)

      turn1=3

      return

  if turn1==3:

      msg = of.ofp_flow_mod()

      msg.command=of.OFPFC_MODIFY_STRICT

      msg.priority =100

      msg.idle_timeout = 0

      msg.hard_timeout = 0

      msg.match.dl_type = 0x0800

      msg.match.nw_dst = "10.0.0.11"

      msg.actions.append(of.ofp_action_output(port = 14))

      core.openflow.getConnection(s1_dpid).send(msg)

      turn1=4

      return

  if turn1==4:

      msg = of.ofp_flow_mod()

      msg.command=of.OFPFC_MODIFY_STRICT

      msg.priority =100

      msg.idle_timeout = 0

      msg.hard_timeout = 0

      msg.match.dl_type = 0x0800

      msg.match.nw_dst = "10.0.0.11"

      msg.actions.append(of.ofp_action_output(port = 15))

      core.openflow.getConnection(s1_dpid).send(msg)

      turn1=5

      return

  if turn1==5:

      msg = of.ofp_flow_mod()

      msg.command=of.OFPFC_MODIFY_STRICT

      msg.priority =100

      msg.idle_timeout = 0

      msg.hard_timeout = 0

      msg.match.dl_type = 0x0800

      msg.match.nw_dst = "10.0.0.11"

      msg.actions.append(of.ofp_action_output(port = 16))

      core.openflow.getConnection(s1_dpid).send(msg)

      turn1=6

      return

  if turn1==6:

      msg = of.ofp_flow_mod()

      msg.command=of.OFPFC_MODIFY_STRICT

      msg.priority =100

      msg.idle_timeout = 0

      msg.hard_timeout = 0

      msg.match.dl_type = 0x0800

      msg.match.nw_dst = "10.0.0.11"

      msg.actions.append(of.ofp_action_output(port = 17))

      core.openflow.getConnection(s1_dpid).send(msg)

      turn1=7

      return


  if turn1==7:

      msg = of.ofp_flow_mod()

      msg.command=of.OFPFC_MODIFY_STRICT

      msg.priority =100

      msg.idle_timeout = 0

      msg.hard_timeout = 0

      msg.match.dl_type = 0x0800

      msg.match.nw_dst = "10.0.0.11"

      msg.actions.append(of.ofp_action_output(port = 18))

      core.openflow.getConnection(s1_dpid).send(msg)

      turn1=8

      return

  if turn1==8:

      msg = of.ofp_flow_mod()

      msg.command=of.OFPFC_MODIFY_STRICT

      msg.priority =100

      msg.idle_timeout = 0

      msg.hard_timeout = 0

      msg.match.dl_type = 0x0800

      msg.match.nw_dst = "10.0.0.11"

      msg.actions.append(of.ofp_action_output(port = 19))

      core.openflow.getConnection(s1_dpid).send(msg)

      turn1=9

      return

  if turn1==9:

      msg = of.ofp_flow_mod()

      msg.command=of.OFPFC_MODIFY_STRICT

      msg.priority =100

      msg.idle_timeout = 0

      msg.hard_timeout = 0

      msg.match.dl_type = 0x0800

      msg.match.nw_dst = "10.0.0.11"

      msg.actions.append(of.ofp_action_output(port = 20))

      core.openflow.getConnection(s1_dpid).send(msg)

      turn1=10

      return

  if turn1==10:

      msg = of.ofp_flow_mod()

      msg.command=of.OFPFC_MODIFY_STRICT

      msg.priority =100

      msg.idle_timeout = 0

      msg.hard_timeout = 0

      msg.match.dl_type = 0x0800

      msg.match.nw_dst = "10.0.0.11"

      msg.actions.append(of.ofp_action_output(port = 21))

      core.openflow.getConnection(s1_dpid).send(msg)

      turn1=11

      return

  if turn1==11:

      msg = of.ofp_flow_mod()

      msg.command=of.OFPFC_MODIFY_STRICT

      msg.priority =100

      msg.idle_timeout = 0

      msg.hard_timeout = 0

      msg.match.dl_type = 0x0800

      msg.match.nw_dst = "10.0.0.11"

      msg.actions.append(of.ofp_action_output(port = 22))

      core.openflow.getConnection(s1_dpid).send(msg)

      turn1=12

      return

  if turn1==12:

      msg = of.ofp_flow_mod()

      msg.command=of.OFPFC_MODIFY_STRICT

      msg.priority =100

      msg.idle_timeout = 0

      msg.hard_timeout = 0

      msg.match.dl_type = 0x0800

      msg.match.nw_dst = "10.0.0.11"

      msg.actions.append(of.ofp_action_output(port = 23))

      core.openflow.getConnection(s1_dpid).send(msg)

      turn1=13

      return

  if turn1==13:

      msg = of.ofp_flow_mod()

      msg.command=of.OFPFC_MODIFY_STRICT

      msg.priority =100

      msg.idle_timeout = 0

      msg.hard_timeout = 0

      msg.match.dl_type = 0x0800

      msg.match.nw_dst = "10.0.0.11"

      msg.actions.append(of.ofp_action_output(port = 24))

      core.openflow.getConnection(s1_dpid).send(msg)

      turn1=14

      return

  if turn1==14:

      msg = of.ofp_flow_mod()

      msg.command=of.OFPFC_MODIFY_STRICT

      msg.priority =100

      msg.idle_timeout = 0

      msg.hard_timeout = 0

      msg.match.dl_type = 0x0800

      msg.match.nw_dst = "10.0.0.11"

      msg.actions.append(of.ofp_action_output(port = 25))

      core.openflow.getConnection(s1_dpid).send(msg)

      turn1=15

      return

  if turn1==15:

      msg = of.ofp_flow_mod()

      msg.command=of.OFPFC_MODIFY_STRICT

      msg.priority =100

      msg.idle_timeout = 0

      msg.hard_timeout = 0

      msg.match.dl_type = 0x0800

      msg.match.nw_dst = "10.0.0.11"

      msg.actions.append(of.ofp_action_output(port = 26))

      core.openflow.getConnection(s1_dpid).send(msg)

      turn1=16

      return

  if turn1==16:

      msg = of.ofp_flow_mod()

      msg.command=of.OFPFC_MODIFY_STRICT

      msg.priority =100

      msg.idle_timeout = 0

      msg.hard_timeout = 0

      msg.match.dl_type = 0x0800

      msg.match.nw_dst = "10.0.0.11"

      msg.actions.append(of.ofp_action_output(port = 27))

      core.openflow.getConnection(s1_dpid).send(msg)

      turn1=17

      return

  if turn1==17:

      msg = of.ofp_flow_mod()

      msg.command=of.OFPFC_MODIFY_STRICT

      msg.priority =100

      msg.idle_timeout = 0

      msg.hard_timeout = 0

      msg.match.dl_type = 0x0800

      msg.match.nw_dst = "10.0.0.11"

      msg.actions.append(of.ofp_action_output(port = 28))

      core.openflow.getConnection(s1_dpid).send(msg)

      turn1=18

      return

  if turn1==18:

      msg = of.ofp_flow_mod()

      msg.command=of.OFPFC_MODIFY_STRICT

      msg.priority =100

      msg.idle_timeout = 0

      msg.hard_timeout = 0

      msg.match.dl_type = 0x0800

      msg.match.nw_dst = "10.0.0.11"

      msg.actions.append(of.ofp_action_output(port = 29))

      core.openflow.getConnection(s1_dpid).send(msg)

      turn1=19

      return

  if turn1==19:

      msg = of.ofp_flow_mod()

      msg.command=of.OFPFC_MODIFY_STRICT

      msg.priority =100

      msg.idle_timeout = 0

      msg.hard_timeout = 0

      msg.match.dl_type = 0x0800

      msg.match.nw_dst = "10.0.0.11"

      msg.actions.append(of.ofp_action_output(port = 30))

      core.openflow.getConnection(s1_dpid).send(msg)

      turn1=0

      return

def _timer_func2():
    global s1_dpid, s2_dpid, s3_dpid, s4_dpid, s5_dpid, s6_dpid, s7_dpid, s8_dpid, s9_dpid, s10_dpid, s11_dpid, s12_dpid, s13_dpid, s14_dpid
    global s15_dpid, s16_dpid, s17_dpid, s18_dpid, s19_dpid, s20_dpid, s21_dpid, s22_dpid
    global turn1, turn2, turn3, turn4, turn5, turn6, turn7, turn8, turn9,turn10,count

    if turn2 == 0:
        msg = of.ofp_flow_mod()

        msg.command = of.OFPFC_MODIFY_STRICT

        msg.priority = 100

        msg.idle_timeout = 0

        msg.hard_timeout = 0

        msg.match.dl_type = 0x0800

        msg.match.nw_dst = "10.0.0.12"

        msg.actions.append(of.ofp_action_output(port=11))

        core.openflow.getConnection(s1_dpid).send(msg)

        turn2 = 1

        return

    if turn2 == 1:
        msg = of.ofp_flow_mod()

        msg.command = of.OFPFC_MODIFY_STRICT

        msg.priority = 100

        msg.idle_timeout = 0

        msg.hard_timeout = 0

        msg.match.dl_type = 0x0800

        msg.match.nw_dst = "10.0.0.12"

        msg.actions.append(of.ofp_action_output(port=12))

        core.openflow.getConnection(s1_dpid).send(msg)

        turn2 = 2

        return

    if turn2 == 2:
        msg = of.ofp_flow_mod()

        msg.command = of.OFPFC_MODIFY_STRICT

        msg.priority = 100

        msg.idle_timeout = 0

        msg.hard_timeout = 0

        msg.match.dl_type = 0x0800

        msg.match.nw_dst = "10.0.0.12"

        msg.actions.append(of.ofp_action_output(port=13))

        core.openflow.getConnection(s1_dpid).send(msg)

        turn2 = 3

        return

    if turn2 == 3:
        msg = of.ofp_flow_mod()

        msg.command = of.OFPFC_MODIFY_STRICT

        msg.priority = 100

        msg.idle_timeout = 0

        msg.hard_timeout = 0

        msg.match.dl_type = 0x0800

        msg.match.nw_dst = "10.0.0.12"

        msg.actions.append(of.ofp_action_output(port=14))

        core.openflow.getConnection(s1_dpid).send(msg)

        turn2 = 4

        return

    if turn2 == 4:
        msg = of.ofp_flow_mod()

        msg.command = of.OFPFC_MODIFY_STRICT

        msg.priority = 100

        msg.idle_timeout = 0

        msg.hard_timeout = 0

        msg.match.dl_type = 0x0800

        msg.match.nw_dst = "10.0.0.12"

        msg.actions.append(of.ofp_action_output(port=15))

        core.openflow.getConnection(s1_dpid).send(msg)

        turn2 = 5

        return

    if turn2 == 5:
        msg = of.ofp_flow_mod()

        msg.command = of.OFPFC_MODIFY_STRICT

        msg.priority = 100

        msg.idle_timeout = 0

        msg.hard_timeout = 0

        msg.match.dl_type = 0x0800

        msg.match.nw_dst = "10.0.0.12"

        msg.actions.append(of.ofp_action_output(port=16))

        core.openflow.getConnection(s1_dpid).send(msg)

        turn2 = 6

        return

    if turn2 == 6:
        msg = of.ofp_flow_mod()

        msg.command = of.OFPFC_MODIFY_STRICT

        msg.priority = 100

        msg.idle_timeout = 0

        msg.hard_timeout = 0

        msg.match.dl_type = 0x0800

        msg.match.nw_dst = "10.0.0.12"

        msg.actions.append(of.ofp_action_output(port=17))

        core.openflow.getConnection(s1_dpid).send(msg)

        turn2 = 7

        return

    if turn2 == 7:
        msg = of.ofp_flow_mod()

        msg.command = of.OFPFC_MODIFY_STRICT

        msg.priority = 100

        msg.idle_timeout = 0

        msg.hard_timeout = 0

        msg.match.dl_type = 0x0800

        msg.match.nw_dst = "10.0.0.12"

        msg.actions.append(of.ofp_action_output(port=18))

        core.openflow.getConnection(s1_dpid).send(msg)

        turn2 = 8

        return

    if turn2 == 8:
        msg = of.ofp_flow_mod()

        msg.command = of.OFPFC_MODIFY_STRICT

        msg.priority = 100

        msg.idle_timeout = 0

        msg.hard_timeout = 0

        msg.match.dl_type = 0x0800

        msg.match.nw_dst = "10.0.0.12"

        msg.actions.append(of.ofp_action_output(port=19))

        core.openflow.getConnection(s1_dpid).send(msg)

        turn2 = 9

        return

    if turn2 == 9:
        msg = of.ofp_flow_mod()

        msg.command = of.OFPFC_MODIFY_STRICT

        msg.priority = 100

        msg.idle_timeout = 0

        msg.hard_timeout = 0

        msg.match.dl_type = 0x0800

        msg.match.nw_dst = "10.0.0.12"

        msg.actions.append(of.ofp_action_output(port=20))

        core.openflow.getConnection(s1_dpid).send(msg)

        turn2 = 10

        return

    if turn2 == 10:
        msg = of.ofp_flow_mod()

        msg.command = of.OFPFC_MODIFY_STRICT

        msg.priority = 100

        msg.idle_timeout = 0

        msg.hard_timeout = 0

        msg.match.dl_type = 0x0800

        msg.match.nw_dst = "10.0.0.12"

        msg.actions.append(of.ofp_action_output(port=21))

        core.openflow.getConnection(s1_dpid).send(msg)

        turn2 = 11

        return

    if turn2 == 11:
        msg = of.ofp_flow_mod()

        msg.command = of.OFPFC_MODIFY_STRICT

        msg.priority = 100

        msg.idle_timeout = 0

        msg.hard_timeout = 0

        msg.match.dl_type = 0x0800

        msg.match.nw_dst = "10.0.0.12"

        msg.actions.append(of.ofp_action_output(port=22))

        core.openflow.getConnection(s1_dpid).send(msg)

        turn2 = 12

        return

    if turn2 == 12:
        msg = of.ofp_flow_mod()

        msg.command = of.OFPFC_MODIFY_STRICT

        msg.priority = 100

        msg.idle_timeout = 0

        msg.hard_timeout = 0

        msg.match.dl_type = 0x0800

        msg.match.nw_dst = "10.0.0.12"

        msg.actions.append(of.ofp_action_output(port=23))

        core.openflow.getConnection(s1_dpid).send(msg)

        turn2 = 13

        return

    if turn2 == 13:
        msg = of.ofp_flow_mod()

        msg.command = of.OFPFC_MODIFY_STRICT

        msg.priority = 100

        msg.idle_timeout = 0

        msg.hard_timeout = 0

        msg.match.dl_type = 0x0800

        msg.match.nw_dst = "10.0.0.12"

        msg.actions.append(of.ofp_action_output(port=24))

        core.openflow.getConnection(s1_dpid).send(msg)

        turn2 = 14

        return

    if turn2 == 14:
        msg = of.ofp_flow_mod()

        msg.command = of.OFPFC_MODIFY_STRICT

        msg.priority = 100

        msg.idle_timeout = 0

        msg.hard_timeout = 0

        msg.match.dl_type = 0x0800

        msg.match.nw_dst = "10.0.0.12"

        msg.actions.append(of.ofp_action_output(port=25))

        core.openflow.getConnection(s1_dpid).send(msg)

        turn2 = 15

        return

    if turn2 == 15:
        msg = of.ofp_flow_mod()

        msg.command = of.OFPFC_MODIFY_STRICT

        msg.priority = 100

        msg.idle_timeout = 0

        msg.hard_timeout = 0

        msg.match.dl_type = 0x0800

        msg.match.nw_dst = "10.0.0.12"

        msg.actions.append(of.ofp_action_output(port=26))

        core.openflow.getConnection(s1_dpid).send(msg)

        turn2 = 16

        return

    if turn2 == 16:
        msg = of.ofp_flow_mod()

        msg.command = of.OFPFC_MODIFY_STRICT

        msg.priority = 100

        msg.idle_timeout = 0

        msg.hard_timeout = 0

        msg.match.dl_type = 0x0800

        msg.match.nw_dst = "10.0.0.12"

        msg.actions.append(of.ofp_action_output(port=27))

        core.openflow.getConnection(s1_dpid).send(msg)

        turn2 = 17

        return

    if turn2 == 17:
        msg = of.ofp_flow_mod()

        msg.command = of.OFPFC_MODIFY_STRICT

        msg.priority = 100

        msg.idle_timeout = 0

        msg.hard_timeout = 0

        msg.match.dl_type = 0x0800

        msg.match.nw_dst = "10.0.0.12"

        msg.actions.append(of.ofp_action_output(port=28))

        core.openflow.getConnection(s1_dpid).send(msg)

        turn2 = 18

        return

    if turn2 == 18:
        msg = of.ofp_flow_mod()

        msg.command = of.OFPFC_MODIFY_STRICT

        msg.priority = 100

        msg.idle_timeout = 0

        msg.hard_timeout = 0

        msg.match.dl_type = 0x0800

        msg.match.nw_dst = "10.0.0.12"

        msg.actions.append(of.ofp_action_output(port=29))

        core.openflow.getConnection(s1_dpid).send(msg)

        turn2 = 19

        return

    if turn2 == 19:
        msg = of.ofp_flow_mod()

        msg.command = of.OFPFC_MODIFY_STRICT

        msg.priority = 100

        msg.idle_timeout = 0

        msg.hard_timeout = 0

        msg.match.dl_type = 0x0800

        msg.match.nw_dst = "10.0.0.12"

        msg.actions.append(of.ofp_action_output(port=30))

        core.openflow.getConnection(s1_dpid).send(msg)

        turn2 = 0

        return

def _timer_func3():
    global s1_dpid, s2_dpid, s3_dpid, s4_dpid, s5_dpid, s6_dpid, s7_dpid, s8_dpid, s9_dpid, s10_dpid, s11_dpid, s12_dpid, s13_dpid, s14_dpid
    global s15_dpid, s16_dpid, s17_dpid, s18_dpid, s19_dpid, s20_dpid, s21_dpid, s22_dpid
    global turn1, turn2, turn3, turn4, turn5, turn6, turn7, turn8, turn9,turn10,count

    if turn3 == 0:
        msg = of.ofp_flow_mod()

        msg.command = of.OFPFC_MODIFY_STRICT

        msg.priority = 100

        msg.idle_timeout = 0

        msg.hard_timeout = 0

        msg.match.dl_type = 0x0800

        msg.match.nw_dst = "10.0.0.13"

        msg.actions.append(of.ofp_action_output(port=11))

        core.openflow.getConnection(s1_dpid).send(msg)

        turn3 = 1

        return

    if turn3 == 1:
        msg = of.ofp_flow_mod()

        msg.command = of.OFPFC_MODIFY_STRICT

        msg.priority = 100

        msg.idle_timeout = 0

        msg.hard_timeout = 0

        msg.match.dl_type = 0x0800

        msg.match.nw_dst = "10.0.0.13"

        msg.actions.append(of.ofp_action_output(port=12))

        core.openflow.getConnection(s1_dpid).send(msg)

        turn3 = 2

        return

    if turn3 == 2:
        msg = of.ofp_flow_mod()

        msg.command = of.OFPFC_MODIFY_STRICT

        msg.priority = 100

        msg.idle_timeout = 0

        msg.hard_timeout = 0

        msg.match.dl_type = 0x0800

        msg.match.nw_dst = "10.0.0.13"

        msg.actions.append(of.ofp_action_output(port=13))

        core.openflow.getConnection(s1_dpid).send(msg)

        turn3 = 3

        return

    if turn3 == 3:
        msg = of.ofp_flow_mod()

        msg.command = of.OFPFC_MODIFY_STRICT

        msg.priority = 100

        msg.idle_timeout = 0

        msg.hard_timeout = 0

        msg.match.dl_type = 0x0800

        msg.match.nw_dst = "10.0.0.13"

        msg.actions.append(of.ofp_action_output(port=14))

        core.openflow.getConnection(s1_dpid).send(msg)

        turn3 = 4

        return

    if turn3 == 4:
        msg = of.ofp_flow_mod()

        msg.command = of.OFPFC_MODIFY_STRICT

        msg.priority = 100

        msg.idle_timeout = 0

        msg.hard_timeout = 0

        msg.match.dl_type = 0x0800

        msg.match.nw_dst = "10.0.0.13"

        msg.actions.append(of.ofp_action_output(port=15))

        core.openflow.getConnection(s1_dpid).send(msg)

        turn3 = 5

        return

    if turn3 == 5:
        msg = of.ofp_flow_mod()

        msg.command = of.OFPFC_MODIFY_STRICT

        msg.priority = 100

        msg.idle_timeout = 0

        msg.hard_timeout = 0

        msg.match.dl_type = 0x0800
		
        msg.match.nw_dst = "10.0.0.13"

        msg.actions.append(of.ofp_action_output(port=16))

        core.openflow.getConnection(s1_dpid).send(msg)

        turn3 = 6

        return

    if turn3 == 6:
        msg = of.ofp_flow_mod()

        msg.command = of.OFPFC_MODIFY_STRICT

        msg.priority = 100

        msg.idle_timeout = 0

        msg.hard_timeout = 0

        msg.match.dl_type = 0x0800

        msg.match.nw_dst = "10.0.0.13"

        msg.actions.append(of.ofp_action_output(port=17))

        core.openflow.getConnection(s1_dpid).send(msg)

        turn3 = 7

        return

    if turn3 == 7:
        msg = of.ofp_flow_mod()

        msg.command = of.OFPFC_MODIFY_STRICT

        msg.priority = 100

        msg.idle_timeout = 0

        msg.hard_timeout = 0

        msg.match.dl_type = 0x0800

        msg.match.nw_dst = "10.0.0.13"

        msg.actions.append(of.ofp_action_output(port=18))

        core.openflow.getConnection(s1_dpid).send(msg)

        turn3 = 8

        return

    if turn3 == 8:
        msg = of.ofp_flow_mod()

        msg.command = of.OFPFC_MODIFY_STRICT

        msg.priority = 100

        msg.idle_timeout = 0

        msg.hard_timeout = 0

        msg.match.dl_type = 0x0800

        msg.match.nw_dst = "10.0.0.13"

        msg.actions.append(of.ofp_action_output(port=19))

        core.openflow.getConnection(s1_dpid).send(msg)

        turn3 = 9

        return

    if turn3 == 9:
        msg = of.ofp_flow_mod()

        msg.command = of.OFPFC_MODIFY_STRICT

        msg.priority = 100

        msg.idle_timeout = 0

        msg.hard_timeout = 0

        msg.match.dl_type = 0x0800

        msg.match.nw_dst = "10.0.0.13"

        msg.actions.append(of.ofp_action_output(port=20))

        core.openflow.getConnection(s1_dpid).send(msg)

        turn3 = 10

        return

    if turn3 == 10:
        msg = of.ofp_flow_mod()

        msg.command = of.OFPFC_MODIFY_STRICT

        msg.priority = 100

        msg.idle_timeout = 0

        msg.hard_timeout = 0

        msg.match.dl_type = 0x0800

        msg.match.nw_dst = "10.0.0.13"

        msg.actions.append(of.ofp_action_output(port=21))

        core.openflow.getConnection(s1_dpid).send(msg)

        turn3 = 11

        return

    if turn3 == 11:
        msg = of.ofp_flow_mod()

        msg.command = of.OFPFC_MODIFY_STRICT

        msg.priority = 100

        msg.idle_timeout = 0

        msg.hard_timeout = 0

        msg.match.dl_type = 0x0800

        msg.match.nw_dst = "10.0.0.13"

        msg.actions.append(of.ofp_action_output(port=22))

        core.openflow.getConnection(s1_dpid).send(msg)

        turn3 = 12

        return

    if turn3 == 12:
        msg = of.ofp_flow_mod()

        msg.command = of.OFPFC_MODIFY_STRICT

        msg.priority = 100

        msg.idle_timeout = 0

        msg.hard_timeout = 0

        msg.match.dl_type = 0x0800

        msg.match.nw_dst = "10.0.0.13"

        msg.actions.append(of.ofp_action_output(port=23))

        core.openflow.getConnection(s1_dpid).send(msg)

        turn3 = 13

        return

    if turn3 == 13:
        msg = of.ofp_flow_mod()

        msg.command = of.OFPFC_MODIFY_STRICT

        msg.priority = 100

        msg.idle_timeout = 0

        msg.hard_timeout = 0

        msg.match.dl_type = 0x0800

        msg.match.nw_dst = "10.0.0.13"

        msg.actions.append(of.ofp_action_output(port=24))

        core.openflow.getConnection(s1_dpid).send(msg)

        turn3 = 14

        return

    if turn3 == 14:
        msg = of.ofp_flow_mod()

        msg.command = of.OFPFC_MODIFY_STRICT

        msg.priority = 100

        msg.idle_timeout = 0

        msg.hard_timeout = 0

        msg.match.dl_type = 0x0800

        msg.match.nw_dst = "10.0.0.13"

        msg.actions.append(of.ofp_action_output(port=25))

        core.openflow.getConnection(s1_dpid).send(msg)

        turn3 = 15

        return

    if turn3 == 15:
        msg = of.ofp_flow_mod()

        msg.command = of.OFPFC_MODIFY_STRICT

        msg.priority = 100

        msg.idle_timeout = 0

        msg.hard_timeout = 0

        msg.match.dl_type = 0x0800

        msg.match.nw_dst = "10.0.0.13"

        msg.actions.append(of.ofp_action_output(port=26))

        core.openflow.getConnection(s1_dpid).send(msg)

        turn3 = 16

        return

    if turn3 == 16:
        msg = of.ofp_flow_mod()

        msg.command = of.OFPFC_MODIFY_STRICT

        msg.priority = 100

        msg.idle_timeout = 0

        msg.hard_timeout = 0

        msg.match.dl_type = 0x0800

        msg.match.nw_dst = "10.0.0.13"

        msg.actions.append(of.ofp_action_output(port=27))

        core.openflow.getConnection(s1_dpid).send(msg)

        turn3 = 17

        return

    if turn3 == 17:
        msg = of.ofp_flow_mod()

        msg.command = of.OFPFC_MODIFY_STRICT

        msg.priority = 100

        msg.idle_timeout = 0

        msg.hard_timeout = 0

        msg.match.dl_type = 0x0800

        msg.match.nw_dst = "10.0.0.13"

        msg.actions.append(of.ofp_action_output(port=28))

        core.openflow.getConnection(s1_dpid).send(msg)

        turn3 = 18

        return

    if turn3 == 18:
        msg = of.ofp_flow_mod()

        msg.command = of.OFPFC_MODIFY_STRICT

        msg.priority = 100

        msg.idle_timeout = 0

        msg.hard_timeout = 0

        msg.match.dl_type = 0x0800

        msg.match.nw_dst = "10.0.0.13"

        msg.actions.append(of.ofp_action_output(port=29))

        core.openflow.getConnection(s1_dpid).send(msg)

        turn3 = 19

        return

    if turn3 == 19:
        msg = of.ofp_flow_mod()

        msg.command = of.OFPFC_MODIFY_STRICT

        msg.priority = 100

        msg.idle_timeout = 0

        msg.hard_timeout = 0

        msg.match.dl_type = 0x0800

        msg.match.nw_dst = "10.0.0.13"

        msg.actions.append(of.ofp_action_output(port=30))

        core.openflow.getConnection(s1_dpid).send(msg)

        turn3 = 0

        return

def _timer_func4():
    global s1_dpid, s2_dpid, s3_dpid, s4_dpid, s5_dpid, s6_dpid, s7_dpid, s8_dpid, s9_dpid, s10_dpid, s11_dpid, s12_dpid, s13_dpid, s14_dpid
    global s15_dpid, s16_dpid, s17_dpid, s18_dpid, s19_dpid, s20_dpid, s21_dpid, s22_dpid
    global turn1, turn2, turn3, turn4, turn5, turn6, turn7, turn8, turn9,turn10,count

    if turn4 == 0:
        msg = of.ofp_flow_mod()

        msg.command = of.OFPFC_MODIFY_STRICT

        msg.priority = 100

        msg.idle_timeout = 0

        msg.hard_timeout = 0

        msg.match.dl_type = 0x0800

        msg.match.nw_dst = "10.0.0.14"

        msg.actions.append(of.ofp_action_output(port=11))

        core.openflow.getConnection(s1_dpid).send(msg)

        turn4 = 1

        return

    if turn4 == 1:
        msg = of.ofp_flow_mod()

        msg.command = of.OFPFC_MODIFY_STRICT

        msg.priority = 100

        msg.idle_timeout = 0

        msg.hard_timeout = 0

        msg.match.dl_type = 0x0800

        msg.match.nw_dst = "10.0.0.14"

        msg.actions.append(of.ofp_action_output(port=12))

        core.openflow.getConnection(s1_dpid).send(msg)

        turn4 = 2

        return

    if turn4 == 2:
        msg = of.ofp_flow_mod()

        msg.command = of.OFPFC_MODIFY_STRICT

        msg.priority = 100

        msg.idle_timeout = 0

        msg.hard_timeout = 0

        msg.match.dl_type = 0x0800

        msg.match.nw_dst = "10.0.0.14"

        msg.actions.append(of.ofp_action_output(port=13))

        core.openflow.getConnection(s1_dpid).send(msg)

        turn4 = 3

        return

    if turn4 == 3:
        msg = of.ofp_flow_mod()

        msg.command = of.OFPFC_MODIFY_STRICT

        msg.priority = 100

        msg.idle_timeout = 0

        msg.hard_timeout = 0

        msg.match.dl_type = 0x0800

        msg.match.nw_dst = "10.0.0.14"

        msg.actions.append(of.ofp_action_output(port=14))

        core.openflow.getConnection(s1_dpid).send(msg)

        turn4 = 4

        return

    if turn4 == 4:
        msg = of.ofp_flow_mod()

        msg.command = of.OFPFC_MODIFY_STRICT

        msg.priority = 100

        msg.idle_timeout = 0

        msg.hard_timeout = 0

        msg.match.dl_type = 0x0800

        msg.match.nw_dst = "10.0.0.14"

        msg.actions.append(of.ofp_action_output(port=15))

        core.openflow.getConnection(s1_dpid).send(msg)

        turn4 = 5

        return

    if turn4 == 5:
        msg = of.ofp_flow_mod()

        msg.command = of.OFPFC_MODIFY_STRICT

        msg.priority = 100

        msg.idle_timeout = 0

        msg.hard_timeout = 0

        msg.match.dl_type = 0x0800

        msg.match.nw_dst = "10.0.0.14"

        msg.actions.append(of.ofp_action_output(port=16))

        core.openflow.getConnection(s1_dpid).send(msg)

        turn4 = 6

        return

    if turn4 == 6:
        msg = of.ofp_flow_mod()

        msg.command = of.OFPFC_MODIFY_STRICT

        msg.priority = 100

        msg.idle_timeout = 0

        msg.hard_timeout = 0

        msg.match.dl_type = 0x0800

        msg.match.nw_dst = "10.0.0.14"

        msg.actions.append(of.ofp_action_output(port=17))

        core.openflow.getConnection(s1_dpid).send(msg)

        turn4 = 7

        return

    if turn4 == 7:
        msg = of.ofp_flow_mod()

        msg.command = of.OFPFC_MODIFY_STRICT

        msg.priority = 100

        msg.idle_timeout = 0

        msg.hard_timeout = 0

        msg.match.dl_type = 0x0800

        msg.match.nw_dst = "10.0.0.14"

        msg.actions.append(of.ofp_action_output(port=18))

        core.openflow.getConnection(s1_dpid).send(msg)

        turn4 = 8

        return

    if turn4 == 8:
        msg = of.ofp_flow_mod()

        msg.command = of.OFPFC_MODIFY_STRICT

        msg.priority = 100

        msg.idle_timeout = 0

        msg.hard_timeout = 0

        msg.match.dl_type = 0x0800

        msg.match.nw_dst = "10.0.0.14"

        msg.actions.append(of.ofp_action_output(port=19))

        core.openflow.getConnection(s1_dpid).send(msg)

        turn4 = 9

        return

    if turn4 == 9:
        msg = of.ofp_flow_mod()

        msg.command = of.OFPFC_MODIFY_STRICT

        msg.priority = 100

        msg.idle_timeout = 0

        msg.hard_timeout = 0

        msg.match.dl_type = 0x0800

        msg.match.nw_dst = "10.0.0.14"

        msg.actions.append(of.ofp_action_output(port=20))

        core.openflow.getConnection(s1_dpid).send(msg)

        turn4 = 10

        return

    if turn4 == 10:
        msg = of.ofp_flow_mod()

        msg.command = of.OFPFC_MODIFY_STRICT

        msg.priority = 100

        msg.idle_timeout = 0

        msg.hard_timeout = 0

        msg.match.dl_type = 0x0800

        msg.match.nw_dst = "10.0.0.14"

        msg.actions.append(of.ofp_action_output(port=21))

        core.openflow.getConnection(s1_dpid).send(msg)

        turn4 = 11

        return

    if turn4 == 11:
        msg = of.ofp_flow_mod()

        msg.command = of.OFPFC_MODIFY_STRICT

        msg.priority = 100

        msg.idle_timeout = 0

        msg.hard_timeout = 0

        msg.match.dl_type = 0x0800

        msg.match.nw_dst = "10.0.0.14"

        msg.actions.append(of.ofp_action_output(port=22))

        core.openflow.getConnection(s1_dpid).send(msg)

        turn4 = 12

        return

    if turn4 == 12:
        msg = of.ofp_flow_mod()

        msg.command = of.OFPFC_MODIFY_STRICT

        msg.priority = 100

        msg.idle_timeout = 0

        msg.hard_timeout = 0

        msg.match.dl_type = 0x0800

        msg.match.nw_dst = "10.0.0.14"

        msg.actions.append(of.ofp_action_output(port=23))

        core.openflow.getConnection(s1_dpid).send(msg)

        turn4 = 13

        return

    if turn4 == 13:
        msg = of.ofp_flow_mod()

        msg.command = of.OFPFC_MODIFY_STRICT

        msg.priority = 100

        msg.idle_timeout = 0

        msg.hard_timeout = 0

        msg.match.dl_type = 0x0800

        msg.match.nw_dst = "10.0.0.14"

        msg.actions.append(of.ofp_action_output(port=24))

        core.openflow.getConnection(s1_dpid).send(msg)

        turn1 = 14

        return

    if turn1 == 14:
        msg = of.ofp_flow_mod()

        msg.command = of.OFPFC_MODIFY_STRICT

        msg.priority = 100

        msg.idle_timeout = 0

        msg.hard_timeout = 0

        msg.match.dl_type = 0x0800

        msg.match.nw_dst = "10.0.0.14"

        msg.actions.append(of.ofp_action_output(port=25))

        core.openflow.getConnection(s1_dpid).send(msg)

        turn4 = 15

        return

    if turn4 == 15:
        msg = of.ofp_flow_mod()

        msg.command = of.OFPFC_MODIFY_STRICT

        msg.priority = 100

        msg.idle_timeout = 0

        msg.hard_timeout = 0

        msg.match.dl_type = 0x0800
		
        msg.match.nw_dst = "10.0.0.14"

        msg.actions.append(of.ofp_action_output(port=26))

        core.openflow.getConnection(s1_dpid).send(msg)

        turn4 = 16

        return

    if turn4 == 16:
        msg = of.ofp_flow_mod()

        msg.command = of.OFPFC_MODIFY_STRICT

        msg.priority = 100

        msg.idle_timeout = 0

        msg.hard_timeout = 0

        msg.match.dl_type = 0x0800

        msg.match.nw_dst = "10.0.0.14"

        msg.actions.append(of.ofp_action_output(port=27))

        core.openflow.getConnection(s1_dpid).send(msg)

        turn4 = 17

        return

    if turn4 == 17:
        msg = of.ofp_flow_mod()

        msg.command = of.OFPFC_MODIFY_STRICT

        msg.priority = 100

        msg.idle_timeout = 0

        msg.hard_timeout = 0

        msg.match.dl_type = 0x0800

        msg.match.nw_dst = "10.0.0.14"

        msg.actions.append(of.ofp_action_output(port=28))

        core.openflow.getConnection(s1_dpid).send(msg)

        turn4 = 18

        return

    if turn4 == 18:
        msg = of.ofp_flow_mod()

        msg.command = of.OFPFC_MODIFY_STRICT

        msg.priority = 100

        msg.idle_timeout = 0

        msg.hard_timeout = 0

        msg.match.dl_type = 0x0800

        msg.match.nw_dst = "10.0.0.14"

        msg.actions.append(of.ofp_action_output(port=29))

        core.openflow.getConnection(s1_dpid).send(msg)

        turn4 = 19

        return

    if turn4 == 19:
        msg = of.ofp_flow_mod()

        msg.command = of.OFPFC_MODIFY_STRICT

        msg.priority = 100

        msg.idle_timeout = 0

        msg.hard_timeout = 0

        msg.match.dl_type = 0x0800

        msg.match.nw_dst = "10.0.0.14"

        msg.actions.append(of.ofp_action_output(port=30))

        core.openflow.getConnection(s1_dpid).send(msg)

        turn4 = 0

        return

def _timer_func5():
    global s1_dpid, s2_dpid, s3_dpid, s4_dpid, s5_dpid, s6_dpid, s7_dpid, s8_dpid, s9_dpid, s10_dpid, s11_dpid, s12_dpid, s13_dpid, s14_dpid
    global s15_dpid, s16_dpid, s17_dpid, s18_dpid, s19_dpid, s20_dpid, s21_dpid, s22_dpid
    global turn1, turn2, turn3, turn4, turn5, turn6, turn7, turn8, turn9,turn10,count

    if turn5 == 0:
        msg = of.ofp_flow_mod()

        msg.command = of.OFPFC_MODIFY_STRICT

        msg.priority = 100

        msg.idle_timeout = 0

        msg.hard_timeout = 0

        msg.match.dl_type = 0x0800

        msg.match.nw_dst = "10.0.0.15"

        msg.actions.append(of.ofp_action_output(port=11))

        core.openflow.getConnection(s1_dpid).send(msg)

        turn5 = 1

        return

    if turn5 == 1:
        msg = of.ofp_flow_mod()

        msg.command = of.OFPFC_MODIFY_STRICT

        msg.priority = 100

        msg.idle_timeout = 0

        msg.hard_timeout = 0

        msg.match.dl_type = 0x0800

        msg.match.nw_dst = "10.0.0.15"

        msg.actions.append(of.ofp_action_output(port=12))

        core.openflow.getConnection(s1_dpid).send(msg)

        turn5 = 2

        return

    if turn5 == 2:
        msg = of.ofp_flow_mod()

        msg.command = of.OFPFC_MODIFY_STRICT

        msg.priority = 100

        msg.idle_timeout = 0

        msg.hard_timeout = 0

        msg.match.dl_type = 0x0800

        msg.match.nw_dst = "10.0.0.15"

        msg.actions.append(of.ofp_action_output(port=13))

        core.openflow.getConnection(s1_dpid).send(msg)

        turn5 = 3

        return

    if turn5 == 3:
        msg = of.ofp_flow_mod()

        msg.command = of.OFPFC_MODIFY_STRICT

        msg.priority = 100

        msg.idle_timeout = 0

        msg.hard_timeout = 0

        msg.match.dl_type = 0x0800

        msg.match.nw_dst = "10.0.0.15"

        msg.actions.append(of.ofp_action_output(port=14))

        core.openflow.getConnection(s1_dpid).send(msg)

        turn5 = 4

        return

    if turn5 == 4:
        msg = of.ofp_flow_mod()

        msg.command = of.OFPFC_MODIFY_STRICT

        msg.priority = 100

        msg.idle_timeout = 0

        msg.hard_timeout = 0

        msg.match.dl_type = 0x0800

        msg.match.nw_dst = "10.0.0.15"

        msg.actions.append(of.ofp_action_output(port=15))

        core.openflow.getConnection(s1_dpid).send(msg)

        turn5 = 5

        return

    if turn5 == 5:
        msg = of.ofp_flow_mod()

        msg.command = of.OFPFC_MODIFY_STRICT

        msg.priority = 100

        msg.idle_timeout = 0

        msg.hard_timeout = 0

        msg.match.dl_type = 0x0800

        msg.match.nw_dst = "10.0.0.15"

        msg.actions.append(of.ofp_action_output(port=16))

        core.openflow.getConnection(s1_dpid).send(msg)

        turn5 = 6

        return

    if turn5 == 6:
        msg = of.ofp_flow_mod()

        msg.command = of.OFPFC_MODIFY_STRICT

        msg.priority = 100

        msg.idle_timeout = 0

        msg.hard_timeout = 0

        msg.match.dl_type = 0x0800

        msg.match.nw_dst = "10.0.0.15"

        msg.actions.append(of.ofp_action_output(port=17))

        core.openflow.getConnection(s1_dpid).send(msg)

        turn5 = 7

        return

    if turn5 == 7:
        msg = of.ofp_flow_mod()

        msg.command = of.OFPFC_MODIFY_STRICT

        msg.priority = 100

        msg.idle_timeout = 0

        msg.hard_timeout = 0

        msg.match.dl_type = 0x0800

        msg.match.nw_dst = "10.0.0.15"

        msg.actions.append(of.ofp_action_output(port=18))

        core.openflow.getConnection(s1_dpid).send(msg)

        turn5 = 8

        return

    if turn5 == 8:
        msg = of.ofp_flow_mod()

        msg.command = of.OFPFC_MODIFY_STRICT

        msg.priority = 100

        msg.idle_timeout = 0

        msg.hard_timeout = 0

        msg.match.dl_type = 0x0800

        msg.match.nw_dst = "10.0.0.15"

        msg.actions.append(of.ofp_action_output(port=19))

        core.openflow.getConnection(s1_dpid).send(msg)

        turn5 = 9

        return

    if turn5 == 9:
        msg = of.ofp_flow_mod()

        msg.command = of.OFPFC_MODIFY_STRICT

        msg.priority = 100

        msg.idle_timeout = 0

        msg.hard_timeout = 0

        msg.match.dl_type = 0x0800

        msg.match.nw_dst = "10.0.0.15"

        msg.actions.append(of.ofp_action_output(port=20))

        core.openflow.getConnection(s1_dpid).send(msg)

        turn5 = 10

        return

    if turn5 == 10:
        msg = of.ofp_flow_mod()

        msg.command = of.OFPFC_MODIFY_STRICT

        msg.priority = 100

        msg.idle_timeout = 0

        msg.hard_timeout = 0

        msg.match.dl_type = 0x0800

        msg.match.nw_dst = "10.0.0.15"

        msg.actions.append(of.ofp_action_output(port=21))

        core.openflow.getConnection(s1_dpid).send(msg)

        turn5 = 11

        return

    if turn5 == 11:
        msg = of.ofp_flow_mod()

        msg.command = of.OFPFC_MODIFY_STRICT

        msg.priority = 100

        msg.idle_timeout = 0

        msg.hard_timeout = 0

        msg.match.dl_type = 0x0800

        msg.match.nw_dst = "10.0.0.15"

        msg.actions.append(of.ofp_action_output(port=22))

        core.openflow.getConnection(s1_dpid).send(msg)

        turn5 = 12

        return

    if turn5 == 12:
        msg = of.ofp_flow_mod()

        msg.command = of.OFPFC_MODIFY_STRICT

        msg.priority = 100

        msg.idle_timeout = 0

        msg.hard_timeout = 0

        msg.match.dl_type = 0x0800

        msg.match.nw_dst = "10.0.0.15"

        msg.actions.append(of.ofp_action_output(port=23))

        core.openflow.getConnection(s1_dpid).send(msg)

        turn5 = 15

        return

    if turn5 == 13:
        msg = of.ofp_flow_mod()

        msg.command = of.OFPFC_MODIFY_STRICT

        msg.priority = 100

        msg.idle_timeout = 0

        msg.hard_timeout = 0

        msg.match.dl_type = 0x0800

        msg.match.nw_dst = "10.0.0.15"

        msg.actions.append(of.ofp_action_output(port=24))

        core.openflow.getConnection(s1_dpid).send(msg)

        turn5 = 14

        return

    if turn5 == 14:
        msg = of.ofp_flow_mod()

        msg.command = of.OFPFC_MODIFY_STRICT

        msg.priority = 100

        msg.idle_timeout = 0

        msg.hard_timeout = 0

        msg.match.dl_type = 0x0800

        msg.match.nw_dst = "10.0.0.15"

        msg.actions.append(of.ofp_action_output(port=25))

        core.openflow.getConnection(s1_dpid).send(msg)

        turn5 = 15

        return

    if turn5 == 15:
        msg = of.ofp_flow_mod()

        msg.command = of.OFPFC_MODIFY_STRICT

        msg.priority = 100

        msg.idle_timeout = 0

        msg.hard_timeout = 0

        msg.match.dl_type = 0x0800

        msg.match.nw_dst = "10.0.0.15"

        msg.actions.append(of.ofp_action_output(port=26))

        core.openflow.getConnection(s1_dpid).send(msg)

        turn5 = 16

        return

    if turn5 == 16:
        msg = of.ofp_flow_mod()

        msg.command = of.OFPFC_MODIFY_STRICT

        msg.priority = 100

        msg.idle_timeout = 0

        msg.hard_timeout = 0

        msg.match.dl_type = 0x0800

        msg.match.nw_dst = "10.0.0.15"

        msg.actions.append(of.ofp_action_output(port=27))

        core.openflow.getConnection(s1_dpid).send(msg)

        turn5 = 17

        return

    if turn5 == 17:
        msg = of.ofp_flow_mod()

        msg.command = of.OFPFC_MODIFY_STRICT

        msg.priority = 100

        msg.idle_timeout = 0

        msg.hard_timeout = 0

        msg.match.dl_type = 0x0800

        msg.match.nw_dst = "10.0.0.15"

        msg.actions.append(of.ofp_action_output(port=28))

        core.openflow.getConnection(s1_dpid).send(msg)

        turn5 = 18

        return

    if turn5 == 18:
        msg = of.ofp_flow_mod()

        msg.command = of.OFPFC_MODIFY_STRICT

        msg.priority = 100

        msg.idle_timeout = 0

        msg.hard_timeout = 0

        msg.match.dl_type = 0x0800

        msg.match.nw_dst = "10.0.0.15"

        msg.actions.append(of.ofp_action_output(port=29))

        core.openflow.getConnection(s1_dpid).send(msg)

        turn5 = 19

        return

    if turn5 == 19:
        msg = of.ofp_flow_mod()

        msg.command = of.OFPFC_MODIFY_STRICT

        msg.priority = 100

        msg.idle_timeout = 0

        msg.hard_timeout = 0

        msg.match.dl_type = 0x0800

        msg.match.nw_dst = "10.0.0.15"

        msg.actions.append(of.ofp_action_output(port=30))

        core.openflow.getConnection(s1_dpid).send(msg)

        turn5 = 0

        return

def _timer_func6():
    global s1_dpid, s2_dpid, s3_dpid, s4_dpid, s5_dpid, s6_dpid, s7_dpid, s8_dpid, s9_dpid, s10_dpid, s11_dpid, s12_dpid, s13_dpid, s14_dpid
    global s15_dpid, s16_dpid, s17_dpid, s18_dpid, s19_dpid, s20_dpid, s21_dpid, s22_dpid
    global turn1, turn2, turn3, turn4, turn5, turn6, turn7, turn8, turn9,turn10,count

    if turn6 == 0:
        msg = of.ofp_flow_mod()

        msg.command = of.OFPFC_MODIFY_STRICT

        msg.priority = 100

        msg.idle_timeout = 0

        msg.hard_timeout = 0

        msg.match.dl_type = 0x0800

        msg.match.nw_dst = "10.0.0.16"

        msg.actions.append(of.ofp_action_output(port=11))

        core.openflow.getConnection(s1_dpid).send(msg)

        turn6 = 1

        return

    if turn6 == 1:
        msg = of.ofp_flow_mod()

        msg.command = of.OFPFC_MODIFY_STRICT

        msg.priority = 100

        msg.idle_timeout = 0

        msg.hard_timeout = 0

        msg.match.dl_type = 0x0800

        msg.match.nw_dst = "10.0.0.16"

        msg.actions.append(of.ofp_action_output(port=12))

        core.openflow.getConnection(s1_dpid).send(msg)

        turn6 = 2

        return

    if turn6 == 2:
        msg = of.ofp_flow_mod()

        msg.command = of.OFPFC_MODIFY_STRICT

        msg.priority = 100

        msg.idle_timeout = 0

        msg.hard_timeout = 0

        msg.match.dl_type = 0x0800

        msg.match.nw_dst = "10.0.0.16"

        msg.actions.append(of.ofp_action_output(port=13))

        core.openflow.getConnection(s1_dpid).send(msg)

        turn6 = 3

        return

    if turn6 == 3:
        msg = of.ofp_flow_mod()

        msg.command = of.OFPFC_MODIFY_STRICT

        msg.priority = 100

        msg.idle_timeout = 0

        msg.hard_timeout = 0

        msg.match.dl_type = 0x0800

        msg.match.nw_dst = "10.0.0.16"

        msg.actions.append(of.ofp_action_output(port=14))

        core.openflow.getConnection(s1_dpid).send(msg)

        turn6 = 4

        return

    if turn6 == 4:
        msg = of.ofp_flow_mod()

        msg.command = of.OFPFC_MODIFY_STRICT

        msg.priority = 100

        msg.idle_timeout = 0

        msg.hard_timeout = 0

        msg.match.dl_type = 0x0800

        msg.match.nw_dst = "10.0.0.16"

        msg.actions.append(of.ofp_action_output(port=15))

        core.openflow.getConnection(s1_dpid).send(msg)

        turn6 = 5

        return

    if turn6 == 5:
        msg = of.ofp_flow_mod()

        msg.command = of.OFPFC_MODIFY_STRICT

        msg.priority = 100

        msg.idle_timeout = 0

        msg.hard_timeout = 0

        msg.match.dl_type = 0x0800

        msg.match.nw_dst = "10.0.0.16"

        msg.actions.append(of.ofp_action_output(port=16))

        core.openflow.getConnection(s1_dpid).send(msg)

        turn6 = 6

        return

    if turn6 == 6:
        msg = of.ofp_flow_mod()

        msg.command = of.OFPFC_MODIFY_STRICT

        msg.priority = 100

        msg.idle_timeout = 0

        msg.hard_timeout = 0

        msg.match.dl_type = 0x0800

        msg.match.nw_dst = "10.0.0.16"

        msg.actions.append(of.ofp_action_output(port=17))

        core.openflow.getConnection(s1_dpid).send(msg)

        turn6 = 7

        return

    if turn6 == 7:
        msg = of.ofp_flow_mod()

        msg.command = of.OFPFC_MODIFY_STRICT

        msg.priority = 100

        msg.idle_timeout = 0

        msg.hard_timeout = 0

        msg.match.dl_type = 0x0800

        msg.match.nw_dst = "10.0.0.16"

        msg.actions.append(of.ofp_action_output(port=18))

        core.openflow.getConnection(s1_dpid).send(msg)

        turn6 = 8

        return

    if turn6 == 8:
        msg = of.ofp_flow_mod()

        msg.command = of.OFPFC_MODIFY_STRICT

        msg.priority = 100

        msg.idle_timeout = 0

        msg.hard_timeout = 0

        msg.match.dl_type = 0x0800

        msg.match.nw_dst = "10.0.0.16"

        msg.actions.append(of.ofp_action_output(port=19))

        core.openflow.getConnection(s1_dpid).send(msg)

        turn6 = 9

        return

    if turn6 == 9:
        msg = of.ofp_flow_mod()

        msg.command = of.OFPFC_MODIFY_STRICT

        msg.priority = 100

        msg.idle_timeout = 0

        msg.hard_timeout = 0

        msg.match.dl_type = 0x0800

        msg.match.nw_dst = "10.0.0.16"

        msg.actions.append(of.ofp_action_output(port=20))

        core.openflow.getConnection(s1_dpid).send(msg)

        turn6 = 10

        return

    if turn6 == 10:
        msg = of.ofp_flow_mod()

        msg.command = of.OFPFC_MODIFY_STRICT

        msg.priority = 100

        msg.idle_timeout = 0

        msg.hard_timeout = 0

        msg.match.dl_type = 0x0800

        msg.match.nw_dst = "10.0.0.16"

        msg.actions.append(of.ofp_action_output(port=21))

        core.openflow.getConnection(s1_dpid).send(msg)

        turn6 = 11

        return

    if turn6 == 11:
        msg = of.ofp_flow_mod()

        msg.command = of.OFPFC_MODIFY_STRICT

        msg.priority = 100

        msg.idle_timeout = 0

        msg.hard_timeout = 0

        msg.match.dl_type = 0x0800

        msg.match.nw_dst = "10.0.0.16"

        msg.actions.append(of.ofp_action_output(port=22))

        core.openflow.getConnection(s1_dpid).send(msg)

        turn6 = 12

        return

    if turn6 == 12:
        msg = of.ofp_flow_mod()

        msg.command = of.OFPFC_MODIFY_STRICT

        msg.priority = 100

        msg.idle_timeout = 0

        msg.hard_timeout = 0

        msg.match.dl_type = 0x0800

        msg.match.nw_dst = "10.0.0.16"

        msg.actions.append(of.ofp_action_output(port=23))

        core.openflow.getConnection(s1_dpid).send(msg)

        turn6 = 13

        return

    if turn6 == 13:
        msg = of.ofp_flow_mod()

        msg.command = of.OFPFC_MODIFY_STRICT

        msg.priority = 100

        msg.idle_timeout = 0

        msg.hard_timeout = 0

        msg.match.dl_type = 0x0800

        msg.match.nw_dst = "10.0.0.16"

        msg.actions.append(of.ofp_action_output(port=24))

        core.openflow.getConnection(s1_dpid).send(msg)

        turn6 = 14

        return

    if turn6 == 14:
        msg = of.ofp_flow_mod()

        msg.command = of.OFPFC_MODIFY_STRICT

        msg.priority = 100

        msg.idle_timeout = 0

        msg.hard_timeout = 0

        msg.match.dl_type = 0x0800

        msg.match.nw_dst = "10.0.0.16"

        msg.actions.append(of.ofp_action_output(port=25))

        core.openflow.getConnection(s1_dpid).send(msg)

        turn6 = 15

        return

    if turn6 == 15:
        msg = of.ofp_flow_mod()

        msg.command = of.OFPFC_MODIFY_STRICT

        msg.priority = 100

        msg.idle_timeout = 0

        msg.hard_timeout = 0

        msg.match.dl_type = 0x0800

        msg.match.nw_dst = "10.0.0.16"

        msg.actions.append(of.ofp_action_output(port=26))

        core.openflow.getConnection(s1_dpid).send(msg)

        turn6 = 16

        return

    if turn6 == 16:
        msg = of.ofp_flow_mod()

        msg.command = of.OFPFC_MODIFY_STRICT

        msg.priority = 100

        msg.idle_timeout = 0

        msg.hard_timeout = 0

        msg.match.dl_type = 0x0800

        msg.match.nw_dst = "10.0.0.16"

        msg.actions.append(of.ofp_action_output(port=27))

        core.openflow.getConnection(s1_dpid).send(msg)

        turn6 = 17

        return

    if turn6 == 17:
        msg = of.ofp_flow_mod()

        msg.command = of.OFPFC_MODIFY_STRICT

        msg.priority = 100

        msg.idle_timeout = 0

        msg.hard_timeout = 0

        msg.match.dl_type = 0x0800

        msg.match.nw_dst = "10.0.0.16"

        msg.actions.append(of.ofp_action_output(port=28))

        core.openflow.getConnection(s1_dpid).send(msg)

        turn6 = 18

        return

    if turn6 == 18:
        msg = of.ofp_flow_mod()

        msg.command = of.OFPFC_MODIFY_STRICT

        msg.priority = 100

        msg.idle_timeout = 0

        msg.hard_timeout = 0

        msg.match.dl_type = 0x0800

        msg.match.nw_dst = "10.0.0.16"

        msg.actions.append(of.ofp_action_output(port=29))

        core.openflow.getConnection(s1_dpid).send(msg)

        turn6 = 19

        return

    if turn6 == 19:
        msg = of.ofp_flow_mod()

        msg.command = of.OFPFC_MODIFY_STRICT

        msg.priority = 100

        msg.idle_timeout = 0

        msg.hard_timeout = 0

        msg.match.dl_type = 0x0800

        msg.match.nw_dst = "10.0.0.16"

        msg.actions.append(of.ofp_action_output(port=30))

        core.openflow.getConnection(s1_dpid).send(msg)

        turn6 = 0

        return

def _timer_func7():
    global s1_dpid, s2_dpid, s3_dpid, s4_dpid, s5_dpid, s6_dpid, s7_dpid, s8_dpid, s9_dpid, s10_dpid, s11_dpid, s12_dpid, s13_dpid, s14_dpid
    global s15_dpid, s16_dpid, s17_dpid, s18_dpid, s19_dpid, s20_dpid, s21_dpid, s22_dpid
    global turn1, turn2, turn3, turn4, turn5, turn6, turn7, turn8, turn9,turn10,count

    if count < 200:
        msg = of.ofp_flow_mod()

        msg.command = of.OFPFC_MODIFY_STRICT

        msg.priority = 100

        msg.idle_timeout = 0

        msg.hard_timeout = 0

        msg.match.dl_type = 0x0800

        msg.match.nw_dst = "10.0.0.17"

        msg.actions.append(of.ofp_action_output(port=17))

        core.openflow.getConnection(s1_dpid).send(msg)

    else:
        if turn7 == 0:
            msg = of.ofp_flow_mod()

            msg.command = of.OFPFC_MODIFY_STRICT

            msg.priority = 100

            msg.idle_timeout = 0

            msg.hard_timeout = 0

            msg.match.dl_type = 0x0800

            msg.match.nw_dst = "10.0.0.17"

            msg.actions.append(of.ofp_action_output(port=11))

            core.openflow.getConnection(s1_dpid).send(msg)

            turn7 = 1

            return

        if turn7 == 1:
            msg = of.ofp_flow_mod()

            msg.command = of.OFPFC_MODIFY_STRICT

            msg.priority = 100

            msg.idle_timeout = 0

            msg.hard_timeout = 0

            msg.match.dl_type = 0x0800

            msg.match.nw_dst = "10.0.0.17"

            msg.actions.append(of.ofp_action_output(port=12))

            core.openflow.getConnection(s1_dpid).send(msg)

            turn7 = 2

            return

        if turn7 == 2:
            msg = of.ofp_flow_mod()

            msg.command = of.OFPFC_MODIFY_STRICT

            msg.priority = 100

            msg.idle_timeout = 0

            msg.hard_timeout = 0

            msg.match.dl_type = 0x0800

            msg.match.nw_dst = "10.0.0.17"

            msg.actions.append(of.ofp_action_output(port=13))

            core.openflow.getConnection(s1_dpid).send(msg)

            turn7 = 3

            return

        if turn7 == 3:
            msg = of.ofp_flow_mod()

            msg.command = of.OFPFC_MODIFY_STRICT

            msg.priority = 100

            msg.idle_timeout = 0

            msg.hard_timeout = 0

            msg.match.dl_type = 0x0800

            msg.match.nw_dst = "10.0.0.17"

            msg.actions.append(of.ofp_action_output(port=14))

            core.openflow.getConnection(s1_dpid).send(msg)

            turn7 = 4

            return

        if turn7 == 4:
            msg = of.ofp_flow_mod()

            msg.command = of.OFPFC_MODIFY_STRICT

            msg.priority = 100

            msg.idle_timeout = 0

            msg.hard_timeout = 0

            msg.match.dl_type = 0x0800

            msg.match.nw_dst = "10.0.0.17"

            msg.actions.append(of.ofp_action_output(port=15))

            core.openflow.getConnection(s1_dpid).send(msg)

            turn7 = 5

            return

        if turn7 == 5:
            msg = of.ofp_flow_mod()

            msg.command = of.OFPFC_MODIFY_STRICT

            msg.priority = 100

            msg.idle_timeout = 0

            msg.hard_timeout = 0

            msg.match.dl_type = 0x0800

            msg.match.nw_dst = "10.0.0.17"

            msg.actions.append(of.ofp_action_output(port=16))

            core.openflow.getConnection(s1_dpid).send(msg)

            turn7 = 6

            return

        if turn7 == 6:
            msg = of.ofp_flow_mod()

            msg.command = of.OFPFC_MODIFY_STRICT

            msg.priority = 100

            msg.idle_timeout = 0

            msg.hard_timeout = 0

            msg.match.dl_type = 0x0800

            msg.match.nw_dst = "10.0.0.17"

            msg.actions.append(of.ofp_action_output(port=17))

            core.openflow.getConnection(s1_dpid).send(msg)

            turn7 = 7

            return

        if turn7 == 7:
            msg = of.ofp_flow_mod()

            msg.command = of.OFPFC_MODIFY_STRICT

            msg.priority = 100

            msg.idle_timeout = 0

            msg.hard_timeout = 0

            msg.match.dl_type = 0x0800

            msg.match.nw_dst = "10.0.0.17"

            msg.actions.append(of.ofp_action_output(port=18))

            core.openflow.getConnection(s1_dpid).send(msg)

            turn7 = 8

            return

        if turn7 == 8:
            msg = of.ofp_flow_mod()

            msg.command = of.OFPFC_MODIFY_STRICT

            msg.priority = 100

            msg.idle_timeout = 0

            msg.hard_timeout = 0

            msg.match.dl_type = 0x0800

            msg.match.nw_dst = "10.0.0.17"

            msg.actions.append(of.ofp_action_output(port=19))

            core.openflow.getConnection(s1_dpid).send(msg)

            turn7 = 9

            return

        if turn7 == 9:
            msg = of.ofp_flow_mod()

            msg.command = of.OFPFC_MODIFY_STRICT

            msg.priority = 100

            msg.idle_timeout = 0

            msg.hard_timeout = 0

            msg.match.dl_type = 0x0800

            msg.match.nw_dst = "10.0.0.17"

            msg.actions.append(of.ofp_action_output(port=20))

            core.openflow.getConnection(s1_dpid).send(msg)

            turn7 = 10

            return

        if turn7 == 10:
            msg = of.ofp_flow_mod()

            msg.command = of.OFPFC_MODIFY_STRICT

            msg.priority = 100

            msg.idle_timeout = 0

            msg.hard_timeout = 0

            msg.match.dl_type = 0x0800

            msg.match.nw_dst = "10.0.0.17"

            msg.actions.append(of.ofp_action_output(port=21))

            core.openflow.getConnection(s1_dpid).send(msg)

            turn7 = 11

            return

        if turn7 == 11:
            msg = of.ofp_flow_mod()

            msg.command = of.OFPFC_MODIFY_STRICT

            msg.priority = 100

            msg.idle_timeout = 0

            msg.hard_timeout = 0

            msg.match.dl_type = 0x0800

            msg.match.nw_dst = "10.0.0.17"

            msg.actions.append(of.ofp_action_output(port=22))

            core.openflow.getConnection(s1_dpid).send(msg)

            turn7 = 12

            return

        if turn7 == 12:
            msg = of.ofp_flow_mod()

            msg.command = of.OFPFC_MODIFY_STRICT

            msg.priority = 100

            msg.idle_timeout = 0

            msg.hard_timeout = 0

            msg.match.dl_type = 0x0800

            msg.match.nw_dst = "10.0.0.17"

            msg.actions.append(of.ofp_action_output(port=23))

            core.openflow.getConnection(s1_dpid).send(msg)

            turn7 = 13

            return

        if turn7 == 13:
            msg = of.ofp_flow_mod()

            msg.command = of.OFPFC_MODIFY_STRICT

            msg.priority = 100

            msg.idle_timeout = 0

            msg.hard_timeout = 0

            msg.match.dl_type = 0x0800

            msg.match.nw_dst = "10.0.0.17"

            msg.actions.append(of.ofp_action_output(port=24))

            core.openflow.getConnection(s1_dpid).send(msg)

            turn7 = 14

            return

        if turn7 == 14:
            msg = of.ofp_flow_mod()

            msg.command = of.OFPFC_MODIFY_STRICT

            msg.priority = 100

            msg.idle_timeout = 0

            msg.hard_timeout = 0

            msg.match.dl_type = 0x0800

            msg.match.nw_dst = "10.0.0.17"

            msg.actions.append(of.ofp_action_output(port=25))

            core.openflow.getConnection(s1_dpid).send(msg)

            turn7 = 15

            return

        if turn7 == 15:
            msg = of.ofp_flow_mod()

            msg.command = of.OFPFC_MODIFY_STRICT

            msg.priority = 100

            msg.idle_timeout = 0

            msg.hard_timeout = 0

            msg.match.dl_type = 0x0800

            msg.match.nw_dst = "10.0.0.17"

            msg.actions.append(of.ofp_action_output(port=26))

            core.openflow.getConnection(s1_dpid).send(msg)

            turn7 = 16

            return

        if turn7 == 16:
            msg = of.ofp_flow_mod()

            msg.command = of.OFPFC_MODIFY_STRICT

            msg.priority = 100

            msg.idle_timeout = 0

            msg.hard_timeout = 0

            msg.match.dl_type = 0x0800

            msg.match.nw_dst = "10.0.0.17"

            msg.actions.append(of.ofp_action_output(port=27))

            core.openflow.getConnection(s1_dpid).send(msg)

            turn7 = 17

            return

        if turn7 == 17:
            msg = of.ofp_flow_mod()

            msg.command = of.OFPFC_MODIFY_STRICT

            msg.priority = 100

            msg.idle_timeout = 0

            msg.hard_timeout = 0

            msg.match.dl_type = 0x0800

            msg.match.nw_dst = "10.0.0.17"

            msg.actions.append(of.ofp_action_output(port=28))

            core.openflow.getConnection(s1_dpid).send(msg)

            turn7 = 18

            return

        if turn7 == 18:
            msg = of.ofp_flow_mod()

            msg.command = of.OFPFC_MODIFY_STRICT

            msg.priority = 100

            msg.idle_timeout = 0

            msg.hard_timeout = 0

            msg.match.dl_type = 0x0800

            msg.match.nw_dst = "10.0.0.17"

            msg.actions.append(of.ofp_action_output(port=29))

            core.openflow.getConnection(s1_dpid).send(msg)

            turn7 = 19

            return

        if turn7 == 19:
            msg = of.ofp_flow_mod()

            msg.command = of.OFPFC_MODIFY_STRICT

            msg.priority = 100

            msg.idle_timeout = 0

            msg.hard_timeout = 0

            msg.match.dl_type = 0x0800

            msg.match.nw_dst = "10.0.0.17"

            msg.actions.append(of.ofp_action_output(port=30))

            core.openflow.getConnection(s1_dpid).send(msg)

            turn7 = 0

            return


def _timer_func8():
    global s1_dpid, s2_dpid, s3_dpid, s4_dpid, s5_dpid, s6_dpid, s7_dpid, s8_dpid, s9_dpid, s10_dpid, s11_dpid, s12_dpid, s13_dpid, s14_dpid
    global s15_dpid, s16_dpid, s17_dpid, s18_dpid, s19_dpid, s20_dpid, s21_dpid, s22_dpid
    global turn1, turn2, turn3, turn4, turn5, turn6, turn7, turn8, turn9,turn10,count

    if count < 200:
        msg = of.ofp_flow_mod()

        msg.command = of.OFPFC_MODIFY_STRICT

        msg.priority = 100

        msg.idle_timeout = 0

        msg.hard_timeout = 0

        msg.match.dl_type = 0x0800

        msg.match.nw_dst = "10.0.0.18"

        msg.actions.append(of.ofp_action_output(port=18))

        core.openflow.getConnection(s1_dpid).send(msg)

        return

    else:
        if turn8 == 0:
            msg = of.ofp_flow_mod()

            msg.command = of.OFPFC_MODIFY_STRICT

            msg.priority = 100

            msg.idle_timeout = 0

            msg.hard_timeout = 0

            msg.match.dl_type = 0x0800

            msg.match.nw_dst = "10.0.0.18"

            msg.actions.append(of.ofp_action_output(port=11))

            core.openflow.getConnection(s1_dpid).send(msg)

            turn8 = 1

            return

        if turn8 == 1:
            msg = of.ofp_flow_mod()

            msg.command = of.OFPFC_MODIFY_STRICT

            msg.priority = 100

            msg.idle_timeout = 0

            msg.hard_timeout = 0

            msg.match.dl_type = 0x0800

            msg.match.nw_dst = "10.0.0.18"

            msg.actions.append(of.ofp_action_output(port=12))

            core.openflow.getConnection(s1_dpid).send(msg)

            turn8 = 2

            return

        if turn8 == 2:
            msg = of.ofp_flow_mod()

            msg.command = of.OFPFC_MODIFY_STRICT

            msg.priority = 100

            msg.idle_timeout = 0

            msg.hard_timeout = 0

            msg.match.dl_type = 0x0800

            msg.match.nw_dst = "10.0.0.18"

            msg.actions.append(of.ofp_action_output(port=13))

            core.openflow.getConnection(s1_dpid).send(msg)

            turn8 = 3

            return

        if turn8 == 3:
            msg = of.ofp_flow_mod()

            msg.command = of.OFPFC_MODIFY_STRICT

            msg.priority = 100

            msg.idle_timeout = 0

            msg.hard_timeout = 0

            msg.match.dl_type = 0x0800

            msg.match.nw_dst = "10.0.0.18"

            msg.actions.append(of.ofp_action_output(port=14))

            core.openflow.getConnection(s1_dpid).send(msg)

            turn8 = 4

            return

        if turn8 == 4:
            msg = of.ofp_flow_mod()

            msg.command = of.OFPFC_MODIFY_STRICT

            msg.priority = 100

            msg.idle_timeout = 0

            msg.hard_timeout = 0

            msg.match.dl_type = 0x0800

            msg.match.nw_dst = "10.0.0.18"

            msg.actions.append(of.ofp_action_output(port=15))

            core.openflow.getConnection(s1_dpid).send(msg)

            turn8 = 5

            return

        if turn8 == 5:
            msg = of.ofp_flow_mod()

            msg.command = of.OFPFC_MODIFY_STRICT

            msg.priority = 100

            msg.idle_timeout = 0

            msg.hard_timeout = 0

            msg.match.dl_type = 0x0800

            msg.match.nw_dst = "10.0.0.18"

            msg.actions.append(of.ofp_action_output(port=16))

            core.openflow.getConnection(s1_dpid).send(msg)

            turn8 = 6

            return

        if turn8 == 6:
            msg = of.ofp_flow_mod()

            msg.command = of.OFPFC_MODIFY_STRICT

            msg.priority = 100

            msg.idle_timeout = 0

            msg.hard_timeout = 0

            msg.match.dl_type = 0x0800

            msg.match.nw_dst = "10.0.0.18"

            msg.actions.append(of.ofp_action_output(port=17))

            core.openflow.getConnection(s1_dpid).send(msg)

            turn8 = 7

            return

        if turn8 == 7:
            msg = of.ofp_flow_mod()

            msg.command = of.OFPFC_MODIFY_STRICT

            msg.priority = 100

            msg.idle_timeout = 0

            msg.hard_timeout = 0

            msg.match.dl_type = 0x0800

            msg.match.nw_dst = "10.0.0.18"

            msg.actions.append(of.ofp_action_output(port=18))

            core.openflow.getConnection(s1_dpid).send(msg)

            turn8 = 8

            return

        if turn8 == 8:
            msg = of.ofp_flow_mod()

            msg.command = of.OFPFC_MODIFY_STRICT

            msg.priority = 100

            msg.idle_timeout = 0

            msg.hard_timeout = 0

            msg.match.dl_type = 0x0800

            msg.match.nw_dst = "10.0.0.18"

            msg.actions.append(of.ofp_action_output(port=19))

            core.openflow.getConnection(s1_dpid).send(msg)

            turn8 = 9

            return

        if turn8 == 9:
            msg = of.ofp_flow_mod()

            msg.command = of.OFPFC_MODIFY_STRICT

            msg.priority = 100

            msg.idle_timeout = 0

            msg.hard_timeout = 0

            msg.match.dl_type = 0x0800

            msg.match.nw_dst = "10.0.0.18"

            msg.actions.append(of.ofp_action_output(port=20))

            core.openflow.getConnection(s1_dpid).send(msg)

            turn8 = 10

            return

        if turn8 == 10:
            msg = of.ofp_flow_mod()

            msg.command = of.OFPFC_MODIFY_STRICT

            msg.priority = 100

            msg.idle_timeout = 0

            msg.hard_timeout = 0

            msg.match.dl_type = 0x0800

            msg.match.nw_dst = "10.0.0.18"

            msg.actions.append(of.ofp_action_output(port=21))

            core.openflow.getConnection(s1_dpid).send(msg)

            turn8 = 11

            return

        if turn8 == 11:
            msg = of.ofp_flow_mod()

            msg.command = of.OFPFC_MODIFY_STRICT

            msg.priority = 100

            msg.idle_timeout = 0

            msg.hard_timeout = 0

            msg.match.dl_type = 0x0800

            msg.match.nw_dst = "10.0.0.18"

            msg.actions.append(of.ofp_action_output(port=22))

            core.openflow.getConnection(s1_dpid).send(msg)

            turn8 = 12

            return

        if turn8 == 12:
            msg = of.ofp_flow_mod()

            msg.command = of.OFPFC_MODIFY_STRICT

            msg.priority = 100

            msg.idle_timeout = 0

            msg.hard_timeout = 0

            msg.match.dl_type = 0x0800

            msg.match.nw_dst = "10.0.0.18"

            msg.actions.append(of.ofp_action_output(port=23))

            core.openflow.getConnection(s1_dpid).send(msg)

            turn8 = 13

            return

        if turn8 == 13:
            msg = of.ofp_flow_mod()

            msg.command = of.OFPFC_MODIFY_STRICT

            msg.priority = 100

            msg.idle_timeout = 0

            msg.hard_timeout = 0

            msg.match.dl_type = 0x0800

            msg.match.nw_dst = "10.0.0.18"

            msg.actions.append(of.ofp_action_output(port=24))

            core.openflow.getConnection(s1_dpid).send(msg)

            turn8 = 14

            return

        if turn8 == 14:
            msg = of.ofp_flow_mod()

            msg.command = of.OFPFC_MODIFY_STRICT

            msg.priority = 100

            msg.idle_timeout = 0

            msg.hard_timeout = 0

            msg.match.dl_type = 0x0800

            msg.match.nw_dst = "10.0.0.18"

            msg.actions.append(of.ofp_action_output(port=25))

            core.openflow.getConnection(s1_dpid).send(msg)

            turn8 = 15

            return

        if turn8 == 15:
            msg = of.ofp_flow_mod()

            msg.command = of.OFPFC_MODIFY_STRICT

            msg.priority = 100

            msg.idle_timeout = 0

            msg.hard_timeout = 0

            msg.match.dl_type = 0x0800

            msg.match.nw_dst = "10.0.0.18"

            msg.actions.append(of.ofp_action_output(port=26))

            core.openflow.getConnection(s1_dpid).send(msg)

            turn8 = 16

            return

        if turn8 == 16:
            msg = of.ofp_flow_mod()

            msg.command = of.OFPFC_MODIFY_STRICT

            msg.priority = 100

            msg.idle_timeout = 0

            msg.hard_timeout = 0

            msg.match.dl_type = 0x0800

            msg.match.nw_dst = "10.0.0.18"

            msg.actions.append(of.ofp_action_output(port=27))

            core.openflow.getConnection(s1_dpid).send(msg)

            turn8 = 17

            return

        if turn8 == 17:
            msg = of.ofp_flow_mod()

            msg.command = of.OFPFC_MODIFY_STRICT

            msg.priority = 100

            msg.idle_timeout = 0

            msg.hard_timeout = 0

            msg.match.dl_type = 0x0800

            msg.match.nw_dst = "10.0.0.18"

            msg.actions.append(of.ofp_action_output(port=28))

            core.openflow.getConnection(s1_dpid).send(msg)

            turn8 = 18

            return

        if turn8 == 18:
            msg = of.ofp_flow_mod()

            msg.command = of.OFPFC_MODIFY_STRICT

            msg.priority = 100

            msg.idle_timeout = 0

            msg.hard_timeout = 0

            msg.match.dl_type = 0x0800

            msg.match.nw_dst = "10.0.0.18"

            msg.actions.append(of.ofp_action_output(port=29))

            core.openflow.getConnection(s1_dpid).send(msg)

            turn8 = 19

            return

        if turn8 == 19:
            msg = of.ofp_flow_mod()

            msg.command = of.OFPFC_MODIFY_STRICT

            msg.priority = 100

            msg.idle_timeout = 0

            msg.hard_timeout = 0

            msg.match.dl_type = 0x0800

            msg.match.nw_dst = "10.0.0.18"

            msg.actions.append(of.ofp_action_output(port=30))

            core.openflow.getConnection(s1_dpid).send(msg)

            turn8 = 0

            return

def _timer_func9():
    global s1_dpid, s2_dpid, s3_dpid, s4_dpid, s5_dpid, s6_dpid, s7_dpid, s8_dpid, s9_dpid, s10_dpid, s11_dpid, s12_dpid, s13_dpid, s14_dpid
    global s15_dpid, s16_dpid, s17_dpid, s18_dpid, s19_dpid, s20_dpid, s21_dpid, s22_dpid
    global turn1, turn2, turn3, turn4, turn5, turn6, turn7, turn8, turn9,turn10,count

    if count<200:
        msg = of.ofp_flow_mod()

        msg.command = of.OFPFC_MODIFY_STRICT

        msg.priority = 100

        msg.idle_timeout = 0

        msg.hard_timeout = 0

        msg.match.dl_type = 0x0800

        msg.match.nw_dst = "10.0.0.19"

        msg.actions.append(of.ofp_action_output(port=19))

        core.openflow.getConnection(s1_dpid).send(msg)

        return

    else:
        if turn9 == 0:
            msg = of.ofp_flow_mod()

            msg.command = of.OFPFC_MODIFY_STRICT

            msg.priority = 100

            msg.idle_timeout = 0

            msg.hard_timeout = 0

            msg.match.dl_type = 0x0800

            msg.match.nw_dst = "10.0.0.19"

            msg.actions.append(of.ofp_action_output(port=11))

            core.openflow.getConnection(s1_dpid).send(msg)

            turn9 = 1

            return

        if turn9 == 1:
            msg = of.ofp_flow_mod()

            msg.command = of.OFPFC_MODIFY_STRICT

            msg.priority = 100

            msg.idle_timeout = 0

            msg.hard_timeout = 0

            msg.match.dl_type = 0x0800

            msg.match.nw_dst = "10.0.0.19"

            msg.actions.append(of.ofp_action_output(port=12))

            core.openflow.getConnection(s1_dpid).send(msg)

            turn9 = 2

            return

        if turn9 == 2:
            msg = of.ofp_flow_mod()

            msg.command = of.OFPFC_MODIFY_STRICT

            msg.priority = 100

            msg.idle_timeout = 0

            msg.hard_timeout = 0

            msg.match.dl_type = 0x0800

            msg.match.nw_dst = "10.0.0.19"

            msg.actions.append(of.ofp_action_output(port=13))

            core.openflow.getConnection(s1_dpid).send(msg)

            turn9 = 3

            return

        if turn9 == 3:
            msg = of.ofp_flow_mod()

            msg.command = of.OFPFC_MODIFY_STRICT

            msg.priority = 100

            msg.idle_timeout = 0

            msg.hard_timeout = 0

            msg.match.dl_type = 0x0800

            msg.match.nw_dst = "10.0.0.19"

            msg.actions.append(of.ofp_action_output(port=14))

            core.openflow.getConnection(s1_dpid).send(msg)

            turn9 = 4

            return

        if turn9 == 4:
            msg = of.ofp_flow_mod()

            msg.command = of.OFPFC_MODIFY_STRICT

            msg.priority = 100

            msg.idle_timeout = 0

            msg.hard_timeout = 0

            msg.match.dl_type = 0x0800

            msg.match.nw_dst = "10.0.0.19"

            msg.actions.append(of.ofp_action_output(port=15))

            core.openflow.getConnection(s1_dpid).send(msg)

            turn9 = 5

            return

        if turn9 == 5:
            msg = of.ofp_flow_mod()

            msg.command = of.OFPFC_MODIFY_STRICT

            msg.priority = 100

            msg.idle_timeout = 0

            msg.hard_timeout = 0

            msg.match.dl_type = 0x0800

            msg.match.nw_dst = "10.0.0.19"

            msg.actions.append(of.ofp_action_output(port=16))

            core.openflow.getConnection(s1_dpid).send(msg)

            turn9 = 6

            return

        if turn9 == 6:
            msg = of.ofp_flow_mod()

            msg.command = of.OFPFC_MODIFY_STRICT

            msg.priority = 100

            msg.idle_timeout = 0

            msg.hard_timeout = 0

            msg.match.dl_type = 0x0800

            msg.match.nw_dst = "10.0.0.19"

            msg.actions.append(of.ofp_action_output(port=17))

            core.openflow.getConnection(s1_dpid).send(msg)

            turn9 = 7

            return

        if turn9 == 7:
            msg = of.ofp_flow_mod()

            msg.command = of.OFPFC_MODIFY_STRICT

            msg.priority = 100

            msg.idle_timeout = 0

            msg.hard_timeout = 0

            msg.match.dl_type = 0x0800

            msg.match.nw_dst = "10.0.0.19"

            msg.actions.append(of.ofp_action_output(port=18))

            core.openflow.getConnection(s1_dpid).send(msg)

            turn9 = 8

            return

        if turn9 == 8:
            msg = of.ofp_flow_mod()

            msg.command = of.OFPFC_MODIFY_STRICT

            msg.priority = 100

            msg.idle_timeout = 0

            msg.hard_timeout = 0

            msg.match.dl_type = 0x0800

            msg.match.nw_dst = "10.0.0.19"

            msg.actions.append(of.ofp_action_output(port=19))

            core.openflow.getConnection(s1_dpid).send(msg)

            turn9 = 9

            return

        if turn9 == 9:
            msg = of.ofp_flow_mod()

            msg.command = of.OFPFC_MODIFY_STRICT

            msg.priority = 100

            msg.idle_timeout = 0

            msg.hard_timeout = 0

            msg.match.dl_type = 0x0800

            msg.match.nw_dst = "10.0.0.19"

            msg.actions.append(of.ofp_action_output(port=20))

            core.openflow.getConnection(s1_dpid).send(msg)

            turn9 = 10

            return

        if turn9 == 10:
            msg = of.ofp_flow_mod()

            msg.command = of.OFPFC_MODIFY_STRICT

            msg.priority = 100

            msg.idle_timeout = 0

            msg.hard_timeout = 0

            msg.match.dl_type = 0x0800

            msg.match.nw_dst = "10.0.0.19"

            msg.actions.append(of.ofp_action_output(port=21))

            core.openflow.getConnection(s1_dpid).send(msg)

            turn9 = 11

            return

        if turn9 == 11:
            msg = of.ofp_flow_mod()

            msg.command = of.OFPFC_MODIFY_STRICT

            msg.priority = 100

            msg.idle_timeout = 0

            msg.hard_timeout = 0

            msg.match.dl_type = 0x0800

            msg.match.nw_dst = "10.0.0.19"

            msg.actions.append(of.ofp_action_output(port=22))

            core.openflow.getConnection(s1_dpid).send(msg)

            turn9 = 12

            return

        if turn9 == 12:
            msg = of.ofp_flow_mod()

            msg.command = of.OFPFC_MODIFY_STRICT

            msg.priority = 100

            msg.idle_timeout = 0

            msg.hard_timeout = 0

            msg.match.dl_type = 0x0800

            msg.match.nw_dst = "10.0.0.19"

            msg.actions.append(of.ofp_action_output(port=23))

            core.openflow.getConnection(s1_dpid).send(msg)

            turn9 = 13

            return

        if turn9 == 13:
            msg = of.ofp_flow_mod()

            msg.command = of.OFPFC_MODIFY_STRICT

            msg.priority = 100

            msg.idle_timeout = 0

            msg.hard_timeout = 0

            msg.match.dl_type = 0x0800

            msg.match.nw_dst = "10.0.0.19"

            msg.actions.append(of.ofp_action_output(port=24))

            core.openflow.getConnection(s1_dpid).send(msg)

            turn9 = 14

            return

        if turn9 == 14:
            msg = of.ofp_flow_mod()

            msg.command = of.OFPFC_MODIFY_STRICT

            msg.priority = 100

            msg.idle_timeout = 0

            msg.hard_timeout = 0

            msg.match.dl_type = 0x0800

            msg.match.nw_dst = "10.0.0.19"

            msg.actions.append(of.ofp_action_output(port=25))

            core.openflow.getConnection(s1_dpid).send(msg)

            turn9 = 15

            return

        if turn9 == 15:
            msg = of.ofp_flow_mod()

            msg.command = of.OFPFC_MODIFY_STRICT

            msg.priority = 100

            msg.idle_timeout = 0

            msg.hard_timeout = 0

            msg.match.dl_type = 0x0800

            msg.match.nw_dst = "10.0.0.19"

            msg.actions.append(of.ofp_action_output(port=26))

            core.openflow.getConnection(s1_dpid).send(msg)

            turn9 = 16

            return

        if turn9 == 16:
            msg = of.ofp_flow_mod()

            msg.command = of.OFPFC_MODIFY_STRICT

            msg.priority = 100

            msg.idle_timeout = 0

            msg.hard_timeout = 0

            msg.match.dl_type = 0x0800

            msg.match.nw_dst = "10.0.0.19"

            msg.actions.append(of.ofp_action_output(port=27))

            core.openflow.getConnection(s1_dpid).send(msg)

            turn9 = 17

            return

        if turn9 == 17:
            msg = of.ofp_flow_mod()

            msg.command = of.OFPFC_MODIFY_STRICT

            msg.priority = 100

            msg.idle_timeout = 0

            msg.hard_timeout = 0

            msg.match.dl_type = 0x0800

            msg.match.nw_dst = "10.0.0.19"

            msg.actions.append(of.ofp_action_output(port=28))

            core.openflow.getConnection(s1_dpid).send(msg)

            turn9 = 18

            return

        if turn9 == 18:
            msg = of.ofp_flow_mod()

            msg.command = of.OFPFC_MODIFY_STRICT

            msg.priority = 100

            msg.idle_timeout = 0

            msg.hard_timeout = 0

            msg.match.dl_type = 0x0800

            msg.match.nw_dst = "10.0.0.19"

            msg.actions.append(of.ofp_action_output(port=29))

            core.openflow.getConnection(s1_dpid).send(msg)

            turn9 = 19

            return

        if turn9 == 19:
            msg = of.ofp_flow_mod()

            msg.command = of.OFPFC_MODIFY_STRICT

            msg.priority = 100

            msg.idle_timeout = 0

            msg.hard_timeout = 0

            msg.match.dl_type = 0x0800

            msg.match.nw_dst = "10.0.0.19"

            msg.actions.append(of.ofp_action_output(port=30))

            core.openflow.getConnection(s1_dpid).send(msg)

            turn9 = 0

            return


def _timer_func10():
    global s1_dpid, s2_dpid, s3_dpid, s4_dpid, s5_dpid, s6_dpid, s7_dpid, s8_dpid, s9_dpid, s10_dpid, s11_dpid, s12_dpid, s13_dpid, s14_dpid
    global s15_dpid, s16_dpid, s17_dpid, s18_dpid, s19_dpid, s20_dpid, s21_dpid, s22_dpid
    global turn1, turn2, turn3, turn4, turn5, turn6, turn7, turn8, turn9,turn10,count
	
    if count<200:
        msg = of.ofp_flow_mod()

        msg.command = of.OFPFC_MODIFY_STRICT

        msg.priority = 100

        msg.idle_timeout = 0

        msg.hard_timeout = 0

        msg.match.dl_type = 0x0800

        msg.match.nw_dst = "10.0.0.20"

        msg.actions.append(of.ofp_action_output(port=20))

        core.openflow.getConnection(s1_dpid).send(msg)

        return

    else:
        if turn10 == 0:
            msg = of.ofp_flow_mod()

            msg.command = of.OFPFC_MODIFY_STRICT

            msg.priority = 100

            msg.idle_timeout = 0

            msg.hard_timeout = 0

            msg.match.dl_type = 0x0800

            msg.match.nw_dst = "10.0.0.20"

            msg.actions.append(of.ofp_action_output(port=11))

            core.openflow.getConnection(s1_dpid).send(msg)

            turn10 = 1

            return

        if turn10 == 1:
            msg = of.ofp_flow_mod()

            msg.command = of.OFPFC_MODIFY_STRICT

            msg.priority = 100

            msg.idle_timeout = 0

            msg.hard_timeout = 0

            msg.match.dl_type = 0x0800

            msg.match.nw_dst = "10.0.0.20"

            msg.actions.append(of.ofp_action_output(port=12))

            core.openflow.getConnection(s1_dpid).send(msg)

            turn10 = 2

            return

        if turn10 == 2:
            msg = of.ofp_flow_mod()

            msg.command = of.OFPFC_MODIFY_STRICT

            msg.priority = 100

            msg.idle_timeout = 0

            msg.hard_timeout = 0

            msg.match.dl_type = 0x0800

            msg.match.nw_dst = "10.0.0.20"

            msg.actions.append(of.ofp_action_output(port=13))

            core.openflow.getConnection(s1_dpid).send(msg)

            turn10 = 3

            return

        if turn10 == 3:
            msg = of.ofp_flow_mod()

            msg.command = of.OFPFC_MODIFY_STRICT

            msg.priority = 100

            msg.idle_timeout = 0

            msg.hard_timeout = 0

            msg.match.dl_type = 0x0800

            msg.match.nw_dst = "10.0.0.20"

            msg.actions.append(of.ofp_action_output(port=14))

            core.openflow.getConnection(s1_dpid).send(msg)

            turn10 = 4

            return

        if turn10 == 4:
            msg = of.ofp_flow_mod()

            msg.command = of.OFPFC_MODIFY_STRICT

            msg.priority = 100

            msg.idle_timeout = 0

            msg.hard_timeout = 0

            msg.match.dl_type = 0x0800

            msg.match.nw_dst = "10.0.0.20"

            msg.actions.append(of.ofp_action_output(port=15))

            core.openflow.getConnection(s1_dpid).send(msg)

            turn10 = 5

            return

        if turn10 == 5:
            msg = of.ofp_flow_mod()

            msg.command = of.OFPFC_MODIFY_STRICT

            msg.priority = 100

            msg.idle_timeout = 0

            msg.hard_timeout = 0

            msg.match.dl_type = 0x0800

            msg.match.nw_dst = "10.0.0.20"

            msg.actions.append(of.ofp_action_output(port=16))

            core.openflow.getConnection(s1_dpid).send(msg)

            turn10 = 6

            return

        if turn10 == 6:
            msg = of.ofp_flow_mod()

            msg.command = of.OFPFC_MODIFY_STRICT

            msg.priority = 100

            msg.idle_timeout = 0

            msg.hard_timeout = 0

            msg.match.dl_type = 0x0800

            msg.match.nw_dst = "10.0.0.20"

            msg.actions.append(of.ofp_action_output(port=17))

            core.openflow.getConnection(s1_dpid).send(msg)

            turn10 = 7

            return

        if turn10 == 7:
            msg = of.ofp_flow_mod()

            msg.command = of.OFPFC_MODIFY_STRICT

            msg.priority = 100

            msg.idle_timeout = 0

            msg.hard_timeout = 0

            msg.match.dl_type = 0x0800

            msg.match.nw_dst = "10.0.0.20"

            msg.actions.append(of.ofp_action_output(port=18))

            core.openflow.getConnection(s1_dpid).send(msg)

            turn10 = 8

            return

        if turn10 == 8:
            msg = of.ofp_flow_mod()

            msg.command = of.OFPFC_MODIFY_STRICT

            msg.priority = 100

            msg.idle_timeout = 0

            msg.hard_timeout = 0

            msg.match.dl_type = 0x0800

            msg.match.nw_dst = "10.0.0.20"

            msg.actions.append(of.ofp_action_output(port=19))

            core.openflow.getConnection(s1_dpid).send(msg)

            turn10 = 9

            return

        if turn10 == 9:
            msg = of.ofp_flow_mod()

            msg.command = of.OFPFC_MODIFY_STRICT

            msg.priority = 100

            msg.idle_timeout = 0

            msg.hard_timeout = 0

            msg.match.dl_type = 0x0800

            msg.match.nw_dst = "10.0.0.20"

            msg.actions.append(of.ofp_action_output(port=20))

            core.openflow.getConnection(s1_dpid).send(msg)

            turn10 = 10

            return

        if turn10 == 10:
            msg = of.ofp_flow_mod()

            msg.command = of.OFPFC_MODIFY_STRICT

            msg.priority = 100

            msg.idle_timeout = 0

            msg.hard_timeout = 0

            msg.match.dl_type = 0x0800

            msg.match.nw_dst = "10.0.0.20"

            msg.actions.append(of.ofp_action_output(port=21))

            core.openflow.getConnection(s1_dpid).send(msg)

            turn10 = 11

            return

        if turn10 == 11:
            msg = of.ofp_flow_mod()

            msg.command = of.OFPFC_MODIFY_STRICT

            msg.priority = 100

            msg.idle_timeout = 0

            msg.hard_timeout = 0

            msg.match.dl_type = 0x0800

            msg.match.nw_dst = "10.0.0.20"

            msg.actions.append(of.ofp_action_output(port=22))

            core.openflow.getConnection(s1_dpid).send(msg)

            turn10 = 12

            return

        if turn10 == 12:
            msg = of.ofp_flow_mod()

            msg.command = of.OFPFC_MODIFY_STRICT

            msg.priority = 100

            msg.idle_timeout = 0

            msg.hard_timeout = 0

            msg.match.dl_type = 0x0800

            msg.match.nw_dst = "10.0.0.20"

            msg.actions.append(of.ofp_action_output(port=23))

            core.openflow.getConnection(s1_dpid).send(msg)

            turn10 = 13

            return

        if turn10 == 13:
            msg = of.ofp_flow_mod()

            msg.command = of.OFPFC_MODIFY_STRICT

            msg.priority = 100

            msg.idle_timeout = 0

            msg.hard_timeout = 0

            msg.match.dl_type = 0x0800

            msg.match.nw_dst = "10.0.0.20"

            msg.actions.append(of.ofp_action_output(port=24))

            core.openflow.getConnection(s1_dpid).send(msg)

            turn10 = 14

            return

        if turn10 == 14:
            msg = of.ofp_flow_mod()

            msg.command = of.OFPFC_MODIFY_STRICT

            msg.priority = 100

            msg.idle_timeout = 0

            msg.hard_timeout = 0

            msg.match.dl_type = 0x0800

            msg.match.nw_dst = "10.0.0.20"

            msg.actions.append(of.ofp_action_output(port=25))

            core.openflow.getConnection(s1_dpid).send(msg)

            turn10 = 15

            return

        if turn10 == 15:
            msg = of.ofp_flow_mod()

            msg.command = of.OFPFC_MODIFY_STRICT

            msg.priority = 100

            msg.idle_timeout = 0

            msg.hard_timeout = 0

            msg.match.dl_type = 0x0800

            msg.match.nw_dst = "10.0.0.20"

            msg.actions.append(of.ofp_action_output(port=26))

            core.openflow.getConnection(s1_dpid).send(msg)

            turn10 = 16

            return

        if turn10 == 16:
            msg = of.ofp_flow_mod()

            msg.command = of.OFPFC_MODIFY_STRICT

            msg.priority = 100

            msg.idle_timeout = 0

            msg.hard_timeout = 0

            msg.match.dl_type = 0x0800

            msg.match.nw_dst = "10.0.0.20"

            msg.actions.append(of.ofp_action_output(port=27))

            core.openflow.getConnection(s1_dpid).send(msg)

            turn10 = 17

            return

        if turn10 == 17:
            msg = of.ofp_flow_mod()

            msg.command = of.OFPFC_MODIFY_STRICT

            msg.priority = 100

            msg.idle_timeout = 0

            msg.hard_timeout = 0

            msg.match.dl_type = 0x0800

            msg.match.nw_dst = "10.0.0.20"

            msg.actions.append(of.ofp_action_output(port=28))

            core.openflow.getConnection(s1_dpid).send(msg)

            turn10 = 18

            return

        if turn10 == 18:
            msg = of.ofp_flow_mod()

            msg.command = of.OFPFC_MODIFY_STRICT

            msg.priority = 100

            msg.idle_timeout = 0

            msg.hard_timeout = 0

            msg.match.dl_type = 0x0800

            msg.match.nw_dst = "10.0.0.20"

            msg.actions.append(of.ofp_action_output(port=29))

            core.openflow.getConnection(s1_dpid).send(msg)

            turn10 = 19

            return

        if turn10 == 19:
            msg = of.ofp_flow_mod()

            msg.command = of.OFPFC_MODIFY_STRICT

            msg.priority = 100

            msg.idle_timeout = 0

            msg.hard_timeout = 0

            msg.match.dl_type = 0x0800

            msg.match.nw_dst = "10.0.0.20"

            msg.actions.append(of.ofp_action_output(port=30))

            core.openflow.getConnection(s1_dpid).send(msg)

            turn10 = 0

            return

def _handle_portstats_received (event):

  global s1_p1,s1_p11, s1_p12, s1_p13,s1_p14,s1_p15,s1_p16, s1_p17, s1_p18,s1_p19,s1_p20,s1_p21,s1_p22
  global s1_p23, s1_p24, s1_p25, s1_p26, s1_p27, s1_p28, s1_p29, s1_p30
  global s2_p1, s3_p1, s4_p1,s5_p1,s6_p1, s7_p1, s8_p1,s9_p1,s10_p1, s11_p1, s12_p1,s13_p1
  global s15_p1, s16_p1, s17_p1, s18_p1, s19_p1, s20_p1, s21_p1, s22_p1
  global s1_p2,s1_p3,s1_p4,s1_p5,s1_p6,s1_p7,s1_p8,s1_p9

  global pre_s1_p1,pre_s1_p11, pre_s1_p12, pre_s1_p13,pre_s1_p14,pre_s1_p15,pre_s1_p16, pre_s1_p17, pre_s1_p18,pre_s1_p19,pre_s1_p20, pre_s1_p21,pre_s1_p22
  global pre_s1_p23,pre_s1_p24, pre_s1_p25, pre_s1_p26,pre_s1_p27,pre_s1_p28,pre_s1_p29, pre_s1_p30
  global pre_s2_p1, pre_s3_p1, pre_s4_p1,pre_s5_p1,pre_s6_p1, pre_s7_p1, pre_s8_p1,pre_s9_p1,pre_s10_p1, pre_s11_p1, pre_s12_p1,pre_s13_p1
  global pre_s15_p1, pre_s16_p1, pre_s17_p1, pre_s18_p1, pre_s19_p1, pre_s20_p1, pre_s21_p1, pre_s22_p1
  global pre_s1_p2,pre_s1_p3,pre_s1_p4,pre_s1_p5,pre_s1_p6,pre_s1_p7,pre_s1_p8,pre_s1_p9,count


  if event.connection.dpid==s1_dpid:

    for f in event.stats:

      if int(f.port_no)<65534:

        if f.port_no==1:

          pre_s1_p1=s1_p1

          s1_p1=f.rx_packets

        if f.port_no==11:

          pre_s1_p11=s1_p11

          s1_p11=f.tx_packets

        if f.port_no==12:

          pre_s1_p12=s1_p12

          s1_p12=f.tx_packets

        if f.port_no==13:

          pre_s1_p13=s1_p13

          s1_p13=f.tx_packets

        if f.port_no==14:

          pre_s1_p14=s1_p14

          s1_p14=f.tx_packets

        if f.port_no==15:

          pre_s1_p15=s1_p15

          s1_p15=f.tx_packets

        if f.port_no==16:

          pre_s1_p16=s1_p16

          s1_p16=f.tx_packets

        if f.port_no==17:

          pre_s1_p17=s1_p17

          s1_p17=f.tx_packets

        if f.port_no==18:

          pre_s1_p18=s1_p18

          s1_p18=f.tx_packets

        if f.port_no==19:

          pre_s1_p19=s1_p19

          s1_p19=f.tx_packets

        if f.port_no==20:

          pre_s1_p20=s1_p20

          s1_p20=f.tx_packets

        if f.port_no == 21:

          pre_s1_p21 = s1_p21

          s1_p21 = f.tx_packets

        if f.port_no == 22:

          pre_s1_p22 = s1_p22

          s1_p22 = f.tx_packets

        if f.port_no == 23:

          pre_s1_p23 = s1_p23

          s1_p23 = f.tx_packets

        if f.port_no == 24:

          pre_s1_p24 = s1_p24

          s1_p24 = f.tx_packets

        if f.port_no == 25:

          pre_s1_p25 = s1_p25

          s1_p25 = f.tx_packets

        if f.port_no == 26:

          pre_s1_p26 = s1_p26

          s1_p26 = f.tx_packets

        if f.port_no == 27:

          pre_s1_p27 = s1_p27

          s1_p27 = f.tx_packets

        if f.port_no == 28:

          pre_s1_p28 = s1_p28

          s1_p28 = f.tx_packets

        if f.port_no == 29:

          pre_s1_p29 = s1_p29

          s1_p29 = f.tx_packets

        if f.port_no == 30:

          pre_s1_p30 = s1_p30

          s1_p30 = f.tx_packets

  if event.connection.dpid==s2_dpid:

    for f in  event.stats:

       if int(f.port_no)<65534:

         if f.port_no==1:

           pre_s2_p1=s2_p1

           s2_p1=f.rx_packets

  if event.connection.dpid==s3_dpid:

     for f in event.stats:

       if int(f.port_no)<65534:

         if f.port_no==1:

           pre_s3_p1=s3_p1

           s3_p1=f.rx_packets

  if event.connection.dpid==s4_dpid:

     for f in event.stats:

       if int(f.port_no)<65534:

         if f.port_no==1:

           pre_s4_p1=s4_p1

           s4_p1=f.rx_packets

  if event.connection.dpid==s5_dpid:

     for f in event.stats:

       if int(f.port_no)<65534:

         if f.port_no==1:

           pre_s5_p1=s5_p1

           s5_p1=f.rx_packets

  if event.connection.dpid==s6_dpid:

     for f in event.stats:

       if int(f.port_no)<65534:

         if f.port_no==1:

           pre_s6_p1=s6_p1

           s6_p1=f.rx_packets

  if event.connection.dpid == s7_dpid:

      for f in event.stats:

          if int(f.port_no) < 65534:

              if f.port_no == 1:
                  pre_s7_p1 = s7_p1

                  s7_p1 = f.rx_packets

  if event.connection.dpid == s8_dpid:

      for f in event.stats:

          if int(f.port_no) < 65534:

              if f.port_no == 1:
                  pre_s8_p1 = s8_p1

                  s8_p1 = f.rx_packets

  if event.connection.dpid == s9_dpid:

      for f in event.stats:

          if int(f.port_no) < 65534:

              if f.port_no == 1:
                  pre_s9_p1 = s9_p1

                  s9_p1 = f.rx_packets

  if event.connection.dpid == s10_dpid:

      for f in event.stats:

          if int(f.port_no) < 65534:

              if f.port_no == 1:
                  pre_s10_p1 = s10_p1

                  s10_p1 = f.rx_packets

  if event.connection.dpid == s11_dpid:

      for f in event.stats:

          if int(f.port_no) < 65534:

              if f.port_no == 1:
                  pre_s11_p1 = s11_p1

                  s11_p1 = f.rx_packets

  if event.connection.dpid == s12_dpid:

      for f in event.stats:

          if int(f.port_no) < 65534:

              if f.port_no == 1:
                  pre_s12_p1 = s12_p1

                  s12_p1 = f.rx_packets

  if event.connection.dpid == s13_dpid:

      for f in event.stats:

          if int(f.port_no) < 65534:

              if f.port_no == 1:
                  pre_s13_p1 = s13_p1

                  s13_p1 = f.rx_packets

  if event.connection.dpid == s15_dpid:

      for f in event.stats:

          if int(f.port_no) < 65534:

              if f.port_no == 1:
                  pre_s15_p1 = s15_p1

                  s15_p1 = f.rx_packets

  if event.connection.dpid == s16_dpid:

      for f in event.stats:

          if int(f.port_no) < 65534:

              if f.port_no == 1:
                  pre_s16_p1 = s16_p1

                  s16_p1 = f.rx_packets

  if event.connection.dpid == s17_dpid:

      for f in event.stats:

          if int(f.port_no) < 65534:

              if f.port_no == 1:
                  pre_s17_p1 = s17_p1

                  s17_p1 = f.rx_packets

  if event.connection.dpid == s18_dpid:

      for f in event.stats:

          if int(f.port_no) < 65534:

              if f.port_no == 1:
                  pre_s18_p1 = s18_p1

                  s18_p1 = f.rx_packets

  if event.connection.dpid == s19_dpid:

      for f in event.stats:

          if int(f.port_no) < 65534:

              if f.port_no == 1:
                  pre_s19_p1 = s19_p1

                  s19_p1 = f.rx_packets

  if event.connection.dpid == s20_dpid:

      for f in event.stats:

          if int(f.port_no) < 65534:

              if f.port_no == 1:
                  pre_s20_p1 = s20_p1

                  s20_p1 = f.rx_packets

  if event.connection.dpid == s21_dpid:

      for f in event.stats:

          if int(f.port_no) < 65534:

              if f.port_no == 1:
                  pre_s21_p1 = s21_p1

                  s21_p1 = f.rx_packets

  if event.connection.dpid == s22_dpid:

      for f in event.stats:

          if int(f.port_no) < 65534:

              if f.port_no == 1:
                  pre_s22_p1 = s22_p1

                  s22_p1 = f.rx_packets

def _handle_ConnectionUp (event):

  global s1_dpid, s2_dpid, s3_dpid, s4_dpid, s5_dpid,s6_dpid,s7_dpid, s8_dpid, s9_dpid, s10_dpid, s11_dpid,s12_dpid, s13_dpid,s14_dpid
  global s15_dpid, s16_dpid, s17_dpid, s18_dpid, s19_dpid, s20_dpid, s21_dpid, s22_dpid
  print "ConnectionUp: ",dpidToStr(event.connection.dpid)

  #remember the connection dpid for switch

  for m in event.connection.features.ports:

    if m.name == "s1-eth1":

      s1_dpid = event.connection.dpid

      print "s1_dpid=", s1_dpid

    elif m.name == "s2-eth1":

      s2_dpid = event.connection.dpid

      print "s2_dpid=", s2_dpid

    elif m.name == "s3-eth1":

      s3_dpid = event.connection.dpid

      print "s3_dpid=", s3_dpid

    elif m.name == "s4-eth1":

      s4_dpid = event.connection.dpid

      print "s4_dpid=", s4_dpid

    elif m.name == "s5-eth1":

      s5_dpid = event.connection.dpid

      print "s5_dpid=", s5_dpid

    elif m.name == "s6-eth1":

      s6_dpid = event.connection.dpid

      print "s6_dpid=", s6_dpid

    elif m.name == "s7-eth1":

      s7_dpid = event.connection.dpid

      print "s7_dpid=", s7_dpid

    elif m.name == "s8-eth1":

      s8_dpid = event.connection.dpid

      print "s8_dpid=", s8_dpid

    elif m.name == "s9-eth1":

      s9_dpid = event.connection.dpid

      print "s9_dpid=", s9_dpid

    elif m.name == "s10-eth1":

      s10_dpid = event.connection.dpid

      print "s10_dpid=", s10_dpid

    elif m.name == "s11-eth1":

      s11_dpid = event.connection.dpid

      print "s11_dpid=", s11_dpid

    elif m.name == "s12-eth1":

      s12_dpid = event.connection.dpid

      print "s12_dpid=", s12_dpid

    elif m.name == "s13-eth1":

      s13_dpid = event.connection.dpid

      print "s13_dpid=", s13_dpid

    elif m.name == "s14-eth1":

      s14_dpid = event.connection.dpid

      print "s14_dpid=", s14_dpid

    elif m.name == "s15-eth1":

      s15_dpid = event.connection.dpid

      print "s15_dpid=", s15_dpid

    elif m.name == "s16-eth1":

      s16_dpid = event.connection.dpid

      print "s16_dpid=", s16_dpid

    elif m.name == "s17-eth1":

      s17_dpid = event.connection.dpid

      print "s17_dpid=", s17_dpid

    elif m.name == "s18-eth1":

      s18_dpid = event.connection.dpid

      print "s18_dpid=", s18_dpid

    elif m.name == "s19-eth1":

      s19_dpid = event.connection.dpid

      print "s19_dpid=", s19_dpid

    elif m.name == "s20-eth1":

      s20_dpid = event.connection.dpid

      print "s20_dpid=", s20_dpid

    elif m.name == "s21-eth1":

      s21_dpid = event.connection.dpid

      print "s21_dpid=", s21_dpid

    elif m.name == "s22-eth1":

      s22_dpid = event.connection.dpid

      print "s22_dpid=", s22_dpid

  if s1_dpid<>0 and s2_dpid<>0 and s3_dpid<>0 and s4_dpid<>0 and s5_dpid<>0 and s6_dpid<>0 and s7_dpid<>0 and s8_dpid<>0 and s9_dpid<>0 and s10_dpid<>0 and s11_dpid<>0 and s12_dpid<>0 and s13_dpid<>0 and s15_dpid<>0 and s16_dpid<>0 and s17_dpid<>0 and s18_dpid<>0 and s19_dpid<>0 and s20_dpid<>0 and s21_dpid<>0 and s22_dpid<>0:

    Timer(a, _timer_func1, recurring=True)

    Timer(a, _timer_func2, recurring=True)

    Timer(a, _timer_func3, recurring=True)

    Timer(a, _timer_func4, recurring=True)

    Timer(a, _timer_func5, recurring=True)

    Timer(a, _timer_func6, recurring=True)

    Timer(a, _timer_func7, recurring=True)

    Timer(a, _timer_func8, recurring=True)

    Timer(a, _timer_func9, recurring=True)

    Timer(a, _timer_func10,recurring=True)

def _handle_PacketIn(event):

  global s1_dpid, s2_dpid, s3_dpid, s4_dpid, s5_dpid,s6_dpid,s7_dpid, s8_dpid, s9_dpid, s10_dpid, s11_dpid,s12_dpid, s13_dpid,s14_dpid
  global s15_dpid, s16_dpid, s17_dpid, s18_dpid, s19_dpid, s20_dpid, s21_dpid, s22_dpid
  packet=event.parsed

  if event.connection.dpid==s1_dpid:

     a=packet.find('arp')

     if a and a.protodst=="10.0.0.11":

       msg = of.ofp_packet_out(data=event.ofp)

       msg.actions.append(of.ofp_action_output(port=11))

       event.connection.send(msg)

     if a and a.protodst=="10.0.0.12":

       msg = of.ofp_packet_out(data=event.ofp)

       msg.actions.append(of.ofp_action_output(port=12))

       event.connection.send(msg)

     if a and a.protodst=="10.0.0.13":

       msg = of.ofp_packet_out(data=event.ofp)

       msg.actions.append(of.ofp_action_output(port=13))

       event.connection.send(msg)
	   
     if a and a.protodst=="10.0.0.14":

       msg = of.ofp_packet_out(data=event.ofp)

       msg.actions.append(of.ofp_action_output(port=14))

       event.connection.send(msg)

     if a and a.protodst=="10.0.0.15":

       msg = of.ofp_packet_out(data=event.ofp)

       msg.actions.append(of.ofp_action_output(port=15))

       event.connection.send(msg)

     if a and a.protodst=="10.0.0.16":

       msg = of.ofp_packet_out(data=event.ofp)

       msg.actions.append(of.ofp_action_output(port=16))

       event.connection.send(msg)

     if a and a.protodst=="10.0.0.17":

       msg = of.ofp_packet_out(data=event.ofp)

       msg.actions.append(of.ofp_action_output(port=17))

       event.connection.send(msg)

     if a and a.protodst=="10.0.0.18":

       msg = of.ofp_packet_out(data=event.ofp)

       msg.actions.append(of.ofp_action_output(port=18))

       event.connection.send(msg)

     if a and a.protodst=="10.0.0.19":

       msg = of.ofp_packet_out(data=event.ofp)

       msg.actions.append(of.ofp_action_output(port=19))

       event.connection.send(msg)

     if a and a.protodst=="10.0.0.20":

       msg = of.ofp_packet_out(data=event.ofp)

       msg.actions.append(of.ofp_action_output(port=20))

       event.connection.send(msg)

     if a and a.protodst=="10.0.0.1":

       msg = of.ofp_packet_out(data=event.ofp)

       msg.actions.append(of.ofp_action_output(port=1))

       event.connection.send(msg)

     if a and a.protodst=="10.0.0.2":

       msg = of.ofp_packet_out(data=event.ofp)

       msg.actions.append(of.ofp_action_output(port=2))

       event.connection.send(msg)

     if a and a.protodst=="10.0.0.3":

       msg = of.ofp_packet_out(data=event.ofp)

       msg.actions.append(of.ofp_action_output(port=3))

       event.connection.send(msg)

     if a and a.protodst=="10.0.0.4":

       msg = of.ofp_packet_out(data=event.ofp)

       msg.actions.append(of.ofp_action_output(port=4))

       event.connection.send(msg)

     if a and a.protodst=="10.0.0.5":

       msg = of.ofp_packet_out(data=event.ofp)

       msg.actions.append(of.ofp_action_output(port=5))

       event.connection.send(msg)

     if a and a.protodst=="10.0.0.6":

       msg = of.ofp_packet_out(data=event.ofp)

       msg.actions.append(of.ofp_action_output(port=6))

       event.connection.send(msg)

     if a and a.protodst=="10.0.0.7":

       msg = of.ofp_packet_out(data=event.ofp)

       msg.actions.append(of.ofp_action_output(port=7))

       event.connection.send(msg)

     if a and a.protodst=="10.0.0.8":

       msg = of.ofp_packet_out(data=event.ofp)

       msg.actions.append(of.ofp_action_output(port=8))

       event.connection.send(msg)

     if a and a.protodst=="10.0.0.9":

       msg = of.ofp_packet_out(data=event.ofp)

       msg.actions.append(of.ofp_action_output(port=9))

       event.connection.send(msg)

     if a and a.protodst=="10.0.0.10":

       msg = of.ofp_packet_out(data=event.ofp)

       msg.actions.append(of.ofp_action_output(port=10))

       event.connection.send(msg)

     msg = of.ofp_flow_mod()

     msg.priority =100

     msg.idle_timeout = 0

     msg.hard_timeout = 0

     msg.match.dl_type = 0x0800

     msg.match.nw_dst = "10.0.0.1"

     msg.actions.append(of.ofp_action_output(port = 1))

     event.connection.send(msg)

     msg = of.ofp_flow_mod()

     msg.priority =100

     msg.idle_timeout = 0

     msg.hard_timeout = 0

     msg.match.dl_type = 0x0800

     msg.match.nw_dst = "10.0.0.2"

     msg.actions.append(of.ofp_action_output(port = 2))

     event.connection.send(msg)

     msg = of.ofp_flow_mod()

     msg.priority =100

     msg.idle_timeout = 0

     msg.hard_timeout = 0

     msg.match.dl_type = 0x0800

     msg.match.nw_dst = "10.0.0.3"

     msg.actions.append(of.ofp_action_output(port = 3))

     event.connection.send(msg)

     msg = of.ofp_flow_mod()

     msg.priority =100

     msg.idle_timeout = 0

     msg.hard_timeout = 0

     msg.match.dl_type = 0x0800

     msg.match.nw_dst = "10.0.0.4"

     msg.actions.append(of.ofp_action_output(port = 4))

     event.connection.send(msg)

     msg = of.ofp_flow_mod()

     msg.priority =100

     msg.idle_timeout = 0

     msg.hard_timeout = 0

     msg.match.dl_type = 0x0800

     msg.match.nw_dst = "10.0.0.5"

     msg.actions.append(of.ofp_action_output(port = 5))

     event.connection.send(msg)

     msg = of.ofp_flow_mod()

     msg.priority =100

     msg.idle_timeout = 0

     msg.hard_timeout = 0

     msg.match.dl_type = 0x0800

     msg.match.nw_dst = "10.0.0.6"

     msg.actions.append(of.ofp_action_output(port = 6))

     event.connection.send(msg)

     msg = of.ofp_flow_mod()

     msg.priority =100

     msg.idle_timeout = 0

     msg.hard_timeout = 0

     msg.match.dl_type = 0x0800

     msg.match.nw_dst = "10.0.0.7"

     msg.actions.append(of.ofp_action_output(port = 7))

     event.connection.send(msg)

     msg = of.ofp_flow_mod()

     msg.priority =100

     msg.idle_timeout = 0

     msg.hard_timeout = 0

     msg.match.dl_type = 0x0800

     msg.match.nw_dst = "10.0.0.8"

     msg.actions.append(of.ofp_action_output(port = 8))

     event.connection.send(msg)

     msg = of.ofp_flow_mod()

     msg.priority =100

     msg.idle_timeout = 0

     msg.hard_timeout = 0

     msg.match.dl_type = 0x0800

     msg.match.nw_dst = "10.0.0.9"

     msg.actions.append(of.ofp_action_output(port = 9))

     event.connection.send(msg)

     msg = of.ofp_flow_mod()

     msg.priority =100

     msg.idle_timeout = 0

     msg.hard_timeout = 0

     msg.match.dl_type = 0x0800

     msg.match.nw_dst = "10.0.0.10"

     msg.actions.append(of.ofp_action_output(port = 10))

     event.connection.send(msg)

     msg = of.ofp_flow_mod()

     msg.priority =100

     msg.idle_timeout = 0

     msg.hard_timeout = 0

     msg.match.dl_type = 0x0800

     msg.match.nw_dst = "10.0.0.11"

     msg.actions.append(of.ofp_action_output(port = 11))

     event.connection.send(msg)

     msg = of.ofp_flow_mod()

     msg.priority =100

     msg.idle_timeout = 0

     msg.hard_timeout = 0

     msg.match.dl_type = 0x0800

     msg.match.nw_dst = "10.0.0.12"

     msg.actions.append(of.ofp_action_output(port = 12))

     event.connection.send(msg)

     msg = of.ofp_flow_mod()

     msg.priority =100

     msg.idle_timeout = 0

     msg.hard_timeout = 0

     msg.match.dl_type = 0x0800

     msg.match.nw_dst = "10.0.0.13"

     msg.actions.append(of.ofp_action_output(port = 13))

     event.connection.send(msg)

     msg = of.ofp_flow_mod()

     msg.priority =100

     msg.idle_timeout = 0

     msg.hard_timeout = 0

     msg.match.dl_type = 0x0800

     msg.match.nw_dst = "10.0.0.14"

     msg.actions.append(of.ofp_action_output(port = 14))

     event.connection.send(msg)

     msg = of.ofp_flow_mod()

     msg.priority =100

     msg.idle_timeout = 0

     msg.hard_timeout = 0

     msg.match.dl_type = 0x0800

     msg.match.nw_dst = "10.0.0.15"

     msg.actions.append(of.ofp_action_output(port = 15))

     event.connection.send(msg)

     msg = of.ofp_flow_mod()

     msg.priority =100

     msg.idle_timeout = 0

     msg.hard_timeout = 0

     msg.match.dl_type = 0x0800

     msg.match.nw_dst = "10.0.0.16"

     msg.actions.append(of.ofp_action_output(port = 16))

     event.connection.send(msg)

     msg = of.ofp_flow_mod()

     msg.priority =100

     msg.idle_timeout = 0

     msg.hard_timeout = 0

     msg.match.dl_type = 0x0800

     msg.match.nw_dst = "10.0.0.17"

     msg.actions.append(of.ofp_action_output(port = 17))

     event.connection.send(msg)

     msg = of.ofp_flow_mod()

     msg.priority =100

     msg.idle_timeout = 0

     msg.hard_timeout = 0

     msg.match.dl_type = 0x0800

     msg.match.nw_dst = "10.0.0.18"

     msg.actions.append(of.ofp_action_output(port = 18))

     event.connection.send(msg)

     msg = of.ofp_flow_mod()

     msg.priority =100

     msg.idle_timeout = 0

     msg.hard_timeout = 0

     msg.match.dl_type = 0x0800

     msg.match.nw_dst = "10.0.0.19"

     msg.actions.append(of.ofp_action_output(port = 19))

     event.connection.send(msg)

     msg = of.ofp_flow_mod()

     msg.priority =100

     msg.idle_timeout = 0

     msg.hard_timeout = 0

     msg.match.dl_type = 0x0800

     msg.match.nw_dst = "10.0.0.20"

     msg.actions.append(of.ofp_action_output(port = 20))

     event.connection.send(msg)

  elif event.connection.dpid==s2_dpid:

     msg = of.ofp_flow_mod()

     msg.priority =10

     msg.idle_timeout = 0

     msg.hard_timeout = 0

     msg.match.in_port = 1

     msg.match.dl_type=0x0806

     msg.actions.append(of.ofp_action_output(port = 2))

     event.connection.send(msg)

     msg = of.ofp_flow_mod()

     msg.priority =10

     msg.idle_timeout = 0

     msg.hard_timeout = 0

     msg.match.in_port = 1

     msg.match.dl_type=0x0800

     msg.actions.append(of.ofp_action_output(port = 2))

     event.connection.send(msg)

     msg = of.ofp_flow_mod()

     msg.priority =10

     msg.idle_timeout = 0

     msg.hard_timeout = 0

     msg.match.in_port = 2

     msg.match.dl_type=0x0806

     msg.actions.append(of.ofp_action_output(port = 1))

     event.connection.send(msg)

     msg = of.ofp_flow_mod()

     msg.priority =10

     msg.idle_timeout = 0

     msg.hard_timeout = 0

     msg.match.in_port = 2

     msg.match.dl_type=0x0800

     msg.actions.append(of.ofp_action_output(port = 1))

     event.connection.send(msg)

  elif event.connection.dpid==s3_dpid:

     msg = of.ofp_flow_mod()

     msg.priority =10

     msg.idle_timeout = 0

     msg.hard_timeout = 0

     msg.match.in_port = 1

     msg.match.dl_type=0x0806

     msg.actions.append(of.ofp_action_output(port = 2))

     event.connection.send(msg)

     msg = of.ofp_flow_mod()

     msg.priority =10

     msg.idle_timeout = 0

     msg.hard_timeout = 0

     msg.match.in_port = 1

     msg.match.dl_type=0x0800

     msg.actions.append(of.ofp_action_output(port = 2))

     event.connection.send(msg)

     msg = of.ofp_flow_mod()

     msg.priority =10

     msg.idle_timeout = 0

     msg.hard_timeout = 0

     msg.match.in_port = 2

     msg.match.dl_type=0x0806

     msg.actions.append(of.ofp_action_output(port = 1))

     event.connection.send(msg)

     msg = of.ofp_flow_mod()

     msg.priority =10

     msg.idle_timeout = 0

     msg.hard_timeout = 0

     msg.match.in_port = 2

     msg.match.dl_type=0x0800

     msg.actions.append(of.ofp_action_output(port = 1))

     event.connection.send(msg)

  elif event.connection.dpid==s4_dpid:

     msg = of.ofp_flow_mod()

     msg.priority =10

     msg.idle_timeout = 0

     msg.hard_timeout = 0

     msg.match.in_port = 1

     msg.match.dl_type=0x0806

     msg.actions.append(of.ofp_action_output(port = 2))

     event.connection.send(msg)

     msg = of.ofp_flow_mod()

     msg.priority =10

     msg.idle_timeout = 0

     msg.hard_timeout = 0

     msg.match.in_port = 1

     msg.match.dl_type=0x0800

     msg.actions.append(of.ofp_action_output(port = 2))

     event.connection.send(msg)

     msg = of.ofp_flow_mod()

     msg.priority =10

     msg.idle_timeout = 0

     msg.hard_timeout = 0

     msg.match.in_port = 2

     msg.match.dl_type=0x0806

     msg.actions.append(of.ofp_action_output(port = 1))

     event.connection.send(msg)

     msg = of.ofp_flow_mod()

     msg.priority =10

     msg.idle_timeout = 0

     msg.hard_timeout = 0

     msg.match.in_port = 2

     msg.match.dl_type=0x0800

     msg.actions.append(of.ofp_action_output(port = 1))

     event.connection.send(msg)

  elif event.connection.dpid == s5_dpid:

      msg = of.ofp_flow_mod()

      msg.priority = 10

      msg.idle_timeout = 0

      msg.hard_timeout = 0

      msg.match.in_port = 1

      msg.match.dl_type = 0x0806

      msg.actions.append(of.ofp_action_output(port=2))

      event.connection.send(msg)

      msg = of.ofp_flow_mod()

      msg.priority = 10

      msg.idle_timeout = 0

      msg.hard_timeout = 0

      msg.match.in_port = 1

      msg.match.dl_type = 0x0800

      msg.actions.append(of.ofp_action_output(port=2))

      event.connection.send(msg)

      msg = of.ofp_flow_mod()

      msg.priority = 10

      msg.idle_timeout = 0

      msg.hard_timeout = 0

      msg.match.in_port = 2

      msg.match.dl_type = 0x0806

      msg.actions.append(of.ofp_action_output(port=1))

      event.connection.send(msg)

      msg = of.ofp_flow_mod()

      msg.priority = 10

      msg.idle_timeout = 0

      msg.hard_timeout = 0

      msg.match.in_port = 2

      msg.match.dl_type = 0x0800

      msg.actions.append(of.ofp_action_output(port=1))

      event.connection.send(msg)

  elif event.connection.dpid == s6_dpid:

      msg = of.ofp_flow_mod()

      msg.priority = 10

      msg.idle_timeout = 0

      msg.hard_timeout = 0

      msg.match.in_port = 1

      msg.match.dl_type = 0x0806

      msg.actions.append(of.ofp_action_output(port=2))

      event.connection.send(msg)

      msg = of.ofp_flow_mod()

      msg.priority = 10

      msg.idle_timeout = 0

      msg.hard_timeout = 0

      msg.match.in_port = 1

      msg.match.dl_type = 0x0800

      msg.actions.append(of.ofp_action_output(port=2))

      event.connection.send(msg)

      msg = of.ofp_flow_mod()

      msg.priority = 10

      msg.idle_timeout = 0

      msg.hard_timeout = 0

      msg.match.in_port = 2

      msg.match.dl_type = 0x0806

      msg.actions.append(of.ofp_action_output(port=1))

      event.connection.send(msg)

      msg = of.ofp_flow_mod()

      msg.priority = 10

      msg.idle_timeout = 0

      msg.hard_timeout = 0

      msg.match.in_port = 2

      msg.match.dl_type = 0x0800

      msg.actions.append(of.ofp_action_output(port=1))

      event.connection.send(msg)

  elif event.connection.dpid == s7_dpid:

      msg = of.ofp_flow_mod()

      msg.priority = 10

      msg.idle_timeout = 0

      msg.hard_timeout = 0

      msg.match.in_port = 1

      msg.match.dl_type = 0x0806

      msg.actions.append(of.ofp_action_output(port=2))

      event.connection.send(msg)

      msg = of.ofp_flow_mod()

      msg.priority = 10

      msg.idle_timeout = 0

      msg.hard_timeout = 0

      msg.match.in_port = 1

      msg.match.dl_type = 0x0800

      msg.actions.append(of.ofp_action_output(port=2))

      event.connection.send(msg)

      msg = of.ofp_flow_mod()

      msg.priority = 10

      msg.idle_timeout = 0

      msg.hard_timeout = 0

      msg.match.in_port = 2

      msg.match.dl_type = 0x0806

      msg.actions.append(of.ofp_action_output(port=1))

      event.connection.send(msg)

      msg = of.ofp_flow_mod()

      msg.priority = 10

      msg.idle_timeout = 0

      msg.hard_timeout = 0

      msg.match.in_port = 2

      msg.match.dl_type = 0x0800

      msg.actions.append(of.ofp_action_output(port=1))

      event.connection.send(msg)

  elif event.connection.dpid == s8_dpid:

      msg = of.ofp_flow_mod()

      msg.priority = 10

      msg.idle_timeout = 0

      msg.hard_timeout = 0

      msg.match.in_port = 1

      msg.match.dl_type = 0x0806

      msg.actions.append(of.ofp_action_output(port=2))

      event.connection.send(msg)

      msg = of.ofp_flow_mod()

      msg.priority = 10

      msg.idle_timeout = 0

      msg.hard_timeout = 0

      msg.match.in_port = 1

      msg.match.dl_type = 0x0800

      msg.actions.append(of.ofp_action_output(port=2))

      event.connection.send(msg)

      msg = of.ofp_flow_mod()

      msg.priority = 10

      msg.idle_timeout = 0

      msg.hard_timeout = 0

      msg.match.in_port = 2

      msg.match.dl_type = 0x0806

      msg.actions.append(of.ofp_action_output(port=1))

      event.connection.send(msg)

      msg = of.ofp_flow_mod()

      msg.priority = 10

      msg.idle_timeout = 0

      msg.hard_timeout = 0

      msg.match.in_port = 2

      msg.match.dl_type = 0x0800

      msg.actions.append(of.ofp_action_output(port=1))

      event.connection.send(msg)

  elif event.connection.dpid == s9_dpid:

      msg = of.ofp_flow_mod()

      msg.priority = 10

      msg.idle_timeout = 0

      msg.hard_timeout = 0

      msg.match.in_port = 1

      msg.match.dl_type = 0x0806

      msg.actions.append(of.ofp_action_output(port=2))

      event.connection.send(msg)

      msg = of.ofp_flow_mod()

      msg.priority = 10

      msg.idle_timeout = 0

      msg.hard_timeout = 0

      msg.match.in_port = 1

      msg.match.dl_type = 0x0800

      msg.actions.append(of.ofp_action_output(port=2))

      event.connection.send(msg)

      msg = of.ofp_flow_mod()

      msg.priority = 10

      msg.idle_timeout = 0

      msg.hard_timeout = 0

      msg.match.in_port = 2

      msg.match.dl_type = 0x0806

      msg.actions.append(of.ofp_action_output(port=1))

      event.connection.send(msg)

      msg = of.ofp_flow_mod()

      msg.priority = 10

      msg.idle_timeout = 0

      msg.hard_timeout = 0

      msg.match.in_port = 2

      msg.match.dl_type = 0x0800

      msg.actions.append(of.ofp_action_output(port=1))

      event.connection.send(msg)

  elif event.connection.dpid == s10_dpid:

      msg = of.ofp_flow_mod()

      msg.priority = 10

      msg.idle_timeout = 0

      msg.hard_timeout = 0

      msg.match.in_port = 1

      msg.match.dl_type = 0x0806

      msg.actions.append(of.ofp_action_output(port=2))

      event.connection.send(msg)

      msg = of.ofp_flow_mod()

      msg.priority = 10

      msg.idle_timeout = 0

      msg.hard_timeout = 0

      msg.match.in_port = 1

      msg.match.dl_type = 0x0800

      msg.actions.append(of.ofp_action_output(port=2))

      event.connection.send(msg)

      msg = of.ofp_flow_mod()

      msg.priority = 10

      msg.idle_timeout = 0

      msg.hard_timeout = 0

      msg.match.in_port = 2

      msg.match.dl_type = 0x0806

      msg.actions.append(of.ofp_action_output(port=1))

      event.connection.send(msg)

      msg = of.ofp_flow_mod()

      msg.priority = 10

      msg.idle_timeout = 0

      msg.hard_timeout = 0

      msg.match.in_port = 2

      msg.match.dl_type = 0x0800

      msg.actions.append(of.ofp_action_output(port=1))

      event.connection.send(msg)

  elif event.connection.dpid == s11_dpid:

      msg = of.ofp_flow_mod()

      msg.priority = 10

      msg.idle_timeout = 0

      msg.hard_timeout = 0

      msg.match.in_port = 1

      msg.match.dl_type = 0x0806

      msg.actions.append(of.ofp_action_output(port=2))

      event.connection.send(msg)

      msg = of.ofp_flow_mod()

      msg.priority = 10

      msg.idle_timeout = 0

      msg.hard_timeout = 0

      msg.match.in_port = 1

      msg.match.dl_type = 0x0800

      msg.actions.append(of.ofp_action_output(port=2))

      event.connection.send(msg)

      msg = of.ofp_flow_mod()

      msg.priority = 10

      msg.idle_timeout = 0

      msg.hard_timeout = 0

      msg.match.in_port = 2

      msg.match.dl_type = 0x0806

      msg.actions.append(of.ofp_action_output(port=1))

      event.connection.send(msg)

      msg = of.ofp_flow_mod()

      msg.priority = 10

      msg.idle_timeout = 0

      msg.hard_timeout = 0

      msg.match.in_port = 2

      msg.match.dl_type = 0x0800

      msg.actions.append(of.ofp_action_output(port=1))

      event.connection.send(msg)

  elif event.connection.dpid == s12_dpid:

      msg = of.ofp_flow_mod()

      msg.priority = 10

      msg.idle_timeout = 0

      msg.hard_timeout = 0

      msg.match.in_port = 1

      msg.match.dl_type = 0x0806

      msg.actions.append(of.ofp_action_output(port=2))

      event.connection.send(msg)

      msg = of.ofp_flow_mod()

      msg.priority = 10

      msg.idle_timeout = 0

      msg.hard_timeout = 0

      msg.match.in_port = 1

      msg.match.dl_type = 0x0800

      msg.actions.append(of.ofp_action_output(port=2))

      event.connection.send(msg)

      msg = of.ofp_flow_mod()

      msg.priority = 10

      msg.idle_timeout = 0

      msg.hard_timeout = 0

      msg.match.in_port = 2

      msg.match.dl_type = 0x0806

      msg.actions.append(of.ofp_action_output(port=1))

      event.connection.send(msg)

      msg = of.ofp_flow_mod()

      msg.priority = 10

      msg.idle_timeout = 0

      msg.hard_timeout = 0

      msg.match.in_port = 2

      msg.match.dl_type = 0x0800

      msg.actions.append(of.ofp_action_output(port=1))

      event.connection.send(msg)

  elif event.connection.dpid == s13_dpid:

      msg = of.ofp_flow_mod()

      msg.priority = 10

      msg.idle_timeout = 0

      msg.hard_timeout = 0

      msg.match.in_port = 1

      msg.match.dl_type = 0x0806

      msg.actions.append(of.ofp_action_output(port=2))

      event.connection.send(msg)

      msg = of.ofp_flow_mod()

      msg.priority = 10

      msg.idle_timeout = 0

      msg.hard_timeout = 0

      msg.match.in_port = 1

      msg.match.dl_type = 0x0800

      msg.actions.append(of.ofp_action_output(port=2))

      event.connection.send(msg)

      msg = of.ofp_flow_mod()

      msg.priority = 10

      msg.idle_timeout = 0

      msg.hard_timeout = 0

      msg.match.in_port = 2

      msg.match.dl_type = 0x0806

      msg.actions.append(of.ofp_action_output(port=1))

      event.connection.send(msg)

      msg = of.ofp_flow_mod()

      msg.priority = 10

      msg.idle_timeout = 0

      msg.hard_timeout = 0

      msg.match.in_port = 2

      msg.match.dl_type = 0x0800

      msg.actions.append(of.ofp_action_output(port=1))

      event.connection.send(msg)

  elif event.connection.dpid == s15_dpid:

      msg = of.ofp_flow_mod()

      msg.priority = 10

      msg.idle_timeout = 0

      msg.hard_timeout = 0

      msg.match.in_port = 1

      msg.match.dl_type = 0x0806

      msg.actions.append(of.ofp_action_output(port=2))

      event.connection.send(msg)

      msg = of.ofp_flow_mod()

      msg.priority = 10

      msg.idle_timeout = 0

      msg.hard_timeout = 0

      msg.match.in_port = 1

      msg.match.dl_type = 0x0800

      msg.actions.append(of.ofp_action_output(port=2))

      event.connection.send(msg)

      msg = of.ofp_flow_mod()

      msg.priority = 10

      msg.idle_timeout = 0

      msg.hard_timeout = 0

      msg.match.in_port = 2

      msg.match.dl_type = 0x0806

      msg.actions.append(of.ofp_action_output(port=1))

      event.connection.send(msg)

      msg = of.ofp_flow_mod()

      msg.priority = 10

      msg.idle_timeout = 0

      msg.hard_timeout = 0

      msg.match.in_port = 2

      msg.match.dl_type = 0x0800

      msg.actions.append(of.ofp_action_output(port=1))

      event.connection.send(msg)

  elif event.connection.dpid == s16_dpid:

      msg = of.ofp_flow_mod()

      msg.priority = 10

      msg.idle_timeout = 0

      msg.hard_timeout = 0

      msg.match.in_port = 1

      msg.match.dl_type = 0x0806

      msg.actions.append(of.ofp_action_output(port=2))

      event.connection.send(msg)

      msg = of.ofp_flow_mod()

      msg.priority = 10

      msg.idle_timeout = 0

      msg.hard_timeout = 0

      msg.match.in_port = 1

      msg.match.dl_type = 0x0800

      msg.actions.append(of.ofp_action_output(port=2))

      event.connection.send(msg)

      msg = of.ofp_flow_mod()

      msg.priority = 10

      msg.idle_timeout = 0

      msg.hard_timeout = 0

      msg.match.in_port = 2

      msg.match.dl_type = 0x0806

      msg.actions.append(of.ofp_action_output(port=1))

      event.connection.send(msg)

      msg = of.ofp_flow_mod()

      msg.priority = 10

      msg.idle_timeout = 0

      msg.hard_timeout = 0

      msg.match.in_port = 2

      msg.match.dl_type = 0x0800

      msg.actions.append(of.ofp_action_output(port=1))

      event.connection.send(msg)

  elif event.connection.dpid == s17_dpid:

      msg = of.ofp_flow_mod()

      msg.priority = 10

      msg.idle_timeout = 0

      msg.hard_timeout = 0

      msg.match.in_port = 1

      msg.match.dl_type = 0x0806

      msg.actions.append(of.ofp_action_output(port=2))

      event.connection.send(msg)

      msg = of.ofp_flow_mod()

      msg.priority = 10

      msg.idle_timeout = 0

      msg.hard_timeout = 0

      msg.match.in_port = 1

      msg.match.dl_type = 0x0800

      msg.actions.append(of.ofp_action_output(port=2))

      event.connection.send(msg)

      msg = of.ofp_flow_mod()

      msg.priority = 10

      msg.idle_timeout = 0

      msg.hard_timeout = 0

      msg.match.in_port = 2

      msg.match.dl_type = 0x0806

      msg.actions.append(of.ofp_action_output(port=1))

      event.connection.send(msg)

      msg = of.ofp_flow_mod()

      msg.priority = 10

      msg.idle_timeout = 0

      msg.hard_timeout = 0

      msg.match.in_port = 2

      msg.match.dl_type = 0x0800

      msg.actions.append(of.ofp_action_output(port=1))

      event.connection.send(msg)

  elif event.connection.dpid == s18_dpid:

      msg = of.ofp_flow_mod()

      msg.priority = 10

      msg.idle_timeout = 0

      msg.hard_timeout = 0

      msg.match.in_port = 1

      msg.match.dl_type = 0x0806

      msg.actions.append(of.ofp_action_output(port=2))

      event.connection.send(msg)

      msg = of.ofp_flow_mod()

      msg.priority = 10

      msg.idle_timeout = 0

      msg.hard_timeout = 0

      msg.match.in_port = 1

      msg.match.dl_type = 0x0800

      msg.actions.append(of.ofp_action_output(port=2))

      event.connection.send(msg)

      msg = of.ofp_flow_mod()

      msg.priority = 10

      msg.idle_timeout = 0

      msg.hard_timeout = 0

      msg.match.in_port = 2

      msg.match.dl_type = 0x0806

      msg.actions.append(of.ofp_action_output(port=1))

      event.connection.send(msg)

      msg = of.ofp_flow_mod()

      msg.priority = 10

      msg.idle_timeout = 0

      msg.hard_timeout = 0

      msg.match.in_port = 2

      msg.match.dl_type = 0x0800

      msg.actions.append(of.ofp_action_output(port=1))

      event.connection.send(msg)

  elif event.connection.dpid == s19_dpid:

      msg = of.ofp_flow_mod()

      msg.priority = 10

      msg.idle_timeout = 0

      msg.hard_timeout = 0

      msg.match.in_port = 1

      msg.match.dl_type = 0x0806

      msg.actions.append(of.ofp_action_output(port=2))

      event.connection.send(msg)

      msg = of.ofp_flow_mod()

      msg.priority = 10

      msg.idle_timeout = 0

      msg.hard_timeout = 0

      msg.match.in_port = 1

      msg.match.dl_type = 0x0800

      msg.actions.append(of.ofp_action_output(port=2))

      event.connection.send(msg)

      msg = of.ofp_flow_mod()

      msg.priority = 10

      msg.idle_timeout = 0

      msg.hard_timeout = 0

      msg.match.in_port = 2

      msg.match.dl_type = 0x0806

      msg.actions.append(of.ofp_action_output(port=1))

      event.connection.send(msg)

      msg = of.ofp_flow_mod()

      msg.priority = 10

      msg.idle_timeout = 0

      msg.hard_timeout = 0

      msg.match.in_port = 2

      msg.match.dl_type = 0x0800

      msg.actions.append(of.ofp_action_output(port=1))

      event.connection.send(msg)

  elif event.connection.dpid == s20_dpid:

      msg = of.ofp_flow_mod()

      msg.priority = 10

      msg.idle_timeout = 0

      msg.hard_timeout = 0

      msg.match.in_port = 1

      msg.match.dl_type = 0x0806

      msg.actions.append(of.ofp_action_output(port=2))

      event.connection.send(msg)

      msg = of.ofp_flow_mod()

      msg.priority = 10

      msg.idle_timeout = 0

      msg.hard_timeout = 0

      msg.match.in_port = 1

      msg.match.dl_type = 0x0800

      msg.actions.append(of.ofp_action_output(port=2))

      event.connection.send(msg)

      msg = of.ofp_flow_mod()

      msg.priority = 10

      msg.idle_timeout = 0

      msg.hard_timeout = 0

      msg.match.in_port = 2

      msg.match.dl_type = 0x0806

      msg.actions.append(of.ofp_action_output(port=1))

      event.connection.send(msg)

      msg = of.ofp_flow_mod()

      msg.priority = 10

      msg.idle_timeout = 0

      msg.hard_timeout = 0

      msg.match.in_port = 2

      msg.match.dl_type = 0x0800

      msg.actions.append(of.ofp_action_output(port=1))

      event.connection.send(msg)

  elif event.connection.dpid == s21_dpid:

      msg = of.ofp_flow_mod()

      msg.priority = 10

      msg.idle_timeout = 0

      msg.hard_timeout = 0

      msg.match.in_port = 1

      msg.match.dl_type = 0x0806

      msg.actions.append(of.ofp_action_output(port=2))

      event.connection.send(msg)

      msg = of.ofp_flow_mod()

      msg.priority = 10

      msg.idle_timeout = 0

      msg.hard_timeout = 0

      msg.match.in_port = 1

      msg.match.dl_type = 0x0800

      msg.actions.append(of.ofp_action_output(port=2))

      event.connection.send(msg)

      msg = of.ofp_flow_mod()

      msg.priority = 10

      msg.idle_timeout = 0

      msg.hard_timeout = 0

      msg.match.in_port = 2

      msg.match.dl_type = 0x0806

      msg.actions.append(of.ofp_action_output(port=1))

      event.connection.send(msg)

      msg = of.ofp_flow_mod()

      msg.priority = 10

      msg.idle_timeout = 0

      msg.hard_timeout = 0

      msg.match.in_port = 2

      msg.match.dl_type = 0x0800

      msg.actions.append(of.ofp_action_output(port=1))

      event.connection.send(msg)

  elif event.connection.dpid == s22_dpid:

      msg = of.ofp_flow_mod()

      msg.priority = 10

      msg.idle_timeout = 0

      msg.hard_timeout = 0

      msg.match.in_port = 1

      msg.match.dl_type = 0x0806

      msg.actions.append(of.ofp_action_output(port=2))

      event.connection.send(msg)

      msg = of.ofp_flow_mod()

      msg.priority = 10

      msg.idle_timeout = 0

      msg.hard_timeout = 0

      msg.match.in_port = 1

      msg.match.dl_type = 0x0800

      msg.actions.append(of.ofp_action_output(port=2))

      event.connection.send(msg)

      msg = of.ofp_flow_mod()

      msg.priority = 10

      msg.idle_timeout = 0

      msg.hard_timeout = 0

      msg.match.in_port = 2

      msg.match.dl_type = 0x0806

      msg.actions.append(of.ofp_action_output(port=1))

      event.connection.send(msg)

      msg = of.ofp_flow_mod()

      msg.priority = 10

      msg.idle_timeout = 0

      msg.hard_timeout = 0

      msg.match.in_port = 2

      msg.match.dl_type = 0x0800

      msg.actions.append(of.ofp_action_output(port=1))

      event.connection.send(msg)

  elif event.connection.dpid==s14_dpid:

     a=packet.find('arp')

     if a and a.protodst=="10.0.0.11":

       msg = of.ofp_packet_out(data=event.ofp)

       msg.actions.append(of.ofp_action_output(port=21))

       event.connection.send(msg)

     if a and a.protodst=="10.0.0.12":

       msg = of.ofp_packet_out(data=event.ofp)

       msg.actions.append(of.ofp_action_output(port=22))

       event.connection.send(msg)

     if a and a.protodst=="10.0.0.13":

       msg = of.ofp_packet_out(data=event.ofp)

       msg.actions.append(of.ofp_action_output(port=23))

       event.connection.send(msg)

     if a and a.protodst=="10.0.0.14":

       msg = of.ofp_packet_out(data=event.ofp)

       msg.actions.append(of.ofp_action_output(port=24))

       event.connection.send(msg)

     if a and a.protodst=="10.0.0.15":

       msg = of.ofp_packet_out(data=event.ofp)

       msg.actions.append(of.ofp_action_output(port=25))

       event.connection.send(msg)

     if a and a.protodst=="10.0.0.16":

       msg = of.ofp_packet_out(data=event.ofp)

       msg.actions.append(of.ofp_action_output(port=26))

       event.connection.send(msg)

     if a and a.protodst=="10.0.0.17":

       msg = of.ofp_packet_out(data=event.ofp)

       msg.actions.append(of.ofp_action_output(port=27))

       event.connection.send(msg)

     if a and a.protodst=="10.0.0.18":

       msg = of.ofp_packet_out(data=event.ofp)

       msg.actions.append(of.ofp_action_output(port=28))

       event.connection.send(msg)

     if a and a.protodst=="10.0.0.19":

       msg = of.ofp_packet_out(data=event.ofp)

       msg.actions.append(of.ofp_action_output(port=29))

       event.connection.send(msg)

     if a and a.protodst=="10.0.0.20":

       msg = of.ofp_packet_out(data=event.ofp)

       msg.actions.append(of.ofp_action_output(port=30))

       event.connection.send(msg)

     if a and a.protodst=="10.0.0.1":

       msg = of.ofp_packet_out(data=event.ofp)

       msg.actions.append(of.ofp_action_output(port=1))

       event.connection.send(msg)

     if a and a.protodst=="10.0.0.2":

       msg = of.ofp_packet_out(data=event.ofp)

       msg.actions.append(of.ofp_action_output(port=2))

       event.connection.send(msg)

     if a and a.protodst=="10.0.0.3":

       msg = of.ofp_packet_out(data=event.ofp)

       msg.actions.append(of.ofp_action_output(port=3))

       event.connection.send(msg)

     if a and a.protodst=="10.0.0.4":

       msg = of.ofp_packet_out(data=event.ofp)

       msg.actions.append(of.ofp_action_output(port=4))

       event.connection.send(msg)

     if a and a.protodst=="10.0.0.5":

       msg = of.ofp_packet_out(data=event.ofp)

       msg.actions.append(of.ofp_action_output(port=5))

       event.connection.send(msg)

     if a and a.protodst=="10.0.0.6":

       msg = of.ofp_packet_out(data=event.ofp)

       msg.actions.append(of.ofp_action_output(port=6))

       event.connection.send(msg)

     if a and a.protodst=="10.0.0.7":

       msg = of.ofp_packet_out(data=event.ofp)

       msg.actions.append(of.ofp_action_output(port=7))

       event.connection.send(msg)

     if a and a.protodst=="10.0.0.8":

       msg = of.ofp_packet_out(data=event.ofp)

       msg.actions.append(of.ofp_action_output(port=8))

       event.connection.send(msg)

     if a and a.protodst=="10.0.0.9":

       msg = of.ofp_packet_out(data=event.ofp)

       msg.actions.append(of.ofp_action_output(port=9))

       event.connection.send(msg)

     if a and a.protodst=="10.0.0.10":

       msg = of.ofp_packet_out(data=event.ofp)

       msg.actions.append(of.ofp_action_output(port=10))

       event.connection.send(msg)

     msg = of.ofp_flow_mod()

     msg.priority =100

     msg.idle_timeout = 0

     msg.hard_timeout = 0

     msg.match.dl_type = 0x0800

     msg.match.nw_dst = "10.0.0.1"

     msg.actions.append(of.ofp_action_output(port = 1))

     event.connection.send(msg)

     msg = of.ofp_flow_mod()

     msg.priority =100

     msg.idle_timeout = 0

     msg.hard_timeout = 0

     msg.match.dl_type = 0x0800

     msg.match.nw_dst = "10.0.0.2"

     msg.actions.append(of.ofp_action_output(port = 2))

     event.connection.send(msg)

     msg = of.ofp_flow_mod()

     msg.priority =100

     msg.idle_timeout = 0

     msg.hard_timeout = 0

     msg.match.dl_type = 0x0800

     msg.match.nw_dst = "10.0.0.3"

     msg.actions.append(of.ofp_action_output(port = 3))

     event.connection.send(msg)

     msg = of.ofp_flow_mod()

     msg.priority =100

     msg.idle_timeout = 0

     msg.hard_timeout = 0

     msg.match.dl_type = 0x0800

     msg.match.nw_dst = "10.0.0.4"

     msg.actions.append(of.ofp_action_output(port = 4))

     event.connection.send(msg)

     msg = of.ofp_flow_mod()

     msg.priority =100

     msg.idle_timeout = 0

     msg.hard_timeout = 0

     msg.match.dl_type = 0x0800

     msg.match.nw_dst = "10.0.0.5"

     msg.actions.append(of.ofp_action_output(port = 5))

     event.connection.send(msg)
	 
     msg = of.ofp_flow_mod()

     msg.priority =100

     msg.idle_timeout = 0

     msg.hard_timeout = 0

     msg.match.dl_type = 0x0800

     msg.match.nw_dst = "10.0.0.6"

     msg.actions.append(of.ofp_action_output(port = 6))

     event.connection.send(msg)

     msg = of.ofp_flow_mod()

     msg.priority =100

     msg.idle_timeout = 0

     msg.hard_timeout = 0

     msg.match.dl_type = 0x0800

     msg.match.nw_dst = "10.0.0.7"

     msg.actions.append(of.ofp_action_output(port = 7))

     event.connection.send(msg)

     msg = of.ofp_flow_mod()

     msg.priority =100

     msg.idle_timeout = 0

     msg.hard_timeout = 0

     msg.match.dl_type = 0x0800

     msg.match.nw_dst = "10.0.0.8"

     msg.actions.append(of.ofp_action_output(port = 8))

     event.connection.send(msg)

     msg = of.ofp_flow_mod()

     msg.priority =100

     msg.idle_timeout = 0

     msg.hard_timeout = 0

     msg.match.dl_type = 0x0800

     msg.match.nw_dst = "10.0.0.9"

     msg.actions.append(of.ofp_action_output(port = 9))

     event.connection.send(msg)

     msg = of.ofp_flow_mod()

     msg.priority =100

     msg.idle_timeout = 0

     msg.hard_timeout = 0

     msg.match.dl_type = 0x0800

     msg.match.nw_dst = "10.0.0.10"

     msg.actions.append(of.ofp_action_output(port = 10))

     event.connection.send(msg)

     msg = of.ofp_flow_mod()

     msg.priority =100

     msg.idle_timeout = 0

     msg.hard_timeout = 0

     msg.match.dl_type = 0x0800

     msg.match.nw_dst = "10.0.0.11"

     msg.actions.append(of.ofp_action_output(port = 21))

     event.connection.send(msg)

     msg = of.ofp_flow_mod()

     msg.priority =100

     msg.idle_timeout = 0

     msg.hard_timeout = 0

     msg.match.dl_type = 0x0800

     msg.match.nw_dst = "10.0.0.12"

     msg.actions.append(of.ofp_action_output(port = 22))

     event.connection.send(msg)

     msg = of.ofp_flow_mod()

     msg.priority =100

     msg.idle_timeout = 0

     msg.hard_timeout = 0

     msg.match.dl_type = 0x0800

     msg.match.nw_dst = "10.0.0.13"

     msg.actions.append(of.ofp_action_output(port = 23))

     event.connection.send(msg)

     msg = of.ofp_flow_mod()

     msg.priority =100

     msg.idle_timeout = 0

     msg.hard_timeout = 0

     msg.match.dl_type = 0x0800

     msg.match.nw_dst = "10.0.0.14"

     msg.actions.append(of.ofp_action_output(port = 24))

     event.connection.send(msg)

     msg = of.ofp_flow_mod()

     msg.priority =100

     msg.idle_timeout = 0

     msg.hard_timeout = 0

     msg.match.dl_type = 0x0800

     msg.match.nw_dst = "10.0.0.15"

     msg.actions.append(of.ofp_action_output(port = 25))

     event.connection.send(msg)

     msg = of.ofp_flow_mod()

     msg.priority =100

     msg.idle_timeout = 0

     msg.hard_timeout = 0

     msg.match.dl_type = 0x0800

     msg.match.nw_dst = "10.0.0.16"

     msg.actions.append(of.ofp_action_output(port = 26))

     event.connection.send(msg)

     msg = of.ofp_flow_mod()

     msg.priority =100

     msg.idle_timeout = 0

     msg.hard_timeout = 0

     msg.match.dl_type = 0x0800

     msg.match.nw_dst = "10.0.0.17"

     msg.actions.append(of.ofp_action_output(port = 27))

     event.connection.send(msg)

     msg = of.ofp_flow_mod()

     msg.priority =100

     msg.idle_timeout = 0

     msg.hard_timeout = 0

     msg.match.dl_type = 0x0800

     msg.match.nw_dst = "10.0.0.18"

     msg.actions.append(of.ofp_action_output(port = 28))

     event.connection.send(msg)

     msg = of.ofp_flow_mod()

     msg.priority =100

     msg.idle_timeout = 0

     msg.hard_timeout = 0

     msg.match.dl_type = 0x0800

     msg.match.nw_dst = "10.0.0.19"

     msg.actions.append(of.ofp_action_output(port = 29))

     event.connection.send(msg)

     msg = of.ofp_flow_mod()

     msg.priority =100

     msg.idle_timeout = 0

     msg.hard_timeout = 0

     msg.match.dl_type = 0x0800

     msg.match.nw_dst = "10.0.0.20"

     msg.actions.append(of.ofp_action_output(port = 30))

     event.connection.send(msg)

def launch ():

  global start_time,count

  core.openflow.addListenerByName("PortStatsReceived",_handle_portstats_received)

  core.openflow.addListenerByName("ConnectionUp", _handle_ConnectionUp)

  core.openflow.addListenerByName("PacketIn",_handle_PacketIn)
