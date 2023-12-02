from django.db import models
from django.forms import ModelForm, Textarea

# Create your models here.

class SignUp(models.Model): # student sign up form fields
	fname = models.CharField(max_length=30) # student first name
	lname = models.CharField(max_length=30) # last name
	uname = models.CharField(max_length=30, default="username") # username
	email = models.EmailField(max_length=30) # email address
	dob = models.DateField(max_length=10) # date of birth
	pw = models.CharField(max_length=20)
	usi = models.CharField(max_length=10) # unique student identifier
	join_date = models.DateField(max_length=10, default="2023-05-07") # date user signed up
	def __str__(self):
		return f"{self.uname}"

class SignUpAd(models.Model): # advertiser sign up form fields
	bname = models.CharField(max_length=40)
	abn = models.CharField(max_length=11)
	uname = models.CharField(max_length=30)
	email = models.EmailField(max_length=30)
	pw = models.CharField(max_length=20)
	join_date = models.DateField(max_length=10, default="2023-05-07")
	def __str__(self):
		return f"{self.uname}"

class SignUpMod(models.Model): # moderator sign up form fields
	fname = models.CharField(max_length=30) 
	lname = models.CharField(max_length=30)
	uname = models.CharField(max_length=30)
	email = models.EmailField(max_length=30)
	pw = models.CharField(max_length=20)
	join_date = models.DateField(max_length=10, default="2023-05-07")
	def __str__(self):
		return f"{self.uname}"

class LogIn(models.Model):
	email = models.EmailField(max_length=30)
	pw = models.CharField(max_length=20)

class Msg(models.Model):
	recipient = models.CharField(max_length=30) # recipient's username
	uname = models.CharField(max_length=30) # sender's username
	subject = models.CharField(max_length=40, default="(Subject here)") # subject of message
	msg = models.CharField(max_length=500) # message
	date_sent = models.DateField(max_length=10, default="2023-05-07") # date message sent
	def __str__(self):
		return f"{self.uname}"

class DealInfo(models.Model):
	ad_desc = models.CharField(max_length=250) # field to enter short description of deal
	start_date = models.DateField(max_length=10, default="2023-05-07") # field to enter date the deal offer starts
	end_date = models.DateField(max_length=10) # field to enter date the deal offer ends
	airline = models.CharField(max_length=30) # field to enter airline for deal
	disc_price = models.FloatField(max_length=7) # field to enter discounted unit price (per ticket) in $AUD
	price = models.FloatField(max_length=7) # field to enter original unit price (per ticket) in $AUD
	acc = models.CharField(max_length=1) # field to enter "Y" for included accommodation or "N" for no accommodation

class AdReview(models.Model):
	mod_uname = models.CharField(max_length=30)
	ad_uname = models.CharField(max_length=1)
	approve = models.CharField(max_length=40)
	feedback = models.CharField(max_length=500)
	date = models.DateField(max_length=10)

class Meta:
	db_table = "ad_user"
	db_table = "mod_user"
	db_table = "stu_user" # to store student user sign up details
	db_table = "deals" # to store deal info to be displayed in tables on deal webpages
	db_table = "msgs"
	db_table = "reviews"
