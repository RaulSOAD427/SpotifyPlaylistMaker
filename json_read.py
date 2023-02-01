import json
import os
from pprint import pprint
id = "Raul"
song_ids = "spotify:track:4iV5W9uYEdYUVa79Axb7Rh,spotify:track:1301WleyT98MSxVHPZCA6M"
URL = f"https://api.spotify.com/v1/playlists/{id}/tracks/{song_ids}"

print(f"{URL}")
# with open('playlist.JSON') as f:
#   data = json.load(f)
#   #data -> dict type
#   print(data.get("uri"))
  
