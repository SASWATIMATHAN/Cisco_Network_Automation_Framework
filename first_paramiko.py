import paramiko

router_ip = "192.168.100.11"
username = "admin"
password = "Cisco@123"

ssh = paramiko.SSHClient()

ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())

ssh.connect(
    hostname=router_ip,
    username=username,
    password=password,
    look_for_keys=False,
    allow_agent=False
)

stdin, stdout, stderr = ssh.exec_command("show ip interface brief")

output = stdout.read().decode()

print(output)

ssh.close()