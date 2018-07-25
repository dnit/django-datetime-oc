# django-datetime-oc
Django 1.7.7 v/s Django 1.11.14


### POC for showing Django==1.11.14 not converting datetimte to timezone aware, while Django==1.7.7 used to (not sure from which version it started breaking)

# STEPS TO REPRODUCE

  
    git clone https://github.com/dnit/django-datetime-oc.git
    git checkout develop
    virtualenv env1
    virtualenv env2
    cd old_django_project
  
## CREATE mysql database name test_db which can be accessed by root user without password 
    

## Install environment1 (i.e Django 1.7.7)
    source ../env1/bin/activate
    pip install -r requirements1.txt
    python manage.py migrate
    python manage.py shell
    >>> Dummy.objects.create()
    >>> Dummy.objects.create()
    >>> from api.models import Dummy
    >>> for obj in Dummy.objects.with_raw():
    ...     obj.is_valid
    
## Install envrironment2 ( i.e Django 1.11.14)
    source ../env2/bin/activate
    pip install -r requirements2.txt
    python manage.py shell
    >>> from api.models import Dummy
    >>> for obj in Dummy.objects.with_raw():
    ...     obj.is_valid  # Breaks due to TypeError: can't compare offset-naive and offset-aware datetimes

