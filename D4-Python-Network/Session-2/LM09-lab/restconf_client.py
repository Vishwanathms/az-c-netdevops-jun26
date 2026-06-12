import requests

requests.packages.urllib3.disable_warnings()

HEADERS = {
    "Accept": "application/yang-data+json",
    "Content-Type": "application/yang-data+json"
}

def create_loopback(host, user, password, loopback_ip):

    url = (
        f"https://{host}/restconf/data/"
        "ietf-interfaces:interfaces"
    )

    payload = {
        "ietf-interfaces:interface": {
            "name": "Loopback10",
            "description": "Created_By_Python",
            "type": "iana-if-type:softwareLoopback",
            "enabled": True,
            "ietf-ip:ipv4": {
                "address": [
                    {
                        "ip": loopback_ip,
                        "netmask": "255.255.255.255"
                    }
                ]
            }
        }
    }

    response = requests.post(
        url,
        auth=(user, password),
        headers=HEADERS,
        json=payload,
        verify=False
    )

    return response