# Description:  
This is a simple implementation of CAPS on kenel and we test CAPS based on mininet 2.3.0.  
  
# Usage:  
Before testing, you should make sure that mininet and the related tools including pox, wireshark, netfilter and python2 are correctly installed. The topology is a leaf-spine structure with 20 senders, 20 receivers, 2 ToR switches and 20 core switches.  
  
### 1. Insert the coding kernel modules.
please refer to the file "kernel-module-readme.md" for the related details.   
  
### 2. In the pox directory, open the controller:  
```Bash
sudo ./pox.py lab_controller_caps  
```   
  
### 3. In the mininet directory, create the topology:    
```Bash  
sudo python ./mininet-caps.py
```  
Note that if the mininet can not run normally, you can try the command "sudo mn -c" to clean up mininet.   
  
### 4. capture the packets on the specified ports of switches using wireshark.  
  
If you have any questions, please email to jinbinhu@csu.edu.cn.  
