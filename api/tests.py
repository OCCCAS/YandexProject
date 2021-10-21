import requests as r
import datetime


uri = 'http://127.0.0.1:5000/api/register'
session = r.Session()
# session.auth = ('Timur', '123')

data = {
    'name': 'Timur',
    'surname': 'Pavlov',
    'birthday': int(datetime.datetime(2006, 3, 23, 0, 0, 0).timestamp()),
    'gender': 'M',
    'password': '123'
}
auth = session.post(uri, json=data)

if auth.status_code == 200:
    print(auth.json())

