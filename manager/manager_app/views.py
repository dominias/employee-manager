from django.shortcuts import render
from django.contrib.auth.decorators import login_required

from manager_app.models import User, CustomUserManager

def index(request):
    return render(request, "index.html")