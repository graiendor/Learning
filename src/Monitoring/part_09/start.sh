#!/bin/bash

bash install_moy_exporter.sh

sudo cp nginx.conf /etc/nginx/nginx.conf
sudo cp prometheus.yml /etc/prometheus/prometheus.yml

sudo systemctl daemon-reload
sudo systemctl start moy_exporter.service
sudo systemctl enable moy_exporter.service

sudo nginx -s reload
