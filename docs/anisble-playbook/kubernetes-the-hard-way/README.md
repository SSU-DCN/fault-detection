This folder include the ansible playbook to bootstrap K8S cluster from binary (Ubuntu host)
This work based on the fancy guides, called as "kubernetes-the-hard-way", you can found it in:
```
https://github.com/kelseyhightower/kubernetes-the-hard-way/blob/master/docs/02-client-tools.md
```
You should firstly install Ansible in local host that runs this script as following:
```
$ sudo apt update
$ sudo apt install software-properties-common
$ sudo apt-add-repository --yes --update ppa:ansible/ansible
$ sudo apt install ansible
```
The ref link : https://docs.ansible.com/ansible/latest/installation_guide/intro_installation.html#installing-ansible-on-ubuntu

To run the scripts:
```
$ ansible -i hosts main.yaml
```
