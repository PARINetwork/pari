#!bin/bash

chmod 400 pari_qa.pem
#todo find a elegant way to instruct ansible to take right pem
cp pari_qa.pem ~/.ssh/id_rsa
git clone https://github.com/PARINetwork/pari-ansible.git
cd pari-ansible
ansible-playbook -l staging -u ubuntu -i hosts.yml -t deploy site.yml
