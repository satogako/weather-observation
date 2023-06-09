from pyowm import OWM
from prettytable import PrettyTable
import math
import json

with open('creds.json', 'r') as json_file:
    file = json.load(json_file)['key']

OMW_KEY = OWM(file)
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
        print('Type a city to see what the weathe is like')

        data_str = input('Enter your city here. Example: Dublin\n')
        city_name = data_str.lower().capitalize()

        if validate_data(city_name):
            break

    return city_name


def validate_data(value):
    '''
    Inside the attempt, it checks whether the value is an empty string and
    whether the value consists entirely of letters. Raises ValueError if
    the value is an empty string and does not consist of letters.
    Throws an Exception when the library does not find the city.
    '''
    try:
        if value == '':
            raise ValueError(
                "You did't enter any data"
            )
        elif ' ' in value[0]:
            raise ValueError(
               "You did't enter any data"
            )
        elif value.isalpha() is False and ' ' not in value:
            raise ValueError(
                f'You should enter only letters, you provided {value}'
            )

        MGR.weather_at_place(value)

    except ValueError as e:
        print(f'Invalid data: {e}, please try again.\n')
        return False
    except Exception:
        print('No city found or you made a mistake.')
        print(f'Please try again, you provided {value}\n')
        return False

    return True


def show_weather(city_name):
    '''
    The function gets the weather from the pyowm library, adds a list with the
    obtained weather values and displays data in the form of a table.
    '''
    observation = MGR.weather_at_place(city_name)
    obs_w = observation.weather

    temperature = math.floor(obs_w.temperature('celsius')['temp'])
    wheather = obs_w.status
    clouds_percentage = obs_w.clouds
    rain_for_hour = obs_w.rain['1h'] if obs_w.rain != {} else '--'
    humidity = obs_w.humidity
    wind_speed_km = round(obs_w.wind()['speed'] * 3600 / 1000, 1)

    data_collected = [
        city_name, temperature, wheather, clouds_percentage,
        rain_for_hour, humidity, wind_speed_km
    ]

    TABLE.field_names = [
        'City', '\u00b0C', 'Weather', 'Clouds,%',
        'Rain,mm/h', 'HUM,%', 'Wind,km/h'
    ]
    TABLE.add_row(data_collected)

    print(TABLE)


def user_answer():
    '''
    Gets the user's response : If YES, then stops the While loop and
    allows you to observe the weather in another city; If NO, it stops
    the program; If none of the above, it displays a message, and continues
    While until the user enters YES or NO.
    '''
    while True:
        print()
        print('Would you like to see the weather in another city?')
        user_answer = input('Please enter: y - Yes or n - No\n')
        choise = user_answer.lower()

        if choise == 'y':
            break
        elif choise == 'n':
            return False
        else:
            print(f'Invalid data: {choise}.')
            print('You must enter: y - Yes or n - NO, please try againe.')

    return True


def main():
    '''
    Run all program functions, loop for repeat program and if statment for
    termination of the program
    '''
    for x in range(10):
        city = get_city_data()
        show_weather(city)

        if user_answer() is False:
            break
        elif x == 9:
            print('The maximum of cities for comparison has been reached!')

    print('Program is completed!')


print("Welcome to Weather Observation!")

main()
