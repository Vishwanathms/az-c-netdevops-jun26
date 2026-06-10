

# LAB 3 – Configuration Compliance Validation

## Business Scenario

Security audit discovered:

* Some routers missing NTP
* Some routers missing SSH
* Some routers missing logging

Ansible must validate compliance automatically.

---

## Student Task

Check:

| Requirement     |
| --------------- |
| NTP Configured  |
| SSH Enabled     |
| Logging Enabled |

Generate report.

---

## Playbook

### compliance.yml

```yaml
---
- name: Compliance Validation
  hosts: routers
  gather_facts: no

  tasks:

  - name: Collect running config
    cisco.ios.ios_command:
      commands:
        - show running-config

    register: running

  - name: Check NTP
    assert:
      that:
        - "'ntp server' in running.stdout[0]"
      fail_msg: NTP Missing

  - name: Check SSH
    assert:
      that:
        - "'ip ssh version 2' in running.stdout[0]"
      fail_msg: SSH Missing

  - name: Check Logging
    assert:
      that:
        - "'logging' in running.stdout[0]"
      fail_msg: Syslog Missing
```

---

## Generate Compliance Report

### compliance_report.yml

```yaml
---
- hosts: routers
  gather_facts: no

  tasks:

  - name: Show Running Config
    cisco.ios.ios_command:
      commands:
        - show run

    register: output

  - copy:
      content: "{{ output.stdout[0] }}"
      dest: "./reports/{{ inventory_hostname }}.txt"
```

---

## Expected Output

```text
Router1 - PASS
Router2 - FAIL (NTP Missing)

Compliance Score:
50%
```

