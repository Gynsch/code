import json
import requests
import urllib3
from login import login
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)


def tenant(
        url,
        username,
        password,
        tenantName,
        tenantAlias,
        tenantDescr):

    token = login(url, username, password)

    base_url = 'https://' + url + '/api/'
    prepend_url = 'node/mo/uni/tn-' + tenantName
    url = base_url + prepend_url

    headers = {
        'Content-Type': 'application/json',
        'connection': 'keep-alive'
    }

    prepayload = {
        "fvTenant": {
            "attributes": {
                "dn": "uni/tn-" + tenantName,
                "name": tenantName,
                "nameAlias": tenantAlias,
                "descr": tenantDescr,
                "rn": "tn-" + tenantName,
                "status": "created"
            },
            "children": []
        }
    }
    payload = json.dumps(prepayload)

    response = requests.request(
        'POST',
        url,
        cookies=token,
        data=payload,
        headers=headers,
        verify=False
    )

    json_response = json.loads(response.text)

    try:
        print("ErrorCode: " + json_response["imdata"]
              [0]["error"]["attributes"]["code"])
        print("ErrorText: " + json_response["imdata"]
              [0]["error"]["attributes"]["text"])
    except:
        print("No Errors")

    return response.status_code


if __name__ == '__main__':
    url = 'sandboxapicdc.cisco.com'
    username = 'admin'
    password = '!v3G@!4@Y'
    tenantName = '3001'
    tenantAlias = '3001-Alias'
    tenantDescr = '3001-Descr'

    print("Response Status Code: " +
          str(
              tenant(
                  url,
                  username,
                  password,
                  tenantName,
                  tenantAlias,
                  tenantDescr
              )
          )
          )
