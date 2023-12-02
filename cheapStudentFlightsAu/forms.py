from django import forms
from .models import SignUp, LogIn, SignUpAd, SignUpMod, Msg, DealInfo, AdReview
 
class SignUpForm(forms.ModelForm):
    confirm_pw = forms.CharField(max_length=20, required=False)
    notif = forms.ChoiceField(choices=[('Y', 'Yes'), ('N', 'No')], required=False)

    class Meta:
        model = SignUp
        fields = ['fname', 'lname', 'uname', 'email', 'pw', 'confirm_pw']

    def clean(self):
        cleaned_data = super().clean()
        pw = cleaned_data.get("pw")
        confirm_pw = cleaned_data.get("confirm_pw")

        # Only validate confirm_pw if it is provided
        if confirm_pw and pw != confirm_pw:
            self.add_error('confirm_pw', "Passwords must match.")

        return cleaned_data


class SignUpAdForm(forms.ModelForm):
    class Meta:
        model = SignUpAd
        fields = ['bname', 'abn', 'uname', 'email', 'pw', 'join_date']
    
    def clean(self):
        cleaned_data = super().clean()
        
        return cleaned_data

class SignUpModForm(forms.ModelForm):
	class Meta:
		model = SignUpMod
		fields = ["fname", "lname", "uname", "email", "pw", "join_date"]

	def clean(self):
		cleaned_data = super().clean()
  
		return cleaned_data

		

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
		model = SignUp
		fields = ['email', 'pw']

	def clean_password(self):
		cleaned_data = super().clean()
		# Add your validation logic here if needed
		return cleaned_data

class DealInfoForm(forms.ModelForm):
	class Meta:
		model = DealInfo
		fields = "__all__"

class AdReviewForm(forms.ModelForm):
	class Meta:
		model = AdReview
		fields = "__all__"