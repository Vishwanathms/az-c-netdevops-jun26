
# LAB 1 – VLAN and Interface Configuration Automation

## Business Scenario

ABC Corporation has opened a new branch office.

Network team needs:

* VLAN 10 for HR
* VLAN 20 for Finance
* VLAN 30 for IT
* Configure router interfaces
* Assign IP addresses
* Enable interfaces

Instead of configuring every device manually, the team wants Ansible automation.

---

## Student Task

Configure:

| Interface | IP Address    |
| --------- | ------------- |
| Fa0/0     | 10.10.10.1/24 |
| Fa0/1     | 10.20.20.1/24 |

Create VLANs:

| VLAN | Name    |
| ---- | ------- |
| 10   | HR      |
| 20   | FINANCE |
| 30   | IT      |

---

## Playbook

### vlan_interface.yml

```yaml
---
- name: Configure VLAN and Interfaces
  hosts: routers
  gather_facts: no

  tasks:

  - name: Create VLANs
    cisco.ios.ios_config:
      lines:
        - vlan 10
        - name HR
        - vlan 20
        - name FINANCE
        - vlan 30
        - name IT

  - name: Configure FastEthernet0/0
    cisco.ios.ios_config:
      parents: interface FastEthernet0/0
      lines:
        - ip address 10.10.10.1 255.255.255.0
        - no shutdown

  - name: Configure FastEthernet0/1
    cisco.ios.ios_config:
      parents: interface FastEthernet0/1
      lines:
        - ip address 10.20.20.1 255.255.255.0
        - no shutdown
```

---

## Verification

```bash
ansible-playbook vlan_interface.yml
```

Verify:

```bash
show vlan
show ip interface brief
```

Expected:

```text
Fa0/0  up/up
Fa0/1  up/up

VLAN10 HR
VLAN20 FINANCE
VLAN30 IT
```

