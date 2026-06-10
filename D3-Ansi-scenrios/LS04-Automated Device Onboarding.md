

# LAB 4 – Automated Device Onboarding

## Business Scenario

A new branch router arrives from the vendor.

It only contains:

```text
IP Address
Username
Password
```

Network team wants zero-touch onboarding.

Automation should:

1. Verify connectivity
2. Configure hostname
3. Configure SSH
4. Configure NTP
5. Configure Syslog
6. Save configuration

---

## Student Task

New Router:

```text
192.168.10.50
```

Add it to inventory and onboard automatically.

---

## onboarding.yml

```yaml
---
- name: New Device Onboarding
  hosts: routers
  gather_facts: no

  tasks:

  - name: Gather Facts
    cisco.ios.ios_facts:

  - name: Configure Hostname
    cisco.ios.ios_config:
      lines:
        - hostname "{{ inventory_hostname }}"

  - name: Configure SSH
    cisco.ios.ios_config:
      lines:
        - ip domain-name corp.local
        - crypto key generate rsa modulus 1024
        - ip ssh version 2

  - name: Configure NTP
    cisco.ios.ios_config:
      lines:
        - ntp server 192.168.10.100

  - name: Configure Syslog
    cisco.ios.ios_config:
      lines:
        - logging 192.168.10.100

  - name: Save Configuration
    cisco.ios.ios_config:
      save_when: always
```
