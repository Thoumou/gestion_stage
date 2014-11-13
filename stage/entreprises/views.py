from django.shortcuts import render
from django.http import HttpResponse
from django.forms import ModelForm
from django import forms
from django.template import RequestContext
from django.shortcuts import render
from django.shortcuts import render_to_response
from django.core.paginator import Paginator

from entreprises.models import Entreprise # import de la class task

def index(request):

	context = {}
	return render(request, 'entreprises/index.html', context)
	
class Form(ModelForm):
	def __init__(self, *args, **kwargs):
		super(Form, self).__init__(*args, **kwargs)
		self.fields['nom'].label = "Nom de l'entreprise : "
	class Meta:
		model = Entreprise
		fields = ('nom',)
		
def ent_listing(request):
	objets=Entreprise.objects.all().order_by('nom')
	return render_to_response('entreprises/listEnt.html',{'objets':objets})	
	

def liste_entreprises(request, page=1):
    liste = Entreprise.objects.order_by("nom")
    p = Paginator(liste, 20)
    n = int(page)
    page = p.page(n)
    return render(request, "entreprises/entreprises.html", {
        "entreprises": page.object_list,
        "page" : page,
        "paginator" : p,
    })
    
#def detail_entreprise(request):
	 
	 
		
