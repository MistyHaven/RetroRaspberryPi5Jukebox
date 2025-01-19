import requests
import base64

# Spotify credentials
client_id = "YOUR_CLIENT ID"
client_secret = "YOUR_CLIENT_SECRET"
redirect_uri = "http://localhost:8888/callback"
authorization_code = "YOUR_AUTHORIZATION_CODE"

# Encode client_id and client_secret
encoded_credentials = base64.b64encode(f"{client_id}:{client_secret}".encode()).decode()

# Token endpoint
url = "https://accounts.spotify.com/api/token"

# POST request to exchange authorization code for access token
headers = {
    "Authorization": f"Basic {encoded_credentials}",
    "Content-Type": "application/x-www-form-urlencoded"
}

data = {
    "grant_type": "authorization_code",
    "code": authorization_code,
    "redirect_uri": redirect_uri
}

response = requests.post(url, headers=headers, data=data)

# Parse response
if response.status_code == 200:
    token_info = response.json()
    access_token = token_info.get("access_token")
    refresh_token = token_info.get("refresh_token")
    expires_in = token_info.get("expires_in")
   
    print("Access Token:", access_token)
    print("Refresh Token:", refresh_token)
    print("Expires In:", expires_in, "seconds")
else:
    print("Failed to get token:", response.status_code, response.json())

