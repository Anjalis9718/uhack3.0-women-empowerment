from django import forms
from django.contrib.auth.models import User
from basic_app.models import UserProfileInfo,rate_organisation

class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())

    class Meta():
        model = User
        fields = ('username','email','password')


class UserProfileInfoForm(forms.ModelForm):
    class Meta():
        model = UserProfileInfo
        fields = ('profile_pic',)

class SkillsForm(forms.ModelForm):
    class Meta():
        model = UserProfileInfo
        fields = ('Area_of_Interests',)

class RateForm(forms.ModelForm):
    class Meta():
        model = rate_organisation
        fields = ('Username','Organization_name','Problem_faced','Suggestion',)
