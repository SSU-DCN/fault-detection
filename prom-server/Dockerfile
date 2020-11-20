FROM ubuntu
ENV TZ=Asia/Seoul
RUN ln -snf /usr/share/zoneinfo/$TZ /etc/localtime && echo $TZ > /etc/timezone
RUN apt-get update -y \
    && apt-get install prometheus -y \
    && apt-get install python3-pip -y

COPY alert-rule.yml /etc/prometheus/alert-rule.yml
COPY targets.json /etc/prometheus/targets.json
COPY prometheus.yml /etc/prometheus/prometheus.yml

WORKDIR /prometheus
COPY . .
RUN python3 -m pip install -r requirements.txt

# RUN service prometheus start
# CMD prometheus --config.file="/etc/prometheus/prometheus.yml" \
#     && python3 server.py  --filesd /etc/prometheus/targets.json --alertfile /etc/prometheus/alert-rule.yml

ENTRYPOINT ["/bin/bash", "extendPrometheus.sh"]
CMD ["--web.enable-lifecycle"]

# Usage:
# docker build -t starlab:v1 --force-rm -f Dockerfile .
# docker run -p 9090:9090 --name prometheus -itd starlab:v1 [option]
