import requests
import requests.auth
import json
from CredentialsReddit import USERNAME, PASSWORD, CLIENT_ID, CLIENT_SECRET

# Connecting to Reddit REST API

client_auth = requests.auth.HTTPBasicAuth(
    CLIENT_ID, CLIENT_SECRET)  # Authenticate Reddit App
post_data = {'grant_type': 'password',
             'username': USERNAME, 'password': PASSWORD}
headers = {
    'User-Agent': 'An automation script.'
}

# Getting token access ID
TOKEN_ACCESS_ENDPOINT = 'https://www.reddit.com/api/v1/access_token'
response = requests.post(TOKEN_ACCESS_ENDPOINT,
                         data=post_data, headers=headers, auth=client_auth)
if response.status_code == 200:
    token_id = response.json()['access_token']


# Using Reddit REST API to get content
OAUTH_ENDPOINT = 'https://oauth.reddit.com'

params_get = {
    'limit': 1
}

headers_get = {
    'User-Agent': 'An automation script.',
    'Authorization': 'Bearer ' + token_id
}

response2 = requests.get(
    OAUTH_ENDPOINT + '/r/ArtefactPorn/top/', headers=headers_get, params=params_get)  # Which posts to grab

data = response2.json()
REDDIT_CONTENT = data["data"]["children"][0]["data"]["title"]
REDDIT_IMAGE = data["data"]["children"][0]["data"]["url_overridden_by_dest"]

# Saving to text file
CONTENT_TEXT = open('RedditContent.txt', 'a+')
CONTENT_TEXT.write(REDDIT_CONTENT + '\n' + REDDIT_IMAGE + '\n')

CONTENT_TEXT.close()
