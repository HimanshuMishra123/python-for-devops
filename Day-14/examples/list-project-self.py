# This code sample uses the 'requests' library:
# http://docs.python-requests.org
import requests                               #request package is used to make api calls
from requests.auth import HTTPBasicAuth       # for Http authentication HTTPBasicAuth module is used
import json

url = "https://mankur123.atlassian.net/rest/api/3/project"     #add your domain

API_TOKEN = " "                                                #add your Jira API Token from sticky notes

auth = HTTPBasicAuth("m.ankur123@gmail.com", API_TOKEN)

headers = {
  "Accept": "application/json"
}

response = requests.request(
   "GET",
   url,
   headers=headers,
   auth=auth
)

#print(json.dumps(json.loads(response.text), sort_keys=True, indent=4, separators=(",", ": ")))
#above will return list of projects


output = json.loads(response.text)  #to parse the json we convert it into dictionaries
#use Json formatter to better view of Json and iteratete through and do indexing in list 
name = output[0]["name"]           # you can create a for loop to print all projects instead of one by one

print(name)

