## PARI (People's Archive of Rural India)

To learn more about the archive, please visit
[About Us](https://ruralindiaonline.org/about/) page on https://ruralindiaonline.org/

### Setup the code

```bash
$ git clone https://github.com/PARINetwork/pari-ansible/
# Replace the IP address in the local section of hosts.yml to add your server entry
$ virtualenv ansible_env
$ source ./ansible_env/bin/activate
$ cd pari-ansible
# Has been tested on Ubuntu 14.04 VMs
$ ansible-playbook -i hosts.yml -l local -u ubuntu site.yml
# Subsequently to deploy any code changes
$ ansible-playbook -i hosts.yml -l local -u ubuntu -t deploy site.yml
```

### Copyright

Licensed under the 3-clause BSD License. Please refer the `LICENSE.txt` for details.
