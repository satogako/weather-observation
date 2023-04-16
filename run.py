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
     
    except ValueError as e:
        print(f'Invalid data: {e}, please try again.\n')
        return False

    return True 
    


def main():
    city = get_city_data()
    print(city)


print("Welcome to Weather Observation!")
main()
