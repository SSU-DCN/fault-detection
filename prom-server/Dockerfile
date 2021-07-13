FROM python:3.6-slim-buster
WORKDIR /app
COPY . .
RUN python3 -m pip install -r requirements.txt

# RUN service prometheus start
# CMD prometheus --config.file="/etc/prometheus/prometheus.yml" \
#     && python3 server.py  --filesd /etc/prometheus/targets.json --alertfile /etc/prometheus/alert-rule.yml

CMD ["python3", "server.py", "--filesd", "targets.json", "--alertfile", "alert-rule.yml" ]

# Usage:
# docker build -t starlab:v1 --force-rm -f Dockerfile .
# docker run -p 9090:9090 --name prometheus -itd starlab:v1 [option]
