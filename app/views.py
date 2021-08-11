from django.shortcuts import render
import requests

f = open("api_key.txt", "r")
api_key = f.read()

# Create your views here.
def index(request):
    headers = {'Authorization': 'bearer ' + api_key}
    response = requests.get('https://api.yelp.com/v3/businesses/good-food-on-montford-charlotte-2', headers=headers)
    data = {'response': response.json()}
    return render(request, 'app/index.html', data)

def dashboard(request):
    data = {}
    return render(request, 'app/dashboard.html', data)

