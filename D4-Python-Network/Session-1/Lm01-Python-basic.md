Since you are teaching **Python for Network Automation**, start with very simple labs and gradually move toward networking use cases. Here are some beginner-friendly hands-on labs.

# Lab 1: Variables and Data Types

### Objective

Understand variables and different data types.

### Code

```python
hostname = "R1"
ip_address = "192.168.10.1"
port_count = 24
cpu_usage = 45.5

print("Hostname:", hostname)
print("IP Address:", ip_address)
print("Ports:", port_count)
print("CPU Usage:", cpu_usage)
```

### Expected Output

```text
Hostname: R1
IP Address: 192.168.10.1
Ports: 24
CPU Usage: 45.5
```

### Challenge

Add a variable called `location`.

---

# Lab 2: User Input

### Objective

Accept input from users.

### Code

```python
hostname = input("Enter router name: ")

print("Device Name:", hostname)
```

### Sample Run

```text
Enter router name: R1
Device Name: R1
```

### Challenge

Ask for IP address and display it.

---

# Lab 3: If-Else Statement

### Objective

Check device status.

### Code

```python
status = input("Enter device status (up/down): ")

if status == "up":
    print("Device is reachable")
else:
    print("Device is unreachable")
```

### Sample Output

```text
Enter device status (up/down): up
Device is reachable
```

### Challenge

Add a third condition for "maintenance".

---

# Lab 4: For Loop

### Objective

Loop through devices.

### Code

```python
devices = ["R1", "R2", "R3"]

for device in devices:
    print(device)
```

### Output

```text
R1
R2
R3
```

### Challenge

Print:

```text
Checking R1
Checking R2
Checking R3
```

---

# Lab 5: List Operations

### Objective

Store multiple network devices.

### Code

```python
devices = ["R1", "R2", "SW1"]

print(devices)

devices.append("FW1")

print(devices)
```

### Output

```text
['R1', 'R2', 'SW1']
['R1', 'R2', 'SW1', 'FW1']
```

### Challenge

Remove SW1 from the list.

---

# Lab 6: Dictionary

### Objective

Store device information.

### Code

```python
router = {
    "hostname": "R1",
    "ip": "192.168.10.1",
    "model": "Cisco 3660"
}

print(router["hostname"])
print(router["ip"])
```

### Output

```text
R1
192.168.10.1
```

### Challenge

Add location information.

---

