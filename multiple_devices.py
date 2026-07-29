from netmiko import ConnectHandler


devices = [
    {
        "device_type": "cisco_ios",
        "host": "192.168.100.11",
        "username": "admin",
        "password": "Cisco@123",
        
    },

    {
        "device_type": "cisco_ios",
        "host": "192.168.100.12",
        "username": "admin",
        "password": "Cisco@123",
        
    },

    {
        "device_type": "cisco_ios",
        "host": "192.168.100.13",
        "username": "admin",
        "password": "Cisco@123",
        
    }
]


for device in devices:

    print("\nConnecting to", device["host"])

    try:

        connection = ConnectHandler(**device)

        print(device["host"],"connected successfully")

        output = connection.send_command(
            "show ip interface brief"
        )

        print(output)

        connection.disconnect()

        print(device["host"], "disconnected")


    except Exception as e:

        print(device["host"], "connection failed")
        print(e)
