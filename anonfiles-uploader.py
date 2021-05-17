import requests
import json

#Defining URL
url = 'https://api.anonfiles.com/upload'

#Defining filename
filename = input("File path: ")

#Setting Response & Sending it
files = {'file': (open(filename, 'rb'))}
print("Uploading ", filename)
r = requests.post(url, files=files)
response = json.loads(r.text)

#Print Status
if response['status']:
    url0 = response['data']['file']['url']['short']
    print(f'URL: {url0}')
    print("")
    input("Press any key to exit")
else:
    message = resp['error']['message']
    errtype = resp['error']['type']
    print(f'[ERROR] {message}\n{errtype}')
    print("")
    input("Press any key to exit")

    