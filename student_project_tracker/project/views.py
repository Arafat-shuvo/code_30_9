from django.shortcuts import render

# Create your views here.
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout 
# Create your views here.
def login_view(request):

    if request.method == 'POST':

        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(
            request,
            username=username,
            password=password
        )

        if user is not None:
            login(request, user)
            return redirect('dashboard')

        else:
            return render(request, 'login.html', {
                'error': 'Invalid username or password'
            })

    return render(request, 'login.html')

def register(request):
    if request.method == 'POST':
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        confirm_password = request.POST['confirm_password']

        if password == confirm_password:
            user = User.objects.create_user(username=username, email=email, password=password)
            user.save()
            return redirect('login')
        else:
            return render(request, 'register.html', {'error': 'Passwords do not match.'})
    return render(request, 'register.html') 


def add_student(request):
    print('current user: ', request.user)
    if request.method == 'POST':
        name = request.POST.get('name')
        phone = request.POST.get('phone')
        dept = request.POST.get('dept')
        image = request.FILES.get('image')

    ProjectModel.objects.creates(

        name = name,
        phone = phone,
        dept = dept,
        image = image,
        created_by = request.user
        )

    return redirect('student_list')
    return render





def dashboard(request):
    return render(request, 'dashboard.html')
    
    