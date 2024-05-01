import requests

API_VERSION = "v2"
DEV_API_URL = "https://www.devapi.slick-pay.com/api/"
PROD_API_URL = "https://www.prodapi.slick-pay.com/api/"


class SlickPayApi:
    def __init__(self) -> None:
        self.api_version = API_VERSION
        self._config = {}

    def config(self, environment, public_key):
        if environment in ["dev", "prod"]:
            self._config["public_key"] = public_key

        if environment == "dev":
            self._config["base_url"] = DEV_API_URL

        if environment == "prod":
            self._config["base_url"] = PROD_API_URL
        
        return self._config

    def build_request_url(self, url_path):
        return f'{self._config["base_url"]}{self.api_version}/{url_path}'

    @property
    def headers(self):
        if self._config:
            return {
                "Authorization": f'Bearer {self._config["public_key"]}',
                "Accept": "application/json",
            }
    
    def post(self, url_path, data):
        request_url = self.build_request_url(url_path=url_path)
        if self.headers:
            response = requests.post(url=request_url, headers=self.headers, json=data)
            return response.json()

    def get(self, url_path):
        request_url = self.build_request_url(url_path=url_path)
        if self.headers:
            response = requests.get(url=request_url, headers=self.headers)
            return response.json()

    def put(self, url_path, data):
        request_url = self.build_request_url(url_path=url_path)
        if self.headers:
            response = requests.put(url=request_url, headers=self.headers, json=data)
            return response.json()

    def delete(self, url_path):
        request_url = self.build_request_url(url_path=url_path)
        if self.headers:
            response = requests.delete(url=request_url, headers=self.headers)
            return response.json()
