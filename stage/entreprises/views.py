from django.shortcuts import render
from django.shortcuts import render_to_response
from django.forms import ModelForm
from django import forms
from django.template import RequestContext
from django.core.paginator import Paginator
from django.http import HttpResponseRedirect
from django.http import Http404
from django.core.context_processors import csrf
from django.http import HttpResponse

from entreprises.models import Entreprise
from entreprises.models import AjoutForm
from entreprises.models import ModifForm


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


def delete(request, entreprise_id=None):
	if (id==None):
		return HttpResponseRedirect('/entreprises')

	else:
		try:
			entreprise = Entreprise.objects.get(pk=entreprise_id)
			entreprise.delete()

		except Entreprise.DoesNotExist:
			raise Http404

		return HttpResponseRedirect('/entreprises')


def ajouter(request):
	form = AjoutForm()
	con ={'form': form}
	con.update(csrf(request))
	if len(request.POST) > 0:
		form =AjoutForm(request.POST)
		con = {'form': form}
		if form.is_valid():
			tache=form.save(commit=False)
			con.update(csrf(request))
			tache.save()
			return HttpResponseRedirect("/entreprises") #Nous renvoie la si le formulaire est juste
		else:
			return render_to_response('entreprises/ajout.html',
			con,context_instance=RequestContext(request))
	else:
		return render_to_response('entreprises/ajout.html',
		con,context_instance=RequestContext(request));	

		
def modifier(request , entreprise_id=None):
	entreprise = Entreprise.objects.get(pk=entreprise_id) 
	form = ModifForm(instance = entreprise)
	con ={'form': form}
	con.update(csrf(request))
	if len(request.POST) > 0:
		form =ModifForm( request.POST , instance = entreprise )
		con = {'form': form}
		if form.is_valid():
			tache=form.save(commit=False)
			con.update(csrf(request))
			tache.save()
			return HttpResponseRedirect("/entreprises") #Nous renvoie la si le formulaire est juste
		else:
			return render_to_response('entreprises/modifier.html',
			con,context_instance=RequestContext(request))
	else:
		return render_to_response('entreprises/modifier.html',
		con,context_instance=RequestContext(request));			
