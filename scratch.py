import requests as req
from json import dumps


BASE_URL = "http://10.6.21.76:8000"

# data = {
#   "alt_name": "",
#   "email": "nolan_wang@bjsmicschool.com",
#   "name": "Jonathan Fernandes",
#   "password": "123456",
#   "role": "student"
# }
#
# response = req.post(f"{BASE_URL}/users", data=dumps(data))
#
# print(response.status_code)
# print(response.json())

# data = {
#   "username": "jonathan_fernandes@bjsmicschool.com",
#   "password": "123456"
# }
#
# response = req.post(f"{BASE_URL}/token", data=data)
#
# print(response.status_code)
# print(response.json())

response = req.get(f"{BASE_URL}/tasks")
response.status_code
response.json()
