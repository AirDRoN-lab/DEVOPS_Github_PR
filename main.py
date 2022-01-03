import requests
import sys
import os

username = 'AirDRoN-lab'
token = os.environ.get("GITHUB_TOKEN")
print(token)

r = requests.get('https://api.github.com/events')


