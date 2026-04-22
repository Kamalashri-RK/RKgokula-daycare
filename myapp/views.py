from django.shortcuts import render, redirect
from django.contrib import messages
from .models import AdmissionEnquiry
from django.core.paginator import Paginator
from django.db.models import Q
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required


def home_page(request):

    if request.method == "POST":

        child_name = request.POST.get('child_name')
        parent_name = request.POST.get('parent_name')
        phone = request.POST.get('phone')
        dob = request.POST.get('dob')
        city = request.POST.get('city')
        age_group = request.POST.get('age_group')
        message = request.POST.get('message')

        data = AdmissionEnquiry(
            child_name=child_name,
            parent_name=parent_name,
            phone=phone,
            dob=dob,
            city=city,
            age_group=age_group,
            message=message
        )

        data.save()

        messages.success(request, "Thank you for contacting Radha Krishna Gokula")

        return redirect("/")

    return render(request,"homepage.html")



def about_page(request):
    return render(request, "about.html")


def program_page(request):
    return render(request, "program.html")


def curriculum_page(request):
    return render(request, "curriculum.html")


def gallery_page(request):
    return render(request, "gallery.html")

def contact_page(request):
    return render(request,"contact.html")

@login_required
def dashboard(request):

    search = request.GET.get('search')

    enquiries = AdmissionEnquiry.objects.all().order_by('-created_at')

    if search:
        enquiries = enquiries.filter(
            Q(parent_name__icontains=search) |
            Q(child_name__icontains=search)
        )

    paginator = Paginator(enquiries, 5)  # 5 rows per page

    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    return render(request,"dashboard.html",{
        "page_obj":page_obj,
        "search":search
    })
def mark_contacted(request,id):

    data = AdmissionEnquiry.objects.get(id=id)
    data.status = "Contacted"
    data.save()

    return redirect("/dashboard")

def delete_enquiry(request,id):

    data = AdmissionEnquiry.objects.get(id=id)
    data.delete()

    return redirect("/dashboard")

def edit_enquiry(request,id):

    data = AdmissionEnquiry.objects.get(id=id)

    if request.method == "POST":

        data.parent_name = request.POST.get('parent_name')
        data.phone = request.POST.get('phone')
        data.child_name = request.POST.get('child_name')
        data.city = request.POST.get('city')
        data.age_group = request.POST.get('age_group')
        data.message = request.POST.get('message')

        data.save()

        return redirect("/dashboard")

    return render(request,"edit.html",{"data":data})

    

def login_view(request):

    if request.method == "POST":

        username = request.POST.get("username")
        password = request.POST.get("password")

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect("/dashboard")
        else:
            messages.error(request,"Invalid username or password")

    return render(request,"login.html")

from django.contrib.auth import logout

def logout_view(request):
    logout(request)
    return redirect("/login")