from .models import *
import django_tables2 as tables
from django_tables2.utils import A  # alias for Accessor
from MedicalSrv.urls import *


class VisitTable(tables.Table):
    amend = tables.TemplateColumn(
        '<form method="post" action="/visit/">{% csrf_token %}<button class="btn btn-primary" name="openvisit" type="submit" value="{{ visits.Id }}">Open Visit</button></form>', verbose_name="")
    link = tables.LinkColumn(
        'openvisit', text='static text', args=[A('pk')])

    class Meta:
        model = Visit

        fields = {'Id', 'Date', 'Patient.FirstName',
                  'Patient.LastName'}
        sequence = ('Id', 'Date', 'Patient.FirstName',
                    'Patient.LastName')

        template = 'django_tables2/bootstrap.html'
