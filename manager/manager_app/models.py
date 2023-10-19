from django.db import models
from django.contrib.auth.models import UserManager, PermissionsMixin, AbstractBaseUser
from django.db.models.base import Model

from django.utils import timezone

def user_directory_path(instance, filename):
    return 'user_{0}/{1}'.format(instance.user.id, filename)

class CustomUserManager(UserManager):
    def _create_user(self, username, email, password, **extra_fields):

        if not username:
            raise ValueError("No valid username provided.");

        email = self.normalize_email(email)

        user = self.model(username = username, **extra_fields)
        user.set_password(password)
        user.save(using = self._db)

        return user;

    def create_user(self, username = None, email = None, password = None, **extra_fields):
        extra_fields.setdefault('is_staff', False)
        extra_fields.setdefault('is_superuser', False)

        return self._create_user(username, email, password, **extra_fields)

    def create_superuser(self, username = None, email = None, password = None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)

        return self._create_user(username, email, password, **extra_fields)

class User(AbstractBaseUser, PermissionsMixin):
    username = models.CharField(max_length = 32, blank = True, default = '', unique = True)
    email = models.EmailField(blank = True, default = '', unique = True) 

    is_active = models.BooleanField(default = True)
    is_staff = models.BooleanField(default = False)
    is_superuser = models.BooleanField(default = False)

    date_joined = models.DateTimeField(default = timezone.now)
    last_login = models.DateTimeField(blank = True, null = True)

    #one to many relationship with department
    department = models.ForeignKey(Department, on_delete=models.SET_NULL)

    objects = CustomUserManager()

    USERNAME_FIELD = 'username'
    EMAIL_FIELD = 'email'
    REQUIRED_FIELDS = []

    class Meta:
        verbose_name = 'User'
        verbose_name_plural = 'Users'

    class Department(models.Model):
        deptID = models.IntegerField(primary_key=True)
        deptName = models.CharField(max_length=100)

    #relationship of an employee belonging to a department (one to many)


