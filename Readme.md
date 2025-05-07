# 🎵 Spotify Playlist to MP3 Downloader

This project fetches all the tracks from a **public Spotify playlist** and downloads them as `.mp3` files using `yt-dlp`, saving them neatly inside a `songs/` folder.

## 🚀 Features

- Fetches songs from any **public Spotify playlist**.
- Searches for each song on **YouTube** and downloads the best audio.
- Converts audio files to **MP3 format** (192 kbps).
- **Skips already-downloaded songs** to avoid duplicates.
- Automatically organizes downloads into a `songs/` folder.

---

## 🛠️ Setup Instructions

### 1. Clone the Repository

```bash
git clone https://github.com/yourusername/spotify-playlist-mp3-downloader.git
cd spotify-playlist-mp3-downloader

2. Install Python Dependencies
Make sure you're using Python 3.8 or later.

bash
Copy
Edit
pip install spotipy yt-dlp pydub
3. Install FFmpeg
This is required for audio conversion.

Windows (Using winget)
bash
Copy
Edit
winget install ffmpeg
Then, add the ffmpeg bin folder to your environment variables.

Example path (adjust if needed):

makefile
Copy
Edit
C:\Users\<your-username>\AppData\Local\Microsoft\WinGet\Packages\Gyan.FFmpeg_Microsoft.Winget.Source_8wekyb3d8bbwe\ffmpeg-7.1.1-full_build\bin
Restart your terminal after adding to the PATH.

🔑 Spotify API Credentials
Go to the Spotify Developer Dashboard.

Create an app to get your Client ID and Client Secret.

Paste them in the script:

python
Copy
Edit
SPOTIFY_CLIENT_ID = 'your-client-id'
SPOTIFY_CLIENT_SECRET = 'your-client-secret'
PLAYLIST_ID = 'your-playlist-id'
You can find the playlist ID from the URL:
https://open.spotify.com/playlist/01Uw1umqVhj3PTDPmkw25i → 01Uw1umqVhj3PTDPmkw25i

▶️ Run the Script
bash
Copy
Edit
python download_songs.py
All downloaded .mp3 files will be saved in the songs/ folder.
