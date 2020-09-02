from django.contrib .auth.models import User
from django.contrib import auth,messages
from django.contrib.auth import authenticate, login , logout , update_session_auth_hash
from django.contrib.auth.forms import PasswordChangeForm,AuthenticationForm,UserChangeForm
# Create your views here.
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render,redirect
from django.urls import reverse
from django.contrib import messages
from .forms import ProfileEditForm,UserForm,ProfileForm
from .models import Personal_info
from django.contrib.auth.decorators import login_required
from django.db import transaction



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




def infor(request):
    if request.method=='POST':
        return render(request,'accounts/hello.html')

    personal=Personal_info.objects.all()
    return render(request,'accounts/infor.html',{'personal':personal})


def edit(request):
        form=ProfileEditForm(instance=request.user)


        return render(request,'accounts/edit_info.html',{'form':form})
#
def updatee(request):
    if request.method=='POST':
        form = ProfileEditForm(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            return redirect('index')
            messages.success(request,'UPdated Successfully')
    else:
        form=ProfileEditForm(instance=request.user)


    return render(request,'accounts/edit_info.html',{'form' : form})




@login_required
@transaction.atomic
def update_profile(request):
    if request.method == 'POST':
        user_form = UserForm(request.POST, instance=request.user)
        profile_form = ProfileForm(request.POST, instance=request.user.personal_info)
        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()
            messages.success(request, _('Your profile was successfully updated!'))
            # return redirect('settings:personal_info')
            return redirect('infor')
        else:
            messages.error(request, _('Please correct the error below.'))
    else:
        user_form = UserForm(instance=request.user)
        profile_form = ProfileForm(instance=request.user.personal_info)
    return render(request, 'accounts/hello.html', { 'user_form': user_form, 'profile_form': profile_form })


















#
# def update_profile(request, user_id):
#     user = User.objects.get(pk=user_id)
#     # user.profile.bio = 'Lorem ipsum dolor sit amet, consectetur adipisicing elit...'
#     user.save()