from django.shortcuts import render
from django.shortcuts import render_to_response
from django.forms import ModelForm
from django import forms
from django.template import RequestContext
from django.core.paginator import Paginator
from django.http import HttpResponseRedirect
from django.http import Http404
from pygeocoder import Geocoder
import os

from entreprises.models import Entreprise


def index(request, page=1):
	liste = Entreprise.objects.order_by("nom")
	p = Paginator(liste, 20)
	n = int(page)
	page = p.page(n)
	return render(request, "entreprises/index.html", {
		"entreprises": page.object_list,
		"page" : page,
		"paginator" : p,
	})

def fiche(request, entreprise_id=None):
	if (id==None):
		return HttpResponseRedirect('/entreprises')

	else:
		try:
			entreprise = Entreprise.objects.get(pk=entreprise_id)

		except Entreprise.DoesNotExist:
			raise Http404

		return render(request, "entreprises/fiche.html", {'entreprise': entreprise})

def geoloc(request, entreprise_id=None):
	geocoder=Geocoder()
	try:
		proxy=os.environ['http_proxy']
		geocoder.set_proxy(proxy)
	except KeyError:
		pass
	entreprise = Entreprise.objects.get(pk=entreprise_id)
	adresseComplete = entreprise.adresse_propre+","+entreprise.ville_propre
	#testAdresse = "20 place de la Republique, Montargis"

	try:
		if geocoder.geocode(adresseComplete).valid_address :
			resultat = geocoder.geocode(adresseComplete)
			entreprise.latitude=resultat[0].coordinates[0]
			entreprise.longitude=resultat[0].coordinates[1]
			message = "adresse : "+str(resultat[0].coordinates)
			entreprise.save()
		else:
			message = "adresse non valide"
	except Exception as inst:
		message=inst.args
		
	return render(request, "entreprises/geolocalisation.html", {
		'entreprise': entreprise,
		'afficherAC': adresseComplete,
		'message':message
	})
