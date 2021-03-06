"""Medical System URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
from Medical import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    # ex /
    url(r'^main/', views.Index, name='main'),
    # ex /login/
    url(r'^login/', views.Log, name='login'),
    url(r'^registration/', views.OnRegistration, name='registration'),
    url(r'^calendar/', views.OnCalendar, name='calendar'),
    url(r'^patients/', views.OnPatients, name='patients'),
    url(r'^account/', views.OnAccount, name='account'),
    url(r'^visit/', views.OnVisit, name='visit'),
    url(r'^openvisit/(?P<visit_id>[0-9]+)/$',
        views.OnOpenVisit, name='openvisit'),
    url(r'^editpatient/(?P<patient_id>[0-9]+)/$',
        views.OnPatientEdit, name='patientedit'),
    url(r'^patientadd/', views.OnPatientAdd, name='patientadd')

] + static(settings.MEDIA_URL,
           document_root=settings.MEDIA_ROOT)
