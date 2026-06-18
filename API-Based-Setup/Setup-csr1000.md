If you want to run **CSR1000v/GNS3 on a VM inside vCenter (ESXi)**, you must enable **Nested Virtualization** for the Ubuntu VM.

---

# Option 1: Ubuntu VM Running GNS3 on ESXi

## Step 1: Power Off Ubuntu VM

```text
vCenter
 └── Virtual Machines
      └── Ubuntu-GNS3
           └── Power Off
```

---

## Step 2: Enable Hardware Virtualization

### vSphere Client

```text
VM
 └── Edit Settings
      └── CPU
```

Enable:

```text
Expose hardware assisted virtualization to the guest OS
```

or

```text
Expose hardware virtualization to guest OS
```

(depending on ESXi version)

---

## Step 3: Add Advanced Parameter

```text
VM
 └── Edit Settings
      └── VM Options
           └── Advanced
                └── Edit Configuration
```

Add:

```text
vhv.enable = TRUE
```

---

## Step 4: Verify Host Supports VT-x

SSH to ESXi Host:

```bash
esxcli hardware cpu global get
```

Look for:

```text
HV Support: 3
```

If:

```text
HV Support: 0
```

then VT-x/AMD-V is disabled in BIOS.

---

## Step 5: Start Ubuntu VM

Inside Ubuntu:

```bash
egrep -c '(vmx|svm)' /proc/cpuinfo
```

Expected:

```text
4
8
16
...
```

not:

```text
0
```

---

## Step 6: Install KVM

```bash
sudo apt update

sudo apt install \
qemu-kvm \
libvirt-daemon-system \
libvirt-clients \
cpu-checker -y
```

Verify:

```bash
sudo kvm-ok
```

Expected:

```text
INFO: /dev/kvm exists
KVM acceleration can be used
```

---

# Option 2: Run CSR1000v Directly on ESXi (Recommended)

Instead of:

```text
ESXi
  |
  +-- Ubuntu
          |
          +-- GNS3
                 |
                 +-- CSR1000v
```

Deploy:

```text
ESXi
  |
  +-- CSR1000v
  |
  +-- Ubuntu Automation Server
  |
  +-- Windows Jumpbox
```

This gives much better performance.

---

# Deploy CSR1000v OVA on vCenter

If you have:

```text
csr1000v-universalk9.17.03.05.ova
```

Deploy:

```text
vCenter
 └── Deploy OVF Template
```

Configure:

```text
CPU : 2 vCPU
RAM : 4096 MB
Disk : Thin Provision
NIC : VMXNET3
```

Then power on.

---

# If You Only Have QCOW2

You mentioned earlier:

```text
csr1000v-universalk9.17.03.05.qcow2
```

ESXi cannot directly use QCOW2.

Convert it:

```bash
qemu-img convert \
-f qcow2 \
-O vmdk \
csr1000v-universalk9.17.03.05.qcow2 \
csr1000v.vmdk
```

Then:

```text
Create New VM
    ↓
Upload VMDK
    ↓
Attach VMDK
    ↓
Power On
```

---

For a **Cisco automation lab**, I recommend:

```text
vCenter
|
+-- Ubuntu-GNS3 Server
|
+-- CSR1000v-R1
|
+-- CSR1000v-R2
|
+-- CSR1000v-R3
|
+-- Ubuntu-Ansible
|
+-- Jenkins
```