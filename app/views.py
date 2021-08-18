from django.shortcuts import render
from .forms import QueryForm
import requests
import random


def index(request):
    form = QueryForm()
    return render(request, 'app/index.html', {'form': form})

 
def data(request):
    if request.method == "POST":
        # Get the posted form
        MyQueryForm = QueryForm(request.POST)

        if MyQueryForm.is_valid():
            categories = MyQueryForm.cleaned_data['categories']
            location = MyQueryForm.cleaned_data['location']
            radius = MyQueryForm.cleaned_data['radius']
            price = MyQueryForm.cleaned_data['price']
            rating = MyQueryForm.cleaned_data['rating']
    else:
        MyQueryForm = QueryForm()
    
    # Format categories to be category1,category2
    categories_str = ""
    for i in range(len(categories)):
        categories_str += categories[i]
        if i != len(categories) - 1:
            categories_str += ","

    # Converting radius from miles to meters for API
    radius = int(radius * 1609.34)

    # Format price to be 1,2   

    # Get API key
    f = open("api_key.txt", "r")
    api_key = f.read()

    # Set endpoint and header
    endpoint = 'https://api.yelp.com/v3/businesses/search'
    header = {'Authorization': 'bearer %s' % api_key}

    # Get parameters for the search
    parameters = {
        'categories': categories_str,
        'location': location,
        'radius': radius,
        'price': price,
        #'open_now': True,
    }

    # Send a response to the API
    response = (requests.get(url=endpoint, params=parameters, headers=header)).json()
    businesses = []

    # Filter out reponse by rating and add valid businesses to new list
    for i in range(len(response.get('businesses'))):
        if response.get('businesses')[i].get('rating') >= rating:
            businesses.append(response.get('businesses')[i])
    response = {'businesses': businesses}

    print("response returned " + str(len(response.get('businesses'))))

    # Return a random restaurant
    randIndex = random.randint(0, len(response.get('businesses'))-1)
    restaurant = response.get('businesses')[randIndex]

    data = {'restaurant': restaurant}
    return render(request, 'app/data.html', data)

    

def dashboard(request):
    data = {}
    return render(request, 'app/dashboard.html', data)
