from django.contrib.auth import authenticate, login
from django.shortcuts import redirect, render

from .models import ProjectModel, UserModel


def home(request):
    return render(request, 'home.html')


def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('dashboard')

        return render(request, 'login.html', {'error': 'Invalid username or password'})

    return render(request, 'login.html')


def register(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')
        confirm_password = request.POST.get('confirm_password')
        student_name = request.POST.get('student_name')
        student_id = request.POST.get('student_id')

        if password == confirm_password:
            UserModel.objects.create_user(
                username=username,
                email=email,
                password=password,
                student_name=student_name,
                student_id=student_id,
            )
            return redirect('login')

        return render(request, 'register.html', {'error': 'Passwords do not match.'})

    return render(request, 'register.html')


def add_student(request):
    if request.method == 'POST':
        project_name = request.POST.get('project_name')
        project_description = request.POST.get('project_description')
        project_status = request.POST.get('project_status')
        project_image = request.FILES.get('project_image')

        ProjectModel.objects.create(
            project_name=project_name,
            project_description=project_description,
            project_status=project_status,
            project_image=project_image,
            created_by=request.user,
        )

        return redirect('dashboard')

    return render(request, 'home.html')


def dashboard(request):
    return render(request, 'dashboard.html')

    