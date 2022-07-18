import os

def block_header(header):
    os.system("iptables -A INPUT -p tcp --dport 80 -m string --string " + header+ " --algo kmp -j DROP")
    os.system("iptables -A OUTPUT -p tcp --dport 80 -m string --string " + header+ " --algo kmp -j DROP")