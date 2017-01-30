#download any song from SoundCloud
import soundcloud
import soundscrape
from soundscrape.soundscrape import process_soundcloud

#Look up tracks of Artist Example
client = soundcloud.Client(client_id='175c043157ffae2c6d5fed16c3d95a4c')
userTracks = client.get('/users/'+USERNAME+'/tracks')
for track in userTracks:
    trackURI = track.uri
    track_info = client.get(uri)
    trackTitle = track_info.title
    print trackTitle

#Download track from SoundCloud Example
vargs = {'path':'', 'folders': False, 'group': False, 'track': 'miracle-prod-mano', 'num_tracks': 1, 'bandcamp': False, 'downloadable': False, 'likes': False, 'open': False, 'artist_url': 'brianfresco', 'keep': False}
process_soundcloud(vargs)
