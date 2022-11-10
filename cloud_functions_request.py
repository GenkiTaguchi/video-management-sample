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
    url = "https://some.cloud.functions.trigger.url"
    json = {
        "key1": 'value1',
        "key2": 'value2',
        "key3": 3
    }

    result = make_authorized_post_request(
        url,
        json
    )
    print(result.text)
