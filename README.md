![N|Solid](https://ruralindiaonline.org/static/img/logo.png)    **People's Archive Of Rural India**

[![Build Status](https://travis-ci.org/PARINetwork/pari.svg?branch=master)](https://travis-ci.org/PARINetwork/pari)

**[PARI](https://ruralindiaonline.org/)** is a digital journalism platform in India, founded by veteran journalist and former rural affairs editor of 'The Hindu', **Palagummi Sainath**. **PARI** is a volunteer-run rural journalism platform.

## Development setup

To start with local development setup, clone both pari.git and pari-ansible.git repositories in a directory.
```sh
$ git clone https://github.com/PARINetwork/pari.git
$ git clone https://github.com/PARINetwork/pari-ansible.git
```

Make sure you have [Vagrant](https://www.vagrantup.com/downloads.html), [Virtualbox](https://www.virtualbox.org/wiki/Downloads) and [Ansible(v2.2.1)](http://docs.ansible.com/ansible/intro_installation.html) installed in your machine.
Also make sure you have internet connectivity. Then, you can get the vagrant box up and provisioned by:

```sh
$ cd pari
$ vagrant up   # This would take a while to complete. You'll be prompted for SUDO password of your host machine for the first time.
```

Once after the initial provisioning is completed, local development instance of PARI can be accessed in the browser. 

    # To access home page
    
    http://development.ruralindiaonline.org/
             
    # To access admin console
    http://development.ruralindiaonline.org/admin/
    # Username: admin
    # Password: admin


Few basic commands to help development,

```sh
$ vagrant ssh                                   # Login to vagrant box
$ cd /vagrant && source pari_env/bin/activate   # Change to project directory and activate project virtualenv   
$ python manage.py shell                        # Access django shell
$ python manage.py dbshell                      # Access postgres DB. Password: pari
$ python manage.py test --keepdb                # Run all the tests
$ deactivate                                    # Exit from project virtualenv
```
## Tech stack:

* [Python](https://www.python.org/) - Features a dynamic type system and automatic memory management and supports multiple programming paradigms.
* [Django](https://www.djangoproject.com/) - Ease the creation of complex, database-driven websites.
* [Wagtail](https://wagtail.io/) - CMS on top of Django framework
* [PostgreSQL](https://www.postgresql.org/) - Database system
* [Nginx](https://www.nginx.com/) - High performance web server and a reverse proxy
* [Gunicorn](http://gunicorn.org/) - WSGI HTTP Server
* [Supervisor](http://supervisord.org/) - Process Control System
* [Elasticsearch](https://www.elastic.co/) - Search engine
* [Bootstrap](http://getbootstrap.com/) - Great UI boilerplate for modern web apps
* [jQuery](https://jquery.com/)

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
To keep in tech with technical team and the pari team,you can use the [**google group**](). If you thought of contributing to **PARI** this is one of the media that you can use. In the case of doubts and queries you can use the group.
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

Licensed under the 3-clause BSD License. Please refer the LICENSE.txt for details.
