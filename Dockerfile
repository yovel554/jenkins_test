FROM jenkins/jenkins:latest
USER root
RUN apt-get install -y pip
# Install app dependencies
RUN pip install --upgrade pip
COPY mod_add.py /
COPY test_add.py /



