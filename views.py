from django.shortcuts import render
from django.contrib import messages
import requests
import datetime

def home(request):
    city = request.POST.get('city', 'Victoria Falls') # Default to Victoria Falls
    image_url = "https://images.unsplash.com/photo-1506744038136-46273834b3fb?auto=format&fit=crop&w=1600&q=80"
    
    # API setup
    url = f'https://api.openweathermap.org/data/2.5/weather?q={city}&appid=5c0f46460ea8715649659215e98cb76d'
    params = {'units': 'metric'}

    try:
        response = requests.get(url, params=params)
        data = response.json()

        if data.get("cod") != 200:
            raise Exception("City not found")

        # Extracting data
        description = data['weather'][0]['description']
        icon = data['weather'][0]['icon']
        temp = data['main']['temp']
        
        # FIX: Added these two lines to get humidity and wind
        humidity = data['main']['humidity']
        wind_speed = data['wind']['speed']
        
        day = datetime.date.today()

        return render(request, 'weatherapp/index.html', {
            'description': description,
            'icon': icon,
            'temp': temp,
            'humidity': humidity,      # Pass to template
            'wind_speed': wind_speed,  # Pass to template
            'day': day,
            'city': city,
            'exception_occured': False,
            'image_url': image_url
        })

    except Exception as e:
        day = datetime.date.today()
        return render(request, 'weatherapp/index.html', {
            'description': 'Clear Sky',
            'icon': '01d',
            'temp': '--',
            'humidity': '--',
            'wind_speed': '--',
            'day': day,
            'city': city,
            'exception_occured': True,
            'image_url': image_url
        })