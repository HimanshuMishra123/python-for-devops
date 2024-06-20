# This code sample uses the 'requests' library:
# http://docs.python-requests.org
import requests
from requests.auth import HTTPBasicAuth
import json
from flask import Flask, request

app = Flask(__name__)

# Define a route that handles GET requests
@app.route('/createJira', methods=['POST'])
def createJira():

    url = "https://mankur123.atlassian.net/rest/api/3/issue"

    API_TOKEN=""

    auth = HTTPBasicAuth("m.ankur123@gmail.com", API_TOKEN)

    headers = {
        "Accept": "application/json",
        "Content-Type": "application/json"
    }

    payload = json.dumps( {
        "fields": {
            "description": {
                "content": [
                    {
                        "content": [
                            {
                                "text": "Order entry fails when selecting supplier.",
                                "type": "text"
                            }
                        ],
                        "type": "paragraph"
                        }
                    ],
                "type": "doc",
                "version": 1
        },
        "project": {
           "key": "HM"
        },
        "issuetype": {
            "id": "10005"
        },
        "summary": "Main order flow broken",
    },
    "update": {}
    } )


    gitdata = json.loads(request.get_json())
    issuebody = gitdata.get("comment", {}).get("body")
    if issuebody == "jira":
        response = requests.request(
            "POST",
            url,
            data=payload,
            headers=headers,
            auth=auth
    )
    else :
        return ("Please type jira if you are trying to create Jira issue")

    return json.dumps(json.loads(response.text), sort_keys=True, indent=4, separators=(",", ": "))

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)