import json
import requests

artist_name = input("Pick a artist/band= ")

response = requests.get("https://itunes.apple.com/search?entity=song&limit=100&term=" + artist_name)

r = response.json()

    
for result in r["results"]:
    print(result["trackName"])
