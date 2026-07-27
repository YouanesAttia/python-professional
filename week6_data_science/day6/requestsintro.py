import requests
from PIL import Image
from io import BytesIO


r = requests.get('https://api.github.com/events')
print(r)

# Passing Parameters In URLs
payload = {'key1': 'value1', 'key2': 'value2'}
r = requests.get('https://httpbin.org/get', params=payload)
print(r.url)         # https://httpbin.org/get?key1=value1&key2=value2

payload = {'key1': 'value1', 'key2': ['value2', 'value3']}
r = requests.get('https://httpbin.org/get', params=payload)
print(r.url)         # https://httpbin.org/get?key1=value1&key2=value2&key2=value3

# Response Content
r = requests.get('https://api.github.com/events')
print(r.text)      # '[{"repository":{"open_issues":0,"url":"https://github.com/...
r.content          # b'[{"repository":{"open_issues":0,"url":"https://github.com/...
r.encoding = 'ISO-8859-1'

# Binary Response Content
i = Image.open(BytesIO(r.content))


# JSON Response Content
r = requests.get('https://api.github.com/events')
r.json()            # [{'repository': {'open_issues': 0, 'url': 'https://github.com/...
r.raise_for_status()       # To check that a request is successful


# Raw Response Content
r = requests.get('https://api.github.com/events', stream=True)
r.raw                     # <urllib3.response.HTTPResponse object at 0x101194810>
r.raw.read(10)            # b'\x1f\x8b\x08\x00\x00\x00\x00\x00\x00\x03'
with open('file', 'wb') as fd:
    for chunk in r.iter_content(chunk_size=128):
        fd.write(chunk)


# Custom Headers
url = 'https://api.github.com/some/endpoint'
headers = {'user-agent': 'my-app/0.0.1'}
r = requests.get(url, headers=headers)


# More complicated POST requests
payload = {'key1': ['value1', 'value2'], 'key2': 'value3'}
r = requests.post('https://httpbin.org/post', data=payload)
print(r.text)     
"""
{
  ...
  "form": {
    "key2": "value2",
    "key1": "value1"
  },
  ...
}
"""


# POST a Multipart-Encoded File
