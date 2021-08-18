from django import forms

class QueryForm(forms.Form):
   CHOICES = (
      ("chinese", "Chinese"),
      ("mexican", "Mexican"),
      ("tradamerican", "American"),
      ("breakfast_brunch", "Breakfast/Brunch"),
      ("caribbean", "Caribbean"),
      ("halal", "Halal"),
      ("indpak", "Indian"),
      ("italian", "Italian"),

   )
   categories = forms.MultipleChoiceField(label="Cuisine", choices=CHOICES, widget=forms.CheckboxSelectMultiple(attrs={'class': 'form-control'}))
   location = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'class': 'form-control'}))
   radius = forms.IntegerField(label="Radius (Miles)", max_value=25)
   price = forms.IntegerField(max_value=4)
   rating = forms.FloatField(max_value=5)

