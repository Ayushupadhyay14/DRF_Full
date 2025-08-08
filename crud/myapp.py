# import requests
# import json

# URL = "http://127.0.0.1:8000/studentapi/"


# def get_data(id=None):
#     data = {}
#     if id is not None:
#         data = {'id': id}
#         json_data = json.dumps(data)
#         r = requests.get(url=URL, data=json_data)
#         data = r.json()
#         print(data)
# get_data()
#
#
#       """GET DATA METHOD """
"""import requests

URL = "http://127.0.0.1:8000/studentapi/"


def get_data(id=None):
    if id:
        r = requests.get(url=URL, params={'id': id})
    else:
        r = requests.get(url=URL)
    print(r.json())


# सभी डेटा लाने के लिए
get_data()"""


# <-----POST DATA METHOD---->
import requests
import json

URL = "http://127.0.0.1:8000/studentapi/"


def post_data():
    data = {
        'name': 'Aniket Tripathi',
        'age': 20,
        'email': 'test@gmail.com'
    }
    json_data = json.dumps(data)
    r = requests.post(url=URL, data=json_data)
    data = r.json()
    print(data)


post_data()
