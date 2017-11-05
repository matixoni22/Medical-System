from django.shortcuts import render
from django.http import *
from polls.models import *
from django.template import loader
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.template import RequestContext


def login(request):
    logout(request)
    username = password = ''
    if request.POST:
        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(username=username, password=password)
        if user is not None:
            if user.IsActive:
                login(request, user)
                return HttpResponseRedirect('/main/')
    return render(request, 'Medical System/login.html')


@login_required(login_url='/login/')
def index(request):
    return render(request, 'Medical System/index.html')
