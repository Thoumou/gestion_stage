from django.conf.urls import patterns, url
from entreprises import views

urlpatterns = patterns("",
    url(r'^$', views.index, name='index'),
    url(r'^(?P<page>\d+)/?$', views.index, name='index-page'),
	#url(r'^entreprises/detail/(?P<id>\d+)/?$', views.detail_entreprise, name="detail-entreprise"),
)
