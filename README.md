# pangu_ansible

#Overview

storm running on a cluster with zookeeper and redis

#Building

yum install rpmdevtools   -- you should use the rpmdevtools to make rpm, and the .spec is under roles/*/files

download the source code

make rpm   

#Installing

ansible-playbook install-pangu.yml

#Running the services

ansible-playbook start-pangu.yml
