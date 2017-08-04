from django import forms

class User(forms.Form):
    username=forms.CharField(min_length=3,max_length=10)
    age=forms.IntegerField()
