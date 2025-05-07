import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
import yt_dlp
import os

# Spotify API Setup
SPOTIFY_CLIENT_ID = '3ec3244731a14f54827c49f205c67876'
SPOTIFY_CLIENT_SECRET = '4903e8fc7f734fa1965a6da6e674e488'
PLAYLIST_ID = '6P94DMTG0YPygMnsi42OZI'

sp = spotipy.Spotify(auth_manager=SpotifyClientCredentials(
    client_id=SPOTIFY_CLIENT_ID,
    client_secret=SPOTIFY_CLIENT_SECRET
))

# Fetch Playlist Tracks
results = sp.playlist_tracks(PLAYLIST_ID)
tracks = results['items']
song_list = []

while results['next']:
    results = sp.next(results)
    tracks.extend(results['items'])

for item in tracks:
    track = item['track']
    name = track['name']
    artist = track['artists'][0]['name']
    song_list.append(f"{name} {artist}")

print(f"Found {len(song_list)} tracks in the playlist.")

# Ensure the 'songs' directory exists
if not os.path.exists('songs'):
    os.makedirs('songs')

# yt-dlp options
ydl_opts = {
    'format': 'bestaudio/best',
    'outtmpl': 'songs/%(title)s.%(ext)s',  # Save in 'songs' folder
    'postprocessors': [{
        'key': 'FFmpegExtractAudio',
        'preferredcodec': 'mp3',
        'preferredquality': '192',
    }],
    'quiet': False,
    'noplaylist': True,
}

# Download songs using yt-dlp search
for song in song_list:
    # Generate the file path based on the song name
    song_filename = f"songs/{song}.mp3"
    
    # Check if the file already exists
    if os.path.exists(song_filename):
        print(f"Skipping {song}, already exists.")
        continue

    try:
        print(f"Searching & downloading: {song}")
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            ydl.download([f"ytsearch1:{song}"])
    except Exception as e:
        print(f"Failed to download {song}: {e}")
