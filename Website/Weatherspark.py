import requests
from bs4 import BeautifulSoup

def get_weather_data(location):
    url = f'https://weatherspark.com/countries/CA'
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')

    # Extract high and low temperatures
    high_temps = soup.find_all('span', class_='high')
    low_temps = soup.find_all('span', class_='low')

    highs = [temp.get_text() for temp in high_temps]
    lows = [temp.get_text() for temp in low_temps]

    return highs, lows

location = '26469'  # Example location ID for Quebec
highs, lows = get_weather_data(location)

print("High Temperatures:", highs)
print("Low Temperatures:", lows)
