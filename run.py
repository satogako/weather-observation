from pyowm import OWM
from prettytable import PrettyTable
import math

OMW_KEY = OWM('6527f0e6cac68cd70fb43502cb0948d7')
MGR = OMW_KEY.weather_manager()
TABLE = PrettyTable()


def get_city_data():
    """
    Get the name of the city entered by the user.
    Run a while loop to collect a valid string of data from the user
    through a terminal that must be a string. 
    The loop will repeatedly request the data until it is valid.
    """
    while True:
        print("Type a city to see what the weathe is like")

        data_str = input("Enter your city here. Example: Dublin\n")
        city_name = data_str.lower().capitalize()

        if validate_data(city_name):
            print(f'You enter city: {city_name}')
            break

    return city_name


def validate_data(value):
    """
    Inside the attempt, it checks whether the value is an empty string and 
    whether the value consists entirely of letters. Raises ValueError if 
    the value is an empty string and does not consist of letters. 
    Throws an Exception when the library does not find the city.
    """
    try:
        if value.isalpha() != True:
            if value == "":
                raise ValueError(
                    "You did't enter any data"
                )
            else:
                raise ValueError(
                    f'You should enter only letters, you provided {value}'
                )

        MGR.weather_at_place(value)
     
    except ValueError as e:
        print(f'Invalid data: {e}, please try again.\n')
        return False
    except Exception:
        print(f'No city found or you made a mistake. Please try again, you provided {value}\n')
        return False

    return True 


def show_weather(city_name):
    '''
    '''
    observation = MGR.weather_at_place(city_name)
    obs_w = observation.weather
    
    temperature = math.floor(obs_w.temperature('celsius')['temp'])
    wheather = obs_w.status
    clouds_percentage = obs_w.clouds
    rain_for_hour = obs_w.rain['1h'] if  obs_w.rain != {} else '--'
    humidity = obs_w.humidity 
    wind_speed_km = round(obs_w.wind ()['speed'] * 3600 / 1000, 1)
    visibility = observation.weather.visibility() / 1000

    data_collected = [
        city_name, temperature, wheather, clouds_percentage, 
        rain_for_hour, humidity, wind_speed_km, visibility
    ]

    TABLE.field_names = [
        'City', '\u00b0C', 'Weather', 'Clouds, %', 'Rain, mm/1h', 'HUM, %', 'Wind, km/h', 'Visib., km'
    ]
    TABLE.add_row(data_collected)

    print(TABLE)
    

def main():
    city = get_city_data()
    show_weather(city)


print("Welcome to Weather Observation!")
main()
