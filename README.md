
## Description

This is a Python script that allows you to download YouTube videos in MP4 or MP3 format. The script uses the `pytube` and `yt-dlp` libraries to interact with YouTube and download media files. It also ensures that all required libraries are installed before running the script.

## Features

- Downloads YouTube videos in MP4 format.
- Downloads audio in MP3 format.
- Interactive installation of required libraries.
- Displays video information such as title, duration, views, and release date.
- Provides an option to install another video after a successful download.

## Requirements

Before running the script, ensure you have the following installed:

- Python 3.x
- `pytube` library
- `yt-dlp` library
- FFmpeg (required for audio conversion)

The script will automatically check if the necessary libraries are installed and prompt you to install any missing ones.

## Installation

1. Clone or download this repository to your local machine.

2. Make sure you have Python 3.x installed. If you don't, download it from the [official Python website](https://www.python.org/).

3. Install the required libraries by running the following commands in your terminal:

    ```bash
    pip install pytube yt-dlp
    ```

4. **FFmpeg**: The script uses FFmpeg for audio conversion. If FFmpeg is not installed or does not work, you can manually install it using the following command in your terminal:

    ```bash
    winget install ffmpeg
    ```

    If you face issues with FFmpeg installation, ensure it's installed correctly on your system.

## Usage

1. Run the script:

    ```bash
    python youtube_downloader.py
    ```

2. The script will ask you to enter the YouTube video link.

3. Once you enter the link, the script will show video details like title, duration, and views.

4. Choose the file type (MP4 or MP3) you want to download:

    - `1` for MP4 (video)
    - `2` for MP3 (audio)

5. The script will then download the file and notify you once it's done.

6. You will be asked if you want to download another video. Type `Y` or press Enter to continue, or type `N` to exit.

## Troubleshooting

- If any required library is missing, the script will prompt you to install it. Follow the on-screen instructions to install the libraries.
- If FFmpeg doesn't work, make sure it's installed correctly by running `ffmpeg -version` in your terminal. If it's not found, use the manual installation command mentioned above.

## License

This script is open source. You can modify and use it according to your needs. Please ensure that you comply with YouTube's terms of service when using this script.
