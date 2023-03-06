import logging

import requests

logging.basicConfig(filename='test.log', encoding='utf-8', level=logging.DEBUG)

url = "https://reqres.in"

response = requests.get(url).json()
print(type(response))


logging.info(f"{response}")