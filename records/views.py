from django.shortcuts import render
from django.views.generic import View
from django.views.generic.edit import FormView
from django.http import HttpResponse, Http404, HttpResponseRedirect

from records.models import *
from records.forms import *

class Index(View):
	def get(self, request):
		a={'receptionist':'reception.html', 'labstaff':'lab.html'}
		a['doctor'] = 'doctor.html'
		a['pharmacist'] = 'pharma.html'
		return render(request, 'records/index.html', a) 


class Receptionist(View):
	template_name = 'reception.html'
	form_class = ReceptionForm
	success_url = '/'

	def form_valid(self, form):
		return super(Receptionist, self).form_valid(form)

	def get(self, request):
		return render(request, 'records/reception.html', {})
	def post(self, request):
		return HttpResponse("haha")

class Doctor(View):
	def get(self, request):
		return render(request, 'records/doctor.html', {})
		
	def post(self, request):
		return	
		
