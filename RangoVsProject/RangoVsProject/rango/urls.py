"""
Definition of urls for RangoVsProject.
"""

from django.conf.urls import patterns, include, url
from rango import views

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'RangoVsProject.views.home', name='home'),
    # url(r'^RangoVsProject/', include('RangoVsProject.RangoVsProject.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    # url(r'^admin/', include(admin.site.urls)),
    url(r'^$', views.index, name='index_function'),
    url(r'^about/',views.getAboutPage,name='getting_about_page'),
    url(r'^category/(?P<category_name_slug>[\w\-]+)/$', views.category, name='category_thingy'),
    url(r'^add_category/$',views.add_category, name = 'add_category'),
    url(r'^category/(?P<category_name_slug>[\w\-]+)/add_page/', views.add_page, name='adding_page')
)
