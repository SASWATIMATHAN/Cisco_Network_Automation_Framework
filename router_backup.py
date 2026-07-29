import paramiko
import time
from datetime import datetime


router_ip = "192.168.100.11"
username = "admin"
password = "Cisco@123"


ssh = paramiko.SSHClient()

ssh.set_missing_host_key_policy(
    paramiko.AutoAddPolicy()
)


print("Connecting to router...")


ssh.connect(
    hostname=router_ip,
    username=username,
    password=password,
    look_for_keys=False,
    allow_agent=False
)


print("Connected successfully")


shell = ssh.invoke_shell()

time.sleep(2)


shell.send("terminal length 0\n")
time.sleep(1)

shell.send("show running-config\n")

time.sleep(5)


output = shell.recv(100000).decode()


timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")

filename = f"router_backup_{timestamp}.txt"


with open(filename, "w") as backup:
    backup.write(output)


print("Backup saved:")
print(filename)


ssh.close()

print("Connection closed")
