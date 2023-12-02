from django import forms
from .models import SignUp, LogIn, SignUpAd, SignUpMod, Msg, DealInfo, AdReview

class SignUpForm(forms.ModelForm):
	class Meta:
		model = SignUp
		fields = "__all__"
	confirm_pw = forms.CharField(max_length=20)
	notif = forms.ChoiceField(choices=[('Y','Yes'),('N', 'No')])
	"""	
	fname = forms.CharField(label = "First Name:", max_length=50)
	lname = forms.CharField(label = "Last Name:", max_length=50)
	email = forms.EmailField(label = "Email address:")
	pw = forms.CharField(label = "Password:", max_length=20)
	confirm_pw = forms.CharField(label = "Confirm Password:", max_length=20)
	usi = forms.CharField(label = "USI:", max_length=20)
	notif =forms.ChoiceField(label = "Opt in for email notifications?", choices=[('Yes'),('No')])
	address = forms.CharField(widget = forms.Textarea )
	"""

class SignUpAdForm(forms.ModelForm):
	class Meta:
		model = SignUpAd
		fields = "__all__"

class SignUpModForm(forms.ModelForm):
	class Meta:
		model = SignUpMod
		fields = "__all__"

class MsgForm(forms.ModelForm):
	class Meta:
		model = Msg
		fields = "__all__"
	"""
	uname = forms.CharField(max_length=30)
	msg = forms.CharField(widget = forms.Textarea)
	"""

class LogInForm(forms.ModelForm):
	class Meta:
		model = LogIn
		fields = "__all__"
		"""
	email = forms.EmailField(label = "Email address:")
	pw = forms.CharField(label = "Password:", max_length=20)
	"""

class DealInfoForm(forms.ModelForm):
	class Meta:
		model = DealInfo
		fields = "__all__"

class AdReviewForm(forms.ModelForm):
	class Meta:
		model = AdReview
		fields = "__all__"