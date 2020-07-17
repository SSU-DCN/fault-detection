## Prometheus commands 

```
./prometheus --config.file=prometheus.yml --web.enable-lifecycle
--web.enable-lifecycle: enable Prometheus to reload its configuration at runtime.
Send POST request to /-/reload to reload.  curl -s -XPOST localhost:9090/-/reload
```
