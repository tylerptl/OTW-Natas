#! /usr/bin/env python

import requests
import re

usn = 'natas22'
url = 'http://%s.natas.labs.overthewire.org/?revelio=1' % usn
passwd = 'chG9fbe1Tq2eWVMgjYYD1MsfIvN461kJ'
login = (usn, passwd)

request = requests.Session()
def get_source_code():
  connection = request.get(url, auth=login, allow_redirects = False)
  pageContent = connection.text
  print pageContent;


#def solve_lab():
  