from speak import speak
from geopy.distance import great_circle
import geocoder # pip install geocoder geopy
from geopy.geocoders import Nominatim
from geopy import distance
import socket,webbrowser

class Maps_utilizer:
    def mapping(self,querry):
        match querry:
            case "show maps":Open_Maps()
            case 'tell me my location':tell_Me_The_Location()
            case _ if "calculate the travel time to reach " in querry or  "what will be the time taken to reach" in querry:calculate_travel_time(querry)
            case _ if "what is the distance between":get_the_distance("delhi",querry)
                
def Open_Maps():
    import random as rd
    url = 'https://www.google.com/maps/place/21%2F70,+Block+21,+Lodi+Colony,+New+Delhi,+Delhi+110003/@28.5873577,77.2174837,17z/data=!3m1!4b1!4m5!3m4!1s0x390ce3e480afec89:0xb6c73da40b857eb7!8m2!3d28.587353!4d77.2196724'
    speak(rd.choice(['showing your location','your are looking at your location','OK, plaese waite I am opening your loction on map']))
    webbrowser.open(url)

#! To get the location based on your current ip address and returning city name and country       
def tell_Me_The_Location():
    speak('This may take a moment.')
    hostname = socket.gethostname()
    local_ip = socket.gethostbyname(hostname)
    # Geolocate the IP address
    location = geocoder.ip("me")
    if location.ok:
        city = location.city
        country = location.country
        latlng = location.latlng
        speak(f"Your local IP address is {local_ip}. Based on this, you are in {city}, {country}.")
        speak(f"Your approximate coordinates are {latlng[0]}, {latlng[1]}.")
        return latlng
    else:speak("Sorry, I couldn't retrieve the location based on your IP address.")
        
def get_the_distance(city, querry):
    try:
        place = querry.replace("what is the distance between"," ").strip()
        geolocator = Nominatim(user_agent="i know python programming")
        mylocation = input("city:- ")
        cur = geolocator.geocode(mylocation)
        cur_latlon = (cur.latitude,cur.longitude) 
        print(cur_latlon)
        # Geolocator to get coordinates of the specific place within the city
        full_place = f"{place}, {city}"  # Concatenating the specific place with the city name
        target_location = geolocator.geocode(full_place)
        if target_location:
            target_latlon = (target_location.latitude, target_location.longitude)
            print(target_latlon)
            # Calculate the distance
            dist = distance.distance(cur_latlon,target_latlon)
            speak(f"The distance from your location to {place} in {city} is approximately {dist}.")
        else:speak(f"Sorry, I couldn't find the location of {place} in {city}.")
    except Exception as e:speak(f"An error occurred: {e}")
      
def calculate_travel_time(querry, average_speed_kmph=46):
    destination = querry.replace("calculate the travell time to reach "," ").replace("what will be the time taken to reach  ","").strip()
    geolocator = Nominatim(user_agent='i know python')
    target_location = geolocator.geocode(destination)
    if target_location is None:
        print("Destination not found. Please provide a more specific location.")
        return None
    target_latlon = (target_location.latitude, target_location.longitude)
    print(target_latlon)
    current_location = geocoder.ip('me')
    if current_location.latlng is None:
        print("Could not determine current location. Please check your internet connection.")
        return None
    current_latlon = current_location.latlng
    distance = great_circle(current_latlon, target_latlon).kilometers
    travel_time_hours = distance / average_speed_kmph
    travel_time_minutes = travel_time_hours * 60
    hours = int(travel_time_hours)
    minutes = round(travel_time_minutes % 60)
    speak(f"Estimated travel time to {destination} is approximately {hours} hours and {minutes} minutes at an average speed of {average_speed_kmph} km/h.")
    return hours, minutes