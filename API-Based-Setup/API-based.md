Since you've already enabled SSH, I recommend using **RESTCONF APIs** on CSR1000v. Cisco IOS-XE exposes YANG models over HTTPS, which Python can consume using the `requests` library. RESTCONF is officially supported on IOS-XE/CSR1000v. ([Cisco][1])

## Enable RESTCONF on CSR1000v

```cisco
conf t

ip http server
ip http secure-server

restconf

username admin privilege 15 secret Cisco123!

end

write memory
```

Verify:

```cisco
show running-config | include restconf
```

---

# Python Example 1: Get Hostname

Install dependency:

```bash
pip install requests
```

Code:

```python
import requests
import urllib3

urllib3.disable_warnings()

ROUTER_IP = "192.168.1.10"
USERNAME = "admin"
PASSWORD = "Cisco123!"

url = f"https://{ROUTER_IP}/restconf/data/Cisco-IOS-XE-native:native/hostname"

headers = {
    "Accept": "application/yang-data+json"
}

response = requests.get(
    url,
    headers=headers,
    auth=(USERNAME, PASSWORD),
    verify=False
)

print("Status Code:", response.status_code)
print(response.json())
```

This uses the IOS-XE RESTCONF hostname endpoint documented in Cisco examples. ([GitHub][2])

---

# Python Example 2: Get Interface Information

```python
import requests
import urllib3
import json

urllib3.disable_warnings()

url = "https://192.168.1.10/restconf/data/ietf-interfaces:interfaces"

response = requests.get(
    url,
    auth=("admin", "Cisco123!"),
    headers={
        "Accept": "application/yang-data+json"
    },
    verify=False
)

print(json.dumps(response.json(), indent=4))
```

---

# Python Example 3: Configure Loopback Interface

```python
import requests
import urllib3

urllib3.disable_warnings()

url = "https://192.168.1.10/restconf/data/Cisco-IOS-XE-native:native/interface/Loopback=100"

payload = {
    "Cisco-IOS-XE-native:Loopback": {
        "name": 100,
        "ip": {
            "address": {
                "primary": {
                    "address": "100.100.100.1",
                    "mask": "255.255.255.255"
                }
            }
        }
    }
}

response = requests.put(
    url,
    auth=("admin", "Cisco123!"),
    headers={
        "Content-Type": "application/yang-data+json",
        "Accept": "application/yang-data+json"
    },
    json=payload,
    verify=False
)

print(response.status_code)
print(response.text)
```

RESTCONF supports standard HTTP verbs such as GET, PUT, PATCH, POST, and DELETE for reading and modifying configuration. ([networkop][3])

---

# Python Example 4: Get Running Hostname and IOS Version

```python
import requests
import urllib3

urllib3.disable_warnings()

router = "192.168.1.10"
auth = ("admin", "Cisco123!")

endpoints = {
    "hostname": "/restconf/data/Cisco-IOS-XE-native:native/hostname",
    "version": "/restconf/data/Cisco-IOS-XE-native:native/version"
}

for name, endpoint in endpoints.items():
    url = f"https://{router}{endpoint}"

    r = requests.get(
        url,
        auth=auth,
        headers={"Accept": "application/yang-data+json"},
        verify=False
    )

    print(f"\n{name.upper()}")
    print(r.json())
```

The hostname and version RESTCONF paths are commonly used in Cisco IOS-XE examples. ([Cisco DevNet][4])

---

# Enterprise-Style Example for Your Automation Labs

```python
from requests.auth import HTTPBasicAuth
import requests
import urllib3

urllib3.disable_warnings()

class CSR1000vAPI:

    def __init__(self, host, username, password):
        self.host = host
        self.auth = HTTPBasicAuth(username, password)
        self.headers = {
            "Accept": "application/yang-data+json",
            "Content-Type": "application/yang-data+json"
        }

    def get_hostname(self):
        url = f"https://{self.host}/restconf/data/Cisco-IOS-XE-native:native/hostname"
        return requests.get(
            url,
            auth=self.auth,
            headers=self.headers,
            verify=False
        ).json()

router = CSR1000vAPI(
    host="192.168.1.10",
    username="admin",
    password="Cisco123!"
)

print(router.get_hostname())
```

This is a good starting point for building your **Network Automation Engineer** labs using CSR1000v, Python, RESTCONF, Jenkins, and Ansible.

[1]: https://www.cisco.com/c/en/us/td/docs/ios-xml/ios/prog/configuration/173/b_173_programmability_cg/restconf_protocol.html?utm_source=chatgpt.com "Chapter: RESTCONF Protocol - Cisco IOS XE 17"
[2]: https://github.com/CiscoDevNet/restconf-examples/blob/master/restconf-102/get_hostname.py?utm_source=chatgpt.com "restconf-examples/restconf-102/get_hostname.py at master"
[3]: https://networkop.co.uk/blog/2017/02/15/restconf-yang/?utm_source=chatgpt.com "Introduction to YANG Programming and RESTCONF on ..."
[4]: https://developer.cisco.com/codeexchange/github/repo/jillesca/xe_hello_world_restconf/?utm_source=chatgpt.com "jillesca/xe_hello_world_restconf - Cisco Code Exchange"
