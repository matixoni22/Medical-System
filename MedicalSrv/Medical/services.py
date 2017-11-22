from .common.choices import *
from .models import *
from datetime import datetime

# todo
# 1.validdation of sex
# 2.validdation of phonenumber
# 1.validdation of pid


def ValidateAndAddPatient(firstname='', lastname='', pid=0, birthdate='', sex='', phonenumber='', doctorid=0):
    CheckIfNull(firstname, firstname.__str__)
    CheckIfNull(lastname, firstname.__str__)
    CheckIfNull(phonenumber, phonenumber.__str__)

    patient = Patient()
    patient.FirstName = firstname
    patient.LastName = lastname
    patient.PID = pid
    patient.BirthDate = ValidateAndParseDateTime(birthdate, birthdate.__str__)
    patient.Sex = ValidateAndSetSex(sex)
    patient.PhoneNumber = phonenumber
    patient.Doctor = UserProfile.objects.get(UserMain_id=doctorid)
    patient.publish()

    return patient.Id


def ValidateAndAddVisit(datetime='', time='', details='', patientId=0):
    visit = Visit()
    visit.Date = ValidateAndParseDateTime(datetime, datetime.__str__, time)
    visit.Details = details
    visit.Patient = Patient.objects.get(pk=patientId)
    visit.publish()


def CheckIfNull(parameter='', parametername=''):
    if(parameter == ''):
        raise ValueError('parameter: ' + parametername + ' is empty')


def ValidateAndParseDateTime(datetimestr='', parametername='', timestr=''):
    CheckIfNull(datetimestr, parametername)
    if timestr != '':
        try:
            date = datetime.strptime(
                datetimestr + ' ' + timestr, "%m/%d/%Y %H:%M")
        except Exception:
            raise ValueError('Wrong date format of ' +
                             datetimestr + ' or ' + timestr)
        return date
    else:
        try:
            date = datetime.strptime(datetimestr, "%m/%d/%Y").date()
        except Exception:
            raise ValueError('Wrong date format of ' + datetimestr)
        return date


def ValidateAndSetSex(sexstr=''):
    CheckIfNull(sexstr, sexstr.__str__)
    sexstr = sexstr.lower().replace(" ", "")
    if sexstr == 'female':
        return 1
    elif sexstr == 'male':
        return 0
    else:
        raise ValueError('cannot parse: ' + sexstr + ' to Sex')
