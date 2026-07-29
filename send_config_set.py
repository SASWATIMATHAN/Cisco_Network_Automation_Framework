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

    print("Connected successfully!")


    config_commands = [
        "hostname R1-NETMIKO",
        "interface gigabitEthernet0/0",
        "ip address 192.168.100.11 255.255.255.0",
        "no shutdown",
    ]


    output = connection.send_config_set(config_commands)


    print("\nConfiguration Output:")
    print(output)


    connection.save_config()


    connection.disconnect()

    print("\nConfiguration completed successfully.")
    print("Disconnected.")


except Exception as e:

    print("Configuration failed!")
    print(e)
