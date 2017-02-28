![N|Solid](https://ruralindiaonline.org/static/img/logo.png)    **People's Archive Of Rural India**

**[PARI](https://ruralindiaonline.org/)** is a digital journalism platform in India, founded by veteran journalist and former rural affairs editor of 'The Hindu', **Palagummi Sainath**. **PARI** is a volunteer-run rural journalism platform.

## Dev Setup

#### Clone Repositories
To start with the dev box setup, clone the pari_ansible repository.
```sh
$ git clone https://github.com/PARINetwork/pari-ansible.git
$ git clone https://github.com/PARINetwork/pari.git
```
#### Setup the Vagrant Box
Setup the vagrant box in your machine. You can download th e-vagrant box from [here.](https://releases.hashicorp.com/vagrant/1.9.1/vagrant_1.9.1.dmg) 
After downloading and installing the Vagrant box, run the ansible_playbook commands from  **pari_ansible** folder,

**Note**
    Replace the **--private-key** in the ansible-playbook command given below with the value of **IdentityFile** , you will get you         IdentityFile by runnig this commnd.
    
```sh 
$ cd pari
$ sudo vagrant ssh-config
```
Commands to run the ansible script,
```sh
$ cd pari-ansible
$ ansible-playbook --private-key=<../pari/.vagrant/machines/default/virtualbox/private_key> -l vagrant -u vagrant -i hosts.yml site.yml
```
The ansible-playbook command will setup all the dependencies and create a environment.

Now get the Vagrant box up and running as below:
```sh 
$ cd pari
$ sudo vagrant up
$ sudo vagrant ssh
```
Go to your virtual environment
```sh 
$ cd /vagrant
$ source pari_env/bin/activate
```
**Note**
To come out from the environment you can run 
```sh
$ deactivate
```
All dependencies like gunicorn, elasticSearch and nginx are up and running in the virtual box.

### Tech stack:

* [Django](https://www.djangoproject.com/) - Ease the creation of complex, database-driven websites.
* [Wagtail]() - CMS on top of Django framework
* [Python]() - Features a dynamic type system and automatic memory management and supports multiple programming paradigms.
* [Bootstrap]() - Great UI boilerplate for modern web apps
* [jQuery]() - duh

### Copyright

Licensed under the 3-clause BSD License. Please refer the LICENSE.txt for details.
