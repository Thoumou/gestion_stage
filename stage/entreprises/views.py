from django.shortcuts import render
from django.http import HttpResponse
from django.core.paginator import Paginator

def index(request):

	context = {}
	return render(request, 'entreprises/index.html', context)