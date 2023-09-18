from django import forms
from .models import *

class FormaSok(forms.Form):
    all = Company.objects.all()
    mas=[]
    for a in all:
        mas.append((a.id,a.title))
    print(mas)
    #firma = forms.ModelChoiceField(all,)
    #firma=forms.ChoiceField(choices=tuple(mas),required=False)
    firma=forms.ModelChoiceField(Company.objects.all(),required=False)
    sok=forms.ModelChoiceField(Product.objects.all(),required=False)
    #((1,'one'),(2,'two'),(3,'tri'))

class FormaUser(forms.Form):
    user = forms.ModelChoiceField(User.objects.all())