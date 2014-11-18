from django.shortcuts import render
from django.shortcuts import render_to_response
from django.forms import ModelForm
from django import forms
from django.template import RequestContext
from django.core.paginator import Paginator
from django.http import HttpResponseRedirect
from django.http import Http404

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