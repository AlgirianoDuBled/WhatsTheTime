from datetime import datetime
import pytz

def get_time_in_cities(cities):
    for city in cities:
        try:
            # Haal de tijdzone van de stad op
            timezone = pytz.timezone(city)
            # Haal de huidige tijd in de specifieke tijdzone op
            city_time = datetime.now(timezone)
            # Print de lokale tijd van de stad
            print(f"The current time in {city} is {city_time.s>
        except Exception as e:
            print(f"Could not find timezone for {city}: {e}")

# Lijst van enkele steden in 'Continent/Stad' formaat
cities = [
    'Europe/Amsterdam',
    'America/New_York',
    'Asia/Tokyo',
    'Australia/Sydney',
    'Africa/Cairo'
]

# Roep de functie aan
get_time_in_cities(cities)
