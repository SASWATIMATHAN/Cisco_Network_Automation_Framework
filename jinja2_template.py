from jinja2 import Environment, FileSystemLoader


# Load template folder

environment = Environment(
    loader=FileSystemLoader("templates")
)


# Load Jinja2 template

template = environment.get_template(
    "cisco_config.j2"
)


# Values to replace template variables

configuration = template.render(
    hostname="R1-NETWORK-AUTO",
    interface="GigabitEthernet0/0",
    ip="192.168.100.11",
    mask="255.255.255.0"
)


print("Generated Cisco Configuration:")
print("--------------------------------")

print(configuration)
