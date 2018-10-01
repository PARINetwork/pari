![N|Solid](https://ruralindiaonline.org/static/img/logo.png)

# People's Archive of Rural India

[![Build Status](https://travis-ci.org/PARINetwork/pari.svg?branch=master)](https://travis-ci.org/PARINetwork/pari)

---

This repository contains the source code of the main website deployed for public consumption at ruralindiaonline.org

## Developer Guide

### Pre-requisites

* [Vagrant](https://www.vagrantup.com/downloads.html)
* [Virtualbox](https://www.virtualbox.org/wiki/Downloads)
* [Ansible(v2.2.1)](http://docs.ansible.com/ansible/intro_installation.html)

### Setup

Clone both [pari](https://github.com/PARINetwork/pari.git) and [pari-ansible](https://github.com/PARINetwork/pari-ansible.git) repositories (ideally in the same parent directory).

```sh
$ git clone https://github.com/PARINetwork/pari.git
$ git clone https://github.com/PARINetwork/pari-ansible.git
$ cd pari
$ vagrant up   # You'll be prompted for SUDO password of your host machine for the first time.
```

### Ansible 2.2.1
Make sure that you have installed Ansible 2.2.1.
You can install Ansible 2.2.1 with the following command

```sh
$ pip install ansible==2.2.1
```

If, however, you have already installed some other version of Ansible you will need to uninstall it
```sh
$ sudo -H pip uninstall ansible
$ #OR
$ brew uninstall ansible # Only if you used homebrew to install ansible
$ pip install ansible==2.2.1
$ git checkout master
$ git pull 
$ rm -rf pari_env (if present)
$ vagrant destroy ( Delete the old version of the box )
$ rm -rf .vagrant (Delete old vagrant cache)
$ vagrant up
```

### Development-specific commands
The above set-up will get the vagrant box up. That is, it will start the virtual machine that pretends to be a remote server at "development.ruralindiaonline.org".

You will need to login via ssh into this pretend-remote virtual machine and start your django webapp server. Please follow the following steps for this.

```sh
$ vagrant ssh                                   # Login to vagrant box
$ cd /vagrant && source pari_env/bin/activate   # Change to project directory and activate project virtualenv
$ python manage.py runserver                    # Local instance available at development.ruralindiaonline.org
```

Admin console can be accessed at [http://development.ruralindiaonline.org/admin/](http://development.ruralindiaonline.org/admin/) (username: admin, password: admin)

```sh
$ python manage.py shell                        # Access django shell
$ python manage.py dbshell                      # Access postgres DB. Password: pari
$ python manage.py test --keepdb                # Run all the tests
$ deactivate                                    # Exit from project virtualenv
```

## Tech stack:

[Python](https://www.python.org/), [Django](https://www.djangoproject.com/), [Wagtail](https://wagtail.io/), [PostgreSQL](https://www.postgresql.org/), [Nginx](https://www.nginx.com/), [Gunicorn](http://gunicorn.org/), [Supervisor](http://supervisord.org/), [Elasticsearch](https://www.elastic.co/), [Bootstrap](http://getbootstrap.com/), [jQuery](https://jquery.com/)

## How to Contribute?
#### Sign up for stories
Choose any card in **Ready for Dev** lane from [Github Projects](https://github.com/PARINetwork/pari/projects/1) and assign it to yourself. Move it to **In Dev** lane. Add Dev tasks to that story briefly so that others who want to understand the work being done can get a overview. 

Use the **Collaboration Channels** to get any questions clarified.

In case of UI stories, follow **UX Mockups** instructions below.

#### Completion of stories
Once done, check if all the **In Scope** items are covered and make a commit with the issue number. Also move the issue to **Ready For QA** column.


##UX Mockups
Download PARI mockup from following [google drive link](https://drive.google.com/drive/folders/0B4TMsel2baWuY1otS0hUM3NxQ2c?usp=sharing). Drive contains visual designs in three formats
Images, PDF and Sketch files. Use [Sketch](https://www.sketchapp.com/) application(Only for mac) to open .sketch files.
 ```sh
https://drive.google.com/drive/folders/0B4TMsel2baWuY1otS0hUM3NxQ2c?usp=sharing
```

## Collaboration channels
To keep in tech with technical team and the pari team,you can use the [**google group**](https://groups.google.com/d/forum/tech-pari
). If you thought of contributing to **PARI** this is one of the media that you can use. In the case of doubts and queries you can use the group.
And you can participate in the IPM's and showcase for the PARI project.

## Roadmap of features

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

Licensed under the 3-clause BSD License. Please refer to LICENSE.txt for details.
