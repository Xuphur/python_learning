import requests
from requests import get, post


url = 'http://solarwinds.travelresorts.com/'


res = requests.get(url)


print('Response status_code : ' + str(res.status_code))


if (res.status_code == 200):
    print('Link is working fine')
else:
    print('Link is down')
