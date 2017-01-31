#scrape tracks from Tidal (attempt) -- requires Python3

import tidalapi

session = tidalapi.Session()
session.login('username', 'password')
tracks = session.get_album_tracks(album_id=16909093)
for track in tracks:
    print (track.name)
