import requests
import datetime
from googletrans import Translator

URL = "https://weather.visualcrossing.com/VisualCrossingWebServices/rest/services/timeline"
KEYS = "?key=ECQ8CSE5FV2R2BS3XTC5S73VP&unitGroup=metric&elements=tempmin,tempmax,datetime,humidity"


def get_data(location):
    """build a request to the weather API and returns the response status and data"""
    today = str(datetime.date.today())
    week = str(datetime.date.today() + datetime.timedelta(days=7))
    request = URL + "/" + location + "/" + today + "/" + week + "/" + KEYS
    response = requests.get(url=request)
    data = response.json()

    return response, data


def data_to_present(location):
    """try to call 'get_data', if success create a new list of dicts from json with the relevant data"""
    try:
        response, data = get_data(location)
    except Exception as er:
        print("Invalid loction", er)
        return False, False
    forcast = []
    trans = Translator()
    days = ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"]
    location = data["resolvedAddress"]
    if not location.isascii():
        location = trans.translate(location, dest='en').text
    for day in data["days"]:
        today = day["datetime"].split("-")
        daily = {
            'day': f"{days[datetime.date(int(today[0]), int(today[1]), int(today[2])).weekday()]} {'/'.join(today[:0:-1])}",
            'day_temp': f"{day['tempmax']}℃",
            'night_temp': f"{day['tempmin']}℃",
            'humidity': f"{day['humidity']}%"
        }
        forcast.append(daily)
    return location, forcast


if __name__ == "__main__":
    pass