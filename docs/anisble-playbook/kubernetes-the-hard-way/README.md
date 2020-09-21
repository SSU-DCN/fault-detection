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
Change the variables in ca.yaml
