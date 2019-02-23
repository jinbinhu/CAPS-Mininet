# Description  
  
The kernel modules of CAPS (Coding-based Adaptive Packet Spraying).   
The kernel modules include coding (codemod.c) and decoding (decodemod.c) at the sender and receiver, respectively.  
  
# Compiling  
  
We have tested the kernel modlues with Linux kernel 3.11.0-15-generic.   
You need the corresponding kernel header files to compile them.   
  
## 1. Modify parameters:
Before compiling, please modify the following parameters according to the actual environment:  
#define ETH "eth0"  //NIC name  
#define DST_IP "192.168.188.133"    //IP address at receiver  
#define SRC_IP "192.168.188.136"    //IP address at sender  
unsigned char SMAC[ETH_ALEN] = {0x00,0x0C,0x29,0x7E,0xB1,0x35};   //MAC address at sender  
unsigned char DMAC[ETH_ALEN] = {0x00,0x0C,0x29,0x18,0xE7,0x78};   //MAC address at receiver  
  
## 2. At the sender:  
cd sender  
make  
Then you can get a kernel module called codemod.ko.  
  
## 3. At the receiver:  
```Bash  
cd receiver  
make
```
Then you can get a kernel module called decodemod.ko.  
  
## 4. Installing  
codemod.ko and decodemod.ko hook into the data path using netfilter hooks.   
  
### 1)To install it:   
at the sender:  
insmod codemod.ko 
  
at the receiver:  
insmod decodemod.ko  
  
### 2)To remove the kernel modules:    
at the sender:  
rmmod codemod.ko  
  
at the receiver:  
rmmod decodemod.ko  
  
# Usage  

We have tested the coding of the following check matrix. We also support the other check matrices generated according to actual requirements including the low density parity check matrices.  
![image](https://github.com/jinbinhu/CAPS-Mininet/blob/master/check_matrix.png)
  
If you have any questions, please email to jinbinhu@csu.edu.cn.  




