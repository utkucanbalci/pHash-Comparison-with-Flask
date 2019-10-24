import requests
import time
url1 = 'http://127.0.0.1:5000/api/computeImage'
url2 = 'http://127.0.0.1:5000/api/computePath'
url3 = 'http://127.0.0.1:5000/api/compareImages'
url4 = 'http://127.0.0.1:5000/api/comparePaths'

files1 = {'image': open('', 'rb')}
files2 = {'image1': open('', 'rb'), 'image2': open('', 'rb') }

path = ""
path2 = ""


resp1 = requests.post(url1, files = files1)
resp2 = requests.post(url2 +"?im1=2"+path)
resp3 = requests.post(url3, files = files2)
resp4 = requests.post(url4 +"?im1="+path+"&&im2="+path2)

print(resp1.text)
print(resp2.text)
print(resp3.text)
print(resp4.text)
