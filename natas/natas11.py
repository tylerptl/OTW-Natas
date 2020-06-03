import base64

key =''
plaintext = '{"showpassword":"no","bgcolor":"#ffffff"}'
ciphertext = ''



for c1, c2 in zip(base64.b64decode('ClVLIh4ASCsCBE8lAxMacFMZV2hdVVotEhhUJQNVAmhSEV4sFxFeaAw='), plaintext):
    #print(c1 + " " + c2)
    key += chr(ord(c1) ^ ord(c2))
    #print("Embedded key: " + key)
print("Key = " + key)

# Will have to manually asign key = 'qw8J'
key = 'qw8J'
plaintext = '{"showpassword":"yes","bgcolor":"#ffffff"}'
for i in range(len(plaintext)):
  str = plaintext[i]
  ciphertext += chr(ord(str) ^ ord(key[i % len(key)]))

print base64.b64encode(ciphertext)