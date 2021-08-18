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
        print(i)
        categories_str += categories[i]
        if i != len(categories) - 1:
            categories_str += ","

    # Converting radius from miles to meters for API
    radius = int(radius * 1609.34)

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

    # Filter out reponse by rating
    for i in range(len(response.get('businesses'))):
        print(response.get('businesses')[i].get('rating'))
        if response.get('businesses')[i].get('rating') < rating:  # TODO Why doesn't this line work. Some reason says index out of bounds
            response.get('businesses').pop(i)

    data = {'response': response}
    return render(request, 'app/data.html', data)


def dashboard(request):
    data = {}
    return render(request, 'app/dashboard.html', data)
