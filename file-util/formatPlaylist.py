# Rename all files in directory
import os
import soundcloud

client = soundcloud.Client(client_id='175c043157ffae2c6d5fed16c3d95a4c')

#retrieve all tracks by given user
userTracks = client.get('/users/brianfresco/tracks')
for track in userTracks:
    title = track.title

#retrieve all tracks LIKED by given user
likes = client.get('users/brianfresco/favorites')
for track in likes:
    title = track.title
    print(title)

#retrieve all tracks in a playlist (i.e., EP, album, set, etc.)
playlist = client.get('/playlists/236846045')
for track in playlist.tracks:
    title = track['title']
    print(title)


for filename in os.listdir("."):
    if filename.startswith("Copy of "):
        os.rename(filename, filename[8:])
