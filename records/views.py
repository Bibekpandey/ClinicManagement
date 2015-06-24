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

from django.contrib.auth import authenticate, login


class Reception(View):

    def get(self, request):
        logintype = request.session.get('logintype','')
        if not logintype : 
            return HttpResponseRedirect(reverse('login'))
        if logintype == 'lab' : 
            return HttpResponseRedirect(reverse('lab'))
        newPatientForm = NewPatientForm()
        docAndTestForm= DoctorAndTestForm()
        #return render(request, 'records/reception1.html', {'newPatientForm':newPatientForm, 'docAndTestForm':docAndTestForm})
        testtypes = TestType.objects.all()
        return render(request, 'records/improvedUI/reception.html', {'request':request, 'newPatientForm':newPatientForm, 'docAndTestForm':docAndTestForm, 'testtypes':testtypes})


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
                        raise Exception('id doesnot exist!!!')
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
    
                    # now create visit object, check if visit of the same day exists or not
                    visits = Visit.objects.filter(patient=patient, date__year=datetime.now().year,date__month=datetime.now().month, date__day=datetime.now().day)
                    if len(visits)==0:
                        visit = Visit(patient=patient, referredBy=doctor)
                        visit.save()
                    else:
                        visit = visits[0]

                    # create test elements, for different tests checked in the reception page
                    testtypes = TestType.objects.all()
                    for x in testtypes:
                        for y in data.keys():
                            if x.name==y:
                            # create new test object
                                newtest = Test(visit=visit, testType=x)
                                newtest.save()
                    return HttpResponseRedirect('/biomed/reception/')
            else:
                return HttpResponse('not a post request')
        except Exception as e:
            error = 'invalid form or entry'
            return render(request, 'records/reception.html', {'request':request, 'error':error, 'newPatientForm':newpatientform, 'docAndTestForm':docAndTestForm})
        except ValueError:
            return HttpResponse('value error')

class LabTest(View):

    def get(self, request):
        logintype = request.session.get('logintype' ,'' )
        if not logintype : 
            return HttpResponseRedirect(reverse('login'))
        else:
            return HttpResponseRedirect(reverse(logintype))

    # post request
    def post(self, request):

        testId = int(request.POST.get('testId', '0'))
        testTypeId = int(request.POST.get('testTypeId', '0'))

        testtype = get_object_or_404(TestType, pk=testTypeId)

        fields_numeric = NumericTestField.objects.filter(testType = testtype)
        fields_boolean = BooleanTestField.objects.filter(testType = testtype)
        categories = Category.objects.filter(testType=testtype)
        
        # we seek fields according to their category
        fields = {}

        # for fields with no category
        none_category_num_field = NumericTestField.objects.filter(testType=testtype, category=None)
        none_category_bool_field = BooleanTestField.objects.filter(testType=testtype, category=None)
        fields['none'] = {}
        fields['none']['bool_fields'] = list(none_category_bool_field)
        fields['none']['num_fields'] = list(none_category_num_field)

        for category in categories:

            fields[category] = {}

            bool_fields = BooleanTestField.objects.filter(testType=testtype, category=category)
            num_fields = NumericTestField.objects.filter(testType=testtype, category=category)

            fields[category]['bool_fields'] = []
            fields[category]['num_fields'] = []
            fields[category]['none'] = []

            for field in num_fields:
                fields[category]['num_fields'].append(field)
            for field in bool_fields:
                fields[category]['bool_fields'].append(field)

        context = {'testId':testId, 'testtype' : testtype.name, 'fields_numeric' : fields_numeric, 'fields_boolean' : fields_boolean, 'categories':categories, 'fields':fields}
        context['request'] = request
        return render(request,'records/labtest.html',  context)

# to process the lab form ( which results in report)
def processLabForm(request):
    if request.method=='POST':
        try:
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
                    fieldid = int(x.split('boolean_')[1])
                    boolfield = get_object_or_404(BooleanTestField, pk=fieldid)
                    boolresult = BooleanResult(value=int(postcopy[x]),test=testObj, field=boolfield)
                    calculation += boolfield.price         
                    boolresult.save()
                    
                if 'numeric' in x: # means it is a numeric field
                    fieldid= int(x.split('numeric_')[1])
                    numericfield = get_object_or_404(NumericTestField, pk=fieldid)
                    numericresult = NumericResult(field=numericfield, test=testObj, value=float(postcopy[x]))
                    calculation += numericfield.price
                    numericresult.save()

            testObj.reportOut = True
            testObj.bill = calculation
            testObj.save();
            return HttpResponseRedirect('/biomed/lab/')
        except ValueError:
            return HttpResponse('value error')
        except Exception as e:
            return HttpResponse('Error: '+ e) 


