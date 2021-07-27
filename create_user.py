import requests
import json
import jsonpath

url="https://reqres.in/api/users"
file=open('C:\\Users\\sagar\\Desktop\\create_user.json','r')
json_input=file.read()
request_json=json.loads(json_input)

print(request_json)

response=requests.post(url,request_json)

assert response.status_code==201

response_json=json.loads(response.text)

id=jsonpath.jsonpath(response_json,'id')
print(id[0])
