## Method 1: Pass a YAML Variable File with `-e @file`

### vars.yml

```yaml
ntp_server: 192.168.10.100
syslog_server: 192.168.10.101
domain_name: corp.local
```

### playbook.yml

```yaml
---
- name: Variable File Demo
  hosts: localhost
  gather_facts: no

  tasks:
    - debug:
        msg:
          - "NTP: {{ ntp_server }}"
          - "Syslog: {{ syslog_server }}"
          - "Domain: {{ domain_name }}"
```

Run:

```bash
ansible-playbook playbook.yml -e @vars.yml
```

Output:

```text
NTP: 192.168.10.100
Syslog: 192.168.10.101
Domain: corp.local
```

---

## Method 2: Multiple Environment Files

### dev.yml

```yaml
ntp_server: 192.168.10.100
domain_name: dev.local
```

### prod.yml

```yaml
ntp_server: 10.10.10.10
domain_name: prod.local
```

Run Dev:

```bash
ansible-playbook playbook.yml -e @dev.yml
```

Run Prod:

```bash
ansible-playbook playbook.yml -e @prod.yml
```

This is useful for student labs where they deploy the same playbook to different environments.

---

## Method 3: Load a Variable File Inside the Playbook

```yaml
---
- name: Variable File Demo
  hosts: localhost
  gather_facts: no

  vars_files:
    - vars.yml

  tasks:
    - debug:
        var: ntp_server
```

Run:

```bash
ansible-playbook playbook.yml
```

---

## Method 4: Dynamically Select a Variable File

### playbook.yml

```yaml
---
- name: Dynamic Variable File Demo
  hosts: localhost
  gather_facts: no

  vars_files:
    - "{{ config_file }}"

  tasks:
    - debug:
        msg: "{{ ntp_server }}"
```

### dev.yml

```yaml
ntp_server: 192.168.10.100
```

### prod.yml

```yaml
ntp_server: 10.10.10.10
```

Run:

```bash
ansible-playbook playbook.yml -e "config_file=dev.yml"
```

or

```bash
ansible-playbook playbook.yml -e "config_file=prod.yml"
```

---

## Method 5: JSON Input File

### vars.json

```json
{
  "ntp_server": "192.168.10.100",
  "syslog_server": "192.168.10.101",
  "domain_name": "corp.local"
}
```

Run:

```bash
ansible-playbook playbook.yml -e @vars.json
```

Ansible supports both YAML and JSON variable files.

For NetDevOps labs, a common structure is:

```text
project/
├── inventory.ini
├── baseline.yml
├── vars/
│   ├── site1.yml
│   ├── site2.yml
│   └── site3.yml
```

Students then run:

```bash
ansible-playbook -i inventory.ini baseline.yml -e @vars/site1.yml
```
