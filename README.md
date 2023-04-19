# WEATHER OBSERVATION
---

Weather Observation is a Python terminal program that runs on the Code Institute mock terminal on Heroku.

Users can view the weather in one city or in several at once.
The program will be useful for people who travel and those who want to compare the weather with their city.

[Here is the live version of my project.](https://weather-observation.herokuapp.com/)

![Responsive site.](assets/images/responsive_page.jpg)


## FEATURES
---
* EXISTING FUNCTIONS
    - To see the weather in a city, you need to enter the name of the city.
    The name of the city can be entered with both lowercase and uppercase letters.
        ![Weather data from one city.](assets/images/one_city.jpg)
    - The program allows you to see the following weather data:
        + Temperature in degrees Celsius;
        + Weather - the state of the sky: sun, clouds, raine.
        + Clouds, % - the percentage of cloudiness in the sky is from 0 to 100%. Where 0 is it has no clouds and 100% is completely cloudy sky, sun isn't visible.
        + Raine, mm/1h - This id how much raine fell in milimeters in one hour. If it shows -- it means that it has not rained in the last hour.
        + HUM, %  - This is humidity, measured as a percentage.
        + Wind, km/h  - wind speed in kilometers per hour.
    - To see the weather in several cities at the same time: after requesting the application "Would you like to see the weather in another city?", answer the letter y - YES and enter the name of another city.
        ![Screenshot of the question.](assets/images/question_y_n.jpg)
    - The program allows you to see the weather of up to ten cities at the same time.
        ![Screenshot of 10 cities.](assets/images/ten_cities.jpg)
    - Input validation
        + The program checks on an empty string.
        + The program checks on numbers and special characters.
        + The program checks on spaces.
        + The program checks for input of the city name with an error.
        + The program checks when requesting "Would you like to see the weather in another city?" a character other than y -YES or n - NO.