from django import forms

class QueryForm(forms.Form):
   CAT_CHOICES = (
      ("chinese", "Chinese"),
      ("mexican", "Mexican"),
      ("tradamerican", "American"),
      ("breakfast_brunch", "Breakfast/Brunch"),
      ("caribbean", "Caribbean"),
      ("halal", "Halal"),
      ("indpak", "Indian"),
      ("italian", "Italian"),
   )
   PRICE_CHOICES = (
      (1, "$"),
      (2, "$$"),
      (3, "$$$"),
      (4, "$$$$"),
   )
   categories = forms.MultipleChoiceField(label="Cuisine", choices=CAT_CHOICES, widget=forms.CheckboxSelectMultiple(attrs={'class': 'form-control'}))
   location = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'class': 'form-control'}))
   radius = forms.IntegerField(label="Radius (Miles)", max_value=25)
   price = forms.MultipleChoiceField(choices=PRICE_CHOICES, widget=forms.CheckboxSelectMultiple(attrs={'class': 'form-control'}))
   rating = forms.FloatField(max_value=5)

