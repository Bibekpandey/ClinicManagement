from django.shortcuts import render, get_object_or_404
from django.views.generic import View
from django.views.generic.edit import FormView
from django.http import HttpResponse, Http404, HttpResponseRedirect
from records.forms import NewPatientForm, DoctorAndTestForm
import json
from records.models import *


class Reception(View):

    def get(self, request):
        newPatientForm = NewPatientForm()
        docAndTestForm= DoctorAndTestForm()
        return render(request, 'records/reception.html', {'newPatientForm':newPatientForm, 'docAndTestForm':docAndTestForm})


    def post(self, request):
        error = None
        newpatientform = NewPatientForm()
        try:
            if request.method == 'POST':
                # check if it is new patient or not
                if request.POST['new_patient']=="1":
                    newpatientform = NewPatientForm(request.POST or None)
    
                    if newpatientform.is_valid(): 
    
                        data = newpatientform.cleaned_data
    
                        # check for patient, if already, send error msg
                        patients = Patient.objects.filter(name=data['name'], contact=data['contact'])
                        if len(patients) > 0:
                            raise Exception('The patient already exists')
    
                        # create new patient
                        patient = Patient(name=data['name'], contact=data['contact'], age=data['age'], address=data['address'], sex=data['sex'], membership='none')
                        patient.save()
                        # patient created
    
                    else:   # if form is not valid
                        error='invalid form'
                        return render(request, 'records/reception.html', {'error':error, 'newPatientForm':newpatientform, 'docAndTestForm':docAndTestForm})
                        raise Exception('invalid form')
    
                else: # if patient is existing patient
                    patientId = int(request.POST.get('patient_id','-1'))
                    if patientId == -1:
                        raise Exception('invalid id')
                    patients = Patient.objects.filter(pk=patientId)
                    if len(patients)==0:
                        raise Exception('id doesnot exist')
                    patient = patients[0]

                # now get doctor and test data
                docandtestform = DoctorAndTestForm(request.POST or None)
                if docandtestform.is_valid():
                    data = docandtestform.cleaned_data
                    if data['referred_by']:
                        docname = data['doctor_name']
                        hospital = data['hospital']

                        doctor = None
                        # check if doctor exists, 
                        doctors = Doctor.objects.filter(name=docname,hospital=hospital)
                        if len(doctors) == 0 : # create new doctor
                            doctor = Doctor(name=docname, hospital=hospital)
                            doctor.save()
                        else:
                            doctor = doctors[0]
    
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
                    return HttpResponseRedirect('/index/reception/')
            else:
                return HttpResponse('not a post request')
        except Exception as e:
            error = e.args[0]
            return render(request, 'records/reception.html', {'error':error, 'newPatientForm':newpatientform})
        except ValueError:
            return HttpResponse('valueerrro')



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

def calculateBillTest(testid, testtypeObj):
    test = get_object_or_404(Test, pk = testid)



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
        #for bill calculation of Test object
        calculation = float(0)
        string = ''
        for x in postcopy:
            if 'boolean' in x: # means it is a boolean field
                fieldname = x.split('boolean_')[1]
                boolfield = get_object_or_404(BooleanTestField, name=fieldname)
                boolresult = BooleanResult(value=int(postcopy[x]),test=testObj, field=boolfield)
                calculation += boolfield.price         
                boolresult.save()
                
            if 'numeric' in x: # means it is a numeric field
                fieldname = x.split('numeric_')[1]
                numericfield = get_object_or_404(NumericTestField, name=fieldname)
                numericresult = NumericResult(field=numericfield, test=testObj, value=float(postcopy[x]))
                calculation += numericfield.price
                numericresult.save()

        testObj.reportOut = True
        testObj.bill = calculation
        testObj.save();
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

class Login(View):

    def get(self, request):
        HttpResponse("login")

    def post(self, request):
        HttpResponse("login post")
