from django.shortcuts import render, redirect
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from manager_app.forms import UserForm

from manager_app.models import User, CustomUserManager, Department

def index(request):
    departments = Department.objects.all()

    for department in departments:
        department.users = User.objects.filter(department = department).order_by('username')

    context = {
        'departments' : departments
    }

    return render(request, "index.html", context)

def create_user(request):
    if request.method == 'POST':
        form = UserForm(request.POST, user = request.user)

        if form.is_valid():
            username = form.cleaned_data['username']
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']
            department = form.cleaned_data['department']
            name = form.cleaned_data['name']
            role = form.cleaned_data['role']
            identification = form.cleaned_data['identification']

            user = User.objects.create_user(username = username, email = email, password = password, department = department, name = name, role = role, identification = identification)

            return redirect("index")

    else:
        form = UserForm(user = request.user)

    context = {
        'form': form
    }

    return render(request, 'create_user.html', context)