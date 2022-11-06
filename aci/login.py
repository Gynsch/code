import json
import requests
import urllib3
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)


def login(
        url,
        username,
        password):

    base_url = 'https://' + url + '/api/'

    # create credentials structure
    name_pwd = {
        'aaaUser':
            {'attributes':
                {'name': username,
                 'pwd': password
                 }
             }
    }
    json_credentials = json.dumps(name_pwd)
    # log in to API
    login_url = base_url + 'aaaLogin.json'
    headers = {
        'content-type': 'application/json'
    }

    try:
        response = requests.request(
            'POST',
            login_url,
            headers=headers,
            data=json_credentials,
            timeout=2,
            verify=False
        )
        data = json.loads(response.text)
        token = {}
        token['APIC-Cookie'] = data["imdata"][0]["aaaLogin"]["attributes"]["token"]
        return token
    except:
        print('Error occured!!!')
