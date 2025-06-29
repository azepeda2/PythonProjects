import requests

# Replace with your actual client ID and client secret
client_id = 'vexupm44u2ry34vzskpheo4pdtydla'
client_secret = '4w9wj1jxaeamy7wqc1ywi9t472bif6'

# Define the endpoint and payload data
token_url = 'https://id.twitch.tv/oauth2/token'
data = {
    'client_id': client_id,
    'client_secret': client_secret,
    'grant_type': 'client_credentials'
}

# Make the POST request
response = requests.post(token_url, data=data)

# Check the response
if response.status_code == 200:
    # The request was successful
    response_data = response.json()
    access_token = response_data['access_token']
    token_type = response_data['token_type']
    print(f'Access Token: {access_token}')
    print(f'Token Type: {token_type}')
else:
    # Request failed
    print(f'Request failed with status code: {response.status_code}')
    print(response.text)
