from django.shortcuts import render,redirect,Http404,HttpResponseRedirect,get_object_or_404,HttpResponse
from .models import faculty,testimonial,about,blog,contact,jobform,home_course,Comment,Lecture
from .forms import ModelForm,contactform,CommentForm
from accounts.forms import vacancyForm
from accounts.views import login_view
from django.contrib.auth.decorators import login_required
# Create your views here.
from django.contrib import messages
from django.contrib .auth.models import User
import datetime




def index(request):
    team = faculty.objects.all()
    test=testimonial.objects.all()
    course=home_course.objects.order_by('-published_date')[:3]



    he = blog.objects.order_by('-published_date').filter(is_published=True)[:4]
    context = {
        'team': team,
        'test':test,
        'he':he,
        'course' : course,
        # 'comment':comment
    }

    return render(request,'pages/index.html',context)




# @login_required(login_url='accounts/h')
def course(request,coursee_id):
    try:

        post=get_object_or_404(home_course,id=coursee_id)
        # qa=home_course.objects.get(id=coursee_id)


        context={
                  "qa" :post,
                # 'comment': comment,
                # 'new_comment': new_comment,
                # 'comment_form': comment_form

            }
        # if next:
        #     return redirect(next)
        return render(request, 'pages/course_details.html',context)
    except home_course.DoesNotExist:
        raise Http404("List Doe's Not Exist ")



# for Lecures handling of each course

def lectures(request, id):
    data=Lecture.objects.filter(course=(home_course.objects.get(id=id)).id)

    return render(request,'lectures/lecture.html',{'data':data})







def gallery(request):
    return render(request,'base.html')


# about us
def abouts(request):
    test = testimonial.objects.all()
    team = faculty.objects.all()
    ab = about.objects.all()
    return render(request,'pages/about.html', {'ab':ab, 'team':team, 'test':test})







# blog list

def blogs(request,blog_id):
    blo= blog.objects.get(id=blog_id)
    return render(request,'pages/blog_details.html',{'blo':blo})






# def course(request,course_id):
#     blo= home_course.objects.get(id=course_id)
#     return render(request,'pages/course.html',{'blo':blo})






def contacts(request):
    if request.method=='POST':
        name=request.POST['name']
        email=request.POST['email']
        subject=request.POST['subject']
        message=request.POST['message']
        if contact.objects.filter(email=email).exists():
            messages.error(request, 'That Username already have mailed ,Please wait for admin response to you ')
            return redirect('contacts')
        else:
            m=contact(name=name,email=email,subject=subject,message=message)

            m.save()
            messages.success(request,'Your Query Has Been Sent To Administrator')
            return redirect('contacts')
    else:
        return render(request,'pages/contact.html')


def jobforme(request):
    if request.method == 'POST':
        form = vacancyForm(request.POST , request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request,'Applied Successfully : ')
            return redirect('jobform')






    else:

        form=vacancyForm(request.POST)
    return render(request,'pages/jobform.html',{'form':form})



def courses(request):

    course = home_course.objects.order_by('-published_date')

    context={
        'course':course,
        #
        # 'comment': comments

    }
    return render(request,'pages/course.html',context)



# @login_required(login_url='accounts/h')

