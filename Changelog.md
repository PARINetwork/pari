# Changelog
All the work that goes into the project will be documented here.


## [Unreleased]

### Added
* Added Hcaptcha to contact us page. Now message which pass all the validations including captcha will be set to contact mail
* Used this [link](https://djangowaves.com/tutorial/django-hcaptcha-contact-form/) as a reference

## 14-08-2022

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
