#!/bin/bash



sudo systemctl daemon-reload
sudo systemctl start grafana-server
sudo systemctl start node_exporter.service
sudo systemctl enable node_exporter.service

prometheus --config.file=/etc/prometheus/prometheus.yml 
