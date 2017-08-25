import requests

chain = '817'
while 1:
    r = requests.get('http://www.pythonchallenge.com/pc/def/linkedlist.php?nothing='+chain)
    print(r.text[:5],'     ',chain)
    try:
        x = int(r.text[-5:].strip())
    except ValueError:
        chain = r.text[-3:]
        continue
    chain = r.text[-5:].strip()
