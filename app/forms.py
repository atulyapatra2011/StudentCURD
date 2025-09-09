from django import forms
from .models import Student

class StudentForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = "__all__"

    # widgets = {
    #     'first_name': forms.TextInput(attrs={'placeholder': 'First Name'}),
    #     'last_name': forms.TextInput(attrs={'placeholder': 'Last Name'}),
    #     'email': forms.EmailInput(attrs={'placeholder': 'Email'}),
    #     'date_of_birth': forms.DateInput(attrs={'type': 'date'}),
    #     'phone_number': forms.TextInput(attrs={'placeholder': 'Phone Number'}),
    #     'address': forms.Textarea(attrs={'placeholder': 'Address', 'rows': 3}),
    #     'course': forms.TextInput(attrs={'placeholder': 'Course'}),
    #     'profile_picture': forms.ClearableFileInput()
        
    # }