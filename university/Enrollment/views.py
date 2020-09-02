from django.shortcuts import render,redirect
from .models import Enrollment
from django.contrib import messages

# Create your views here.
def enrollment(request):
    if request.method=='POST':
        course_id=request.POST['course_id']
        course=request.POST['listing']
        name=request.POST['name']
        email=request.POST['email']
        phone=request.POST['phone']
        user_id=request.POST['user_id']


        # if already contacted then this code will work
        
        if request.user.is_authenticated:
            user_id=request.user.id
            has_enrolled=Enrollment.objects.all().filter(course_id=course_id,user_id=user_id)
            if has_enrolled:
                messages.error(request,'You are already enrolled in this Course :')
                return redirect('/' + course_id)

    enroll=Enrollment(course_id=course_id,course=course,name=name,email=email,phone=phone,user_id=user_id)
    enroll.save()
    messages.success(request,'Enrolled Successfully ')

    return redirect('/'+course_id)


def dashboard(request):
    data=Enrollment.objects.all().order_by('-enroll_Date').filter(user_id=request.user.id)

    return render(request,'accounts/dashboard.html',{'data':data})