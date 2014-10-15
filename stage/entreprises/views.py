from django.shortcuts import render

def index(request):
	return HttpResponse("Salut tout le monde")
