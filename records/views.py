from django.shortcuts import render
from django.views.generic import View
from django.views.generic.edit import FormView
from django.http import HttpResponse, Http404, HttpResponseRedirect
import json

from records.models import *

class Index(View):
	def get(self, request):
		a={'receptionist':'reception', 'labstaff':'lab'}
		a['doctor'] = 'doctor'
		a['pharmacist'] = 'pharma'
		return render(request, 'records/index.html', a) 


class ReceptionistPage(View):

	def get(self, request):
		doctors = Doctor.objects.all()

		docs = [{'name':(doc.firstName + " " + doc.lastName), 'id':doc.pk} for doc in doctors]
		docId = [(doc.pk) for doc in doctors] # for sending primary keys to template, later it will be easier to select doctor
		times = json.dumps([[doc.workingHour.sunday,doc.workingHour.monday, doc.workingHour.tuesday,
						doc.workingHour.wednesday, doc.workingHour.thursday, doc.workingHour.friday,
						doc.workingHour.saturday] for doc in doctors])

		return render(request, 'records/reception.html', {'doctors':docs, 'times':times})

	def post(self, request):
		return HttpResponse("haha")

class DoctorPage(View):
	def get(self, request):
		return render(request, 'records/doctor.html', {})
		
	def post(self, request):
		return	
		
