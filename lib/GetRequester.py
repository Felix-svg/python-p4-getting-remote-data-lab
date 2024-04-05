import requests
import json

class GetRequester:

    def __init__(self, url):
        self.url = url

    def get_response_body(self):
        # URL = 'https://learn-co-curriculum.github.io/json-site-example/endpoints/people.json'
        response = requests.get(self.url)
        return response.content

    def load_json(self):
        # URL = 'https://learn-co-curriculum.github.io/json-site-example/endpoints/people.json'
        response = requests.get(self.url)
        return response.json()



response_body = GetRequester('https://learn-co-curriculum.github.io/json-site-example/endpoints/people.json').get_response_body()
print(response_body)
json_object = GetRequester('https://learn-co-curriculum.github.io/json-site-example/endpoints/people.json').load_json()
print(json_object)