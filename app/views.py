from django.shortcuts import render
from .forms import QueryForm
import requests


def index(request):
    form = QueryForm()
    return render(request, 'app/index.html', {'form': form})

 
def data(request):
    if request.method == "POST":
        # Get the posted form
        MyQueryForm = QueryForm(request.POST)

        if MyQueryForm.is_valid():
            cuisine = MyQueryForm.cleaned_data['cuisine']
            location = MyQueryForm.cleaned_data['location']
            radius = MyQueryForm.cleaned_data['radius']
            price = MyQueryForm.cleaned_data['price']
            rating = MyQueryForm.cleaned_data['rating']
    else:
        MyQueryForm = QueryForm()

    #Converting radius from miles to meters for API
    radius = radius * 1609.34

    print("cuisine is ", cuisine)
    print("radius is ", radius)

    #Get API key
    f = open("api_key.txt", "r")
    api_key = f.read()

    #Set endpoint and header
    endpoint = 'https://api.yelp.com/v3/businesses/search'
    header = {'Authorization': 'bearer %s' % api_key}

    #Get parameters for the search
    parameters = {
        'categories': cuisine,
        'location': location,
        'radius': radius,
        'price': price,
        #'open_now': True,
    }


    # Do something with rating



    #Send a response to the API
    response = requests.get(url=endpoint, params=parameters, headers=header)
    data = {'response': response.json()}
    return render(request, 'app/data.html', data)


def dashboard(request):
    data = {}
    return render(request, 'app/dashboard.html', data)
