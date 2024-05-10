from django import  forms
from app.models import Signup


class SignUpForm(forms.ModelForm):
    class Meta:
        model=Signup
        fields = ['email']