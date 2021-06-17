from django.db.models import fields
from djangoTest.models import order
from django import forms

class orderForm(forms.ModelForm):
    class Meta:
        model = order
        fields = '__all__'
