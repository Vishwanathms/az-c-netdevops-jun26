# Lab 7: Function

### Objective

Create reusable code.

### Code

```python
def device_info(hostname):
    print("Connecting to", hostname)

device_info("R1")
device_info("R2")
```

### Output

```text
Connecting to R1
Connecting to R2
```

### Challenge

Pass hostname and IP address.

---

# Lab 8: Loop Through Dictionary

### Objective

Display device inventory.

### Code

```python
devices = {
    "R1": "192.168.10.1",
    "R2": "192.168.10.2",
    "R3": "192.168.10.3"
}

for device, ip in devices.items():
    print(device, "=", ip)
```

### Output

```text
R1 = 192.168.10.1
R2 = 192.168.10.2
R3 = 192.168.10.3
```

---

# Lab 9: Multiple Lists (Network Inventory)

### Objective

Map routers to models.

### Code

```python
routers = ["R1", "R2", "R3"]
models = ["3660", "3750", "7200"]

for router, model in zip(routers, models):
    print(router, "=", model)
```

### Output

```text
R1 = 3660
R2 = 3750
R3 = 7200
```

---

# Lab 10: Network Device Inventory (Real-World Mini Project)

### Objective

Create a simple inventory system.

### Code

```python
devices = [
    {"hostname": "R1", "ip": "192.168.10.1", "model": "3660"},
    {"hostname": "R2", "ip": "192.168.10.2", "model": "7200"},
    {"hostname": "SW1", "ip": "192.168.10.10", "model": "3750"}
]

for device in devices:
    print("----------------")
    print("Hostname:", device["hostname"])
    print("IP:", device["ip"])
    print("Model:", device["model"])
```

### Output

```text
----------------
Hostname: R1
IP: 192.168.10.1
Model: 3660

----------------
Hostname: R2
IP: 192.168.10.2
Model: 7200

----------------
Hostname: SW1
IP: 192.168.10.10
Model: 3750
```

---

# Final Practice Assignment

Create a Python script that:

1. Stores 5 routers in a list.
2. Stores their IP addresses in another list.
3. Uses a loop to print:

```text
Router R1 has IP 192.168.10.1
Router R2 has IP 192.168.10.2
Router R3 has IP 192.168.10.3
Router R4 has IP 192.168.10.4
Router R5 has IP 192.168.10.5
```

4. Create a function called `check_device()` that accepts hostname and IP.
5. Print:

```text
Connecting to R1 (192.168.10.1)
```

This sequence works very well for a **2–3 hour Python fundamentals lab session** before introducing JSON, YAML, Netmiko, Requests, and network automation libraries.
