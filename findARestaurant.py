from geocode import getGeocodeLocation
import json
import httplib2
import requests
import sys
import codecs

#sys.stdout = codecs.getwriter('utf8')(sys.stdout)
#sys.stderr = codecs.getwriter('utf8')(sys.stderr)

def get_secrets():
    with open('../secrets.json') as secrets_file:
        secrets = json.load(secrets_file)

    return secrets

secrets = get_secrets()

foursquare_client_id = secrets.get("foursquare_client_id")
foursquare_client_secret = secrets.get("foursquare_client_secret")
foursquare_version = secrets.get("foursquare_version")
foursquare_api_key = secrets.get("foursquare_api_key")

def findARestaurant(mealType, location):
    try:
        # 1. Use getGeocodeLocation to get the latitude and longitude coordinates of the location string.
        latitude, longitude = getGeocodeLocation(location)
        
        # Print latitude and longitude for debugging
        print("Latitude:", latitude)
        print("Longitude:", longitude)

        # 2. Use foursquare API to find a nearby restaurant with the latitude, longitude, and mealType strings.
        url = ('https://api.foursquare.com/v3/places/search?client_id=%s&client_secret=%s&ll=%s,%s&query=%s&v=%s' % (foursquare_client_id, foursquare_client_secret, latitude, longitude, mealType, foursquare_version))
        
        headers = {"accept": "application/json", "Authorization": foursquare_api_key}

        h = httplib2.Http()

        result = json.loads(h.request(url, 'GET', headers=headers)[1])

        if result['results'][0]['categories'][0]:
            # 3. Grab the first restaurant
            restaurant = result['results'][0]['categories'][0]
            fsq_id =  result['results'][0]["fsq_id"]
            restaurant_name = restaurant['name']
            restaurant_address = result['results'][0]['location']["formatted_address"]

            # 4. Get a 300x300 picture of the restaurant using the venue_id
            url = ('https://api.foursquare.com/v3/places/%s/photos' % ((fsq_id)))
            headers = {"accept": "application/json", "Authorization": "fsq3JXM0g5VsJpnflAsebDYaAiSsQB9uvEEmMt207ptLdK0="}
            result = json.loads(h.request(url, 'GET', headers=headers)[1])

            # 5. Grab the first image
            if  result and result[0]:
                firstpic = result[0]
                prefix = firstpic['prefix']
                suffix = firstpic['suffix']
                imageURL = prefix + "300x300" + suffix
            else:
                # 6. If no image available, insert default image URL
                imageURL = "http://pixabay.com/get/8926af5eb597ca51ca4c/1433440765/cheeseburger-34314_1280.png?direct"

            # 7. Return a dictionary containing the restaurant name, address, and image URL
            restaurantInfo = {'name': restaurant_name, 'address': restaurant_address, 'image': imageURL}
            print("Restaurant Name: %s" % restaurantInfo['name'])
            print("Restaurant Address: %s" % restaurantInfo['address'])
            print("Image: %s \n" % restaurantInfo['image'])
            return restaurantInfo
        else:
            print("No Restaurants Found for %s" % location)
            return "No Restaurants Found"

    except Exception as e:
        # Print any exception that occurs
        print("Exception:", str(e))

if __name__ == '__main__':
    findARestaurant("Pizza", "Tokyo, Japan")
    findARestaurant("Tacos", "Jakarta, Indonesia")
    findARestaurant("Tapas", "Maputo, Mozambique")
    findARestaurant("Falafel", "Cairo, Egypt")
    findARestaurant("Spaghetti", "New Delhi, India")
    findARestaurant("Cappuccino", "Geneva, Switzerland")
    findARestaurant("Sushi", "Los Angeles, California")
    findARestaurant("Steak", "La Paz, Bolivia")
    findARestaurant("Gyros", "Sydney, Australia")
    findARestaurant("Jollof", "Toronto, Canada")