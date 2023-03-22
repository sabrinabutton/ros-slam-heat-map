import base64
import json
import requests
import os
import subprocess
import random
import string

from base64 import b64encode

# TO DO: Install postman on the Pi to get all this info

client_id = '5f59b96111571e5'
client_secret = 'ea3e6bdb795066b81fae5280c39d8f722b4b98d2'

headers = {"Authorization": "Client-ID 3958cfa79f989a3"}

api_key = 'my-api-key'

url_imgur = "https://api.imgur.com/3/upload.json"

# Get the image path
path = "/catkin_ws/src/hector_slam/hector_geotiff/maps/newest_map.png"

# Function to generate a random code


def get_random_string(length):
    # choose from all lowercase letter
    letters = string.ascii_lowercase
    result_str = ''.join(random.choice(letters) for i in range(length))
    return result_str


random_str = get_random_string(10)

# Post to Imgur
j1 = requests.post(
    url_imgur,
    headers=headers,
    data={
        'key': api_key,
        'image': b64encode(open(path, 'rb').read()),
        'type': 'base64',
        'name': 'heatmap' + random_str + '.jpg',
        'title': 'heatmap' + random_str
    }
)

# Then, send the URL of the image to the heat map viewer website.
url_post = "https://ventus-robotics.onrender.com/api/imgur_post"
# TODO: figure out where we get this url
requests.post(url_post, data={"url": ""})

