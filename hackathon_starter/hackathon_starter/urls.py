from django.conf.urls import patterns, include, url
from django.contrib import admin
from hackathon import views
from link.views import *

urlpatterns = patterns('',
    url(r'^$', views.index, name='index'),
    url(r'^hackathon/', include('hackathon.urls')),
    url(r'^link/', include('link.urls')),
    url(r'^admin/', include(admin.site.urls)),
    # url(r'^openid/(.*)', SessionConsumer()),
)
