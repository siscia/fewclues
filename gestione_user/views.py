# Create your views here.
from django.http import HttpResponse, HttpResponseRedirect
from django.template import RequestContext
from django.shortcuts import render_to_response
from django.contrib.auth.models import User
from fewclues.gestione_user.forms import RegistrationForm

def salva_utente(user, password):
    nuovo = User.objects.create_user(username = user, password = password, email = '')

def registrazione(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            info = form.cleaned_data
            user = info['nick']
            password = info['password1']
            salva_utente(user, password)

            return HttpResponseRedirect('/1/')
    else:
        form = RegistrationForm()
    return render_to_response('registration/register.html', {'form':form}, context_instance = RequestContext(request))
    
