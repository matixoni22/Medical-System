from .models import *
import django_tables2 as tables
from django_tables2.utils import A  # alias for Accessor
from MedicalSrv.urls import *


class VisitTable(tables.Table):
    link = tables.LinkColumn(
        'openvisit', text='open Visit', args=[A('pk')])

    class Meta:
        model = Visit

        fields = {'Id', 'Date', 'Patient.FirstName',
                  'Patient.LastName'}
        sequence = ('Id', 'Date', 'Patient.FirstName',
                    'Patient.LastName')

        template = 'django_tables2/bootstrap.html'


class PatientTable(tables.Table):
    link = tables.LinkColumn(
        'patientedit', text='edit', args=[A('pk')])

    class Meta:
        model = Patient

        fields = {'Id', 'FirstName', 'LastName',
                  'PID', 'Sex', 'BirthDate', 'PhoneNumber'}
        sequence = ('Id', 'FirstName', 'LastName',
                    'PID', 'Sex', 'BirthDate', 'PhoneNumber')

        template = 'django_tables2/bootstrap.html'


class RegPatientTable(tables.Table):
    selection = tables.CheckBoxColumn(accessor='pk')
    class Meta:
        model = Patient
        
        fields = {'Id', 'FirstName', 'LastName',
                  'PID', 'Sex', 'BirthDate', 'PhoneNumber'}
        sequence = ('Id', 'FirstName', 'LastName',
                    'PID', 'Sex', 'BirthDate', 'PhoneNumber')

        template = 'django_tables2/bootstrap.html'
