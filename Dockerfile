FROM ubuntu:20.04

RUN apt-get update && apt-get install -y software-properties-common && add-apt-repository -y ppa:oisf/suricata-stable && apt-get update && apt-get install -y suricata python3 python3-pip

WORKDIR /app

COPY . .

CMD ["suricata", "-c", "suricata.yaml", "-i", "eth0"]
