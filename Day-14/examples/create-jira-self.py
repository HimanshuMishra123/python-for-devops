# This code sample uses the 'requests' library:
# http://docs.python-requests.org
import requests
from requests.auth import HTTPBasicAuth
import json

url = "https://mankur123.atlassian.net/rest/api/3/issue"


API_TOKEN = " " #add your Jira API Token from sticky notes

auth = HTTPBasicAuth("m.ankur123@gmail.com", API_TOKEN) #enter email and token

headers = {
  "Accept": "application/json",
  "Content-Type": "application/json"
}

#keep only mandatory (*) fields (refer manaul Create issue)
payload = json.dumps( {                    
  "fields": {  
    "description": {
      "content": [
        {
          "content": [
            {
              "text": "Bug in code, jira ticket",
              "type": "text"
            }
          ],
          "type": "paragraph"
        }
      ],
      "type": "doc",
      "version": 1
    },
    #for issue-type-id > goto Jira projects > Board > 3 flat dots on upper right side > configure board > left pane click on "issue types" > select any issue type > on the url end you will get issue ID (ex. for story 10005) 
    "issuetype": {
      "id": "10005"     
    },
    "project": {
      "key": "HM"   #inplace of id use key and get key from jira projects
    },
    "summary": "First jira ticket by himanshu",
  },
  "update": {}
} )

response = requests.request(
   "POST",
   url,
   data=payload,
   headers=headers,
   auth=auth
)

print(json.dumps(json.loads(response.text), sort_keys=True, indent=4, separators=(",", ": ")))