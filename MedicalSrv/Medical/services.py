from .common.choices import *
from .models import *
from .find_changes import *
from datetime import datetime

# todo
# 1.validdation of sex
# 2.validdation of phonenumber
# 1.validdation of pid


def ValidateAndAddPatient(firstname='', lastname='', pid=0, birthdate='', sex='', phonenumber='', doctorid=0, patient_id=0):
    CheckIfNull(firstname, firstname.__str__)
    CheckIfNull(lastname, firstname.__str__)
    CheckIfNull(phonenumber, phonenumber.__str__)
    patient = Patient()

    if patient_id != 0:
        patient = Patient.objects.get(pk=patient_id)

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


def ValidateAndAddPhotography(image='', discription='', visitId=0):
    CheckIfNull(image, image.__str__)
    photography = Photography()
    photography.Name = image.name
    photography.Discription = discription
    photography.Visit = Visit.objects.get(pk=visitId)
    photography.Image = image

    photography.publish()

    return photography.Id


def ValidateAndCalculeteImages(images_ids=''):
    CheckIfNull(images_ids)
    img_ids = images_ids.split(',')
    if(len(img_ids) != 2):
        raise ValueError('there are no 2 of image')
    ReturnChanges(img_ids[0], img_ids[1])


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
