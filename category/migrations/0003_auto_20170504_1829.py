# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models

def update_categories(apps, schema_editor):
    Category = apps.get_model('category.category')
    category_update_dict = {
        "things-we-do": { "name": "Things We Do", "description": "The world of rural labour" },
        "things-we-make": { "name": "Things We Make", "description": "Artisans, artists and craftspersons" },
        "farming-and-its-crisis": { "name": "Farming and its Crisis", "description": "The troubled world of agriculture" },
        "Little takes": { "name": "Little Takes", "description": "Small, impactful video clips" },
        "the-rural-in-the-urban": { "name": "The Rural in the Urban", "description": "Migrant workers across India" },
        "women": { "name": "Women", "description": "More than half the sky" },
        "adivasis": { "name": "Adivasis", "description": "The first dwellers" },
        "dalits": { "name": "Dalits", "description": "Struggles of the oppressed" },
        "we-are": { "name": "We Are", "description": "Communities and cultures" },
        "resource-conflicts": { "name": "Resource Conflicts", "description": "Jal, jungle, zameen" },
        "foot-soldiers-of-freedom": { "name": "Foot-Soldiers of Freedom", "description": "The last living freedom fighters" },
        "small-world": { "name": "Small World", "description": "A focus on children" },
        "musafir": { "name": "Musafir", "description": "Travellers’ tales, everyday lives" },
        "getting-there": { "name": "Getting There", "description": "Zany rural transportation" },
        "the-wild": { "name": "The Wild", "description": "The world of nature" },
        "sports-games": { "name": "Rural Sports", "description": "Games people play" },
        "health": { "name": "Healthcare", "description": "The state of rural health" },
        "folklore": { "name": "Mosaic", "description": "Culture and folklore" },
        "environment": { "name": "Environment", "description": "People, livelihoods, habitats" },
        "tongues": { "name": "Tongues", "description": "The universe of our languages" },
        "visible-work-invisible-women": { "name": "Visible Work, Invisible Women", "description": "Women and work: a photo exhibition" },
        "one-offs": { "name": "One-Offs", "description": "Videos, photos, articles" },
        "headgear": { "name": "Things We Wear", "description": "Clothing, headgear, jewellery..." },
        "pari-for-schools": { "name": "PARI for Schools", "description": "Work done for PARI by students" },
        "videozone": { "name": "VideoZone", "description": "Stories told in moving pictures" },
        "audiozone": { "name": "AudioZone", "description": "You could listen all day" },
        "photozone": { "name": "PhotoZone", "description": "Collections of photographs" }
    }

    for slug, value in category_update_dict.iteritems():
        name = value["name"]
        description = value["description"]
        try:
            category = Category.objects.get(slug=slug)
        except Category.DoesNotExist:
            category = None

        if(category):
            category.name = name
            category.description = description
            category.save()

class Migration(migrations.Migration):

    dependencies = [
        ('category', '0002_category_image'),
    ]

    operations = [
        migrations.RunPython(update_categories),
    ]
