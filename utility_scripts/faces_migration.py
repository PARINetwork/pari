import csv
from datetime import datetime

import django
from django.utils.text import slugify

from author.models import Author
from location.models import Location
from location.models import SubDistrictType
from face.models import Face
from core.models import AffixImage

django.setup()

with open('updated_faces_data.csv') as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:

        # Face data
        face_image_id = row['id']
        name, occupation, occupation_of_parent = row['name'], row['occupation'], row['occupation of parent']
        age, is_a_child = row['age'], row['is_a_child']
        gender, quote = row['gender'], row['quote']
        adivasi = row['adivasi']
        additional_info = row['additional info']

        # Face image data
        camera, date, photographer = row['camera'], row['date'], row['photographer']

        # Location data
        location_name, location_district, location_state = row['village'], row['district'], row['state']
        region, panchayat = row['region'], row['panchayat']
        subdistrict_name = row['mandal'] or row['mandapam'] or row['taluka'] or row['tehsil'] or row['block']
        subdistrict_type = (row['mandal'] and 'mandal') or (row['mandapam'] and 'mandapam') \
                           or (row['taluka'] and 'taluka') or (row['tehsil'] and 'tehsil') or (row['block'] and 'block')

        subdistrict_type = subdistrict_name and subdistrict_type and SubDistrictType.objects.get(name=subdistrict_type)

        face = Face.objects.get(image_id=face_image_id)
        face_image = AffixImage.objects.get(pk=face_image_id)
        face_location = Location.objects.get(pk=face.location_id)
        location_name = location_name or face_location.name

        if face.has_unpublished_changes and face.first_published_at is not None:
            face.revisions.all().delete()
        if face.has_unpublished_changes and face.first_published_at is None:
            face.revisions.all().delete()

        print
        print "location_name: " + location_name
        print "subdistrict_name: " + subdistrict_name
        print "subdistrict_type: " + (subdistrict_type and subdistrict_type.name)

        new_location, created = Location.objects.get_or_create(
            name=location_name,
            district=location_district,
            state=location_state,
            point=face.location.point,
            sub_district_name=subdistrict_name or None,
            sub_district_type_id=(subdistrict_type and subdistrict_type.id) or None,
            region=region or None,
            panchayat=panchayat or None
        )

        print "Face id: %s" % face.id
        print "Face image id: %s" % face.image_id
        print "New location %s, %s" % (new_location.name, created)
        print "Current location ID: %s" % face.location_id
        print "Newlocation ID: %s" % new_location.id

        face.location_id = new_location.id

        if name:
            face.name = name
        if occupation:
            face.occupation = occupation
        if occupation_of_parent:
            face.occupation_of_parent = occupation_of_parent
        if age:
            face.age = age
        if is_a_child:
            face.child = True if is_a_child.lower() == 'yes' else False
        if gender:
            if gender.lower() == 'female':
                face.gender = 'F'
            elif gender.lower() == 'male':
                face.gender = 'M'
            elif gender.lower() == 'transgender':
                face.gender = 'T'
            else:
                raise Exception('Non matching gender for face id: %s' % face.id)
        if quote:
            face.quote = quote
        if adivasi:
            face.adivasi = adivasi

        face.additional_info = additional_info

        face.save()

        new_location.slug = slugify(name)[:50]
        new_location.save()

        if camera:
            face_image.camera = camera
        if date:
            face_image.date = datetime.strptime(date, '%B %d, %Y')
        face_image.save()

        if photographer:
            new_photographer, created = Author.objects.get_or_create(name=photographer)
            new_photographer.slug = slugify(photographer)
            new_photographer.save()
            face_image.photographers.add(new_photographer)

        updated_face = Face.objects.get(image_id=face_image_id)
        print "updated ID: %s" % updated_face.location_id

        print "Current Face image locations: %s" % ",".join([each.name for each in face_image.locations.all()])
        face_image.locations.clear()

        face_image_locations_after_clear = AffixImage.objects.get(pk=face_image_id).locations
        print "After clear face image locations: %s" % ",".join(
            [each.name for each in face_image_locations_after_clear.all()])

        face_image_locations_after_clear.add(new_location)

        face_image_locations_after_update = AffixImage.objects.get(pk=face_image_id).locations
        print "After update face image locations: %s" % ",".join(
            [each.name for each in face_image_locations_after_update.all()])
