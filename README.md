![N|Solid](https://ruralindiaonline.org/static/img/logo.png)    **People's Archive Of Rural India**
# Documentation
**Pari** is a digital journalism platform in India. Founded by veteran journalist and former Rural Affairs Editor of The Hindu, **Palagummi Sainath**, **PARI** is a volunteer-run rural journalism platform.

## Dev Setup

#### clone Repositories
To start with the dev setup, clone the pari_ansible repository.
```sh
$ git clone https://github.com/PARINetwork/pari-ansible.git
$ git clone https://github.com/PARINetwork/pari.git
```
#### Setup the Vagrant Box
Setup the vagrant box in you machine.You can download th evagrant from the link given bellow
Downoad  [Vagrant here.](https://releases.hashicorp.com/vagrant/1.9.1/vagrant_1.9.1.dmg) 
After downloading and installing the Vgarant box Run the ansible_playbook below commands from you **pari_ansible** folder,

**Note**
    Replace the **--private-key** in the ansible-playbook command given bellow with the value of **IdentityFile** , you will get you         IdentityFile by runnig this commnd.
    
```sh 
$ cd pari
$ sudo vagrant ssh-config
```
Cammands to run the ansible script,
```sh
$ cd pari-ansible
$ ansible-playbook --private-key=<../pari/.vagrant/machines/default/virtualbox/private_key> -l vagrant -u vagrant -i hosts.yml site.yml
```
The ansible-playbook command will setup all the deppendencies and create a environment.
Now make you Vagrant Up and Running, run the following commands
```sh 
$ cd pari
$ sudo vagrant up
$ sudo vagrant ssh
```
Now your vagrant machine is up and running ,now move to you virtual evironment by,
```sh 
$ cd /vagrant
$ source pari_env/bin/activate
```
**Note**
To come out from the environment you can run 
```sh
$ deactivate
```
Now you are in the virtual environment where we have all our dependencies up and running, like gunicorn, elasticSearch and nginx.







> The overriding design goal for Markdown's
> formatting syntax is to make it as readable

This text you see here is *actually* written in Markdown! To get a feel for Markdown's syntax, type some text into the left window and watch the results in the right.

### Tech

Tech stacks used in PARI:

* [Django](https://www.djangoproject.com/) - Ease the creation of complex, database-driven websites.
* [Wagtail]() - CMS on top of Django framework
* [Python]() - features a dynamic type system and automatic memory management and supports multiple programming paradigms.
* [Bootstrap]() - great UI boilerplate for modern web apps
* [jQuery]() - duh
* 
### Copyright

Licensed under the 3-clause BSD License. Please refer the LICENSE.txt for details.
