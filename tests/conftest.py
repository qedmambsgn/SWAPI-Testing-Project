import pytest
import requests

# Base URL for the SWAPI

BASE_URL = "https://swapi.dev/api"

# Fixtures for sample data for different SWAPI resources

@pytest.fixture(scope="session")
def sample_character_data():
    """Fixture for sample character data."""
    return {
        "name": "Luke Skywalker",
        "height": "172",
        "mass": "77",
        "hair_color": "blond",
        "eye_color": "blue"
    }

@pytest.fixture(scope="session")
def sample_planet_data():
    """Fixture for sample planet data."""
    return {
        "name": "Tatooine",
        "climate": "arid",
        "terrain": "desert",
        "population": "200000"
    }

@pytest.fixture(scope="session")
def sample_starships_data():
    """Fixture for sample starships data."""
    return {
        "name": "Star Destroyer",
        "model": "Imperial I-class Star Destroyer"
    }

@pytest.fixture(scope="session")
def sample_films_data():
    """Fixture for sample films data."""
    return{
        "title": "A New Hope",
        "director": "George Lucas"
    }


# Fixture for getting SWAPI resource by type and id

@pytest.fixture(scope="session")
def get_swapi_resource():
    """Fixture for getting SWAPI resource by type and id."""
    def _get_swapi_resource(resource_type, resource_id):
        response = requests.get(f"{BASE_URL}/{resource_type}/{resource_id}")
        return response
    return _get_swapi_resource
