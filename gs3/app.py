import requests
import json

URL = "http://localhost:8000/studentapi/"


def get_data(id=1):
    data = {}
    if id is not None:
        data = {'id': id}
        json_data = json.dumps(data)
        r = requests.get(url=URL, data=json_data)
        data = r.json()
        print(data)
        get_data(1)
