# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.template import RequestContext

from django.shortcuts import render
from primeFormDoer import primeFormLaunch
from invertDoer import theInverter
from transposeDoer import theTransposer
from retrogradeDoer import retrogradeLaunch
from intervalsDoer import intervalsLaunch

# Create your views here.

def homepage(request):
	name = 'Chaz'
	return render(request, 'primeForm/homepage.html', {'name': name,})

def primeformfinder(request):
	if request.method == 'POST':
		notes = request.POST['notestring']
		adjustedNotes = primeFormLaunch(notes)
		return render(request, 'primeForm/primeformfinal.html', {'inputNotes': notes, 'finalNotes': adjustedNotes})
	return render(request, 'primeForm/primeformfinder.html', {})

def transpose(request):
	if request.method == 'POST':
		notes = request.POST['notestring']
		theStep = request.POST['stepStep']
		adjustedNotes = theTransposer(notes, theStep)
		# assert False 
		return render(request, 'primeForm/transposefinal.html', {'inputNotes': notes, 'inputStep': theStep, 'finalNotes': adjustedNotes,})
	return render(request, 'primeForm/transpose.html', {})

def invert(request):
	if request.method == 'POST':
		notes = request.POST['notestring']
		theSum = request.POST['sumSum']
		adjustedNotes = theInverter(notes, theSum)
		return render(request, 'primeForm/invertfinal.html', {'inputNotes': notes, 'inputSum': theSum, 'finalNotes': adjustedNotes})
	return render(request, 'primeForm/invert.html', {})

def retrograde(request):
	if request.method == 'POST':
		notes = request.POST['notestring']
		adjustedNotes = retrogradeLaunch(notes)
		return render(request, 'primeForm/retrogradefinal.html', {'inputNotes': notes, 'finalNotes': adjustedNotes})
	return render(request, 'primeForm/retrograde.html', {})

def intervalsfinder(request):
	if request.method == 'POST':
		notes = request.POST['notestring']
		intveralsInstances = intervalsLaunch(notes)
		return render(request, 'primeForm/intervalsfinal.html', {'inputNotes': notes, 'intervals': intveralsInstances})
	return render(request, 'primeForm/intervalsfinder.html', {})




