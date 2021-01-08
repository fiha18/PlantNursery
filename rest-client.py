import requests



#Get auth token

def get_token():
    url = "http://127.0.0.1:8000/api/auth/"
    response = requests.post(url, data={'username':'Fee101','password':'asdfghjkl'})
    return (response.json())

def get_data():
    url = "http://127.0.0.1:8000/api/auth/"
    token = get_token()
    header = {'Authorization' : f'Token {get_token()}'}
    response = requests.get(url, headers= header)
    print(response.text)