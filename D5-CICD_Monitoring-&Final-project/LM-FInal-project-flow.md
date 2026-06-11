Excellent next step. Now the students move from **Network Automation Engineer** to **Network DevOps Engineer**.

The workflow becomes:

```text
Developer
    |
    v
Git Repository
    |
    v
Jenkins Pipeline
    |
    v
Python Validation
    |
    v
Router Configuration
    |
    v
Proof Collection
    |
    v
Configuration Backup
    |
    v
Store Evidence in Git
```

---

# Enterprise Lab Scenario

## Business Requirement

A network team manages 100 branch routers.

Requirements:

1. All network automation code must be version controlled.
2. Every configuration change must be approved through Git.
3. Jenkins should execute the automation.
4. Validation reports should be generated automatically.
5. Device backups should be archived.

---

# Architecture

```text
                +-------------+
                | Developer   |
                +-------------+
                       |
                       | git push
                       |
                       v
                +-------------+
                | Git Repo    |
                +-------------+
                       |
                       | webhook
                       |
                       v
                +-------------+
                | Jenkins     |
                +-------------+
                       |
          +------------+------------+
          |                         |
          v                         v

  Validation Stage        Deployment Stage
          |                         |
          +------------+------------+
                       |
                       v
               Cisco Routers
                       |
                       v

             Proofs + Backups
                       |
                       v

                Git Artifacts
```

---

# Repository Structure

```text
network-devops/

├── inventory/
│   └── inventory.json
│
├── configs/
│   └── onboarding.py
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

---

# Step 1: Git Repository

Initialize Git.

```bash
git init
```

Add files.

```bash
git add .
git commit -m "Initial onboarding automation"
```

Create repository in:

* [GitHub](https://github.com?utm_source=chatgpt.com)
* [GitLab](https://gitlab.com?utm_source=chatgpt.com)

Push code.

```bash
git remote add origin https://github.com/company/network-devops.git

git push -u origin main
```

---

# Step 2: Python Requirements

## requirements.txt

```text
netmiko
paramiko
```

Jenkins installs automatically.

```bash
pip install -r requirements.txt
```

---

# Step 3: Store Credentials Securely

Never store passwords in Git.

## Jenkins Credentials

```text
NET_USERNAME
NET_PASSWORD
```

Jenkins →

```text
Manage Jenkins
    |
    Credentials
```

Add:

```text
admin
Password123
```

---

# Step 4: Parameterized Inventory

## inventory.json

```json
{
  "routers": {
    "R1": {
      "device_type": "cisco_ios",
      "host": "192.168.10.1"
    },
    "R2": {
      "device_type": "cisco_ios",
      "host": "192.168.10.2"
    },
    "R3": {
      "device_type": "cisco_ios",
      "host": "192.168.10.3"
    }
  }
}
```

---

# Step 5: Generate Reports

Modify Python.

```python
report = []

report.append(
    f"{hostname},{router['host']},SUCCESS"
)
```

Generate:

```text
reports/deployment.csv
```

Example:

```text
Hostname,IP,Status
R1,192.168.10.1,SUCCESS
R2,192.168.10.2,SUCCESS
R3,192.168.10.3,SUCCESS
```

---

# Step 6: Jenkins Pipeline

## Jenkinsfile

```groovy
pipeline {

    agent any

    environment {

        NET_USERNAME = credentials('net-user')
        NET_PASSWORD = credentials('net-pass')
    }

    stages {

        stage('Checkout') {

            steps {

                git branch: 'main',
                    url: 'https://github.com/company/network-devops.git'
            }
        }

        stage('Install Dependencies') {

            steps {

                sh '''
                python3 -m venv venv

                . venv/bin/activate

                pip install -r requirements.txt
                '''
            }
        }

        stage('Deploy Configuration') {

            steps {

                sh '''
                . venv/bin/activate

                python configs/onboarding.py
                '''
            }
        }

        stage('Archive Evidence') {

            steps {

                archiveArtifacts(
                    artifacts: 'proofs/*,backups/*,reports/*',
                    fingerprint: true
                )
            }
        }
    }
}
```

---

# Pipeline Execution Flow

```text
Stage 1
Checkout Source Code

        |
        v

Stage 2
Install Python Modules

        |
        v

Stage 3
Connect to Routers

        |
        v

Apply Configuration

        |
        v

Validate Configuration

        |
        v

Create Backups

        |
        v

Generate Reports

        |
        v

Stage 4
Archive Artifacts
```

---

# Git Workflow for Students

### Engineer modifies banner

```python
banner motd #Welcome Chennai Branch#
```

Commit:

```bash
git add .

git commit -m "Updated branch banner"

git push
```

---

### Jenkins Trigger

```text
Git Push
    |
Webhook
    |
Jenkins Job
    |
Deploy
    |
Validate
    |
Backup
    |
Report
```

---

# Advanced Lab: Change Approval

Create branches.

```bash
git checkout -b feature/banner-change
```

Modify code.

Push:

```bash
git push origin feature/banner-change
```

Create Pull Request.

```text
Engineer
    |
Pull Request
    |
Reviewer Approval
    |
Merge Main
    |
Jenkins Deploy
```

This covers:

* Git workflows
* Branching
* Pull Requests
* CI/CD concepts
* Infrastructure as Code
* Network as Code
* Automated compliance validation
* Configuration backup management
* Jenkins pipelines for network automation

