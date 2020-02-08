from django.shortcuts import render,redirect,Http404,HttpResponseRedirect,get_object_or_404,HttpResponse
from .models import faculty,testimonial,about,blog,contact,jobform,home_course,Comment
from .forms import ModelForm,contactform,CommentForm
from accounts.views import login_view
from django.contrib.auth.decorators import login_required
# Create your views here.
from django.contrib import messages
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
        comment=Comment.objects.all().filter(post=coursee_id).order_by('-id')
        if request.method =='POST':
            comment_form=CommentForm(request.POST or None)
            if comment_form.is_valid():
                content=request.POST.get('content')
                comments=Comment.objects.create(post=coursee_id,user=request.user,content=content)
                comments.save()
                return HttpResponseRedirect(coursee_id.get_absolute_url())
        else:
                comment_form=CommentForm

        context={
                  "qa" :post,
                'comment': comment,
                # 'new_comment': new_comment,
                'comment_form': comment_form

            }
        # if next:
        #     return redirect(next)
        return render(request, 'pages/course_details.html',context)
    except home_course.DoesNotExist:
        raise Http404("List Doe's Not Exist ")













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
    if request.method=='POST':
        name = request.POST['full_name']
        email = request.POST['email']
        image = request.POST['file_cv']
        message = request.POST['message']
        if jobform.objects.filter(email=email).exists():
            messages.error(request, 'This Email is already have applied,Please wait for admin approve your request! ')
            return redirect('jobform')
        else:
            h=jobform(name=name,email=email,message=message,image=image)
            h.save()
            messages.success(request,'Applied Successfully')

            return redirect('jobform')
    else:
        return render(request,'pages/jobform.html')

# def hello(request):
#     return render(request,'pages/jobform.html')




def courses(request):

    course = home_course.objects.order_by('-published_date')

    context={
        'course':course,
        #
        # 'comment': comments

    }
    return render(request,'pages/course.html',context)



@login_required(login_url='accounts/h')
def enrollment(request):
    return render(request,'cart/cart.html')