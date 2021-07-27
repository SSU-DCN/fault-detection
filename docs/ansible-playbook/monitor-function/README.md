# Ansible-playbook
This repo includes Ansible-playbook for installing Monitor function (NFV Closed-loop).
To get started, Change the ansible_host and ansible_user of both alertmanager and prometheus in the hosts file and run:
```
$ ansible-playbook main.yml  -i hosts
```
To customize the parameter, check each role's default var.
