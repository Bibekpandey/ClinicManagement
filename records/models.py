from django.db import models
from datetime import datetime


# for the ranges of values like RBC count normal value lies between 12000 - 15000 cucmm(just example)

class Range(models.Model):
    startValue  = models.DecimalField(max_digits=12, decimal_places=5)
    endValue    = models.DecimalField(max_digits=12, decimal_places=5)
    unit        = models.CharField(max_length=20)

    def __str__(self):
        return str(self.startValue) + " - " + str(self.endValue) + " " + self.unit


# Test types like Haematology, Serology, Urine, etc.

class TestType(models.Model):
    name        = models.CharField(max_length=30)
    comments    = models.CharField(max_length=200, blank=True)

    def __str__(self):
        return self.name


# for the category of the tests like differential count, absolute count, etc

class Category(models.Model):
    testType = models.ForeignKey('TestType', null=True)
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name


# test field contains subtests done in overall tests like Haematology, Serology.
# More clearly, a Haematology test consists of Lymphocyte counts, Neurophill counts and so on.

class TestField(models.Model):
    category    = models.ForeignKey('Category', blank=True, null=True)
    testType    = models.ForeignKey('TestType')
    name        = models.CharField(max_length=50)
    price       = models.FloatField(default= 0)

    def __str__(self):
        return self.name


# field for tests having boolean results like parasites found/not found, and so on

class BooleanTestField(TestField):
    positive = models.CharField(max_length=30) # like, in parasites field, positive means 'found' and negative means 'not found'
    negative = models.CharField(max_length=30)


# field for tests having numerical results like RBC count

class NumericTestField(TestField):
    maleRange   = models.ForeignKey('Range', related_name="male_range", null=True, blank=True)
    femaleRange = models.ForeignKey('Range', related_name="female_range", null=True, blank=True)
    childRange  = models.ForeignKey('Range', related_name="child_range", null=True, blank=True)


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
    value   = models.FloatField(default=0)

    def __str__(self):
        return self.field.name + " " + str(self.value)


# A person

class Person(models.Model):
    name = models.CharField(max_length=50)
    age = models.IntegerField(default=0)
    address = models.CharField(max_length=50)
    contact = models.CharField(max_length=50)
    sex = models.CharField(max_length=6)

    def __str__(self):
        return self.name + " " + self.contact


# Doctor

class Doctor(models.Model):
    name = models.CharField(max_length=50)
    hospital = models.CharField(max_length=50)
    field = models.CharField(max_length=40, blank=True)

    def __str__(self):
        return self.name + "  "+ self.hospital


# Patient

class Patient(Person):
   numberOfVisits = models.IntegerField(default=1)
   membership = models.CharField(max_length=40)


# Visit model, records details of patient's each visit

class Visit(models.Model):
    patient = models.ForeignKey('Patient')
    referredBy = models.ForeignKey('Doctor', null=True) 
    date = models.DateTimeField(default=datetime.now())
    totalBill = models.FloatField(default=0)
    comments = models.CharField(max_length=100, blank=True)

    def __str__(self):
        return self.patient.name + " on " + str(self.date)


# Test model, records tests done and reports of the test in a visit of patient

class Test(models.Model):
    visit = models.ForeignKey('Visit')
    testType = models.ForeignKey('TestType')
    reportOut = models.BooleanField(default=False) # stores whether report is out or not
    reportDate = models.DateTimeField(default=datetime.now()) # stores the date when the report was prepared
    testDone = models.BooleanField(default=False) # stores whether test is carried out or not
    bill = models.FloatField(default=0)

    def __str__(self):
        return self.testType.name + " ("+self.visit.patient.name+")"

class LabStaff(models.Model):
    username = models.CharField(max_length = 50)
    password = models.CharField(max_length = 200)

    def __str__(self):
        return "labstaff : " + self.username

class ReceptionStaff(models.Model):
    username = models.CharField(max_length = 50)
    password = models.CharField(max_length = 200)

    def __str__(self):
        return "receptionstaff : " + self.username
