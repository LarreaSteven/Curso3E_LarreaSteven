from django.shortcuts import render
from .models import LarreaMuñozGit

def gitgit(request) :
    return render(request,'Git.html')
#----------herencia-------------#

def hijo(request) :
    select = LarreaMuñozGit.objects.all()
    return render(request,'herencia/hijo.html',{'enviaSteven':select})



