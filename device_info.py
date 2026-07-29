import paramiko
import time

ssh = paramiko.SSHClient()
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())

router_ip = "192.168.100.11"
username = "admin"
password = "Cisco@123"

ssh.connect(
    hostname=router_ip,
    username=username,
    password=password,
    look_for_keys=False,
    allow_agent=False
)

shell = ssh.invoke_shell()
time.sleep(2)
commands = [
    "show version",
    "show ip interface brief",
    "show running-config",
    "show inventory",
    "show processes cpu",
    "show memory"
]

output = ""
for command in commands:
        shell.send(command + "\n")
        time.sleep(2)
        output += shell.recv(65535).decode()

with open("device_information.txt", "w") as file:
    file.write(output)
print("Device information saved successfully.")
ssh.close()


