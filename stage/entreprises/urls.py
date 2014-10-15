from django.conf.urls import patterns, url
from entreprises import views

urlpatterns = patterns('',
    url(r'^$', views.index, name='index'),
)
