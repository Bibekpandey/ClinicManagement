from django.shortcuts import render
from django.views.generic import View
from django.views.generic.edit import FormView
from django.http import HttpResponse, Http404, HttpResponseRedirect
from records.forms import ContactForm, ReceptionForm
import json
from records.models import *

def contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            return HttpResponse(cd.errors)
        else:
            return HttpResponse('invalid form')
    else:
        form = ContactForm()
        return render(request, 'records/reception.html', {'form':form})



class Reception(View):

    def get(self, request):
        form  = ReceptionForm()
        return render(request, 'records/reception.html', {'form':form})


    def post(self, request):

        if request.method == 'POST':

            form = ReceptionForm(request.POST)

            if form.is_valid(): # check for patient, if already, make new visit object , if new, make new patient and visit object

                data = form.cleaned_data
                patients = Patient.objects.filter(name=data['name'], contact=data['contact'])

                if data['referred_by']: # this may be false too
                    # search for doctor
                    doctors = Doctor.objects.filter(name=data['doctor_name'], hospital=data['hospital'])
                    if len(doctors)==0:
                        doctor = Doctor(name=data['doctor_name'], hospital=data['hospital'])
                        doctor.save()
                    else:
                        doctor = doctors[0]
                else:
                    doctor = None

                if len(patients) == 0:
                    #means, no such patient, create new

                    patient = Patient(name=data['name'], contact=data['contact'], age=data['age'], address=data['address'], sex=data['sex'], membership='none', referredBy=doctor)
                    patient.save()
                    # patient created
                else:
                    patient = patients[0]

                # now create visit object
                visit = Visit(patient=patient)
                visit.save()
                return HttpResponse('created')
            else:
                return HttpResponse('invalid')
        else:
            return HttpResponse('not a post')



class LabTest(View):

    def get(self, request):
        getvar = request.GET.get('testtype','').lower()
        testtype = TestType.objects.filter(name = getvar)

        if len(testtype) == 0:
            return HttpResponse("invalid lab test query")

        testtype = testtype[0]

        fields_numeric = NumericTestField.objects.filter(testType = testtype)
        fields_boolean = BooleanTestField.objects.filter(testType = testtype)

        context = {'testtype' : testtype.name, 'fields_numeric' : fields_numeric, 'fields_boolean' : fields_boolean}
        return render(request,'records/labtest.html',  context)

    # post request
    def post(self, request):

        # a hidden type to know what type of test
        getvar = request.POST.get('testtype','')
        testtype = TestType.objects.filter(name = getvar)[0]

        # now remove testtype and csrfmiddlewaretoken, we don't need them
        test = request.POST.copy()
        test.pop('testtype')
        test.pop('csrfmiddlewaretoken')
        x = test.keys()
        return HttpResponse(str(x))

        fields_numeric = NumericTestField.objects.filter(testType = testtype)
        fields_boolean = BooleanTestField.objects.filter(testType = testtype)

        temp = ''
        
        for field in fields_numeric:
            if request.POST.get(field.name,''):
                temp += (field.name + " " + request.POST.get(field.name,'') + "<br/>")

        return HttpResponse(temp)









