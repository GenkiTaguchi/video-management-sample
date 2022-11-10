import google.oauth2.id_token
import google.auth.transport.requests
import requests

def make_authorized_post_request(target_url, json={}):
    auth_req = google.auth.transport.requests.Request()
    id_token = google.oauth2.id_token.fetch_id_token(auth_req, target_url)

    headers = {
        "Authorization": f"Bearer {id_token}"
    }
    response = requests.post(target_url, headers=headers, json=json)

    return response

if __name__ == "__main__":
    url = os.environ.get('CLOUD_FUNCTIONS_URL_FOR_SQL_INSERT')
    json = {
        "camera_id": 'B-3',
        "cycle_id": 'A-1',
        "video_url": video_url,
        "video_length": 300
    }

    result = make_authorized_post_request(
        url,
        json
    )
    print(result.text)
