# Spotify Playlist Downloader

## Overview

This Python script allows you to download Spotify playlists to your local machine using the Spotdl command-line tool. It authenticates with your Spotify account, lists your playlists, and lets you choose which playlist to download. You can also choose to download multiple playlists one by one.

## How It Works

1. **Authentication**: The script authenticates with your Spotify account using the Spotify OAuth 2.0 authorization flow. It obtains an access token that allows it to access your Spotify data.

2. **List Your Playlists**: It fetches a list of your Spotify playlists and displays them, along with their names and a numbered list.

3. **Choose a Playlist**: You can choose a playlist to download by entering the corresponding number. If you enter '0', the script exits.

4. **Download Playlist**: If you choose to download a playlist, it creates a folder for the playlist (if it doesn't already exist), changes the working directory to that folder, and uses the Spotdl tool to download the entire playlist.

5. **Repeat or Exit**: After downloading a playlist, you can choose to download another playlist or exit the script.
## Future Features

Here are some additional features that could be added to enhance the script in the future:

- **Automatic Updates**: Implement a feature to check for updates to the script and notify the user if a new version is available. This ensures users have access to the latest improvements and bug fixes.

- **Download Quality Options**: Allow users to choose the audio quality when downloading tracks. Options could include high, medium, and low quality to cater to different preferences.

- **Download Specific Tracks**: Provide an option for users to download specific tracks from a playlist rather than downloading the entire playlist. This can be useful when users want to select only certain songs.

- **Enhanced Error Handling**: Improve error handling within the script to provide more informative error messages to users. Clear error messages help users troubleshoot issues more effectively.

- **User Profiles**: Enable users to enter Spotify usernames to download public playlists from other users. This expands the functionality of the script by allowing users to access a wider range of playlists.

Feel free to contribute to this project and add these features if you find them useful! 
## Usage

1. Clone or download the repository to your local machine.

2. Set up your Spotify Developer Application to obtain your `client_id`, `client_secret`, and `redirect_uri`. You need these credentials to authenticate your script.

3. [OPTIONAL] Create a `.env` file in the project directory and add your Spotify credentials as environment variables:
   

4. Install the required Python libraries using pip from the `requirements.txt` file:

```bash
pip install -r requirements.txt

