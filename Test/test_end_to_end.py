import requests
import json
import jsonpath

def test_add_new_data():
    app_url="http://thetestingworldapi.com/api/studentsDetails"
    f=open('C:/Users/sagar/Desktop/request.json','r')
    request_json=json.loads(f.read())
    response=requests.post(app_url,request_json)
    #print(response.text)
    id=jsonpath.jsonpath(response.json(),'id')
    print(id[0])

    tech_api_url= "http://thetestingworldapi.com/api/technicalskills"
    f = open("C:\\Users\\sagar\\Desktop\\techdetails.json", "r")
    request_json = json.loads(f.read())
    request_json['id']=int(id[0])
    request_json['st_id']=id[0]
    response = requests.post(tech_api_url, request_json)
    print(response.text)

    finaldetails="http://thetestingworldapi.com/api/FinalStudentDetails/"+str(id[0])
    response=requests.get(finaldetails)
    print(response.text)

