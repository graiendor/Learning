#!bin/bash

sudo docker build -t jenkins-python .

sudo docker run --rm -p 8080:8080 -p 50000:50000 \
        -v `pwd`/volume:/var/jenkins_home jenkins-python