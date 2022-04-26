from django.shortcuts import render,redirect
from .models import contactregister
from .forms import ContactregisterForm
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.contrib import messages

from .filters import ContactFilter


# Create your views here.
#--------------HOME PAGE-------------------------------------
def home(request):
    return render(request,'home.html')


def register(request):
    listall=contactregister.objects.all()
    contact_filter=ContactFilter(request.GET,queryset=listall)
    return render(request,'register.html',{'listall':listall,'filter':contact_filter})


#-----------------SAVE CONTACT NAME AND ADDRESS
def Addcontact(request):
        listall=contactregister.objects.all()
        contact_filter=ContactFilter(request.GET,queryset=listall)
        contactform=ContactregisterForm()
        content={'listall':listall,'form':contactform,'filter':contact_filter}
        if request.method=="POST":
            name=request.POST['cname']
            numb=request.POST['cnumber']
            check_status=contactregister.objects.filter(name=name).exists()
            if check_status:
                messages.info(request,"Alredy Exists")
                return render(request,"register.html",{'listall':listall,'filter':contact_filter})
            else:
                contact_list=contactregister.objects.create(name=name,contact_num=numb)
                contact_list.save()
                messages.info(request,"Contact Saved")
                return render(request,"register.html",content)
        else:
            return HttpResponse("Error")


#---------------DISPLAY TABLE--------------------------
def allcontacts(request):   
    try:
        contact_list=contactregister.objects.all()
        contact_filter=ContactFilter(request.GET,queryset=contact_list)
        return render(request,"display.html",{"contact":contact_list,'filter':contact_filter})
    except Exception as e:
        return HttpResponse("Error")


def view(request,id):
    select_id=contactregister.objects.get(id=id)
    return render(request,'update.html',{"contact":select_id})
   
def edit(request,id):
    select_id=contactregister.objects.get(id=id)
    return render(request,'update.html',{"contact":select_id})

def delete(request):
    if request.method=="POST":
        id=request.POST['delete_id']
        del_id=contactregister.objects.get(id=id)
        del_id.delete()
        return redirect('/Reg')
    else:
        return HttpResponse("Error")

def delete_view(request):
    if request.method=="POST":
        id=request.POST['delete_id']
        del_id=contactregister.objects.get(id=id)
        del_id.delete()
        return redirect('/View')
    else:
        return HttpResponse("Error")


# ---------------DISPLAY LINK PAGE-------------------
def index(request):
    listall=contactregister.objects.all()
    contactform=ContactregisterForm()
    content={'listall':listall,'form':contactform}
    




#---------------UPDATE NAME AND NUMBER-----------------
def update(request,id):
    select_id=contactregister.objects.get(id=id)
    if request.method=="POST":
        select_id.name=request.POST.get('cname') 
        select_id.contact_num=request.POST.get('cnumber')
        select_id.save()
        return redirect('/View')
        
    else:
       return HttpResponse("Error")  
    
        