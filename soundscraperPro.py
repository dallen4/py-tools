#download any song from SoundCloud
import soundcloud
import soundscrape
from soundscrape.soundscrape import process_soundcloud

client = soundcloud.Client(client_id='175c043157ffae2c6d5fed16c3d95a4c')

#print("Welcome to SoundScraper Pro. \nBuilt on Miserlou's SoundScrape at https://github.com/Miserlou/SoundScrape. \nBy dallen4 @ https://github.com/dallen4.")
#USERNAME = raw_input("What is the username of the artist you are looking for (as appears in the URL on their page)?\n")


# userTracks = client.get('/users/brianfresco/tracks')
# for track in userTracks:
#     trackURI = track.uri
#     track_info = client.get(trackURI)
#     trackTitle = track_info.title
#     print (trackTitle)

#Download track from SoundCloud Example
vargs = {'path':'', 'folders': False, 'group': False, 'track': 'miracle-prod-mano', 'num_tracks': 1, 'bandcamp': False, 'downloadable': False, 'likes': False, 'open': False, 'artist_url': 'brianfresco', 'keep': False}
process_soundcloud(vargs)
