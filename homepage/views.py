from __future__ import unicode_literals
from django.shortcuts import render, redirect, get_object_or_404
from django.http import Http404, HttpResponse, HttpResponseRedirect
from homepage.models import 
from django.contrib.auth import authenticate

def index(request):
	context_dict= {}

	# home_list = Home.objects.all

	# context_dict['card'] = card_list
		
	return render(request, "index.html", context_dict)