from django.shortcuts import render
from django.http import *
from django.template import loader
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.template import RequestContext
from datetime import datetime
from .models import *
from .services import *
from .viewmodel import *
from django_tables2.config import *
from django.core.files.storage import FileSystemStorage


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
            patientId = ValidateAndAddPatient(request.POST['firstname'], request.POST['lastname'], request.POST['pid'],
                                              request.POST['birthdate'], request.POST['sex'], request.POST['phonenumber'], request.user.id)
            ValidateAndAddVisit(
                request.POST['visitdate'], request.POST['visittime'], request.POST.get('description', False), patientId)
            return render(request, 'Medical/Registration/main-registration.html', {'registration_status': 'Visit was added!'})
        except Exception as inst:
            errorMessage = ('Cannot add patient! Error: ' + inst.args.__str__)
            return render(request, 'Medical/Registration/main-registration.html', {'registration_status': errorMessage})
    return render(request, 'Medical/Registration/main-registration.html')


@login_required(login_url='/login/')
def OnVisit(request):
    if request.POST:
        url = '/openvisit/' + request.POST['visit_id']
        return HttpResponseRedirect(url)
    visits = VisitTable(Visit.objects.all())
    RequestConfig(request).configure(visits)
    return render(request, 'Medical/Visit/main-visit.html', {'visits': visits})


@login_required(login_url='/login/')
def OnOpenVisit(request, visit_id=0):
    if request.POST:
        myFile = request.FILES['myfile']
        try:
            ValidateAndAddPhotography(myFile, "image", visit_id)
        except Exception as inst:
            errorMessage = ''
            if hasattr(inst, 'message'):
                errorMessage = inst.message
            else:
                errorMessage = inst
            return render(request, 'Medical/Visit/open-visit.html', {'status': errorMessage})

    return render(request, 'Medical/Visit/open-visit.html')


@login_required(login_url='/login/')
def OnPatients(request):
    return render(request, 'Medical/Patients/main-patients.html')


@login_required(login_url='/login/')
def OnCalendar(request):
    return render(request, 'Medical/Calendar/main-calendar.html')


@login_required(login_url='/login/')
def OnAccount(request):
    return render(request, 'Medical/Account/main-account.html')
