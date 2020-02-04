from django.contrib .auth.models import User
from django.contrib import auth,messages
from django.contrib.auth import authenticate, login , logout , update_session_auth_hash
from django.contrib.auth.forms import PasswordChangeForm,AuthenticationForm
# Create your views here.
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render,redirect
from django.urls import reverse
from django.contrib import messages


def index(request):
    if not request.user.is_authenticated:
        return render(request, "pages/login.html")

    else:
        return render('pages/index.html')


def login_view(request):
        username = request.POST["username"]
        password = request.POST["pass"]
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            if 'next' in request.POST:
                return redirect(request.POST.get('next'))
            else:
                return redirect("index")
        else:
            messages.error(request,'Invalid Credentials ')
            return render(request, "pages/login.html")


def logout_view(request):
    if request.method=='POST':
        auth.logout(request)
        messages.success(request, 'Loged Out')
        return redirect('index1')


def dashboard(request):
    return render(request,'accounts/loggedin.html')


def signup(request):
    if request.method=='POST':
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password1']
        password2 = request.POST['password2']

        if password== password2:
            if User.objects.filter(email=email).exists():
                messages.error(request, 'That Username alreay taken ,Please choose Some Other ')
                return redirect('signup')
            else:
                if User.objects.filter(username=username).exists():
                    messages.error(request, 'That Email is  alreay taken ,Please choose Some Other ')
                    return redirect('register')
        else:
            messages.error(request, 'Password did not match')
            return redirect('signup')

        user = User.objects.create_user( username=username,password=password, email=email, first_name=first_name,
                                        last_name=last_name)
        # auth.login(request.user)
        user.save();
        messages.success(request, 'Account created Successfully , Plz Login here !')
        return redirect('index1')


    else:
        # return render(request, 'accounts/register.html')
        return render(request,'accounts/signup.html')



# Change Password


def change_password(request):
    if request.method=='POST':
        form =PasswordChangeForm(request.user,request.POST)
        if form.is_valid():
            user=form.save()
            update_session_auth_hash(request,user)
            messages.success(request,'password changed')
            return redirect('index1')
        else:
            messages.error(request,'try again')
    else:
        form=PasswordChangeForm(request.user)
    return render(request,'accounts/change.html',{'form':form})
