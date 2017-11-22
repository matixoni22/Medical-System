from .models import *
import django_tables2 as tables


class VisitTable(tables.Table):
    edit_entries = tables.TemplateColumn(
        '<a href="/visit/{{record.id}}">Edit</a>')

    class Meta:
        model = Visit
        fields = {'Id', 'Date', 'Patient.FirstName', 'Patient.LastName'}
        sequence = ('Id', 'Date', 'Patient.FirstName', 'Patient.LastName')
        template = 'django_tables2/bootstrap.html'
