from django.conf.urls import patterns, url
from entreprises import views

urlpatterns = patterns("",
    url(r'^$', views.index, name='index'),
    url(r'^(?P<page>\d+)/?$', views.index, name='index-page'),
    url(r'^ajout/$', views.ajouter, name="ajout"),
    url(r'^modif/(?P<entreprise_id>\d+)/?$', views.modifier, name="modif"),
)
