from django import forms

from .models import *

class News11Form(forms.ModelForm):

    class Meta:
        model = News11
        fields = ['Artical_datetime', 'Artical_name', 'Artical_author','Artical_image','Artical_image_name', 'Artical_here','Artical_video']



class userform(forms.ModelForm):
    username = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Enter username'}),required=True,max_length=50)
    email = forms.CharField(widget=forms.EmailInput(attrs={'class':'form-control','placeholder':'Enter Email Id'}),required=True,max_length=50)
    first_name = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Enter first name'}),required=True,max_length=50)
    last_name = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Enter last name'}),required=True,max_length=50)
    password = forms.CharField(widget=forms.PasswordInput(attrs={'class':'form-control','placeholder':'Enter password'}),required=True,max_length=50)
    confirm_password = forms.CharField(widget=forms.PasswordInput(attrs={'class':'form-control','placeholder':'Enter password'}),required=True,max_length=50)

    class Meta():
        model = User
        field = ['username','email','first_name','last_name','password']
