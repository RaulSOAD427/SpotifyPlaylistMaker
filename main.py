import json
from requests.compat import urljoin
import requests
from pprint import pprint 
CLIENT_ID =  "9478f7eee2aa4dac9fa95dbd44621167"
CLIENT_SECRET = "df59e2ec0b6149aeb3a7abdd480b3de8"
CURRENT_SONG_URL = "https://api.spotify.com/v1/me/player/currently-playing"

TOP_TRACKS_URL = "https://api.spotify.com/v1/me/top/tracks?time_range=short_term&limit=50"
MAKE_PLAYLIST_URL = "https://api.spotify.com/v1/users/edgy_raul/playlists"
FILL_PLAYLIST_URL = "https://api.spotify.com/v1/playlists/{playlist_id}/tracks/{song_ids}"
TOKEN_URL = "BQDMdZ_bzlK87szBtf1ShbzFq6AaiAw7XC2RSv_WPQqAWiJDrY8cpr2uY4ZC8eGtBrmTmwU-UCRr779-dYoPJ5DnhaS-2KBXFEh81aCEQ9zuOzPKPNQ77xispDUKPZ_Q70OovCuZjuH31ZU6D9MzHCDs9pOhZ3OorOx3O_zC5QWsdh4ioXoFnEU0u5kKVKuOujbjkPdeaREEdFqI3Sic"
data = {"name":"boom", 
"description" : "Playlist started by API", 
"public": "true" } 
#sorts through Spotify dict to find the names of the tracks 
def findNames(data):
  #data -> dict type
  data_list = data["items"]
  songs_list= []
  # for name in songs:
  for i in range(len(data_list)):
    dict_song = data_list[i]
    songs_list.append(dict_song.get("uri"))
  return songs_list

def findPlaylistID(data):
    return data.get("uri")

def get_top_tracks(token):
    response = requests.get(TOP_TRACKS_URL, headers={"Authorization" : f"Bearer {token}"})
    resp_json = response.json()
    return findNames(resp_json)
  

def get_current_track(token):
    response = requests.get(CURRENT_SONG_URL, headers={"Authorization" : f"Bearer {token}"})
    return response.json()

def make_playlist(token):
    return requests.post(MAKE_PLAYLIST_URL, headers = {"Authorization" : f"Bearer {token}"}, json=data).json()


def fill_playlist(url, token):
    requests.post(url, headers = {"Authorization" : f"Bearer {token}"})


def main():
    list_songs = get_top_tracks(TOKEN_URL)
    songs_url_format = "%2C".join(list_songs) 
    songs_url_format = songs_url_format.replace(":","%3A")
    playlist_id = (findPlaylistID(make_playlist(TOKEN_URL)))  
    playlist_id = playlist_id.replace("spotify:playlist:","")
    
    add_songs_url = f"https://api.spotify.com/v1/playlists/{playlist_id}/tracks?uris={songs_url_format}"
    fill_playlist(add_songs_url, TOKEN_URL)

# def main():
#     playlist_id = "1vWZkoFvKNSNkhjrQORZAm"
#     songs_url_format = "spotify:track:0pUVeEgZuNyFzIMKp67RbS"
#     songs_url_format = the_song.replace(":","%3A")
#     songs_url_format = the_song.replace(",","%2C")
#     add_songs_url = f"https://api.spotify.com/v1/playlists/{playlist_id}/tracks?uris={songs_url_format}"
#     # print(add_songs_url)
#     fill_playlist(add_songs_url, TOKEN_URL)
  

if __name__ == "__main__":
  main()


