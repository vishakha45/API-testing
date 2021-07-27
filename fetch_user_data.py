import requests
import json
import jsonpath

url="https://reqres.in/api/users?page=2"

response=requests.get(url)

print(response,type(response))
print("\n")
print(response.content)
print("\n")
print(response.headers)
json_response=json.loads(response.text)
print("\n")
print(json_response)
print("\n")
print(type(json_response))

pages=jsonpath.jsonpath(json_response,'total_pages')
print("\n")
print(pages[0])
assert pages[0]==2