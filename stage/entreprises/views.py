from django.shortcuts import render
from django.http import HttpResponse
from django.forms import ModelForm
from django import forms
from django.template import RequestContext
from django.shortcuts import render
from django.shortcuts import render_to_response
from django.core.paginator import Paginator

from entreprises.models import Entreprise # import de la class task


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