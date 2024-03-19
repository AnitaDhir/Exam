from django.shortcuts import render,redirect

# Create your views here.
def home(request):
    return render(request, 'core/home.html')

# def index(request):
#     return render(request,'index.html')

# def registration(request):
#     if request.method == "POST":
#         user_form=RegistrationForm(request.POST)
#         if user_form.is_valid():
#             user_form.save()
#             return HttpResponse ("<h1>Registration Sucessfully</h1>")
#     else:
#         user_form=RegistrationForm()
#     return render(request,'registration.html',{'user_form':user_form})
from .models import User

def register(request):
    if request.method=='POST':
        User.objects.create(
            name=request.POST['name'],
            email=request.POST['email'],
            password=request.POST['password']
        )
    return render(request,'register.html')

def login(request):
    if request.method=='POST':
        user_data=User.objects.get(email=request.POST['email'])
        if (request.POST['password'],user_data.password):
            return redirect(home)

    return render(request,'core/login.html')

def contact(request):
    if request.method=='POST':
        User.objects.create(
            name=request.POST['name'],
            email=request.POST['email'],
            password=request.POST['password']
        )
    return render(request,'core/contact.html')