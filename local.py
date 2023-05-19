from geopy.geocoders import Nominatim

geolocator = Nominatim(user_agent="FPM_DNU")

def getto(addres: str):
    location = geolocator.geocode(addres)

    return f'{location.latitude} {location.longitude}'
