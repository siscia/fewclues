#!/usr/bin/python
# -*- coding: utf-8 -*-
from django.http import Http404, HttpResponse
from django.shortcuts import render_to_response
from django.template import RequestContext
from django.contrib.auth.decorators import login_required

from fewclues.qualcheindizio.models import *
from fewclues.qualcheindizio.form import formRisposta

def hello(request):
    return HttpResponse("Hello word")

def checkRequest(request):
    """Controlla che sia tutto a posto nella request"""
    return True

def checkID(ID):
    """Controlla l'esistenza della domanda ritorna se esiste la domanda"""
    try:
        domanda = Domanda.objects.get(pk = ID)
        return domanda
    except: 
        return False

def checkRisposta(domanda, risposta):
    """Controlla se la risposta e' giusta"""
    print type(risposta)
    if domanda.Soluzione.lower() == risposta.lower():
        return True
    else:
        return False

def risultatoVittoria(testo = None):
    if testo == None:
        testo = "Complimenti hai vinto ;-)"
    return testo

def risultatoPerdita(testo = None):
    if testo == None:
        testo = "Mi spiace, non è la risposta giusta"
    return testo

def salvaRisposta(contenuti):
    ans = Risposte(Risposta = contenuti['risposta'], Giocatore = contenuti['user'], Vincente = contenuti['vittoria'], Indizio = getLastIndizio(checkID(contenuti['ID'])))
    ans.save()

def getIndizi(domanda, quantita = None):
    """Non e' stato implementato uno slicing perche' questo dovrebbe essere
    fatto lato client con uno script javascript, comunque dovrebbe essere 
    qualcosa simile a 
    return domanda.indizio_set.all().order_by('-DataCreazione')[quantita]
    SICURAMENTE DA VERIFICARE IN CASO DI IMPLEMENTAZIONE"""
    
    return domanda.indizio_set.filter(Online = True).order_by('-DataCreazione')

def getSbagliate(indizi):
    """La funzione ritorna un dizionario del tipo
    indizio : risposte abbinate ad indizio
    gestire nel template il dizionario se possibile...
    ...e' possibile ed è stato fatto XP"""

    risposteSbagliate = {indizio : indizio.risposte_set.all().order_by('-DataCreazione') for indizio in indizi}
    return risposteSbagliate

def isOpen(domanda):
    if domanda.DataChiusura:
        return False
    else:
        return True

def closeDomanda(domanda):
    """Chiude la domanda nel caso in cui qualcuno indovini"""
    domanda.DataChiusura = datetime.datetime.now()
    domanda.save()

@login_required(login_url = '/user/login')
def QualcheindizioMain(request, ID):
    """La funzione ha il compito di gestire le richieste che arrivano e di ritornare una risposta"""
    contenuti = dict() #necessario per memorizzare le varie info
    domanda = checkID(ID)
    if domanda:
        if isOpen(domanda):
            if request.method == 'POST':
                form = formRisposta(request.POST)
                if form.is_valid():
                    risposta = form.cleaned_data['risposta']
                    contenuti = {'ID':ID, 'user':request.user, 'risposta':risposta}

                    if checkRisposta(domanda, risposta):
                        contenuti['risultato'] = risultatoVittoria()
                        contenuti['vittoria'] = True
                        closeDomanda(domanda)
                    else:
                        contenuti['risultato'] = risultatoPerdita()
                        contenuti['vittoria'] = False

                    salvaRisposta(contenuti)
            
            contenuti['indizi'] = getIndizi(domanda)
            contenuti['risposte_sbagliate'] = getSbagliate(contenuti['indizi'])
            contenuti['form'] = formRisposta()
        
            return render_to_response('domanda_templates.html', contenuti, context_instance=RequestContext(request))

        else:   #Se la domanda non è gia stata risolta 2 if
            return HttpResponse('La domanda è gia stata risolta')

    else:   #Se la domanda non esiste 1 if
        return HttpResponse('Non esiste al domanda')
