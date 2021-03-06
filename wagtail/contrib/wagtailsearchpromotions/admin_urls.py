from __future__ import absolute_import, unicode_literals

from django.conf.urls import url

from wagtail.contrib.wagtailsearchpromotions import views

app_name = 'wagtailsearchpromotions'
urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^add/$', views.add, name='add'),
    url(r'^(\d+)/$', views.edit, name='edit'),
    url(r'^(\d+)/delete/$', views.delete, name='delete'),
]
