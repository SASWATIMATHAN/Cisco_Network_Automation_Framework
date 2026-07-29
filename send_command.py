from netmiko import ConnectHandler


router = {
    "device_type": "cisco_ios",
    "host": "192.168.100.11",
    "username": "admin",
    "password": "Cisco@123",
}


print("Connecting to Cisco router...")

try:

    connection = ConnectHandler(**router)

    print("Connected successfully!\n")


    commands = [
        "show version",
        "show ip interface brief",
        "show ip route"
    ]


    for command in commands:

        print("=" * 50)
        print("Executing command:", command)
        print("=" * 50)

        output = connection.send_command(command)

        print(output)


    connection.disconnect()

    print("\nDisconnected successfully.")


except Exception as e:

    print("Connection failed!")
    print(e)
