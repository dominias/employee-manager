from django.db import models
from django.contrib.auth.models import UserManager, PermissionsMixin, AbstractBaseUser
from django.db.models.base import Model
from django.shortcuts import get_object_or_404

from django.utils import timezone

def user_directory_path(instance, filename):
    return 'user_{0}/{1}'.format(instance.user.id, filename)

# Relationship of an employee belonging to a department (one to many)
class Department(models.Model):
    department_id = models.IntegerField(primary_key = True)
    department_name = models.CharField(max_length = 100)
    department_description = models.CharField(max_length = 200)

    def __str__(self):
        return self.department_name;

    class Meta:
        verbose_name = "Department"
        verbose_name_plural = "Departments"

class CustomUserManager(UserManager):
    def _create_user(self, username, email, password, name, role, identification, **extra_fields):

        if not username:
            raise ValueError("No valid username provided.");

        email = self.normalize_email(email)

        user = self.model(username = username, email = email, name = name, identification = identification, role = role, **extra_fields)
        user.set_password(password)
        user.save(using = self._db)

        return user;

    def create_user(self, username = None, email = None, password = None, name = None, role = None, identification = None, **extra_fields):
        extra_fields.setdefault('is_staff', False)
        extra_fields.setdefault('is_superuser', False)

        return self._create_user(username, email, password, name, role, identification, **extra_fields)

    def create_superuser(self, username = None, email = None, password = None, name = None, role = None, identification = None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)

        return self._create_user(username, email, password, name, role, identification, **extra_fields)

class User(AbstractBaseUser, PermissionsMixin):
    username = models.CharField(max_length = 32, blank = True, default = '', unique = True)
    email = models.EmailField(blank = True, default = '', unique = True) 
    name = models.CharField(max_length = 32)
    role = models.CharField(max_length = 32)
    identification = models.IntegerField()
    
    is_active = models.BooleanField(default = True)
    is_staff = models.BooleanField(default = False)
    is_superuser = models.BooleanField(default = False)

    date_joined = models.DateTimeField(default = timezone.now)
    last_login = models.DateTimeField(blank = True, null = True)

    # One to many relationship with department
    department = models.ForeignKey(Department, on_delete = models.SET_NULL, null = True)

    objects = CustomUserManager()

    USERNAME_FIELD = 'username'
    EMAIL_FIELD = 'email'
    REQUIRED_FIELDS = []

    class Meta:
        verbose_name = 'User'
        verbose_name_plural = 'Users'

class Stream(models.Model):
    user = models.ForeignKey(User, on_delete = models.CASCADE, related_name = "stream_user")
    department = models.ForeignKey(Department, on_delete = models.CASCADE, null = True)

    def add_department(sender, instance, *args, **kwargs):
        
        if user.is_superuser:
            departments = Departments.objects.all()

            for d in departments:

                u, created = User.objects.get_or_create(username = user.username, email = user.email, department = d)

                stream = Stream(user = user, department = d)
                stream.save()

                stream = Stream(user = u, department = d)
                stream.save()

        else:

            if department:
                stream = Stream(user = user, department = department)
                stream.save()

                users = Users.objects.filter(department = department)

                for u in users:
                    stream = Stream(user = u, department = department)
                    stream.save()



