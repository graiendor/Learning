#!bin/bash

VERSION="0.18.1"
wget https://github.com/prometheus/node_exporter/releases/download/v$VERSION/node_exporter-$VERSION.linux-amd64.tar.gz -O - | tar -xzv -C /tmp
sudo cp /tmp/node_exporter-$VERSION.linux-amd64/node_exporter /usr/local/bin
sudo chown -R prometheus:prometheus /usr/local/bin/node_exporter

sudo cp node_exporter.service /etc/systemd/system/node_exporter.service
