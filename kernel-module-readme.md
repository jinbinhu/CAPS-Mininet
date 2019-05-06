# Description  
  
The kernel modules of CAPS (Coding-based Adaptive Packet Spraying).   
The kernel modules include coding (codemod.c) and decoding (decodemod.c) at the sender and receiver, respectively.  
  
# Compiling  
  
We have tested the kernel modlues with Linux kernel 3.11.0-15-generic under ubuntu 12.04.   
You need the corresponding kernel header files to compile them.   
  
## 1. Modify parameters:
Before compiling, please modify the following parameters according to the actual environment:  
#define ETH "eth0"  //NIC name  
#define DST_IP "192.168.188.133" &nbsp; //IP address at receiver  
#define SRC_IP "192.168.188.136" &nbsp; //IP address at sender  
unsigned char SMAC[ETH_ALEN] = {0x00,0x0C,0x29,0x7E,0xB1,0x35}; &nbsp; //MAC address at sender  
unsigned char DMAC[ETH_ALEN] = {0x00,0x0C,0x29,0x18,0xE7,0x78}; &nbsp; //MAC address at receiver  
  
## 2. At the sender:  
```Bash  
cd sender  
make 
```
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
```Bash  
insmod codemod.ko 
```
    
at the receiver:
```Bash   
insmod decodemod.ko 
```  
    
### 2)To remove the kernel modules:    
at the sender: 
```Bash  
rmmod codemod.ko  
```  
    
at the receiver: 
```Bash  
rmmod decodemod.ko  
```  
  
# Usage  

We have tested the coding of the following check matrix. We also support the other check matrices generated according to actual requirements including the low density parity check matrices.  
![image](https://github.com/jinbinhu/CAPS-Mininet/blob/master/check_matrix.png)

For example, the detailed steps of testing the above matrix are as follows:
1. Please follow the steps described in 1, 2, 3, 4 1) above in this document;

2. Open Wireshark at the sender or receiver;

3. At the receiver: compile the file “recv_app” in the file fold “recv_app” 
```Bash
  cd recv_app
  make 
```
generate the executable file “recv_app”, run "recv_app":

```Bash
  ./recv_app
```
waiting for receiving requests from client.

4. At the sender: compile the file “send_app” in the file fold “send_app”
```Bash
  cd send_app
  make
```
  generate executable file “send_app”, run "send_app":
  
```Bash
  ./send_app
```
we have sent a message (8 source packets) to the receiver.

5. Now, we can capture 8 source packets and 4 encoding packets in the Wireshark as the following picture:

   filter: tcp and ip.addr == ip address (sender or receiver)
   
![image](https://github.com/jinbinhu/CAPS-Mininet/blob/master/wireshark-capturepkt.png)
  
The results show that we send the source message, and the 8 source packets of the message are encoded into 12 encoded packets in the kernel at the sender, then the encoded packets are decoded successfully in the kernel at the receiver, the received message on the application layer at the receiver is the same as the source message.
  
If you have any questions, please email to jinbinhu@csu.edu.cn.  




