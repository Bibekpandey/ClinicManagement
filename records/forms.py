from django import forms

class ContactForm(forms.Form):
    subject = forms.CharField()
    email = forms.EmailField()
    message = forms.CharField()
    ulala = forms.ChoiceField(choices=[('male','male'), ('female','female')], widget=forms.RadioSelect())

class ReceptionForm(forms.Form):
    name = forms.CharField(label='name')
    sex = forms.ChoiceField(label="sex",choices=[('male','male'), ('female','female')], widget=forms.RadioSelect())
    contact = forms.CharField(label='contact')
    address = forms.CharField(label='address')
    age = forms.IntegerField(label='age')
    referred_by = forms.BooleanField()
    doctor_name = forms.CharField()
    hospital = forms.CharField()
