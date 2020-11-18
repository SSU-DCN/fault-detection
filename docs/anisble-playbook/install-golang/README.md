This folder, I write an ansible play-book for go1.15 installation.

If there is no ansbile in your hosts, you should firstly install Ansible in local host to run this script as following:
```
$ sudo apt update
$ sudo apt install software-properties-common
$ sudo apt-add-repository --yes --update ppa:ansible/ansible
$ sudo apt install ansible
```
To run the scripts:
```
$ ansible-playbook -i hosts main.yaml
```
