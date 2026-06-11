
## This example is to read json file from python
## create json file and python file 


# create file called "device.json"
```
{
  "hostname": "R1",
  "ip": "192.168.1.1",
  "vendor": "Cisco"
}
```

# create file called  ex04.py

```
import json

with open("device.json") as f:
    data = json.load(f)

print(data["hostname"])
```


## This example is to read complex json file from python

# example02

* filename "device.json"
```
{
  "R1": {
    "ip": "192.168.1.1",
    "vendor": "Cisco",
    "type": "router-cat1",
    "model": "3660"
  },
  "R2": {
    "ip": "192.168.1.2",
    "vendor": "Cisco",
    "type": "router-cat2",
    "model": "7200"
  }
}
```

* filename "ex05.py"
```
import json

with open("device.json") as f:
    inventory = json.load(f)

device = inventory["R1"]

print(f"Hostname : R1")
print(f"IP       : {device['ip']}")
print(f"Vendor   : {device['vendor']}")
print(f"Type     : {device['type']}")
print(f"Model    : {device['model']}")
```

## This example is to read key value (R1 or R2) while execution and then pick correcposnding values in json file from python

# example02

* same json file

* python -- ex06.py
```
import json

with open("inventory.json") as f:
    inventory = json.load(f)

device_name = input("Enter device name (R1/R2)")
device = inventory[device_name]

print(f"Hostname : {device_name}")
print(f"IP       : {device['ip']}")
print(f"Vendor   : {device['vendor']}")
print(f"Type     : {device['type']}")
print(f"Model    : {device['model']}")
```