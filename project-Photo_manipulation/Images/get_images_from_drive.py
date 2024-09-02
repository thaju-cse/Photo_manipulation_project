import os
import pickle
import sys
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request
from googleapiclient.discovery import build
from googleapiclient.http import MediaIoBaseDownload

# Define constants
SCOPES = ['https://www.googleapis.com/auth/drive.readonly']
CREDENTIALS_FILE = 'access.json'  # Path to your OAuth 2.0 credentials file
TOKEN_FILE = 'token.pickle'  # Path to the token file


def authenticate_drive():
    creds = None
    if os.path.exists(TOKEN_FILE):
        with open(TOKEN_FILE, 'rb') as token:
            creds = pickle.load(token)
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file(CREDENTIALS_FILE, SCOPES)
            creds = flow.run_local_server(port=0)
        with open(TOKEN_FILE, 'wb') as token:
            pickle.dump(creds, token)
    drive_service = build('drive', 'v3', credentials=creds)
    return drive_service


def download_file_from_drive(drive_service, file_id, destination):
    request = drive_service.files().get_media(fileId=file_id)
    with open(destination, 'wb') as file:
        downloader = MediaIoBaseDownload(file, request)
        done = False
        while not done:
            status, done = downloader.next_chunk()
            print(f"Download {int(status.progress() * 100)}%.")
    print(f"File downloaded to {destination}")


if __name__ == "__main__":
    drive_service = authenticate_drive()

    # Replace with your Google Drive file ID
    FILE_ID = '1vuxa79tkhoLqh7XUowxcxKiPmlKGsNuS'  # Replace this with the actual file ID
    LOCAL_DESTINATION = sys.argv[1]  # Replace this with the desired local filename

    download_file_from_drive(drive_service, FILE_ID, LOCAL_DESTINATION)
