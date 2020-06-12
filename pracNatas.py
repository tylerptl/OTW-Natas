#Currently practicing natas16
import requests
import re 
from string import *

alpha_num = lowercase + uppercase + digits 
usn = 'natas17'
url = "http://%s.natas.labs.overthewire.org/?debug=true" % usn
password = '8Ps3H0GWbn5rd9S7GmAdgQNdkhPkq9cw'
login = (usn, password)
request = requests.Session()
confirmed_pass = list()

def get_source_code():
  connection = request.get(url, auth = login)

  pageContent = connection.text
  print pageContent


def solve_lab():
  connection = request.post(url, data = {"username" : "natas"}, auth = login )  
    #response = request.get(url, auth = login)
  response = connection.text
  print response
