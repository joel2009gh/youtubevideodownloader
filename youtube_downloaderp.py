#!/usr/bin/env python3
import argparse
import os
import sys
import yt_dlp
def download_video(url, output_path=None, resolution=None, audio_only=False):
    try:
        if not output_path:
            output_path = os.getcwd()
        if not os.path.exists(output_path):
            os.makedirs(output_path)
        ydl_opts = {
            'quiet': False,
            'progress_hooks': [lambda d: print(f"\rDownloading: {d['_percent_str']} of {d.get('_total_bytes_str', 'unknown size')}", end='') if d['status'] == 'downloading' else None],
            'outtmpl': os.path.join(output_path, '%(title)s.%(ext)s'),
        }
        if audio_only:
            ydl_opts.update({
                'format': 'bestaudio/best',
                'postprocessors': [{
                    'key': 'FFmpegExtractAudio',
                    'preferredcodec': 'mp3',
                    'preferredquality': '192',
                }],
            })
        elif resolution:
            ydl_opts.update({
                'format': f'bestvideo[height<={resolution[:-1]}]+bestaudio/best[height<={resolution[:-1]}]',
            })
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            info = ydl.extract_info(url, download=False)
            print(f"\nTitle: {info.get('title', 'Unknown')}")
            print(f"Author: {info.get('uploader', 'Unknown')}")
            print(f"Length: {info.get('duration', 0)} seconds")
            if not audio_only and not resolution:
                print("\nAvailable formats:")
                formats = info.get('formats', [])
                video_formats = [f for f in formats if f.get('vcodec') != 'none' and f.get('acodec') != 'none']
                for i, fmt in enumerate([f for f in video_formats if f.get('height')]):
                    print(f"{i+1}. {fmt.get('height')}p - {fmt.get('ext')}")
            ydl.download([url])
            print(f"\nDownload complete!")
    except Exception as e:
        print(f"\nError: {str(e)}")
        return False
    return True
def main():
    parser = argparse.ArgumentParser(description='Download YouTube videos')
    parser.add_argument('--url', '-u', required=True, help='YouTube video URL')
    parser.add_argument('--output', '-o', help='Output directory (default: current directory)')
    parser.add_argument('--resolution', '-r', help='Video resolution (e.g., 720p, 1080p)')
    parser.add_argument('--audio', '-a', action='store_true', help='Download audio only')
    args = parser.parse_args()
    download_video(args.url, args.output, args.resolution, args.audio)
if __name__ == "__main__":
    main()
