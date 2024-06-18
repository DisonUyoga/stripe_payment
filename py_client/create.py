import requests

endpoint="http://127.0.0.1:8000/api/v1/stripe/"
token_endpoint="http://127.0.0.1:8000/api/users/token/"

data={
    "username":"dison33@gmail.com",
    "password":"disonnnnnnn123"
}

token=requests.post(token_endpoint, json=data).json()["token"]

headers={
    "Authorization": f"Token {token}"
}

reply_data={"name":"pizza", "description":"testing", "price": 1200, "quantity":5}
response=requests.post(endpoint, json=reply_data, headers=headers)
print(response.json())