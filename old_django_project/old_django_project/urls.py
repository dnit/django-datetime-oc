from django.conf.urls import include, url
from django.contrib import admin

urlpatterns = (
    # Examples:
    # url(r'^$', 'old_django_project.views.home', name='home'),
    url(r'^/', include('api.urls')),

    # url(r'^admin/', include(admin.site.urls)),
)
