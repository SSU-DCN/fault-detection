## Create key
openssl genrsa -out prometheus.key 2048

## Create key with username: prometheus, group: monitor-tools
openssl req -new -key prometheus.key -out prometheus.csr -subj "/CN=prometheus/O=monitor-tools"

## Create Certificate Signing Requests
https://kubernetes.io/docs/reference/access-authn-authz/certificate-signing-requests/

## Create Clusterrole and ClusterroleBinding
https://kubernetes.io/docs/reference/access-authn-authz/rbac/
