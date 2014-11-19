from django.conf.urls import patterns, url
from entreprises import views

urlpatterns = patterns("",
    url(r'^$', views.index, name='index'),
    url(r'^(?P<page>\d+)/?$', views.index, name='index-page'),
	url(r'^fiche/(?P<entreprise_id>\d+)/?$', views.fiche, name="fiche"),
	url(r'^fiche/(?P<entreprise_id>\d+)/?/geolocalisation$', views.geoloc, name="geolocal"),
)
