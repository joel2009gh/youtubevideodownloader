A simple command-line tool to download YouTube videos using yt-dlp.

## Features

- Download videos in various resolutions
- Download audio-only in MP3 format
- View available video formats
- Progress tracking during download
- Simple command-line interface

## Installation

### Prerequisites

1. Python 3.6 or higher
2. pip (Python package manager)
3. FFmpeg (for audio extraction)

### Step 1: Clone or download this repository

```bash
git clone https://github.com/joel2009/youtube-downloader
cd youtube-downloader
```

Or simply download the `youtube_downloader.py` file.

### Step 2: Install required Python packages

```bash
pip install yt-dlp
```

### Step 3: Install FFmpeg (required for audio extraction)

#### On Ubuntu/Debian:
```bash
sudo apt-get update
sudo apt-get install ffmpeg
```

#### On macOS (using Homebrew):
```bash
brew install ffmpeg
```

#### On Windows:
Download from [ffmpeg.org](https://ffmpeg.org/download.html) and add to your PATH.

## Usage

### Basic Usage

Download a video with the highest available quality:

```bash
python3 youtube_downloader.py --url "URL"
```

### Command Line Options

- `--url` or `-u`: YouTube video URL (required)
- `--output` or `-o`: Output directory (optional, defaults to current directory)
- `--resolution` or `-r`: Desired video resolution like 720p, 1080p (optional)
- `--audio` or `-a`: Download audio only (optional)

### Examples

1. Download a video with the highest available resolution:
```bash
python3 youtube_downloader.py --url "URL"
```

2. Download a video with a specific resolution:
```bash
python3 youtube_downloader.py --url "URL" --resolution 720p
```

3. Download audio only (MP3 format):
```bash
python3 youtube_downloader.py --url "URL" --audio
```

4. Specify an output directory:
```bash
python3 youtube_downloader.py --url "URL" --output ~/Downloads
```

## Troubleshooting

### Common Issues

1. **Error: "FFmpeg not found"**
   - Make sure FFmpeg is installed and in your system PATH
   - This is only required for audio extraction

2. **Error: "HTTP Error 429: Too Many Requests"**
   - YouTube is rate-limiting your requests
   - Wait a while before trying again

3. **Video unavailable or private**
   - The video might be region-restricted, private, or removed
   - Try with a different video

## Legal Disclaimer

This tool is for personal use only. Please respect copyright laws and YouTube's Terms of Service. Do not download videos without permission from the content creator or if prohibited by the platform's terms of service.
