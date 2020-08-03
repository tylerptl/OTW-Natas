#!usr/env/python3

import requests
import base64
import re
from urllib.parse import unquote

plaintext = '{"showpassword":"no","bgcolor":"#ffffff"}'
target_plaintext = '{"showpassword":"yes","bgcolor":"#ffffff"}'
session = requests.Session()
cookies = {"data":"ClVLIh4ASCsCBE8lAxMacFMOXTlTWxooFhRXJh4FGnBTVF4sFxFeLFMK"}
url = "http://natas11.natas.labs.overthewire.org"
response = session.get(url, auth=(
    "natas11", "U82q5TCMMQ9xuFoI3dYX61s7OZD9JKoK"))
pageContent = response.text
data_cookie = unquote(response.cookies['data'])
#print(pageContent)

print("Data cookie: (", data_cookie, ") \n")
def get_key(plain, cipher):
    key = ''
    for char1, char2 in zip(plain, cipher):
        key += chr(ord(char1) ^ ord(char2))
       # print("ord(char1) = ", ord(char1), " ord(char2) = ", ord(char2), " key = " , key)
    return key


def xor_encrypt(plain, key):
    cipher = ''
    for i, char in enumerate(plain):
        cipher += chr(ord(char) ^ ord(key[i % len(key)]))
    return cipher

decoded_data = base64.b64decode(data_cookie).decode()
#print("Decoded data: \n", decoded_data)

key = get_key(plaintext, decoded_data)


# print(key)

key = 'qw8J'  # Manually set key based on repeated sequence 
target_cookie = base64.b64encode( xor_encrypt(target_plaintext, key).encode()).decode()
target_cookie = unquote(target_cookie)
print(target_cookie)


