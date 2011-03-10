from django.conf.urls.defaults import *
from mits.views import *
from django.views.generic import list_detail
from mits.models import Task
import operator
import os
from django.views.generic.simple import direct_to_template

handler500 = 'djangotoolbox.errorviews.server_error'
# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()


task_info = {
    'queryset': Task.objects.all()[0:7],
    'template_name' : 'celebrate_view.html',
}


urlpatterns = patterns('',
    # Example:
    # (r'^gentlementor/', include('gentlementor.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # (r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    # (r'^admin/', include(admin.site.urls)),
                       
    ('^_ah/warmup$', 'djangoappengine.views.warmup'),
    ('^$', decide),
    ('^time/$', current_datetime),
    ('^decide/$', decide),
    ('^track/$', track),
    (r'^celebrate/$', list_detail.object_list, task_info),
    (r'^contact/$', direct_to_template, {
        'template': 'contact.html'
    })
   
)
