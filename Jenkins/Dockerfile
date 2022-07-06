FROM jenkins/jenkins:lts
USER root
RUN apt-get update \
    && apt-get install -y python3.10 pip \
    && rm -rf /var/lib/apt/lists/*
RUN pip install tox