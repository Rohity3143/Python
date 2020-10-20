import paramiko
import time

conn=paramiko.SSHClient()
conn.set_missing_host_key_policy(paramiko.AutoAddPolicy())
conn.connect("ip of the server", port=22, username="username", password="password")
conn1 = conn.invoke_shell()
conn1.recv(65535)
conn1.send("vshell \n")
time.sleep(5)
conn1.send("ssh username@ip \n")
time.sleep(5)
conn1.send("password\n")
time.sleep(3)
conn1.recv(9999999)
conn1.send("screen-length 0 \n")
time.sleep(2)
conn1.send("show version \n")
time.sleep(2)
conn1.send("show interface description |tab \n")
time.sleep(4)
conn1.send("show interface | tab \n")
time.sleep(3)
conn1.send("show system status \n")
time.sleep(3)
conn1.send("show run \n")
time.sleep(5)
conn1.send("show clock \n")
time.sleep(3)
out=conn1.recv(9999999).decode()
out1=out.splitlines()
name="Pre_checks" + str(time.strftime("%Y%m%d-%H%M%S")) + ".txt"
with open(name,"w") as f:
    for i in out1:
        f.write(i)  
        f.write("\n")   
        
        
