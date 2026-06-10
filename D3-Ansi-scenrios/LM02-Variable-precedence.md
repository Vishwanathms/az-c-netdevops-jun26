Here is a simple lab demonstrating all three methods.

---

# 1. Variable Inside Playbook YAML

### playbook.yml

```yaml
---
- name: Variable Demo
  hosts: Routers
  gather_facts: no

  vars:
    ntp_server: 192.168.10.100

  tasks:
    - name: Display variable
      debug:
        msg: "NTP Server = {{ ntp_server }}"
```

Run:

```bash
ansible-playbook -i inventory.ini playbook.yml
```

Output:

```text
NTP Server = 192.168.10.100
```

---

# 2. Variable Using group_vars

### Directory Structure

```text
project/
├── inventory.ini
├── playbook.yml
└── group_vars/
    └── Routers.yml
```

### inventory.ini

```ini
[Routers]
192.168.10.1
192.168.10.2
```

### group_vars/Routers.yml

```yaml
---
ntp_server: 192.168.10.200
```

### playbook.yml

```yaml
---
- name: Variable Demo
  hosts: Routers
  gather_facts: no

  tasks:
    - name: Display variable
      debug:
        msg: "NTP Server = {{ ntp_server }}"
```

Run:

```bash
ansible-playbook -i inventory.ini playbook.yml
```

Output:

```text
NTP Server = 192.168.10.200
```

Ansible automatically loads variables from `group_vars/Routers.yml`.

---

# 3. Variable Using CLI (-e)

### playbook.yml

```yaml
---
- name: Variable Demo
  hosts: Routers
  gather_facts: no

  tasks:
    - name: Display variable
      debug:
        msg: "NTP Server = {{ ntp_server }}"
```

Run:

```bash
ansible-playbook \
-i inventory.ini \
playbook.yml \
-e "ntp_server=192.168.10.250"
```

Output:

```text
NTP Server = 192.168.10.250
```

---

# Variable Precedence Demo

### playbook.yml

```yaml
---
- name: Variable Demo
  hosts: Routers
  gather_facts: no

  vars:
    ntp_server: 192.168.10.100

  tasks:
    - debug:
        msg: "NTP Server = {{ ntp_server }}"
```

### group_vars/Routers.yml

```yaml
ntp_server: 192.168.10.200
```

### Run with CLI

```bash
ansible-playbook \
-i inventory.ini \
playbook.yml \
-e "ntp_server=192.168.10.250"
```

Result:

```text
NTP Server = 192.168.10.250
```

Priority:

```text
CLI (-e)                  Highest
Playbook vars
group_vars
Inventory vars
Role defaults             Lowest
```
