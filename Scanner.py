import socket
from datetime import datetime
import sys

ports = {
    20: "FTP-DATA", 21: "FTP", 22: "SSH", 23: "Telnet",
    25: "SMTP", 43: "WHOIS", 53: "DNS", 80: "http",
    115: "SFTP", 123: "NTP", 143: "IMAP", 161: "SNMP",
    179: "BGP", 443: "HTTPS", 445: "MICROSOFT-DS",
    514: "SYSLOG", 515: "PRINTER", 993: "IMAPS",
    995: "POP3S", 1080: "SOCKS", 1194: "OpenVPN",
    1433: "SQL Server", 1723: "PPTP", 3128: "HTTP",
    3268: "LDAP", 3306: "MySQL", 3389: "RDP", 5000: "Flask APP",
    5432: "PostgreSQL", 5900: "VNC", 8080: "Tomcat", 10000: "Webmin",
    25565:  "Minecraft", 25566:"Minecraft 2"
}

start = datetime.now()
host_name = sys.argv[1]
ip = socket.gethostbyname(host_name)
res = []
for port in ports:
    print('\rTrying:', port, 'Found:', len(res), end='')
    cont = socket.socket()
    cont.settimeout(1)
    try:
        cont.connect((ip, port))
    except socket.error:
        pass
    else:
        res.append(f"{socket.gethostbyname(ip)}:{str(port)} is open/{ports[port]}")
        cont.close()

ends = datetime.now()
print(f"\nTime: {ends - start}\n")
for i in res: print(i)

input("\nPress Enter to the exit....")