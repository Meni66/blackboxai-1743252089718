from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import User, Report

class RegistrationForm(UserCreationForm):
    email = forms.EmailField(required=True)
    phone = forms.CharField(max_length=15, required=True)
    address = forms.CharField(widget=forms.Textarea(attrs={'rows': 3}), required=True)

    class Meta:
        model = User
        fields = ('username', 'email', 'phone', 'address', 'password1', 'password2')

class ReportForm(forms.ModelForm):
    class Meta:
        model = Report
        fields = ['waste_type', 'quantity', 'description', 'collection_point', 'image']
        widgets = {
            'description': forms.Textarea(attrs={'rows': 3, 'class': 'form-textarea'}),
            'collection_point': forms.Select(attrs={'class': 'form-select'}),
        }
