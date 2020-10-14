This folder includes the ansible playbook scripts to bootstrap a K8S cluster from binaries on Ubuntu host.
This work based on the fancy guides, called as "kubernetes-the-hard-way", you also can found it in:
```
https://github.com/kelseyhightower/kubernetes-the-hard-way/blob/master/docs/02-client-tools.md
```
You should firstly install Ansible in local host to run this script as following:
```
$ sudo apt update
$ sudo apt install software-properties-common
$ sudo apt-add-repository --yes --update ppa:ansible/ansible
$ sudo apt install ansible
```
The ref link for installing Ansible guide: https://docs.ansible.com/ansible/latest/installation_guide/intro_installation.html#installing-ansible-on-ubuntu

To run the scripts:
```
$ ansible -i hosts main.yaml
```
Note:
- This document use "dcn" that is set as root user in both master and worker node.
- If you wanna change to another user, some part in the source scripts should be changed to correctly bootstrap k8s-cluster.
- The "dcn" user should be added to sudoers by changing /etc/sudoers directory as following:
```
$ sudo visudo
```
```
dcn   ALL=(ALL:ALL) ALL
dcn   ALL=(ALL) NOPASSWD: ALL
```
- The infomation of master node and worker nodes such as: IP address, hostname... should be change to match your environment:
```
  + hosts
tasks/
  + bootstrap_controller.yaml
  + bootstrap_etcd.yaml
  + ca.yaml
  + kube-config.yaml
```
- The related pod-migartion document can be found here: https://docs.google.com/document/d/1E5p_FOHDGAp5YEQ23dCi9I8wPnMzd4aOazxI4uO_AMo/edit#
  
 
