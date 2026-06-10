

# LAB 2 – Standard Baseline Configuration Deployment

## Business Scenario

Company has purchased 25 new routers.

Every router must have:

* Hostname
* Banner
* NTP Server
* Logging
* SSH
* Secure Passwords

Operations team wants one-click deployment.

---

## Student Task

Deploy corporate baseline:

```text
Hostname
Banner
SSH
NTP
Syslog
```

---

## Variables File

### group_vars/all.yml

```yaml
ntp_server: 192.168.10.100
syslog_server: 192.168.10.100
domain_name: corp.local
```

---

## Playbook

### baseline.yml

```yaml
---
- name: Baseline Deployment
  hosts: routers
  gather_facts: no

  tasks:

  - name: Configure Hostname
    cisco.ios.ios_config:
      lines:
        - hostname "{{ inventory_hostname }}"

  - name: Configure Banner
    cisco.ios.ios_config:
      lines:
        - banner motd # Unauthorized access prohibited #

  - name: Configure Domain
    cisco.ios.ios_config:
      lines:
        - ip domain-name {{ domain_name }}

  - name: Configure SSH
    cisco.ios.ios_config:
      lines:
        - crypto key generate rsa modulus 1024
        - ip ssh version 2

  - name: Configure NTP
    cisco.ios.ios_config:
      lines:
        - ntp server {{ ntp_server }}

  - name: Configure Syslog
    cisco.ios.ios_config:
      lines:
        - logging {{ syslog_server }}
```

---

## Verification

```bash
show run | section ntp
show run | section logging
show ip ssh
```

