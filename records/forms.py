from django import forms
from records.models import * 

class NewPatientForm(forms.Form):
    name = forms.CharField(label='name')
    sex = forms.ChoiceField(label="sex",choices=[('male','male'), ('female','female')], widget=forms.RadioSelect())
    contact = forms.CharField(label='contact')
    address = forms.CharField(label='address')
    age = forms.IntegerField(label='age')
    

class DoctorAndTestForm(forms.Form):
    referred_by = forms.BooleanField(required=False)
    doctor_name = forms.CharField(required=False)
    hospital = forms.CharField(required=False)
    
    def __init__(self, *args, **kwargs):
        super(DoctorAndTestForm, self).__init__(*args, **kwargs)
        testtypes = TestType.objects.all()
        for x in testtypes:
            self.fields[x.name]= forms.BooleanField(label=x.name, required=False)


