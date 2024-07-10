import uuid
from .models import Country,State,City
from typing import List

# Insert a Country
def addCountry() -> Country:
    country = Country(
        name="Two India",
        country_code="IN",
        curr_symbol="Ru",
        phone_code="+91"
    )
    country.save()
    return country

# Insert a State
def addState(country: Country) -> State:
    state = State(
        name="Teleangana",
        state_code="TG",
        gst_code="GST12",
        country=country
    )
    state.save()
    return state

# Insert a City
def addCity(state: State) -> City:
    city = City(
        name="Nizamabad",
        city_code="NZ",
        phone_code="+91",
        population=50000,
        avg_age=35,
        num_of_adult_males=24300,
        num_of_adult_females=32321,
        state=state
    )
    city.save()
    return city

def bulk_insert_countries(countries: List[Country]) -> None:
    Country.objects.bulk_create(countries)

# Bulk Insert States
def bulk_insert_states(states: List[State]) -> None:
    State.objects.bulk_create(states)

# Bulk Insert Cities
def bulk_insert_cities(cities: List[City]) -> None:
    City.objects.bulk_create(cities)

# Query to fetch

def fetch_all_countries() -> List[Country]:
    return list(Country.objects.all())

# Fetch all States
def fetch_all_states() -> List[State]:
    return list(State.objects.all())

# Fetch all Cities
def fetch_all_cities() -> List[City]:
    return list(City.objects.all())

# Fetch all cities of a State
def fetch_cities_of_state(state_id: uuid.UUID) -> List[City]:
    return list(City.objects.filter(state_id=state_id))

# Fetch all states of a Country
def fetch_states_of_country(country_id: uuid.UUID) -> List[State]:
    return list(State.objects.filter(country_id=country_id))

# Fetch all Cities of a Country name
def fetch_cities_of_country_name(country_name: str) -> List[City]:
    return list(City.objects.filter(state__country__name=country_name))

# Fetch a City of a Country with Minimum and Maximum Population
def fetch_city_with_min_max_population(country_name: str) -> dict:
    cities = City.objects.filter(state__country__name=country_name)
    min_pop_city = cities.order_by('population').first()
    max_pop_city = cities.order_by('-population').first()
    return {
        "min_population_city": min_pop_city,
        "max_population_city": max_pop_city
    }

#Query to get single city
def get_a_city_by_id(id: uuid.UUID) -> City:
    return City.objects.get(id=id)

