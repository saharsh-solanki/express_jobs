from django.contrib import messages
from django.http import JsonResponse
from django.shortcuts import render, redirect

# Create your views here.
from job_management.models import main_category, sub_category, sub_sub_category, Add_Job, Manager


def managerlogin(request):
    if 'manager_email' in request.session:
        messages.success(request, 'You Are Already Login ')
        return redirect('manager_dashboard')
    else:
        if request.method=="POST":
            email=request.POST['email']
            password=request.POST['password']
            if Manager.objects.filter(email=email,password=password).exists():
                request.session['manager_email']=email
                messages.success(request,'Login Successfull ! ')
                return redirect('manager_dashboard')
            else:
                messages.success(request, 'Invalid Details !!!')
                return render(request, "job_management/login.html")
        else:
            return render(request,'job_management/login.html')



#manager_dashboard Function
def main(request):
    if 'manager_email' in request.session:
       return render(request,"job_management/mainhome.html")
    else:
        messages.success(request,'You Need To Login !!!')
        return redirect('managerlogin')


def maincategory(request):
    if 'manager_email' in request.session:
        data=main_category.objects.all()
        return render(request,"job_management/maincategory.html",{"data":data})
    else:
        messages.success(request,'You Need To Login !!!')
        return redirect('managerlogin')


def subcategory(request):
    if 'manager_email' in request.session:
        data = main_category.objects.all()
        obj=sub_category.objects.all()
        return render(request,"job_management/subcategory.html",{"data":data,"obj":obj})
    else:
        messages.success(request,'You Need To Login !!!')
        return redirect('managerlogin')


def subsubcategory(request):
    if 'manager_email' in request.session:
        data = main_category.objects.all()
        dat = sub_category.objects.all()
        obj=sub_sub_category.objects.all()
        return render(request,"job_management/subsubcategory.html",{"data":data,"dat":dat,"obj":obj})
    else:
        messages.success(request,'You Need To Login !!!')
        return redirect('managerlogin')

def addjob(request):
    if 'manager_email' in request.session:
        data = main_category.objects.all()
        dat = sub_category.objects.all()
        da = sub_sub_category.objects.all()
        return render(request,"job_management/addjob.html",{"data":data,"dat":dat,"da":da})
    else:
        messages.success(request,'You Need To Login !!!')
        return redirect('managerlogin')


def doaddmaincategory(request):
    if 'manager_email' in request.session:
        if request.method=="POST":
            main_category_name=request.POST['main_category_name']
            data = main_category.objects.all()
            if main_category.objects.filter(main_category_name=main_category_name).exists():
                messages.success(request,'This Categery Is Already Available')
                return redirect('maincategory')
            else:
                o=main_category(main_category_name=main_category_name)
                o.save()
                messages.success(request, 'Added Successfully')
                return redirect('maincategory')
    else:
        messages.success(request, 'You Need To Login !!!')
        return redirect('managerlogin')



def doaddsubcategory(request):
    if 'manager_email' in request.session:
        if request.method == "POST":
            main_category_name = request.POST['main_category_name']
            sub_category_name = request.POST['sub_category_name']
            data = main_category.objects.all()
            obj = sub_category.objects.all()
            if sub_category.objects.filter(main_category_name=main_category_name,sub_category_name=sub_category_name).exists():
                messages.success(request, 'This Category Is Already Added !!!')
                return render(request, 'job_management/subcategory.html', {"msg": "Already Added", "data": data, "obj": obj})
            else:
                o = sub_category(main_category_name=main_category_name,sub_category_name=sub_category_name)
                o.save()
                messages.success(request, 'Added Successfully !!!')
                return render(request, 'job_management/subcategory.html', {"msg": "add success","data":data,"obj":obj})
    else:
        messages.success(request, 'You Need To Login !!!')
        return redirect('managerlogin')


def doaddsubsubcategory(request):
    if 'manager_email' in request.session:
        if request.method == "POST":
            main_category_name = request.POST['main_category_name']
            sub_category_name = request.POST['sub_category_name']
            sub_sub_category_name = request.POST['sub_sub_category_name']
            data = main_category.objects.all()
            dat=sub_category.objects.all()
            obj = sub_sub_category.objects.all()
            if sub_sub_category.objects.filter(main_category_name=main_category_name,sub_category_name=sub_category_name,sub_sub_category_name=sub_sub_category_name).exists():
                return render(request, 'job_management/subsubcategory.html',
                              {"msg": "Already Added", "data": data, "dat": dat, "obj": obj})
            else:
                o = sub_sub_category(main_category_name=main_category_name,sub_category_name=sub_category_name,sub_sub_category_name=sub_sub_category_name)
                o.save()
                messages.success(request, 'Added Successfully')
                return render(request, 'job_management/subsubcategory.html', {"msg": "add success","data":data,"dat":dat,"obj":obj})
    else:
        messages.success(request, 'You Need To Login !!!')
        return redirect('managerlogin')


