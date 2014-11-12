from django.conf.urls import patterns, url
from entreprises import views

urlpatterns = patterns("",
    url(r'^$', views.index, name='index'),
    #url(r'^form/$', views.Form, name="form"),
    url(r'^list/$', views.ent_listing, name="list"),
    url(r'^entreprises/?$'                   , views.liste_entreprises, name="liste-entreprises"     ),
    url(r'^entreprises/(?P<page>\d+)/?$'     , views.liste_entreprises, name="liste-entreprises-page"),
    #url(r'^entreprises/detail/(?P<id>\d+)/?$', views.detail_entreprise, name="detail-entreprise"     ),
)
