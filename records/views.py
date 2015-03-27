from django.shortcuts import render, get_object_or_404
from django.views.generic import View
from django.views.generic.edit import FormView
from django.http import HttpResponse, Http404, HttpResponseRedirect
from records.forms import NewPatientForm, DoctorAndTestForm
from django.core.urlresolvers import reverse
import json
from records.models import *
from django.utils.timezone import get_current_timezone
from datetime import datetime


class Reception(View):

    def get(self, request):
        logintype = request.session.get('logintype','')
        if not logintype : 
            return HttpResponseRedirect(reverse('login_reception'))
        if logintype == 'lab' : 
            return HttpResponseRedirect(reverse('lab'))
        newPatientForm = NewPatientForm()
        docAndTestForm= DoctorAndTestForm()
        #return render(request, 'records/reception1.html', {'newPatientForm':newPatientForm, 'docAndTestForm':docAndTestForm})
        testtypes = TestType.objects.all()
        return render(request, 'records/reception.html', {'newPatientForm':newPatientForm, 'docAndTestForm':docAndTestForm, 'testtypes':testtypes})


    def post(self, request):
        error = None
        newpatientform = NewPatientForm()
        docAndTestForm= DoctorAndTestForm()
        try:
            if request.method == 'POST':
                data = request.POST.copy()
                # check if it is new patient or not
                if request.POST['new_patient']=="1":
                    newpatientform = NewPatientForm(request.POST or None)
    
                    if 1 or newpatientform.is_valid(): 
    
                        #data = newpatientform.cleaned_data
                        data = request.POST.copy()
    
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
                #docandtestform = DoctorAndTestForm(request.POST or None)
                doctor=None
                #if 1 or docandtestform.is_valid():
                if 1:
                    #data = docandtestform.cleaned_data
                    data = request.POST.copy()
                    if 'referred_by' in data.keys():
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
                        for y in data.keys():
                            if x.name==y:
                            # create new test object
                                newtest = Test(visit=visit, testType=x)
                                newtest.save()
                    return HttpResponseRedirect('/index/reception/')
            else:
                return HttpResponse('not a post request')
        except Exception as e:
            error = e.args[0]
            return render(request, 'records/reception1.html', {'error':error, 'newPatientForm':newpatientform})
        except ValueError:
            return HttpResponse('valueerrro')



class LabTest(View):

    def get(self, request):
        logintype = request.session.get('logintype' ,'' )
        if not logintype : 
            return HttpResponseRedirect(reverse('login_lab'))
        if logintype == "lab":
            return HttpResponseRedirect(reverse('lab'))
        if logintype == "reception" : 
            return HttpResponseRedirect(reverse('reception'))
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
        logintype = request.session.get('logintype','')

        if not logintype : 
            return HttpResponseRedirect(reverse('login_lab'))
        if logintype == 'reception' : 
            return HttpResponseRedirect(reverse('login_reception'))

        # get all the tests which have not been carried out 
        tests = Test.objects.filter(reportOut=False)
        context['tests'] = tests

        return render(request, 'records/lab.html', context)

    def post(self, request):
        return HttpResponse('test')

# our generalized login system -> works for both @reception and @lab
class Login(View):
    # for logintype
    logintype = None
    error = ""
    
    #counstructor shit
    def __init__(self, logintype):
        self.logintype = logintype
        self.error = ""
    
    # get methid
    def get(self, request):
        context = {}
        context['logintype'] = self.logintype
        context['error'] = self.error
        logintype = request.session.get('logintype','')
        if logintype : 
            return HttpResponseRedirect('/index/' + logintype)
        else:
            return render(request, 'records/login.html', context)

    # post method
    def post(self, request):
        error = None
        context = {}

        username = request.POST.get('username', '')
        password = request.POST.get('password', '')
        logintype = request.POST.get('logintype', '')
        context['logintype'] = logintype

        # for redirecting things
        redirect = ''
        if(logintype == "lab"):
            redirect="lab"
        if(logintype == 'reception') : 
            redirect = "reception"

        user = None
        if username=='' or password=='':
            error = "username/password cannot be empty :D"
            self.error = error
            return HttpResponseRedirect(reverse("login_" + redirect))
        else:
            if logintype == "lab":
                user = LabStaff.objects.filter(username = username, password = password)
            if logintype == "reception":
                user = ReceptionStaff.objects.filter(username = username, password = password)

        if len(user) == 0:
            error = "invalid username/password"
            context['error'] = error
            self.error = error
            return HttpResponseRedirect('/index/login/' + logintype ) 
        else:
            request.session['logintype'] = logintype
            return HttpResponseRedirect(reverse(redirect))

