import paramiko
import time

# Router Details
router_ip = "192.168.100.11"
username = "admin"
password = "Cisco@123"

# Create SSH Client
ssh = paramiko.SSHClient()

# Accept unknown SSH keys automatically
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())

# Connect to Router
ssh.connect(
    hostname=router_ip,
    username=username,
    password=password
)

# Start Interactive Shell
shell = ssh.invoke_shell()

# Wait for CLI prompt
time.sleep(1)

# Enter Privileged EXEC Mode
shell.send("enable\n")

time.sleep(1)

# Execute Cisco Command
shell.send("show version\n")

time.sleep(2)

# Read Router Output
output = shell.recv(5000).decode()

print(output)

# Close Connection
ssh.close()