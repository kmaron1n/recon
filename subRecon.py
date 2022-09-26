import requests
import sys
import json

def help():
    help ="""
    subRecon by kmaron1n inspired by Domie13
    Usage: python3 subRecon.py <domain>
    """
    print(help)


if len(sys.argv)<2:
    help()
else:

    url = "https://api.securitytrails.com/v1/domain/{}/subdomains?children_only=false&include_inactive=true".format(sys.argv[1])

    headers = {
        "accept": "application/json",
        "APIKEY": "WGwQk4d44v04HclcxQNOftWldp4eI9sI"
    }

    response = requests.get(url, headers=headers)


dicc = json.loads(response.text)

arr = dicc['subdomains']
for i in arr:
    print(i+"."+sys.argv[1])