def doaddjob(request):
    if 'manager_email' in request.session:
        if request.method=="POST":
            data = main_category.objects.all()
            dat = sub_category.objects.all()
            da = sub_sub_category.objects.all()
            main_category_name = request.POST['main_category_name']
            sub_category_name = request.POST['sub_category_name']
            sub_sub_category_name = request.POST['sub_sub_category_name']
            jobname=request.POST['jobname']
            startdate = request.POST['startdate']
            lastdate = request.POST['lastdate']
            offlinedate = request.POST['offlinedate']
            applylink= request.POST['applylink']
            official_notification_link = request.POST['official_notification_link']
            official_website_link = request.POST['official_website_link']
            obj=Add_Job(main_category_name=main_category_name,sub_category_name=sub_category_name,sub_sub_category_name=sub_sub_category_name,jobname=jobname,startdate=startdate,lastdate=lastdate,offlinedate=offlinedate,applylink=applylink,official_notification_link=official_notification_link,official_website_link=official_website_link)
            obj.save()
            messages.success(request, 'Job Added Succssfully')
            return redirect('addjob')
    else:
        messages.success(request, 'You Need To Login !!!')
        return redirect('managerlogin')

def viewjob(request):
    if 'manager_email' in request.session:
        data=Add_Job.objects.all()
        return render(request,'job_management/viewjob.html',{"data":data})
    else:
        messages.success(request, 'You Need To Login !!!')
        return redirect('managerlogin')



def delete(request):
    if 'manager_email' in request.session:
        id=request.GET.get('id')
        pi=Add_Job.objects.get(id=id)
        pi.delete()
        return JsonResponse({'status':'Delete'})
    else:
        messages.success(request, 'You Need To Login !!!')
        return redirect('managerlogin')


def updatejob(request,id):
    if 'manager_email' in request.session:
        dataa = main_category.objects.all()
        dat = sub_category.objects.all()
        da = sub_sub_category.objects.all()
        data=Add_Job.objects.get(id=id)
        return render(request,'job_management/updatejob.html',{"data":data,"dataa":dataa,"dat":dat,"da":da})
    else:
        messages.success(request, 'You Need To Login !!!')
        return redirect('managerlogin')


def doupdatejob(request,id):
    if 'manager_email' in request.session:
        data=Add_Job.objects.get(id=id)
        data.main_category_name=request.POST['main_category_name']
        data.sub_category_name = request.POST['sub_category_name']
        data.sub_sub_category_name = request.POST['sub_sub_category_name']
        data.jobname = request.POST['jobname']
        data.startdate = request.POST['startdate']
        data.lastdate = request.POST['lastdate']
        data.offlinedate = request.POST['offlinedate']
        data.applylink = request.POST['applylink']
        data.official_notification_link = request.POST['official_notification_link']
        data.official_website_link = request.POST['official_website_link']
        data.save()
        messages.success(request, 'Job Updated Successfully')
        return redirect(viewjob)
    else:
        messages.success(request, 'You Need To Login !!!')
        return redirect('managerlogin')




def deletemaincategory(request):
    if 'manager_email' in request.session:
        id = request.GET.get('id')
        pi = main_category.objects.get(id=id)
        pi.delete()
        return JsonResponse({'status': 'Delete'})
    else:
        messages.success(request, 'You Need To Login !!!')
        return redirect('managerlogin')




def deletesubcategory(request):
    if 'manager_email' in request.session:
        id = request.GET.get('id')
        pi = sub_category.objects.get(id=id)
        pi.delete()
        return JsonResponse({'status': 'Delete'})
    else:
        messages.success(request, 'You Need To Login !!!')
        return redirect('managerlogin')



def deletesubsubcategory(request):
    if 'manager_email' in request.session:
        id = request.GET.get('id')
        pi = sub_sub_category.objects.get(id=id)
        pi.delete()
        return JsonResponse({'status': 'Delete'})
    else:
        messages.success(request, 'You Need To Login !!!')
        return redirect('managerlogin')


def logout(request):
    request.session.flush()
    messages.success(request,'Logout !!')
    return redirect('managerlogin')
