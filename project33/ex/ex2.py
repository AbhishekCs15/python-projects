import requests
from datetime import datetime
# our latitude and longitude
parameters = {
    "lat": 12.840936511088092,
    "lng": 77.5117750690624,
    "formatted": 0  # To get the clock in 24 hrs
}
response = requests.get(url="https://api.sunrise-sunset.org/json", params=parameters)  # should pass lat and lang as dict in params to get our loc
response.raise_for_status()
data = response.json()
print(data)
sunrise = int(data["results"]["sunrise"].split("T")[1].split(":")[0])
sunset = int(data["results"]["sunset"].split("T")[1].split(":")[0])
print(sunrise)  # print(sunrise.split("T")[1].split(":")[0])
print(sunset)
present = datetime.now()
print(present.hour)


# import requests
#
# response = requests.get(url="http://api.open-notify.org/iss-now.json")  # get is a method in the request url gets a API end point print(response)
# response.raise_for_status()  # Method handles Error and Exception print(data)
# data = response.json()  # Takes json file from response
# longitude = data["iss_position"]["longitude"]
# latitude = data["iss_position"]["latitude"]
# iss_position = ( latitude, longitude )
# print(iss_position)