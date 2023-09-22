from django.shortcuts import render,HttpResponseRedirect
from django.http import HttpResponse
from .forms import StudentReg
from .models import User

# Create your views here.

#(1)HOME PAGE
def say_hello(request):
    return render(request, 'home.html')

#(2)GET and POST Data
def add_show(request):
    stud = User.objects.all()
    if request.method == 'POST':
        fm = StudentReg(request.POST)
        if fm.is_valid():
            nm=fm.cleaned_data['name']                  #THIS
            em=fm.cleaned_data['email']                 #IS 
            pw=fm.cleaned_data['password']              #PART OF
            #reg = User(name=nm, email=em, password=pw)  #SECOND
            # Check if the data already exists in the database
            existing_user = User.objects.filter(name=nm, email=em, password=pw).first()
            if not existing_user:
                reg = User(name=nm, email=em, password=pw)
                reg.save()
            
            # Always provide an empty form after processing POST data
            fm = StudentReg() 
            #reg.save()                                  #METHOD
            #fm = StudentReg() 
            #fm.save()
    else:
        fm = StudentReg()
    return render(request, 'add_&_show.html', {'form':fm,'stu':stud}) 

#(3)DELETE Data
def del_data(request, id):    #We can delete through GET but we will make a form and then use POST to Del 
    if request.method == 'POST':
        pi = User.objects.get(pk=id) #pk-primary key
        pi.delete()
        return HttpResponseRedirect('/')  #Home Page


#(4)UPDATE DATA
def upd_data(request,id):
    if request.method == 'POST':
        pi = User.objects.get(pk=id) #pk-primary key
        fm = StudentReg(request.POST, instance=pi)
        if fm.is_valid():
            fm.save()
    else:
        pi = User.objects.get(pk=id) #pk-primary key
        fm = StudentReg( instance=pi)

    return render(request, 'update_data.html', {'form':fm})


#(5) VIEW DATABASE
def view_db(request):
    stud = User.objects.all()
    return render(request, 'database.html',{'stu':stud})
    



             
