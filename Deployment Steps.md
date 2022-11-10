# Deployment Steps
Document steps for all the deployments

## Added captcha
Last updated: 07-11-2022

* Deployment on production
  * Add Recaptcha secret and site keys to pari/settings/local.py
    ```
    RECAPTCHA_PUBLIC_KEY = '<key>'
    RECAPTCHA_PRIVATE_KEY = '<key>'
    ```
    
  * Merge the PR https://github.com/bhuvankrishna/pari/pull/3 
  * On the server, ensure that you are on `release-candidate` branch and run
   
    ```sh
    git pull bhuvan-pari release-candidate
    ```
  * For adding Recaptcha to file upload follow these steps
  * Get permission to access the scripts which is in google drive with the name "File Upload"
  * When you open the file "File Upload" from inside google drive you are taken to script.google.com site. Here you can see 2 files form.html and server.gs.
  * Add public/site key to form.html and any other modifications
  * Add private/secret key to server.gs and do the needed changes
  * Generate a new link from "New Deployment"
  * Update this link in core/templates/core/contribute.html and core/templates/core/contact-us.html files


## Freedom Fighters Gallery
Last updated: 14-08-2022

* For test deployment, on the server, run
    ```sh
    git fetch bhuvan-pari freedom-fighters && git checkout freedom-fighters
    ```

* During actual deployment, 
  * Merge the PR https://github.com/bhuvankrishna/pari/pull/1 and 
  * On the server, ensure that you are on `release-candidate` branch and run

    ```sh
    git pull bhuvan-pari release-candidate && git checkout release-candidate
    ```

* As ubuntu user, go to the project root
    ```sh
    cd ~/pari
    ```

* Activate the python environment
    ```sh
    source ../pari_env/bin/activate
    ```

* Install dependencies
    ```sh
    pip3 install django-clear-cache
    pip install wagtail-clear-cache
    ```

* Migrate all the changes
    ```sh
    python3 manage.py migrate
    ```

* Collect all static files to the root static folder (Choose `Yes` on prompt)
    ```sh
    python3 manage.py collectstatic
    ```

* Restart gnuicorn service as root
    ```sh
    supervisorctl restart pari:gunicorn_pari
    ```

* Restart elasticsearch service as root
    ```sh
    service elasticsearch restart
    ```
