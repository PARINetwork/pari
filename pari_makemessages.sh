#!/bin/bash

python manage.py makemessages -l $1 --ignore={'*wagtail*','*apps.py','*core/models.py','*feeds.py','*validators.py','*models/base.py','*__init__.py','*files.py','*related.py','*fields.py','*forms/forms.py','*formsets.py','*models.py','*utils.py','*widgets.py','*defaultfilters.py','*ipv6.py','*text.py','*timesince.py','*csrf.py','*debug.py','*generic/dates.py','*list.py','*static.py','*compat.py'}
