import requests
url = 'http://127.0.0.1:5000/alarms'
files = {'image': ('1.jpg', open ('1.jpg', 'rb'), 'image/png')}
r = requests.post (url, files=files)
print (r.text)
