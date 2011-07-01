from django.db import models
from django.contrib.auth.models import User

import datetime

def getLastIndizio(Domanda):
    return Domanda.indizio_set.order_by('-DataCreazione')[0]
        
class Domanda(models.Model):
    Domanda = models.CharField(max_length = 140)
    Soluzione = models.CharField(max_length = 140)
    Autore = models.ForeignKey(User)
    DataCreazione = models.DateTimeField(default = datetime.datetime.now)
    DataChiusura = models.DateTimeField(null = True, blank = True)

    def __unicode__(self):
        return self.Domanda


class Indizio(models.Model):
    Indizio = models.TextField(max_length = 140)
    Autore = models.ForeignKey(User)
    DataCreazione = models.DateTimeField(default = datetime.datetime.now)
    Domanda = models.ForeignKey(Domanda)
    Online = models.BooleanField(default = False)

    def __unicode__(self):
        return self.Indizio
        
class Risposte(models.Model):
    Risposta = models.CharField(max_length = 140)
    Giocatore = models.ForeignKey(User)
    Time = models.DateTimeField(default = datetime.datetime.now)
    #Domanda = models.ForeignKey(Domanda)
    Indizio = models.ForeignKey(Indizio)
    DataCreazione = models.DateTimeField(default = datetime.datetime.now)
    Vincente = models.BooleanField(default = False)
    
    def __unicode__(self):
        return self.Risposta
        

        
    

