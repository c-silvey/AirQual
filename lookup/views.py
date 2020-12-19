from django.shortcuts import render

def home(request):
    import json
    import requests

    api_request = requests.get("https://www.airnowapi.org/aq/observation/zipCode/current/?format=application/json&zipCode=93401&distance=25&API_KEY=0F165C58-600F-450D-91F7-90B66B9B8B46")
    
    try:
        api = json.loads(api_request.content)
    
    except Exception as e:
        api = "Error..."

    return render(request, 'home.html', {'api':api})

def about(request):
    return render(request, 'about.html', {})