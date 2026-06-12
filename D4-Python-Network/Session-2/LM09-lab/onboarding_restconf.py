import json
import csv
import os

from dotenv import load_dotenv

from restconf_client import create_loopback

load_dotenv()

USERNAME = os.getenv("USERNAME")
PASSWORD = os.getenv("PASSWORD")

with open("inventory.json") as f:
    inventory = json.load(f)

report = open("reports/report.csv","w")

writer = csv.writer(report)

writer.writerow(
    ["Hostname","IP","Status"]
)

for index,(hostname,device) in enumerate(
        inventory["routers"].items(),
        start=1):

    loopback_ip = f"10.10.10.{index}"

    print(
        f"Configuring {hostname} "
        f"Loopback {loopback_ip}"
    )

    result = create_loopback(
        device["host"],
        USERNAME,
        PASSWORD,
        loopback_ip
    )

    if result.status_code in [200,201,204]:

        status="SUCCESS"

    else:

        status=f"FAILED-{result.status_code}"

    writer.writerow(
        [
            hostname,
            device["host"],
            status
        ]
    )

report.close()