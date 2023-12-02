#-*- coding:utf-8 -*-
from .models import Offer
from django import forms

# Form create an offer
class TaskForm(forms.ModelForm):

    class Meta:
        model = Offer
        fields = '__all__'


