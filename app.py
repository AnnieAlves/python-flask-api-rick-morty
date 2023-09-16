from flask import Flask, render_template
import urllib.request, json

app = Flask(__name__)


@app.route('/')
def get_list_characters_page():
    url = "https://rickandmortyapi.com/api/character/"
    all_chars = []

    while url:
        response = urllib.request.urlopen(url)
        char_data = json.loads(response.read())
        characters = char_data["results"]

        all_chars.extend(characters)

        next_page = char_data.get("info", {}).get("next")
        if next_page:
            url = next_page
        else:
            url = None

    return render_template("characters.html", characters=all_chars)


@app.route("/profile/<id>")
def get_profile(id):
    url = "https://rickandmortyapi.com/api/character/" + id
    response = urllib.request.urlopen(url)
    data = response.read()
    profile = json.loads(data)

    location_url = profile["location"]["url"]
    location_response = urllib.request.urlopen(location_url)
    location_data = location_response.read()
    location_dict = json.loads(location_data)

    return render_template("profile.html", profile=profile, location=location_dict)


@app.route('/lista')
def get_list_characters():
    url = "https://rickandmortyapi.com/api/character/"
    response = urllib.request.urlopen(url)
    characters = response.read()
    dict = json.loads(characters)

    characters = []

    for char in dict["results"]:
        character = {
            "name": char["name"],
            "status": char["status"]
        }

        characters.append(character)

    return {"characters": characters}


@app.route('/locations')
def get_list_locations():
    url = "https://rickandmortyapi.com/api/location"
    all_locations = []

    
    while url:
        response = urllib.request.urlopen(url)
        locations_data = json.loads(response.read())
        locations = locations_data["results"]

        
        all_locations.extend(locations)

        
        next_page = locations_data.get("info", {}).get("next")
        if next_page:
            url = next_page
        else:
            url = None

    return render_template("locations.html", locations=all_locations)

@app.route('/locations/<id>')
def get_location_profile(id):
    url = "https://rickandmortyapi.com/api/location/" + id
    response = urllib.request.urlopen(url)
    data = response.read()
    location_dict = json.loads(data)

    characters = []
    for character_url in location_dict["residents"]:
        character_response = urllib.request.urlopen(character_url)
        character_data = character_response.read()
        character_dict = json.loads(character_data)
        characters.append(character_dict)

    return render_template("location_profile.html", location=location_dict, characters=characters)


@app.route('/episodes')
def get_list_episodes():
    url = "https://rickandmortyapi.com/api/episode"
    all_episodes = []

    
    while url:
        response = urllib.request.urlopen(url)
        episodes_data = json.loads(response.read())
        episodes = episodes_data["results"]

        
        all_episodes.extend(episodes)

        
        next_page = episodes_data.get("info", {}).get("next")
        if next_page:
            url = next_page
        else:
            url = None

    return render_template("episodes.html", episodes=all_episodes)

@app.route('/episodes/<id>')
def get_episode_profile(id):
    url = "https://rickandmortyapi.com/api/episode/" + id
    response = urllib.request.urlopen(url)
    data = response.read()
    dict = json.loads(data)

    characters = []
    
    for character_url in dict["characters"]:
        character_response = urllib.request.urlopen(character_url)
        character_data = character_response.read()
        character_dict = json.loads(character_data)
        characters.append(character_dict)

    return render_template("episode_profile.html", episode=dict, characters=characters)

    

