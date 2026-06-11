
## convert python variables to json
```
import json

device = {
    'hostname': "R1",
    'ip': "192.168.1.1"
}

json_data = json.dumps(device, indent=4)
print(json_data)
```

