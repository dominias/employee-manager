from django.shortcuts import render
from django.contrib.auth.decorators import login_required

from manager_app.models import User, CustomUserManager, Department

def index(request):
    departments = Department.objects.all()

    for department in departments:
        department.users = User.objects.filter(department = department).order_by('username')

    context = {
        'departments' : departments
    }

    return render(request, "index.html", context)
