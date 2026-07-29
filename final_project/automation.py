import yaml
from jinja2 import Environment, FileSystemLoader
from netmiko import ConnectHandler
from datetime import datetime

# Load router inventory
with open("inventory/routers.yml", "r") as file:
    routers = yaml.safe_load(file)

# Load Jinja2 template
env = Environment(loader=FileSystemLoader("templates"))
template = env.get_template("cisco_config.j2")

print("=" * 60)
print("Cisco Network Automation Framework")
print("=" * 60)

for router_name, device in routers.items():

    print(f"\nProcessing {router_name}...")

    # Generate configuration from template
    config = template.render(
        hostname=router_name,
        interface="GigabitEthernet0/0",
        ip=device["ip"],
        mask="255.255.255.0"
    )

    print("Configuration generated successfully.")

    try:
        connection = ConnectHandler(
            device_type=device["device_type"],
            host=device["ip"],
            username=device["username"],
            password=device["password"]
        )

        print("Connected successfully.")

        # Push configuration
        output = connection.send_config_set(config.splitlines())
        print(output)

        # Backup running configuration
        backup = connection.send_command("show running-config")

        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        filename = f"backups/{router_name}_{timestamp}.txt"

        with open(filename, "w") as backup_file:
            backup_file.write(backup)

        print(f"Backup saved to {filename}")

        connection.disconnect()
        print("Disconnected.")

    except Exception as e:
        print("Connection failed.")
        print(e)

print("\nAutomation process completed.")
