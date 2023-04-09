from django.http import HttpResponse
from django.shortcuts import redirect, render
from django.contrib.auth.models import User
from django.contrib.auth import login,authenticate, logout
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.decorators import login_required

from user.forms import NewUserForm

# Create your views here.
@login_required(login_url='/home')
def index(request):
    user = request.user
    users = User.objects.all()
    context = {
        'users': users,
	    "user": user,
    }
    return render (request, 'user.html', context)

@login_required(login_url='/home')
def login_request(request):
	user = request.user
	# if user.is_authenticated():
        
	if request.method == "POST":
		form = AuthenticationForm(request, data=request.POST)
		if form.is_valid():
			username = form.cleaned_data.get('username')
			password = form.cleaned_data.get('password')
			user = authenticate(username=username, password=password)
			if user is not None:
				login(request, user)
				return redirect('/home')
			else:
				return HttpResponse("Invalid username or password.")
		else:
			return HttpResponse("Invalid username or password.")
	form = AuthenticationForm()
	return render(request=request, template_name="login.html", context={"login_form":form})


@login_required(login_url='/home')
def register_request(request):
	if request.method == "POST":
		form = NewUserForm(request.POST)
		if form.is_valid():
			user = form.save()
			login(request, user)
			return HttpResponse(request, "Registration successful." )
		return HttpResponse("Unsuccessful registration. Invalid information.")
	form = NewUserForm()
	return render (request=request, template_name="register.html", context={"register_form":form})

def logout_request(request):
	logout(request= request)
	return redirect('/')