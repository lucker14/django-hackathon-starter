from django.conf.urls import patterns, url, include

from link import views

urlpatterns = patterns('',
    url(r'^create-new-link/$', views.create_new_link, name='create_new_link'),
    url(r'^create-link/$', views.create_link, name='create_link'),
    url(r'^delete-link/$', views.delete_link, name='delete_link'),
    url(r'^dashboard/$', views.links_overview, name='links_overview'),
)
