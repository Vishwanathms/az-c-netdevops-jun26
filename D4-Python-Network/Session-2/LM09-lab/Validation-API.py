def get_loopback(host,user,password):

    url = (
        f"https://{host}/restconf/data/"
        "ietf-interfaces:interfaces/"
        "interface=Loopback10"
    )

    response = requests.get(
        url,
        auth=(user,password),
        headers=HEADERS,
        verify=False
    )

    return response.json()