# report view
class Report(View):

    def get(self, request):
        context = {}
        logintype = request.session.get('logintype' , '')
        if not logintype : 
            return HttpResponseRedirect(reverse('login_lab'))
        if logintype == 'reception' : 
            return HttpResponseRedirect(reverse('reception'))
        try:
            #our query string for fetching patient information
            patientid = int(request.GET.get('patient',''))

            patient = get_object_or_404(Patient, pk=patientid)
            visits = Visit.objects.filter(patient = patient).order_by('-date')

            context['name'] = patient.name
            context['contact'] = patient.contact

            context['visits'] = visits

            # now get list of all the tests of the visits
            alltests = []
            for visit in visits:
                visittests = Test.objects.filter(visit=visit)
                alltests.append(visittests)
            context['alltests'] = alltests

            return render(request, 'records/report.html', context)
        except ValueError:
            raise Http404

    def post(self, request):
        return HttpResponse("report")

# for detail view of the report of the 'visit' specified by 'visitid'
class ReportDetail(View):

    def get(self, request):
        logintype = request.session.get('logintype' , '')
        if not logintype : 
            return HttpResponseRedirect(reverse('login_lab'))
        if logintype == 'reception' : 
            return HttpResponseRedirect(reverse('reception'))
        # here we get test id as get variable
        try:
            testid = int(request.GET.get("testid",""))
            test = get_object_or_404(Test,pk=testid)

            # get all the numeric results whose test is test
            numeric_results = NumericResult.objects.filter(test=test)
            # get all the boolean results whose test is test
            boolean_results = BooleanResult.objects.filter(test=test)
            #now categorize the results by category
            categories = Category.objects.filter(testType=test.testType)
            categorized_numeric_values = []
            categorized_boolean_values = []
            # categoriezed values in same list
            for category in categories:
                filterednumeric = numeric_results.filter(field__category__name=category)
                filteredboolean = boolean_results.filter(field__category__name=category)
                categorized_numeric_values.append(filterednumeric)
                categorized_boolean_values.append(filteredboolean)

            noncategorized_numeric = numeric_results.filter(field__category=None)
            noncategorized_boolean = boolean_results.filter(field__category=None)
            context = {}
            context['categories'] = categories
            context['numeric_categorized'] = categorized_numeric_values
            context['boolean_categorized'] = categorized_boolean_values
            context['numeric_uncategorized'] = noncategorized_numeric
            context['boolean_uncategorized'] = noncategorized_boolean
            context['visit'] = test.visit
            context['patient'] = test.visit.patient

            return render(request, 'records/report_detail.html', context)
            
        except ValueError:
            return HttpResponse("something went wrong with the request/request variables")

    def post(self, request):
        context = {}
        # get post data
        name = request.POST.get("name","")
        contact = request.POST.get("contact","")
        visitid = request.POST.get("id", "")
       
        # get patient,visit, and test object
        patient = Patient.objects.filter(name = name, contact = contact)[0]
        visit = get_object_or_404(Visit, pk = visitid)
        tests = Test.objects.filter(visit = visit)
        
        context['patient'] = patient
        context['visit'] = visit
        context['tests'] = tests

        return render(request, 'records/report_detail.html', context)
