import smtplib
import socket
import fcntl
import struct


def get_ip_address(ifname):
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    return socket.inet_ntoa(fcntl.ioctl(
        s.fileno(),
        0x8915,  # SIOCGIFADDR
        struct.pack('256s', ifname[:15])
    )[20:24])


server = smtplib.SMTP('smtp.gmail.com', 587)
print(server.starttls())
server.login("natelampimailer@gmail.com", "lampimailer377")

hostname = socket.gethostname()
ip_addr = socket.gethostbyname(hostname)
msg = get_ip_address('wlan0')
server.sendmail("natelampimailer@gmail.com", "ntc14@case.edu", msg)
server.quit()
