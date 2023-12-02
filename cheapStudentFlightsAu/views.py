from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.template import loader
from .forms import SignUpForm, SignUpAdForm, SignUpModForm, LogInForm, MsgForm, DealInfoForm, AdReviewForm
from .models import SignUp, SignUpAd, SignUpMod, LogIn, Msg, DealInfo, AdReview
from django.shortcuts import render, redirect
from django.contrib import messages

def cheapStudentFlightsAu(request):
	return HttpResponse("Hello world!")

# Create your views here.

def index(request):
	template = loader.get_template('index.html')
	return HttpResponse(template.render())

def search_results(request):
	template = loader.get_template('search_results.html')
	return HttpResponse(template.render())

def about(request):
	template = loader.get_template('about.html')
	return HttpResponse(template.render())

def help(request):
	template = loader.get_template('help.html')
	return HttpResponse(template.render())

def deal1(request):
	dealinfos = DealInfo.objects.filter(id="1") # only display deal with id=1 from dealinfos table
	return render(request, 'deal1.html', {'dealinfos': dealinfos})

def deal1_st(request):
	dealinfos = DealInfo.objects.filter(id="1") # only display deal with id=1 from dealinfos table
	return render(request, 'deal1_st.html', {'dealinfos': dealinfos})

def deal1_ad(request):
	dealinfos = DealInfo.objects.filter(id="1") # only display deal with id=1 from dealinfos table
	return render(request, 'deal1_ad.html', {'dealinfos': dealinfos})

def deal2(request):
	dealinfos = DealInfo.objects.filter(id="2") # only display deal with id=2 from dealinfos table
	return render(request, 'deal2.html', {'dealinfos': dealinfos})

def deal3(request):
	dealinfos = DealInfo.objects.filter(id="3") # only display deal with id=3 from dealinfos table
	return render(request, 'deal3.html', {'dealinfos': dealinfos})

def deal4(request):
	dealinfos = DealInfo.objects.filter(id="4") # only display deal with id=4 from dealinfos table
	return render(request, 'deal4.html', {'dealinfos': dealinfos})


def deal5(request):
	dealinfos = DealInfo.objects.filter(id="5") # only display deal with id=5 from dealinfos table
	return render(request, 'deal5.html', {'dealinfos': dealinfos})

def deal5_st(request):
	dealinfos = DealInfo.objects.filter(id="5") # only display deal with id=5 from dealinfos table
	return render(request, 'deal5_st.html', {'dealinfos': dealinfos})

def logout(request):
	template = loader.get_template('logout.html')
	return HttpResponse(template.render())

def ad_info(request):
	signup_ads = SignUpAd.objects.filter(id="1") # only display advertiser with id=1 from signup_ads table
	return render(request, 'ad_info.html', {'signup_ads': signup_ads})

def mod_info(request):
	signup_mods = SignUpMod.objects.filter(id="1") # only display moderatore with id=1 from signup_mods table
	return render(request, 'mod_info.html', {'signup_mods': signup_mods})

def st_info(request):
	signups = SignUp.objects.filter(id="1") # only display student with id=1 from signups table
	return render(request, 'st_info.html', {'signups': signups})

def home_ad(request):
	template = loader.get_template('home_ad.html')
	return HttpResponse(template.render())

def home_mod(request):
	template = loader.get_template('home_mod.html')
	return HttpResponse(template.render())

def home_st(request):
	template = loader.get_template('home_st.html')
	return HttpResponse(template.render())

def review(request):
	if request.method == "POST":
		form = AdReviewForm(request.POST)
		if form.is_valid():
			try:
				form.save()
				return redirect('/msg_sent')

			except:
				pass

	else:
		form=AdReviewForm()
	return render(request,'review.html', {'form':form})

def signup_success(request):
	template = loader.get_template('signup_success.html')
	return HttpResponse(template.render())


def signup(request):
	if request.method == "POST":
		form = SignUpForm(request.POST)
		if form.is_valid():
			try:
				form.save()
				return redirect('/signup_success')

			except:
				pass

	else:
		form=SignUpForm()
	return render(request,'signup.html', {'form':form})

def signup_ad(request):
	if request.method == "POST":
		form = SignUpAdForm(request.POST)
		if form.is_valid():
			try:
				form.save()
				return redirect('/signup_success')

			except:
				pass

	else:
		form=SignUpAdForm()
	return render(request,'signup_ad.html', {'form':form})

def signup_mod(request):
	if request.method == "POST":
		form = SignUpModForm(request.POST)
		if form.is_valid():
			try:
				form.save()
				return redirect('/signup_success')

			except:
				pass

	else:
		form=SignUpModForm()
	return render(request,'signup_mod.html', {'form':form})



def login(request):
    if request.method == 'POST':
        form = LogInForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']
            try:
                user = LogIn.objects.get(email=email, pw=password)
                # Authenticate the user (This is a simple example, for actual authentication use Django's authentication system)
                request.session['user_id'] = user.id
                return redirect('/home')  # Redirect to home after successful login
            except LogIn.DoesNotExist:
                messages.error(request, 'Invalid email or password')
    else:
        form = LogInForm()
    return render(request, 'login.html', {'form': form})

def msg(request):
	if request.method == "POST":
		form = MsgForm(request.POST)
		if form.is_valid():
			try:
				form.save()
				return redirect('/msg_sent')

			except:
				pass

	else:
		form=MsgForm()
	return render(request,'msg.html', {'form':form})

def msg_sent(request):
	template = loader.get_template('msg_sent.html')
	return HttpResponse(template.render())

def deal_ad(request):
	if request.method == "POST":
		form = DealInfoForm(request.POST)
		if form.is_valid():
			try:
				form.save()
				return redirect('/deal_sent')

			except:
				pass

	else:
		form=DealInfoForm()
	return render(request,'deal_ad.html', {'form':form})

def deal_sent(request):
	template = loader.get_template('deal_sent.html')
	return HttpResponse(template.render())

"""
def view(request):
	students = Student.objects.all()
	return render(request, 'view.html', {'students': students}

	"""