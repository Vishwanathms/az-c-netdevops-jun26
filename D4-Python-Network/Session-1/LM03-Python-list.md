In Python, you can pass an array (typically a **list**) to a function just like any other variable.

### Example 1: Pass a List to a Function

```python
def show_devices(devices):
    for device in devices:
        print(device)

routers = ["R1", "R2", "R3"]

show_devices(routers)
```

**Output:**

```text
R1
R2
R3
```

---

### Example 2: Pass a List and Return a Value

```python
def calculate_sum(numbers):
    total = 0
    for num in numbers:
        total += num
    return total

values = [10, 20, 30, 40]

result = calculate_sum(values)
print(result)
```

**Output:**

```text
100
```

---

### Example 3: Modify the List Inside the Function

Lists are mutable, so changes inside the function affect the original list.

```python
def add_router(devices):
    devices.append("R4")

routers = ["R1", "R2", "R3"]

add_router(routers)

print(routers)
```

**Output:**

```text
['R1', 'R2', 'R3', 'R4']
```

---

### Example 4: Passing Multiple Values Using `*args`

```python
def configure_devices(*devices):
    for device in devices:
        print(f"Configuring {device}")

configure_devices("R1", "R2", "R3")
```

**Output:**

```text
Configuring R1
Configuring R2
Configuring R3
```

---

### Example 5: Passing a List as Individual Arguments

```python
def show_devices(dev1, dev2, dev3):
    print(dev1, dev2, dev3)

routers = ["R1", "R2", "R3"]

show_devices(*routers)
```

**Output:**

```text
R1 R2 R3
```

---

### Network Automation Example

```python
def backup_configs(router_list):
    for router in router_list:
        print(f"Taking backup of {router}")

routers = [
    "192.168.10.1",
    "192.168.10.2",
    "192.168.10.3"
]

backup_configs(routers)
```