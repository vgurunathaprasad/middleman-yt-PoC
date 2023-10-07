import os
import google.auth
import googleapiclient.discovery
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
from googleapiclient.http import MediaFileUpload

CLIENT_SECRETS_FILE = 'secret.json'  
VIDEO_FILE_PATH = 'video.mp4' 
YOUTUBE_CHANNEL_ID = 'gmanyt-du1xu'  

scopes = ['https://www.googleapis.com/auth/youtube.upload']



flow = InstalledAppFlow.from_client_secrets_file(
    CLIENT_SECRETS_FILE, scopes)
credentials = flow.run_local_server(port=0)

youtube = build('youtube', 'v3', credentials=credentials)

request_body = {
    'snippet': {
        'title': 'My Uploaded Video Title',
        'description': 'Description for my uploaded video',
        'tags': ['tag1', 'tag2'],
        'categoryId': '22',  # Category ID for 'People & Blogs'
    },
    'status': {
        'privacyStatus': 'public',  # Change to 'private' for private videos
    }
}

media_file = MediaFileUpload(VIDEO_FILE_PATH)
videos_insert_response = youtube.videos().insert(
    part='snippet,status',
    body=request_body,
    media_body=media_file
).execute()

print(f'Video uploaded with ID: {videos_insert_response["id"]}')
