![N|Solid](https://ruralindiaonline.org/static/img/logo.png)    **People's Archive Of Rural India**

**[PARI](https://ruralindiaonline.org/)** is a digital journalism platform in India, founded by veteran journalist and former rural affairs editor of 'The Hindu', **Palagummi Sainath**. **PARI** is a volunteer-run rural journalism platform.

## Dev Setup
***
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
    Replace the **--private-key** in the ansible-playbook command given below with the value of **IdentityFile** , you will get your         IdentityFile by runnig this commnd.

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

### Open pari admin and local web console
Now you can open pari admin user web console ,

    http://0.0.0.0/admin/
**Username and Password**

    username: pari
    pass: !abcd1234

and user face of the pari web page

    http://0.0.0.0

### Accessing database
From your vagrant machine run,
```sh
$ sudo su postgress
$ psql
```
**Basic command for psql**
> **\c**  -   to connect db
> **\dt**   -   list tables
> **\x**    -   for turning on the Expanded display


### Tech stack:

* [Django](https://www.djangoproject.com/) - Ease the creation of complex, database-driven websites.
* [Wagtail](https://wagtail.io/) - CMS on top of Django framework
* [Python](https://www.python.org/) - Features a dynamic type system and automatic memory management and supports multiple programming paradigms.
* [Bootstrap](http://getbootstrap.com/) - Great UI boilerplate for modern web apps
* [jQuery](https://jquery.com/)

## How to contribute ?
***

##### Sign up for stories
Pickup stories from  [Pari Projects](https://github.com/PARINetwork/pari/projects/1) and sign up. Choose the stories that are **ready for Dev**. Drag and drop the story you picked in to **In Dev** column. Make sure that, task you done on the story staisfies the acceptance criteria(In scope) of the story. If you want to sign up for specific stories feel free to ask through the **Collaboration channels**.

##### Completion of stories
After you completes stories you can drag and drop the story to **Ready For QA** column.

## Collaboration channels
----
To keep in tech with technical team and the pari team,you can use the [**google group**](). If you thought of contributing to **PARI** this is one of the media that you can use. In the case of doubts and queries you can use the group.
And you can participate in the IPM's and showcase for the PARI project.

## Roadmap of features
---
### Goals
### Goals
- Increase discoverability of Pari's content
- Increase interactions on social media
- Increase donations on the site
- Increasing content contributed by existing volunteers
- Sign up of new volunteers who contribute content  

### Roadmap

| Realease 1 features|
|:--------:|
|`CI/CD setup`|
|`Make Development OSS Friendly`|
|`CMS - Data structure`|
|`Information architecture of website` |
|`Website UI revamp`|
|`Setting the default style`|
|`Optimising SEO for regional language translations for articles `|
|`SEO for pari website`|
|**Realease 2 features**|
|`Articles`|
|`Faces`|
|`Resources`|
|`Talking albums`|
|`Videos`|
|`Audios`|
|`Albums (pics, talking pics)`|
|`Maps`|
|`One-offs`|
|**Realease 3 features**|
|`Language selection `|
|`Translations`|
|`Improve elastic search`|
|`Improve search for specifc data on website`|
|`Social Sharing`|
|`Contributions`|
|`PARI Analytics`|
|`Editing articles for publishing `|
|**Realease 4 features**|
|`Editing articles for publishing `|
|`CMS - Bulk upload`|
|`CMS - Data language`|
|`CMS - Editing `|
|`Showcase grindmill content`|
|`Manage Grindmill Content`|







### Copyright
---
Licensed under the 3-clause BSD License. Please refer the LICENSE.txt for details.
