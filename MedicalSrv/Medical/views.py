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
    patients = RegPatientTable(Patient.objects.all())
    return render(request, 'Medical/Registration/main-registration.html', {'patients': patients})


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
        try:
            ids = request.POST['images_id']
            ValidateAndCalculeteImages(ids)
        except Exception as inst:
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

    images = Photography.objects.select_related().filter(Visit=visit_id)
    patient = Visit.objects.get(pk=visit_id).Patient
    result = Result.objects.select_related().filter(Visit=visit_id)[0]
    return render(request, 'Medical/Visit/open-visit.html', {'imgs': images,
                                                             'patient': patient,
                                                             'result': result})


@login_required(login_url='/login/')
def OnPatients(request):
    patients = PatientTable(Patient.objects.all())
    RequestConfig(request).configure(patients)
    return render(request, 'Medical/Patients/main-patients.html', {'patients': patients})


@login_required(login_url='/login/')
def OnPatientEdit(request, patient_id=0):
    if request.POST:
        patientId = ValidateAndAddPatient(request.POST['firstname'], request.POST['lastname'], request.POST['pid'],
                                          request.POST['birthdate'], request.POST['sex'], request.POST['phonenumber'], request.user.id, patient_id)
    patient = Patient.objects.get(pk=patient_id)
    birth = str(patient.BirthDate.month) + '/' + \
        str(patient.BirthDate.day) + '/' + str(patient.BirthDate.year)
    return render(request, 'Medical/Patients/edit-patient.html', {'patient': patient, 'bd': birth})


@login_required(login_url='/login/')
def OnPatientAdd(request):
    if request.POST:
        patientId = ValidateAndAddPatient(request.POST['firstname'], request.POST['lastname'], request.POST['pid'],
                                          request.POST['birthdate'], request.POST['sex'], request.POST['phonenumber'], request.user.id)
        patients = PatientTable(Patient.objects.all())
        RequestConfig(request).configure(patients)
        return render(request, 'Medical/Patients/main-patients.html', {'patients': patients})
    return render(request, 'Medical/Patients/add-patient.html')


@login_required(login_url='/login/')
def OnCalendar(request):
    return render(request, 'Medical/Calendar/main-calendar.html')


@login_required(login_url='/login/')
def OnAccount(request):
    return render(request, 'Medical/Account/main-account.html')
