import requests


json_result = requests.get("http://localhost:8000/api/todos").json()
print(json_result)

for special in json_result:
    print(special["title"])
    print(special["id"])
    print(special["completed"])
    print(special["order"])
