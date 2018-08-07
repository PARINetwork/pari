#!/usr/bin/env bash

# traivis_wait doesn't work with deploy script
# Workaround to make travis wait for more than default wait time(10 mins) before aborting the build
# Refer: https://github.com/travis-ci/travis-ci/issues/7961
while true; do echo "Deploying..."; sleep 60; done &

# Deployment steps
chmod 400 pari_qa
#todo find a elegant way to instruct ansible to take right pem
cp pari_qa ~/.ssh/id_rsa
git clone https://github.com/PARINetwork/pari-ansible.git
cd pari-ansible
ansible-playbook -l staging -u ubuntu -i hosts.yml -t deploy site.yml
exit $?