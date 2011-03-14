from django.conf.urls.defaults import *
from mits.views import *
from django.views.generic import list_detail
from mits.models import Task
import operator
import os
from django.views.generic.simple import direct_to_template
from django.http import HttpRequest

handler500 = 'djangotoolbox.errorviews.server_error'
# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()




urlpatterns = patterns('',
    # Example:
    # (r'^gentlementor/', include('gentlementor.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # (r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    # (r'^admin/', include(admin.site.urls)),
                       
    ('^_ah/warmup$', 'djangoappengine.views.warmup'),
    ('^$', decide),
     (r'^login/$', login),
     (r'^logout/$',logout),
     (r'^register/$',register),
    ('^time/$', current_datetime),
    ('^decide/$', decide),
    ('^track/$', track),
    ('^about/$', direct_to_template,{'template': 'about.html'}),
    (r'^celebrate/$', celebrate),
    
    (r'^contact/$', hidden_contact, {
        'template': 'contact.html'
    })
   
)
