# -*- coding: utf-8 -*-
"""
Created on Fri Jun 27 02:10:29 2025

@author: ESDYOL
"""

from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from sdr_app.models import Client,Table,reservation,Plat,Menu

class ClientForm(forms.ModelForm):
    username = forms.CharField(max_length=50,label="Nom utilisateur")
    password = forms.CharField(widget=forms.PasswordInput,label="Mot de passe")
    email = forms.EmailField(label="Email")
    
    class Meta:
        model = Client
        fields='__all__'
        exclude =('user','role',)
        
    def save (self,commit = True):
        user = User.objects.create_user(
            username=self.cleaned_data["username"],
            email=self.cleaned_data["email"],
            password=self.cleaned_data["password"]
            )
        client = super().save(commit=False)
        client.user = user
        client.role = 'client'
        if commit :
            client.save()
        return client
        
class TableForm(forms.ModelForm):
    class Meta:
        model = Table
        fields='__all__'
        
class PlatForm(forms.ModelForm):
    class Meta:
        model = Plat
        fields='__all__'
        
class MenuForm(forms.ModelForm):
    class Meta:
        model = Menu
        fields='__all__'


class ReservationForm(forms.ModelForm):
    class Meta:
        model = reservation
        fields='__all__'
        exclude = ('create_at','client','table',)
        widgets = {
            "date":forms.DateInput(attrs={"type":"date","classe":"form-control"}),
            "heure":forms.TimeInput(attrs={"type":"time","classe":"form-control"}),
            "nombre_personne":forms.NumberInput(attrs={"classe":"form-control","placeholder":"nombre de personnes"}),
            }
        
class UserForm(UserCreationForm):
    class Meta :
        model = User
        fields = [
            'username',
            'email',
            'first_name',
            'last_name',
            'password1',
            'password2',
            ]
