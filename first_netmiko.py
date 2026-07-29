from netmiko import ConnectHandler

router = {
    "device_type": "cisco_ios",
    "host": "192.168.100.11",
    "username": "admin",
    "password": "Cisco@123",
}

try:
    print("Connecting to Cisco router...")

    net_connect = ConnectHandler(**router)

    print("Connection Successful!")

    net_connect.disconnect()

    print("Disconnected Successfully.")

except Exception as e:
    print("\nConnection Failed!")
    print(e)
