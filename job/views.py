from django.contrib import messages
from django.shortcuts import render, redirect
from django.core.mail import EmailMessage, send_mail

# Create your views here.
from job.models import contact
from job_env import settings
from job_management.models import Add_Job, sub_sub_category


def index(request):
    data = Add_Job.objects.all().order_by('-id')
    return render(request, "index.html", {"data": data})


# Create your views here.
def jobs(request):
    if 'job_cat' in request.GET:
        job_cat = request.GET['job_cat']
        cat = sub_sub_category.objects.get(id=job_cat)
        data = Add_Job.objects.filter(sub_sub_category_name=cat.sub_sub_category_name)
        context = {
            'job_data': data,
        }
    elif 'main_job' in request.GET:
        main_job = request.GET['main_job']
        print()
        data = Add_Job.objects.get(id=main_job)
        context = {
            'main_job': data,
        }
    else:
        data = Add_Job.objects.all()
        context = {
            'job_data': data,
        }
    return render(request, "jobs.html", context)


def about_us(request):
    return render(request, 'about-us.html')


def contact_us(request):
    if request.method == "POST":
        name = request.POST['name']
        email = request.POST['name']
        message = request.POST['name']
        data = contact(name=name, email=email, message=message)
        data.save()

        send_mail(
            "New Query",
            'You Have Recived New Query <br><br> Name => ' + name + '/n Email => ' + email + '/n Message => ' + message,
            settings.EMAIL_HOST_USER,
            ['solankiharsh5888@gmail.com'],
            fail_silently=False,
        )

        send_mail(
            "Success",
            'We Have Recived Your Your Query We Will Reply To You As Soon As Possible',
            settings.EMAIL_HOST_USER,
            ['solankiharsh5888@gmail.com'],
            fail_silently=False,
        )
        messages.success(request, 'We Have Recived Your Query We Will Reply To You As Soon As Possible!!')
        return redirect('contact-us')
    else:
        return render(request, 'contact-us.html')
