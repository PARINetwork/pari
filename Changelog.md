# Changelog
All the work that goes into the project will be documented here.

## 2022-11-08

### Modified
* Removed Hcaptcha as it was not working post deployment
* Added Google reCaptcha-v2
* Used (this)[https://simpleisbetterthancomplex.com/tutorial/2017/02/21/how-to-add-recaptcha-to-django-site.html] as a reference

## 2022-11-07

### Added
* Added Hcaptcha to contact us page. Now message which pass all the validations including captcha will be set to contact mail
* Used (this)[https://djangowaves.com/tutorial/django-hcaptcha-contact-form/] as a reference

## 2022-08-14

## Added
### Album
* Boolean field to identify Freedom Fighters Gallery album
* Short description field used on Freedom Fighters Gallery Listing Page
* View for Freedom Fighters Gallery albums listing using the new boolean field
* Template for Freedom Fighters Gallery albums listing page

## Modified
### Album
* Album Detail Page to show different content for Freedom Fighters Gallery album
  * Used justifiedGallery library for styling images below the slider
  * First image from album is used as top image (shown above slider)
  * Clicking on image will select that image on the slider
### Core
* Modified grid title template to include additional content on Freedom Fighters Gallery albums listing page
