from django.shortcuts import render, redirect
from .models import *
# Create your views here.


def InsertPageView(request):
    return render(request,"insert.html")


def Inserdata(request):
    # Data Come From HTML to View
    fname = request.POST['fname']
    lname = request.POST['lname']
    email = request.POST['email']
    contact = request.POST['contact']
    # Creating Object of Model Class
    newuser = student.objects.create(Firstname = fname, Lastname = lname, Email = email, Contact = contact)
    # After insert render on Showpage View
    return redirect("showpage")

# Show Page View
def ShowPage(request):
    # select * from tablename
    # For fetching all the data of the table
    all_data = student.objects.all()
    return render (request, "show.html", {"key1":all_data})


def EditPage(request,pk):
    # fetching the data of perticular id
    get_data = student.objects.get(id=pk)
    return render(request,"edit.html", {"key2":get_data})

# Update Data view
def UpdateData(request,pk):
    udata = student.objects.get(id=pk)
    udata.Firstname = request.POST['fname']
    udata.Lastname = request.POST['lname']
    udata.Email = request.POST['email']
    udata.Contact = request.POST['contact']
    # Query for Update
    udata.save()
    # render to show page
    return redirect("showpage")


def DeleteData(request,pk):
    ddata = student.objects.get(id=pk)
    # query for delete
    ddata.delete()
    return redirect("showpage")
    