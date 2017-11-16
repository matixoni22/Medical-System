from django.shortcuts import render
from django.http import *
from django.template import loader
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.template import RequestContext
from datetime import datetime
from .models import *
from .services import *


def Log(request):
    logout(request)
    username = password = ''
    if request.POST:
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        if user is not None:
            if user.is_active:
                login(request, user, backend=None)
                return HttpResponseRedirect('/main/')
    return render(request, 'Medical/login.html')


@login_required(login_url='/login/')
def Index(request):
    return render(request, 'Medical/index.html')


@login_required(login_url='/login/')
def OnRegistration(request):
    if request.POST:
        try:
            ValidateAndAddPatient(request.POST['firstname'], request.POST['lastname'], request.POST['pid'],
                                  request.POST['birthdate'], request.POST['sex'], request.POST['phonenumber'], request.user.id)
        except Exception as inst:
            print('Cannot add patient! Error: ' + inst.__str__)
    return render(request, 'Medical/Registration/main-registration.html')


@login_required(login_url='/login/')
def OnPatients(request):
    return render(request, 'Medical/Patients/main-patients.html')


@login_required(login_url='/login/')
def OnCalendar(request):
    return render(request, 'Medical/Calendar/main-calendar.html')


@login_required(login_url='/login/')
def OnAccount(request):
    return render(request, 'Medical/Account/main-account.html')
