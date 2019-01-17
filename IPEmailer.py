import smtplib
import socket

server = smtplib.SMTP('smtp.gmail.com', 587)
print(server.starttls())
server.login("natelampimailer@gmail.com", "lampimailer377")

hostname = socket.gethostname()
ip_addr = socket.gethostbyname(hostname)
msg = ip_addr
server.sendmail("natelampimailer@gmail.com", "ntc14@case.edu", msg)
server.quit()