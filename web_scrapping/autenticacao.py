import requests

url = 'http://httpbin.org/basic-auth/user/passwd'

req = requests.get(url, auth=('user', 'passwd'))
print(req.status_code)