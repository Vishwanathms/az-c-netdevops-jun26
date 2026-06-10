# NetDevOps with Ansible Lab Guide (Cisco 3660 on GNS3)

## Lab Environment

### Topology

```text
                Ubuntu Ansible Server
                      |
              192.168.10.100
                      |
            --------------------
            |                  |
      192.168.10.1       192.168.10.2
        Router1            Router2
       Cisco 3660         Cisco 3660
```

### Device Credentials

```yaml
Username: admin
Password: Password123
Enable Password: Password123
```

### Inventory File

```ini
[routers]
r1 ansible_host=192.168.10.1
r2 ansible_host=192.168.10.2

[routers:vars]
ansible_user=admin
ansible_password=Password123
ansible_connection=network_cli
ansible_network_os=ios
ansible_become=yes
ansible_become_method=enable
ansible_become_password=Password123
```
