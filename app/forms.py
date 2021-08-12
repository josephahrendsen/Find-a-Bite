from django import forms

class LoginForm(forms.Form):
   cusine = forms.CharField(max_length = 100)
   distance = forms.IntegerField(max_value=25)
   price = forms.IntegerField(max_value=250)
   rating = forms.IntegerField(max_value=5)