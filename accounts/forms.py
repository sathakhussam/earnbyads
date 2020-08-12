from django import forms
from . import models
from django.contrib.auth import login, logout, authenticate

class SignupForm(forms.ModelForm):
    password1 = forms.CharField(label='Password', widget=forms.PasswordInput(attrs={'placeholder':'Password'}))
    password2 = forms.CharField(label='Password confirmation', widget=forms.PasswordInput(attrs={'placeholder':'Confirm Password'}))

    class Meta:
        model = models.MyUser
        fields = ('email', 'name')
        widgets = {
            'email': forms.EmailInput(attrs={'placeholder': 'Email'}),
            'name': forms.TextInput(attrs={'placeholder': 'Name'}),
        }
    def clean_password2(self):
        # Check that the two password entries match
        password1 = self.cleaned_data.get("password1")
        password2 = self.cleaned_data.get("password2")
        if password1 and password2 and password1 != password2:
            raise forms.ValidationError("Passwords don't match")
        return password2

    def save(self, commit=True):
        # Save the provided password in hashed format
        user = super().save(commit=False)
        user.set_password(self.cleaned_data["password1"])
        if commit:
            user.save()
        return user

class LoginForm(forms.Form):
    email = forms.EmailField(label='email', widget=forms.EmailInput(attrs={'placeholder':'Email'}))
    password = forms.CharField(label='Password', widget=forms.PasswordInput(attrs={'placeholder':'Password'}))
    def login_acc(self,request):
        user = authenticate(email=self.cleaned_data.get("email"),password=self.cleaned_data.get("password"))
        if user is not None:
            login(request,user)
            return True
        else:
            return False
        