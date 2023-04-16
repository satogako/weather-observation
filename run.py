from pyowm import OWM
from prettytable import PrettyTable


OMW_KEY = OWM('6527f0e6cac68cd70fb43502cb0948d7')
MGR = OMW_KEY.weather_manager()


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


def main():
    city = get_city_data()
    print(city)


print("Welcome to Weather Observation!")
main()
