#-*- coding:utf-8 -*-
from typing import Any
from .models import Offer
from django import forms

# Form create an offer
class TaskForm(forms.ModelForm):

    class Meta:
        model = Offer
        fields = ["title", "url", "description", "depart", "arrival", "depart_time", "available_at", "price", "feedback", "favourite", "status"]
    
    def clean(self) -> dict[str, Any]:
        return super().clean()


