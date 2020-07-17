## Prometheus commands 

```
./prometheus --config.file=prometheus.yml --web.enable-lifecycle
--web.enable-lifecycle: enable Prometheus to reload its configuration at runtime.
Send POST request to /-/reload to reload.  curl -s -XPOST localhost:9090/-/reload
```

## Prometheus-openstack-exporter
```
docker run --env-file openstack-expoter-config -it rakeshpatnaik/prometheus-openstack-exporter:v0.2 -p 9103:9103

Pull exporter image and expose to port 9103. 
```