import yaml


with open("inventory/routers.yml") as file:

    devices = yaml.safe_load(file)


for router, details in devices.items():

    print("Router Name:", router)
    print("IP Address:", details["ip"])
    print("Username:", details["username"])
    print("-" * 30)
