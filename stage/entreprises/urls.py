from django.conf.urls import patterns, url
from entreprises import views

urlpatterns = patterns("",
    url(r'^$', views.index, name='index'),
    url(r'^(?P<page>\d+)/?$', views.index, name='index-page'),
    # url(r'^entreprises/?$'                   , views.liste_entreprises, name="liste-entreprises"     ),
    # url(r'^entreprises/(?P<page>\d+)/?$'     , views.liste_entreprises, name="liste-entreprises-page"),
	#url(r'^entreprises/detail/(?P<id>\d+)/?$', views.detail_entreprise, name="detail-entreprise"     ),
)
