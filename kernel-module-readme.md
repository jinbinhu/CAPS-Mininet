# Description  
  
The kernel modules of CAPS (Coding-based Adaptive Packet Spraying).   
The kernel modules include coding (sender/codemod.c) and decoding (receiver/decodemod.c) at the sender and receiver, respectively.  
  
# Compiling  
  
We have tested the kernel modules with Linux kernel 3.11.0-15-generic under ubuntu 12.04.   
You need the corresponding kernel header files to compile them.   
**Please change the downloaded files to the executable files.**
```Bash
sudo chmod -R 777 * 
```  
  
## 1. Installing:
at the sender: 
```Bash  
sudo ./sender.sh
```
    
at the receiver:
```Bash   
sudo ./receiver.sh 
```  
Please enter the parameters (Network card name，Source IP address, Destination IP address，Source MAC，Destination MAC） according to the terminal prompt. Then the kernel modules named codemod.ko and decodemod.ko have been inserted. 
    
## 2. At the end of testing, you can remove the kernel modules:    
at the sender: 
```Bash  
sudo rmmod codemod.ko  
```  
    
at the receiver: 
```Bash  
sudo rmmod decodemod.ko  
```  
  
# Usage  

We have tested the coding of the following check matrix. We also support the other check matrices generated according to actual requirements including the low density parity check matrices.  
![image](https://github.com/jinbinhu/CAPS-Mininet/blob/master/check_matrix.png)

For example, the detailed steps of testing the above matrix are as follows:

#### 1. Please do the first step "1.Installing:" described in this document; 

#### 2. Open Wireshark at the sender or receiver, capturing （e.g eth0）;  
（Install wireshark: *sudo apt-get install wireshark*）

#### 3. At the receiver: 

##### 1). compile the file “recv_app” in the file fold “recv_app”, generate the executable file “recv_app”:

```Bash
  cd recv_app
  sudo make 
```
##### 2). run the file "recv_app":

```Bash
  sudo ./recv_app 192.168.188.133
```
##### 192.168.188.133 is the IP address at receiver.

##### 3). waiting for receiving requests from client.

#### 4. At the sender:

##### 1). compile the file “send_app” in the file fold “send_app”, generate the executable file “send_app”:
  
```Bash
  cd send_app
  sudo make
```
##### 2). run the file "send_app" to send a message (8 source packets) to the receiver:
  
```Bash 
  sudo ./send_app  192.168.188.133
```
##### 192.168.188.133 is the IP address at receiver.

#### 5. Now, we can capture 8 source packets and 4 encoding packets in the Wireshark as the following picture:

  wireshark filter: tcp and ip.addr == ***ip address*** at sender or receiver (e.g. 192.168.188.133)
   
![image](https://github.com/jinbinhu/CAPS-Mininet/blob/master/wireshark-capturepkt.png)
  
The results show that we send the source message, and the 8 source packets of the message are encoded into 12 encoded packets in the kernel at the sender, then the encoded packets are decoded successfully in the kernel at the receiver, the received message on the application layer at the receiver is the same as the source message.
  
  
**Note:** Because the following files exceed 25M, you can download the test environment (ubuntu 12.04 with Linux kernel 3.11.0-15-generic) at the following address:
https://pan.baidu.com/s/1zzm32pk5YKivlKxIB1GCVQ  
Download password： gczb   
sudo password: master    
  
If you have any questions, please email to jinbinhu@csu.edu.cn.  




