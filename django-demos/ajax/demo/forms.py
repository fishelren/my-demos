from django import forms

class StudentForm(forms.Form):
    username=forms.CharField(widget=forms.TextInput(attrs={'id':'id_username'}),max_length=30)
    age=forms.IntegerField(widget=forms.NumberInput(attrs={'id':'id_age'}),min_value=0,max_value=120)
