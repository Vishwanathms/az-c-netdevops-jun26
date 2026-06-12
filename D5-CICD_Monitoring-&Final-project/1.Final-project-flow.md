
A better DevOps workflow would be:

```text
Developer
    |
    v
Git Repository
    |
    v
Jenkins Pipeline
    |
    +----------------------+
    |                      |
    v                      v

Python Deployment      Ansible Validation
    |                      |
    v                      v

Router Config       Compliance Checks
    |                      |
    +----------+-----------+
               |
               v

       Backup Collection
               |
               v

      Reports + Evidence
               |
               v

         Jenkins Archive
```

---

# Repository Structure

```text
network-devops/

├── inventory/
│   ├── inventory.json
│   └── hosts.ini
│
├── configs/
│   └── onboarding.py
│
├── ansible/
│   ├── validate.yml
│   └── ansible.cfg
│
├── proofs/
│
├── backups/
│
├── reports/
│
├── requirements.txt
│
└── Jenkinsfile
```