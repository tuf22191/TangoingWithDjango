﻿from django.conf.urls import patterns, include, url
from django.contrib import admin


urlpatterns = patterns('',
    # Examples:
    #url(r'^$', 'RangoProject.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^$', include('rango.urls')), # ADD THIS NEW TUPLE!
    url(r'^admin/', include(admin.site.urls)),
    url(r'^rango/', include('rango.urls')), # ADD THIS NEW TUPLE!
)
