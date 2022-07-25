import requests
from settings import settings 
from math import radians, cos, sin, asin, sqrt

def getCoordinates(address):
    url = f"https://maps.googleapis.com/maps/api/geocode/json?address={address}&key={settings.GOOGLE_API_KEY}"
    # url = f"https://nominatim.openstreetmap.org/search?format=geojson&q={address}"
    resp = requests.post(url).json()
    return resp


def get_distance(lat1, lat2, lon1, lon2):
    lon1 = radians(lon1)
    lon2 = radians(lon2)
    lat1 = radians(lat1)
    lat2 = radians(lat2)
      
    # Haversine formula
    dlon = lon2 - lon1
    dlat = lat2 - lat1
    a = sin(dlat / 2)**2 + cos(lat1) * cos(lat2) * sin(dlon / 2)**2
 
    c = 2 * asin(sqrt(a))
    
    # Radius of earth in kilometers. Use 3956 for miles
    radius = 6371
      
    return (c * radius)