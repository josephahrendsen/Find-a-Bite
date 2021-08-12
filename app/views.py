from django.shortcuts import render
from app.forms import LoginForm
import requests

f = open("api_key.txt", "r")
api_key = f.read()


def index(request):
    data = {}
    return render(request, 'app/index.html', data)


def index_post(request):
    if request.method == "POST":
        # Get the posted form
        MyLoginForm = LoginForm(request.POST)

        if MyLoginForm.is_valid():
            cuisine = MyLoginForm.cleaned_data['username']
            distance = MyLoginForm.cleaned_data['distance']
            price = MyLoginForm.cleaned_data['price']
            rating = MyLoginForm.cleaned_data['rating']
    else:
        MyLoginForm = LoginForm()

    headers = {'Authorization': 'bearer ' + api_key}
    query = 0

    response = requests.get(
        query, headers=headers
    )
    data = {'response': response.json()}
    return render(request, 'app/index.html', data)


def dashboard(request):
    data = {}
    return render(request, 'app/dashboard.html', data)
