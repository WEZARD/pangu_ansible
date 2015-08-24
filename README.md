# pangu_ansible

#Overview

storm running on a cluster with zookeeper and redis

#Building

yum install rpmdevtools   -- you should use the rpmdevtools to make rpm, and the .spec is under roles/*/files

download the source code

sudo make rpm   -- especially for storm, you should rename the apache-storm-0.9.2-incubating as storm-0.9.2 when making rpm

#Installing

ansible-playbook install-pangu.yml

#Running the services

ansible-playbook start-pangu.yml
