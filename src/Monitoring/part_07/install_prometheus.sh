#!/bin/bash

wget https://github.com/prometheus/prometheus/releases/download/v2.35.0/prometheus-2.35.0.linux-amd64.tar.gz

tar -xvf prometheus-2.35.0.linux-amd64.tar.gz 

mv prometheus-2.35.0.linux-amd64 prometheus-files

sudo useradd --no-create-home --shell /bin/false prometheus
sudo mkdir /etc/prometheus
sudo mkdir /var/lib/prometheus
sudo chown prometheus:prometheus /etc/prometheus
sudo chown prometheus:prometheus /var/lib/prometheus

sudo cp prometheus-files/prometheus /usr/bin/
sudo cp prometheus-files/promtool /usr/bin/
sudo chown prometheus:prometheus /usr/bin/prometheus
sudo chown prometheus:prometheus /usr/bin/promtool

sudo cp -r prometheus-files/consoles /etc/prometheus
sudo cp -r prometheus-files/console_libraries /etc/prometheus
sudo chown -R prometheus:prometheus /etc/prometheus/consoles
sudo chown -R prometheus:prometheus /etc/prometheus/console_libraries

sudo cp prometheus.yml /etc/prometheus/prometheus.yml

sudo rm -rf prometheus-2.35.0.linux-amd64.tar.gz prometheus-files

# sudo bash install_node_exporter.sh