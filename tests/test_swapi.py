import pytest
import requests

def test_get_character(sample_character_data, get_swapi_resource):
    """Test for retrieving character data from SWAPI"""
    resource_type = "people"
    resource_id = 1
    character = get_swapi_resource(resource_type, resource_id)

    assert character["name"] == sample_character_data["name"]
    assert character["height"] == sample_character_data["height"]
    assert character["mass"] == sample_character_data["mass"]
    assert character["hair_color"] == sample_character_data["hair_color"]
    assert character["eye_color"] == sample_character_data["eye_color"]

def test_get_planet(sample_planet_data, get_swapi_resource):
    """Test for retrieving planet data from SWAPI"""
    resource_type = "planets"
    resource_id = 1
    planet = get_swapi_resource(resource_type, resource_id)

    assert planet["name"] == sample_planet_data["name"]
    assert planet["climate"] == sample_planet_data["climate"]
    assert planet["terrain"] == sample_planet_data["terrain"]
    assert planet["population"] == sample_planet_data["population"]

def test_get_starships(sample_starships_data, get_swapi_resource):
    """Test for retrieving starship data from SWAPI"""
    resource_type = "starships"
    resource_id = 9  # A Star Destroyer, for example
    starship = get_swapi_resource(resource_type, resource_id)

    assert starship["name"] == sample_starships_data["name"]
    assert starship["model"] == sample_starships_data["model"]

def test_get_films(sample_films_data, get_swapi_resource):
    """Test for retrieving film data from SWAPI"""
    resource_type = "films"
    resource_id = 1
    film = get_swapi_resource(resource_type, resource_id)

    assert film["title"] == sample_films_data["title"]
    assert film["director"] == sample_films_data["director"]


def test_search_characters(get_swapi_resource):
    """Test for searching characters in SWAPI"""
    search_query = 'Skywalker'
    resource_type = 'people'
    response = get_swapi_resource(resource_type, f'?search={search_query}')

    assert response.status_code == 200

    json_content = response.json()

    assert 'results' in json_content
    assert any(search_query in character['name'] for character in json_content['results'])
