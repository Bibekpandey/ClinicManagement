from django.db import models
from datetime import datetime


# for the ranges of values like RBC count normal value lies between 12000 - 15000 cucmm(just example)

class Range(models.Model):
    startValue  = models.IntegerField(default=0)
    endValue    = models.IntegerField(default=0)
    unit        = models.CharField(max_length=20)

    def __str__(self):
        return self.startValue + " - " + self.endValue + " " + unit


# Test types like Haematology, Serology, Urine, etc.

class TestType(models.Model):
    name        = models.CharField(max_length=30)
    comments    = models.CharField(max_length=200)

    def __str__(self):
        return self.name


# test field contains subtests done in overall tests like Haematology, Serology.
# More clearly, a Haematology test consists of Lymphocyte counts, Neurophill counts and so on.

class TestField(models.Model):
    testType    = models.ForeignKey('TestType')
    name        = models.CharField(max_length=50)
    price       = models.IntegerField(default= 0)

    def __str__(self):
        return self.name


# field for tests having boolean results like parasites found/not found, and so on

class BooleanTestField(TestField):
    positive = models.CharField(max_length=30) # like, in parasites field, positive means 'found' and negative means 'not found'
    negative = models.CharField(max_length=30)


# field for tests having numerical results like RBC count

class NumericTestField(TestField):
    maleRange   = models.OneToOneField('Range', related_name="male_range")
    femaleRange = models.OneToOneField('Range', related_name="female_range")
    childRange  = models.OneToOneField('Range', related_name="child_range")


# for storing result

class BooleanResult(models.Model):
    field   = models.ForeignKey('BooleanTestField') # which field it belongs to
    test    = models.ForeignKey('Test') # which test does it belongs to
    value   = models.BooleanField(default=False)

    def __str__(self):
        if self.value:
            result = self.field.positive
        else:
            result = self.field.negative
        return self.field.name + " " + result 


# for storing numeric result

class NumericResult(models.Model):
    field   = models.ForeignKey('NumericTestField') # which field it belongs to
    test    = models.ForeignKey('Test') # which test does it belongs to
    value   = models.IntegerField(default=0)

    def __str__(self):
        return self.field.name + " " + self.value


# A person

class Person(models.Model):
    name = models.CharField(max_length=50)
    age = models.IntegerField(default=0)
    address = models.CharField(max_length=50)
    contact = models.CharField(max_length=50)
    sex = models.CharField(max_length=6)

    def __str__(self):
        return self.name


# Doctor

class Doctor(Person):
    hospital = models.CharField(max_length=50)
    field = models.CharField(max_length=40)


# Patient

class Patient(Person):
   referredBy = models.OneToOneField('Doctor', null=True) 
   numberOfVisits = models.IntegerField(default=1)
   membership = models.CharField(max_length=40)


# Visit model, records details of patient's each visit

class Visit(models.Model):
    patient = models.ForeignKey('Patient')
    date = models.DateTimeField(default=datetime.now())
    totalBill = models.IntegerField(default=0)
    comments = models.CharField(max_length=100, blank=True)

    def __str__(self):
        return self.patient.name + " on " + str(self.date)


# Test model, records tests done and reports of the test in a visit of patient

class Test(models.Model):
    visit = models.ForeignKey('Visit')
    testType = models.ForeignKey('TestType')
    reportDate = models.DateTimeField(default=datetime.now()) # stores the date when the report was prepared

    def __str__(self):
        return self.testType.name + " ("+self.visit.patient+")"
