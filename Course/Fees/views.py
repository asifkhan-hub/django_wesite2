from django.shortcuts import render,redirect
from django.contrib import messages
# from django.http import HttpResponse
from.models import Contact
def home(request):
    return render(request,'index.html')
def about(request):
    return render(request,'about.html')
def service(request):
    return render(request,'service.html')
def battery(request):
    return render(request,'battery.html')
def folder(request):
    return render(request,'folder.html')
def explore(request):
    return render(request,'explore.html')



def contact(request):
        if request.method == "POST":

            contact = Contact()
            name = request.POST.get('name')
            email = request.POST.get('email')
            message = request.POST.get('message')

            contact.name = name
            contact.email = email
            contact.message = message
            contact.save()
            # messages.add_message(request,messages.SUCCESS,'sent sucessfully !!')
            messages.success(request, ' message sent sucessfully')
        return render(request, 'contact.html')

# Create your views here.
