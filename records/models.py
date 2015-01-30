from django.db import models

class Person(models.Model):
	firstName 	= models.CharField(max_length=30)
	middleName 	= models.CharField(max_length=30,blank=True)
	lastName 	= models.CharField(max_length=30)
	age 		= models.IntegerField()
	address 	= models.CharField(max_length=50)
	sex 		= models.CharField(max_length=6)
	
	def __string__(self):
		return self.firstName + " " + self.lastName


class Patient(Person):
	bloodGroup 		= models.CharField(max_length=5)
	firstVisit 		= models.DatetimeField()
	numberOfVisits 	= models.IntegerField(default=1)
	

class Doctor(Person):
	dateJoined 		= models.DatetimeField()
	qualification 	= models.CharField(max_length = 100)
	specialization 	= models.CharField(max_length = 100)
	# working hour to be added


class Staff(Person):
	dateJoined 		= models.DatetimeField()
	qualification 	= models.CharField(max_length = 100)
	workingField 	= models.CharField(max_length = 50)
	# working hour to be added


class Visit(models.Model):
	patient 		= models.ForeignKey(Patient)
	date 			= models.DatetimeField()
	isFirstVisit 	= models.BoolField() ## check whether it is first visit or not
	isFollowup 		= models.BoolField() ## check whether the patient's visit is for followup or not
	patientProblems = models.CharField(max_length = 200)  # the problems the patient states
	problems 		= models.CharField(max_length = 500) ## the problems/illness that doctor sees
	appointmentTime = models.DateTimeField()
	appointmentDoc	= models.ForeignKey(Doctor)
	test 			= models.ForeignKey(Test)
	report 			= mdoels.ForeignKey(Report)
