# fault-detection
This repo include 3 sub component:
- Alert-hook: Receives Alert Manager's events and send it to Tacker because Alert Manager couldn't create custom request to Openstack
- Doc: Ansible playbook to create K8s Cluster, deploy node-exporter to multiple nodes and configure service discovery for K8s Nodes
- prom-server: Create a GRPC server to receive new services created by Tacker and add to Prometheus's file discovery (This should by deployed the same server as Prometheus)
