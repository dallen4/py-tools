#scrape tracks from Tidal (attempt) -- requires Python3
import requests
import tidalapi
import sys
import urllib3

session = tidalapi.Session()
session.login('email', 'pwd')
# tracks = session.get_album_tracks(album_id=16909093)
# for track in tracks:
#     print (track.name)

#download test
song = session.get_media_url(track_id='22560696')
song = 'https://' + song
r = requests.get(song, stream=True)
with open('~/Projects/py-scripts/', 'wb') as f:
    total_length = int(r.headers.get('content-length', 0))
    for chunk in progress.bar(r.iter_content(chunk_size=1024), expected_size=(total_length / 1024) + 1):
        if chunk:
            f.write(chunk)
            f.flush()
