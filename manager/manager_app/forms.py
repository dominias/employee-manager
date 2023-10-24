from django import forms
from manager_app.models import Department

class UserForm(forms.Form):
    username = forms.CharField(max_length = 32)
    email = forms.EmailField(required = True) 
    password = forms.CharField(widget = forms.PasswordInput())
    department = forms.ModelChoiceField(queryset = Department.objects.none())
    name = forms.CharField(max_length = 32)
    role = forms.CharField(max_length = 32)
    identification = forms.IntegerField()

    def __init__(self, *args, **kwargs):
        user = kwargs.pop('user', None)

        super(UserForm, self).__init__(*args, **kwargs)

        if user:
            if user.is_superuser:
                self.fields['department'].queryset = Department.objects.all()
            elif user.is_staff:
                self.fields['department'].queryset = Department.objects.filter(department_id = user.department_id)
