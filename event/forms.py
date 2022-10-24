from django.contrib.auth import get_user_model
from django import forms
from .models import Event

User = get_user_model()

class Registration(forms.ModelForm):
    class Meta:
        model = User
        fields = ["username", "password", "first_name", "last_name", "email","is_staff"]

        widgets = {
            "password": forms.PasswordInput(),
        }


class UserLogin(forms.Form):
    username = forms.CharField(required=True)
    password = forms.CharField(required=True, widget=forms.PasswordInput())



class EventForm(forms.ModelForm):
    class Meta:
        model = Event
        fields = ["title", "image", "number_of_seats","date_of_event"]
