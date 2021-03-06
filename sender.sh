#!/bin/bash

echo "Please enter ETH name: e.g. eth0" 
read ETH
echo "Please enter DST_IP address: e.g. 192.168.188.133"
read DSTIP
echo "Please enter SRC_IP address: e.g. 192.168.188.136" 
read SRCIP
echo "Please enter SRC_MAC address: e.g. 0x00,0x0C,0x29,0x7E,0xB1,0x35" 
read SMAC
echo "Please enter DST_MAC address: e.g. 0x00,0x0C,0x29,0x7E,0xB1,0x35" 
read DMAC


eth="#define ETH \"$ETH\""
dstip="#define DST_IP \"$DSTIP\""
srcip="#define SRC_IP \"$SRCIP\""
smac="unsigned char SMAC[ETH_ALEN] = {$SMAC};"
dmac="unsigned char DMAC[ETH_ALEN] = {$DMAC};"


cd sender 
sed -i "/#define ETH/c\\$eth" codemod.c
sed -i "/#define DST_IP/c\\$dstip" codemod.c
sed -i "/#define SRC_IP/c\\$srcip" codemod.c
sed -i "/unsigned char SMAC[ETH_ALEN]/c\\$smac" codemod.c
sed -i "/unsigned char DMAC[ETH_ALEN]/c\\$smac" codemod.c

sudo make

sudo insmod codemod.ko


