import requests
from bs4 import BeautifulSoup

# The above lines of code import the Requests and Beautiful soup libraries

# This gets the HTML document of the weather website for Kingston for the next 10 days

http_text = requests.get("https://weather.com/en-CA/weather/tenday/l/ac1c001e07fc19e6a28d15a16800eb1a0136fc4c616009f0bfe15ebcee352be2#detailIndex5").text

# print(http_text)

''' BeautifulSoup(a,b) essentially passes in the HTML data from the website into BeautifulSoup and asks
BeautifulSoup to use the lxml library to interact with the HTTP variable which contains the HTML data'''

soup = BeautifulSoup(http_text, 'lxml')
''' 
We are now going to webscrape the data we're interested in. We know that the line of data that we're looking
for is inside a Parent<div>tag, thus we're going to search through. 
 
Soup.find_all() function searches the entire HTML document for all the tags we specified, we pass div as an argument

The only issue is that there is many <div> tags in the doc, so we have to filter for the Parent div tags specific

Each div tag that we need have the following parameter <div data-testid="DetailsSummary" class="DetailsSummary--DetailsSummary--
1DqhO DetailsSummary--fadeOnOpen--KnNyF"> 

Thus, DetailsSummary--DetailsSummary--1DqhO DetailsSummary--fadeOnOpen--KnNyF will be our class_ argument

This way the final_all() function will only find the Parent<div>tags '''

weather_data = soup.find_all('div', class_="DetailsSummary--DetailsSummary--1DqhO DetailsSummary--fadeOnOpen--KnNyF")

# This will print out 15, which is equal to the number of lines
# print(len(weather_data))

''' We need a for loop over the weather_data variable so that in each iteration of the for loop, we work with the
weather data for a single day'''

for day in weather_data:
    ''' 
    In the following iterations, the day variable will contain the weather information for a single day
    The for loop code will scrape the data within each "date"
    The <h3> tag inside the Parent <div> tag will contain the date information
    '''
    date = day.find('h3', class_="DetailsSummary--daypartName--kbngc").text

    # This will print out the 15 days we're interested in
    # print(date)

    # This will scrape day for the child tag which contains the temperature section

    temp_section = day.find('div', class_="DetailsSummary--temperature--1kVVp")

    # There are only 2 span tags within the temp section, so we need to find them

    span_tags = temp_section.find_all('span')

    # Since there are only two <spans> tags, we don't need to filter them out
    # The maximum temperature data is inside the first span that we found, thus

    max_temp = span_tags[0].text
    min_temp = span_tags[2].span.text

    # print(max_temp)
    # print(min_temp)

    # Just like maximum and minimum temperatures, we want to scrape the weather conditions

    weather_condition = day.find('div', class_="DetailsSummary--condition--2JmHb").span.text

    #print(weather_condition)

    # Now we're going to scrape for the chance of rain/snow
    # This information is buried inside a <span> tag which is within a child <div> tag so inside the for loop we will do

    chance = day.find('div', class_="DetailsSummary--precip--1a98O").span.text

    # print(chance)

    # Now we're going to scrape the wind speed and wind direction
    wind_section = day.find('div', class_="DetailsSummary--wind--1tv7t DetailsSummary--extendedData--307Ax").span.text

    # Wind direction and wind speeds on the website are not seperated, they're both within a single string
    # This will split the values within the string [DIR], [SPEED], [UNITS]
    wind_seperated = wind_section.split()

    # print(wind_seperated)

    wind_direction = wind_seperated[0]
    wind_speed = wind_seperated[1]

    final_data = (date, max_temp, min_temp, weather_condition, chance, wind_direction, wind_speed)
    print(final_data)










