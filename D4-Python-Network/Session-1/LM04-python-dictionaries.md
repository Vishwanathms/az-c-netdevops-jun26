A real-world network automation scenario is a much better fit for **dictionaries** because each device has multiple attributes.


## Simple dictionaries with for loop 

```python
inventory = {
    "R1": {
        "type": "router-cat1",
        "model": "3660"
    },
    "R2": {
        "type": "router-cat2",
        "model": "7200"
    }
}

for hostname, details in inventory.items():
    print(f"Hostname :  {hostname}")
    print(f"Type     :  {details['type']}")
    print(f"Model    :  {details['model']}")
```


## Use Case: Network Device Inventory

Suppose you are managing devices in a data center and need to store:

* Hostname
* Device Type
* Model
* Management IP
* Location

### Inventory Data

```python
inventory = {
    "R1": {
        "type": "router",
        "model": "3660",
        "ip": "192.168.10.1",
        "location": "Chennai"
    },
    "R2": {
        "type": "switch",
        "model": "3750",
        "ip": "192.168.10.2",
        "location": "Bangalore"
    },
    "R3": {
        "type": "router",
        "model": "7200",
        "ip": "192.168.10.3",
        "location": "Mumbai"
    }
}
```

---

## Function to Display Device Inventory

```python
def show_inventory(devices):
    for hostname, details in devices.items():
        print(f"Hostname : {hostname}")
        print(f"Type     : {details['type']}")
        print(f"Model    : {details['model']}")
        print(f"IP       : {details['ip']}")
        print(f"Location : {details['location']}")
        print("-" * 30)

show_inventory(inventory)
```

### Output

```text
Hostname : R1
Type     : router
Model    : 3660
IP       : 192.168.10.1
Location : Chennai
------------------------------
Hostname : R2
Type     : switch
Model    : 3750
IP       : 192.168.10.2
Location : Bangalore
------------------------------
Hostname : R3
Type     : router
Model    : 7200
IP       : 192.168.10.3
Location : Mumbai
------------------------------
```

---

## Use Case: Configure Only Routers

A common network automation requirement is to run tasks only on routers.

```python
def configure_routers(devices):
    for hostname, details in devices.items():
        if details["type"] == "router":
            print(f"Connecting to {hostname} ({details['ip']})")
            print("Applying OSPF Configuration")
            print()

configure_routers(inventory)
```

### Output

```text
Connecting to R1 (192.168.10.1)
Applying OSPF Configuration

Connecting to R3 (192.168.10.3)
Applying OSPF Configuration
```

---

## Use Case: Generate Ansible Inventory

```python
def generate_inventory(devices):
    print("[routers]")

    for hostname, details in devices.items():
        if details["type"] == "router":
            print(details["ip"])

generate_inventory(inventory)
```

### Output

```text
[routers]
192.168.10.1
192.168.10.3
```

---

## More Pythonic Approach (List of Dictionaries)

This format is commonly used when reading JSON/YAML files.

```python
devices = [
    {
        "hostname": "R1",
        "type": "router",
        "model": "3660",
        "ip": "192.168.10.1"
    },
    {
        "hostname": "R2",
        "type": "switch",
        "model": "3750",
        "ip": "192.168.10.2"
    },
    {
        "hostname": "R3",
        "type": "router",
        "model": "7200",
        "ip": "192.168.10.3"
    }
]

for device in devices:
    print(
        f"{device['hostname']} | "
        f"{device['type']} | "
        f"{device['model']} | "
        f"{device['ip']}"
    )
```

### Why dictionaries are preferred in Network Automation

Instead of maintaining separate arrays:

```python
routers = ["R1", "R2", "R3"]
types   = ["router", "switch", "router"]
models  = ["3660", "3750", "7200"]
ips     = ["192.168.10.1", "192.168.10.2", "192.168.10.3"]
```

which can get out of sync, a dictionary keeps all information for a device together:

```python
inventory["R1"]["model"]
inventory["R1"]["ip"]
inventory["R1"]["type"]
```
