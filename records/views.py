from django.shortcuts import render, get_object_or_404
from django.views.generic import View
from django.views.generic.edit import FormView
from django.http import HttpResponse, Http404, HttpResponseRedirect
from records.forms import ContactForm, ReceptionForm
import json
from records.models import *


class Reception(View):

    def get(self, request):
        x = TestType.objects.all()
        form  = ReceptionForm()
        return render(request, 'records/reception.html', {'form':form})


    def post(self, request):

        if request.method == 'POST':

            form = ReceptionForm(request.POST)

            if form.is_valid(): 

                data = form.cleaned_data

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

                # check for patient, if already, make new visit object , if new, make new patient and visit object
                patients = Patient.objects.filter(name=data['name'], contact=data['contact'])
                if len(patients) == 0:
                    #means, no such patient, create new

                    patient = Patient(name=data['name'], contact=data['contact'], age=data['age'], address=data['address'], sex=data['sex'], membership='none')
                    patient.save()
                    # patient created
                else:
                    patient = patients[0]

                # now create visit object
                visit = Visit(patient=patient, referredBy=doctor)
                visit.save()

                # create test elements, for different tests checked in the reception page
                testtypes = TestType.objects.all()
                for x in testtypes:
                    if data[x.name]==True: ## means test is chosen
                        # create new test object
                        newtest = Test(visit=visit, testType=x)
                        newtest.save()
                return HttpResponseRedirect('reception')

            else:
                return HttpResponse('invalid')
        else:
            return HttpResponse('not a post')



class LabTest(View):

    def get(self, request):
            return HttpResponse('we dont need get')

    # post request
    def post(self, request):

        testId = int(request.POST.get('testId', '0'))
        testTypeId = int(request.POST.get('testTypeId', '0'))

        testtype = get_object_or_404(TestType, pk=testTypeId)

        fields_numeric = NumericTestField.objects.filter(testType = testtype)
        fields_boolean = BooleanTestField.objects.filter(testType = testtype)

        context = {'testId':testId, 'testtype' : testtype.name, 'fields_numeric' : fields_numeric, 'fields_boolean' : fields_boolean}
        return render(request,'records/labtest.html',  context)



# to process the lab form ( which results in report)
def processLabForm(request):
    if request.method=='POST':
        # a hidden type to know what type of test
        testtype = request.POST.get('testtype','')
        testid = int(request.POST.get('testid', ''))
        testObj = get_object_or_404(Test, pk=testid)

        testtypeObj = TestType.objects.filter(name=testtype)[0]

        # now remove testtype and csrfmiddlewaretoken, we don't need them
        postcopy = request.POST.copy()
        postcopy.pop('csrfmiddlewaretoken')
        postcopy.pop('testtype')
        postcopy.pop('testid')

        # now we have all the fields(numeric and boolean) and their values in the postcopy dict, can be iterated

        string = ''
        for x in postcopy:
            if 'boolean' in x: # means it is a boolean field
                fieldname = x.split('boolean_')[1]
                boolfield = get_object_or_404(BooleanTestField, name=fieldname)
                boolresult = BooleanResult(value=int(postcopy[x]),test=testObj, field=boolfield)
                boolresult.save()
                
            if 'numeric' in x: # means it is a numeric field
                fieldname = x.split('numeric_')[1]
                numericfield = get_object_or_404(NumericTestField, name=fieldname)
                numericresult = NumericResult(field=numericfield, test=testObj, value=float(postcopy[x]))
                numericresult.save()
        
        return HttpResponseRedirect('/index/lab/')



class Lab(View):
    
    def get(self, request):
        context = {}

        # get all the tests which have not been carried out 
        tests = Test.objects.filter(reportOut=False)
        context['tests'] = tests

        return render(request, 'records/lab.html', context)

    def post(self, request):
        return HttpResponse('test')
