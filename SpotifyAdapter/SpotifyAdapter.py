import requests
import webbrowser
import base64

class SpotifyAdapter:
    client_id = "d0f0f7d875c745dda41a5f8d4be43a4a"
    client_secret = "0a9c2b122bd34e0ba1cb26225dec1877"
    redirect_uri = 'http://localhost:3000'
    url_accounts = 'https://accounts.spotify.com'
    api_url = "https://api.spotify.com/v1"
    code = ""
    scope = "user-modify-playback-state"
    access_token = ""
    refresh_token = ""
    _instance = None
    reproducing = False

    def __new__(cls):
        if cls._instance is None:
            # print('Creating the object')
            cls._instance = super(SpotifyAdapter, cls).__new__(cls)
        return cls._instance
    
    def authenticate_user(self):
        auth_endpoint = self.url_accounts[:]+"/authorize"
        auth_endpoint += '?response_type=code'
        auth_endpoint += '&client_id=' + self.client_id
        auth_endpoint += '&scope=' + self.scope
        auth_endpoint += '&redirect_uri=' + self.redirect_uri
        # response = requests.get(self.url)
        webbrowser.open(auth_endpoint)

    def get_auth_code(self):
        authCodeResponse = requests.get(self.redirect_uri+"/code")

        self.code =  authCodeResponse.text
    def get_access_token(self):
        body = {
        'code': self.code,
        'redirect_uri': self.redirect_uri,
        'grant_type': 'authorization_code'
        }
        headers = {
            'Authorization': 'Basic '+ 
                                str(base64.b64encode(
                                    (self.client_id + ":" + self.client_secret).encode("ascii")
                                ).decode('utf-8')),
            'Content-Type': "application/x-www-form-urlencoded"
        }
        response = requests.post(self.url_accounts+"/api/token", data = body, headers=headers)
        self.access_token = response.json().get('access_token')
    
    def skip_to_next(self):
        headers = {"Authorization": "Bearer " + self.access_token}
        requests.post(self.api_url + "/me/player/next", headers=headers)
    
    def skip_to_previous(self):
        headers = {"Authorization": "Bearer "+self.access_token}
        requests.post(self.api_url + "/me/player/previous", headers=headers)
    
    def toggle_pause_play(self):
        headers = {"Authorization": "Bearer "+self.access_token}
        if self.reproducing:
            requests.put(self.api_url + "/me/player/pause", headers=headers)
        else:
            requests.put(self.api_url + "/me/player/play", headers=headers, data = "{\"position_ms\":0}")
        self.reproducing = not self.reproducing