class Lab(View):
    
    def get(self, request):
        context = {}
        logintype = request.session.get('logintype','')
        context['logintype'] =  logintype
        context['request'] = request

        if not logintype or logintype=='reception' : 
            return HttpResponseRedirect(reverse('login'))

        # get all the tests which have not been carried out 
        tests = Test.objects.filter(reportOut=False)
        context['tests'] = tests
        return render(request, 'records/improvedUI/lab.html', context)

    def post(self, request):
        return HttpResponse('test')

# our generalized login system -> works for both @reception and @lab
class Login(View):
    # for logintype
    
    # get methid
    def get(self, request):
        context = {}
        context['logintype'] = ''
        context['error'] = ''
        context['request'] = request
        logintype = request.session.get('logintype','')
        if logintype : 
            return HttpResponseRedirect('/biomed/' + logintype)
        else:
            return render(request, 'records/login.html', context)

    # post method
    def post(self, request):
        error = None
        context = {}
        context['request'] = request

        username = request.POST.get('username', '')
        password = request.POST.get('password', '')
        logintype = request.POST.get('selection', '')
        context['logintype'] = logintype

        if not logintype : 
            error = "plese select the account type" 
            context['error'] = error
            return render(request, 'records/login.html', context)

        userlog = None
        if username=='' or password=='':
            error = "username/password cannot be empty :D"
            context['error'] = error
            return render(request, 'records/login.html', context)
        else:
            if logintype == "lab":
                tempuser = authenticate(username=username, password=password)
                userlog = LabStaff.objects.filter(user=tempuser)
            if logintype == "reception":
                tempuser = authenticate(username=username, password=password)
                userlog = ReceptionStaff.objects.filter(user=tempuser)

        if len(userlog) == 0:
            error = "invalid username/password"
            context['error'] = error
            return render(request, 'records/login.html', context)
        else:
            request.session['logintype'] = logintype
            return HttpResponseRedirect(reverse(logintype))

# report view
class Report(View):

    def get(self, request):
        context = {}
        # search and patient will be used in template to distinguish
        # if the request is for searching or getting patient visits
        context['search'] = False 
        context['individual'] = False 
        context['request'] = request
        logintype = request.session.get('logintype' , '')
        if not logintype : 
            return HttpResponseRedirect(reverse('login'))
        if logintype == 'reception' : 
            return HttpResponseRedirect(reverse('reception'))
        try:
            #our query string for fetching patient information
            patientid = request.GET.get('patient','')
            searchstring = request.GET.get('search','')

            # if patientid is given, then it means show visits of patients
            if patientid != '':
                context['individual'] = True
                context['title'] = 'Visits'
                patient = get_object_or_404(Patient, pk=int(patientid))
                visits = Visit.objects.filter(patient = patient).order_by('-date')

                context['patient'] = patient
                context['subtitle'] = patient.name + ', Patient ID: '+str(patient.pk)

                context['visit_list'] = visits

                # now get list of all the tests of the visits
                alltests = []
                for visit in visits:
                    visittests = Test.objects.filter(visit=visit)
                    alltests.append(visittests)
                context['alltests'] = alltests
                # return the patient visits  
                return render(request, 'records/report.html', context)

            else:
                context['title'] = 'Search patients'
                context['subtitle'] = 'search in the box above'
                return render(request, 'records/report.html', context)

        except ValueError:
            raise Http404

    def post(self, request):
        context = {}
        context['request'] = request
        context['search'] = True
        context['individual'] = False
        if request.POST:
            searchstring = request.POST.get('search', '')
            context['title'] = "Search Results"
            context['subtitle'] = searchstring
            patients = Patient.objects.filter(name__icontains=searchstring)
            context['patient_list'] = patients

            return render(request, 'records/report.html', context)

            return HttpResponse("report")
        else:
            raise Http404

# for detail view of the report of the 'visit' specified by 'visitid'
class ReportDetail(View):

    def get(self, request):
        logintype = request.session.get('logintype' , '')
        if not logintype : 
            return HttpResponseRedirect(reverse('login'))
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
            context['testtype'] = test.testType
            context['request'] = request

            return render(request, 'records/report_detail.html', context)
            
        except ValueError:
            return HttpResponse("something went wrong with the request/request variables")

    def post(self, request):
        context = {}
        context['request'] = request
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

# logging out 
class Logout(View):

    def get(self, request):
        #get login session
        del request.session['logintype']
        return HttpResponseRedirect(reverse('login'))

    def post(self, request):
        pass
