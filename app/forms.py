from django import forms

class QueryForm(forms.Form):
   CHOICES = (
      ("chinese", "Chinese"),
      ("mexican", "Mexican"),
   )
   cuisine = forms.ChoiceField(choices=CHOICES, widget=forms.Select(attrs={'class': 'form-control'})) 
   location = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'class': 'form-control'}))
   radius = forms.IntegerField(max_value=50000)
   price = forms.IntegerField(max_value=4)
   rating = forms.IntegerField(max_value=5)