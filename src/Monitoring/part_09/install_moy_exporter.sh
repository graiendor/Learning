sudo cp moy_exporter /usr/local/bin
# sudo chown -R prometheus:prometheus /usr/local/bin/moy_exporter

sudo cp moy_exporter.service /etc/systemd/system/moy_exporter.service
sudo cp nginx.conf /etc/nginx/nginx.conf

sudo mkdir /metric
sudo chown -R graien /metric
sudo chmod 777 /metric