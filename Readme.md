# 🎵 SpotMP3 - Spotify Playlist to MP3 Downloader

SpotMP3 is a Python tool that lets you download songs from a **public Spotify playlist** by searching and fetching them from **YouTube**, then converting them to **MP3 format** using `yt-dlp` and `ffmpeg`.

---

## 🚀 Features

- 🔗 Fetch tracks from any public Spotify playlist  
- 🔍 Automatically search songs on YouTube  
- ⬇️ Downloads and converts to high-quality MP3  
- 📂 Stores all songs neatly in a `songs/` folder  
- 🧠 Skips songs that already exist locally  

---

## 🛠️ Requirements

- Python 3.8+
- [yt-dlp](https://github.com/yt-dlp/yt-dlp)
- [ffmpeg](https://ffmpeg.org/)
- [spotipy](https://spotipy.readthedocs.io/)
- [pydub](https://github.com/jiaaro/pydub)

---

## 🔧 Setup Instructions

### 1. Clone the Repository

```bash
git clone https://github.com/yourusername/SpotMP3.git
cd SpotMP3
2. Create and Activate a Virtual Environment
bash
Copy
Edit
# On Windows
python -m venv venv
venv\Scripts\activate

# On macOS/Linux
python3 -m venv venv
source venv/bin/activate
3. Install Python Dependencies
bash
Copy
Edit
pip install -r requirements.txt
Or manually:

bash
Copy
Edit
pip install spotipy yt-dlp pydub
📦 Install FFmpeg
Option 1: Using Winget (Recommended for Windows 10/11)
bash
Copy
Edit
winget install ffmpeg
Option 2: Manual Download
Go to https://www.gyan.dev/ffmpeg/builds/

Download the Full build

Extract it and add the bin/ path to your system's Environment Variables > PATH

✅ Ensure both ffmpeg and ffprobe are accessible from your terminal/PowerShell.

📂 Folder Structure
bash
Copy
Edit
project/
│
├── songs/               # All MP3s downloaded go here
├── downloader.py        # Your main script
└── README.md            # This file
🧪 How It Works
Authenticates using Spotify's public API.

Fetches all track names + artists from a playlist.

Searches for each song on YouTube via yt-dlp.

Downloads the best audio format.

Converts the result to .mp3 using ffmpeg.

Skips songs already downloaded.

🚀 Run the Script
bash
Copy
Edit
python downloader.py
🧾 Example Output
less
Copy
Edit
Found 11 tracks in the playlist.
Searching & downloading: Time in a Bottle Jim Croce
Downloading...
Converting to MP3...
Saved to /songs/
