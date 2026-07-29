import paramiko
import time
ssh = paramiko.SSHClient()
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
router_ip = "192.168.100.11"
username = "admin"
password = "Cisco@123"
ssh.connect(hostname=router_ip, 
            username=username,
            password =password, 
            look_for_keys=False, 
            allow_agent=False)
shell = ssh.invoke_shell()
commands = [
    "configure terminal",
    "hostname R1",
    "interface FastEthernet0/0",
    "ip address 192.168.100.11 255.255.255.0",
    "no shutdown",
    "exit",
    "end"
]
for command in commands:
    shell.send(command + "\n")
time.sleep(2)
output = shell.recv(65535).decode()
print(output)
ssh.close()


