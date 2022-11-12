import os
from dotenv import load_dotenv
# Load environment variables in .env file
load_dotenv('./.env')

# Upload a video file specified by a path/to/the/file
import cloud_storage_functions
bucket_name = os.environ.get('BUCKET_NAME')
source_file = "./videos/sample-video-5s.mp4"
destination_file = "sample-video-5s.mp4"
print("Uploading the video...")
cloud_storage_functions.upload_blob(
    bucket_name,
    source_file,
    destination_file
)

video_url = f'https://storage.cloud.google.com/{bucket_name}/{destination_file}'
print("Finished uploading the video!!")
print(f'Video url: {video_url}')
