from django.forms import ModelForm
from .models import Students

class StudentForm(ModelForm):
    class Meta:
        model = Students
        fields = '__all__'



class StudentUpdateForm(ModelForm):
    class Meta:
        model = Students
        fields = ['name', 'email', 'city']