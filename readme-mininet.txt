Description:
This is a simple implementation of CAPS on kenel and we test CAPS based on mininet 2.3.0.

Usage:
Before testing, you should make sure that python2, mininet including related tools, pox, wireshark, and netfilter are correctly installed. 
The topology is a leaf-spine structure with 20 senders, 20 receivers, 2 ToR switches and 20 core switches.

1. insert the coding kernel modules (please refer to the kernel-module-readme.txt). 

2. in the /pox, open the controller: 
sudo ./pox.py lab_controller_caps

3. in the /mininet, create the topology:  
sudo python ./mininet-caps.py
Note that if the mininet can not run normally, you can try the command "sudo mn -c" to clean up mininet. 

4. capture the packets on the specified ports of switches using wireshark.

If you have any questions, please email to jinbinhu@csu.edu.cn.