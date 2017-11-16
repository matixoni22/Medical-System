from django.shortcuts import render
from django.http import *
from django.template import loader
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.template import RequestContext
from datetime import datetime
from .models import *
from django.db.models.manager import Manager


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
        patient = Patient()
        patient.FirstName = request.POST['firstname']
        patient.LastName = request.POST['lastname']
        patient.PID = request.POST['pid']
        patient.BirthDate = datetime.strptime(
            request.POST['birthdate'], "%m/%d/%Y").date()
        patient.PhoneNumber = request.POST['phonenumber']
        patient.Doctor = UserProfile.objects
        patient.save()

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
