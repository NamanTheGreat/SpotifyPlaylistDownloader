from spotipy.oauth2 import SpotifyOAuth
import spotipy
import requests
import subprocess
import os

#Authenticating
client_id = 'your_client_id' # Replace your_client_id with your actual client id
client_secret = 'your_client_secret' # Replace your_client_secret with your actual client secret
redirect_uri='your_redirect_url' # Replace your_redirect_url with your actual redirect url
scope = "user-library-read playlist-read-private" # Change this if you want additional permissions
# Create the SpotifyOAuth object
sp_oauth = SpotifyOAuth(client_id=client_id, client_secret=client_secret, redirect_uri=redirect_uri, scope=scope)

# Use get_cached_token() to obtain the access token
token_info = sp_oauth.get_cached_token()
if token_info is None:
    # Token is missing or expired, prompt user to re-authenticate
    print("Access token is missing or expired. Please re-authenticate.")

    # Get the authorization URL
    auth_url = sp_oauth.get_authorize_url()

    # Prompt the user to open the auth_url in their web browser
    print("Please open the following URL in your web browser and authorize the application:")
    print(auth_url)

    # Ask the user to paste the redirect URL after authorization
    redirect_url = input("Paste the redirect URL from your browser here: ").strip()

    # Extract the authorization code from the redirect URL
    authorization_code = sp_oauth.parse_response_code(redirect_url)

    # Exchange the authorization code for an access token
    token_info = sp_oauth.get_access_token(authorization_code)
    access_token = token_info['access_token']
else:
    access_token = token_info['access_token']

# Now you can use the 'access_token' to make authorized requests to the Spotify API
sp = spotipy.Spotify(auth=access_token)

while True:
    # Get the user's playlists
    playlists = sp.current_user_playlists()

    if not playlists:
        print("No playlists found for this user.")
        break

    # List the user's playlists
    print("Your Playlists:")
    for i, playlist in enumerate(playlists['items'], start=1):
        print(f"{i}. {playlist['name']}")

    # Ask the user to choose a playlist to download
    while True:
        try:
            choice = int(input("Enter the number of the playlist you want to download (or 0 to exit): "))
            if choice == 0:
                exit()
            elif 1 <= choice <= len(playlists['items']):
                break
            else:
                print("Invalid choice. Please enter a valid number.")
        except ValueError:
            print("Invalid input. Please enter a valid number.")

    selected_playlist = playlists['items'][choice - 1]
    playlist_id = selected_playlist['id']
    playlist_name = selected_playlist['name']

    # Create a folder for the playlist if it doesn't exist
    playlist_folder = f"Playlist_{playlist_name}"
    if not os.path.exists(playlist_folder):
        os.makedirs(playlist_folder)

    # Change the current working directory to the playlist folder
    os.chdir(playlist_folder)

    # Get the tracks in the selected playlist
    tracks = sp.playlist_tracks(playlist_id)

    # Print the tracks in the selected playlist
    print(f"Tracks in '{playlist_name}':")
    for track in tracks['items']:
        print(f"Track: {track['track']['name']}")

    # Ask the user if they want to download the entire playlist
    download_choice = input(f"Do you want to download the entire playlist '{playlist_name}'? (yes/no): ").strip().lower()

    if download_choice == 'yes':
        # Construct the spotdl command to download the entire playlist
        spotdl_command = ["spotdl", f"https://open.spotify.com/playlist/{playlist_id}"]
        try:
            subprocess.run(spotdl_command, check=True)
            print("Download completed successfully!")
        except subprocess.CalledProcessError as e:
            print(f"Error: {e}")
    else:
        print("Playlist not downloaded.")

    # Ask if the user wants to download another playlist
    another_download = input("Do you want to download another playlist? (yes/no): ").strip().lower()
    if another_download != 'yes':
        break


