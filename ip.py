import os


# block an IP address
def block_ip_addr(io, sd, ip_addr):
    os.system("iptables -A " + io + " -" + sd + " " + ip_addr + " -j DROP")


# remove block from the selected table
def remove_ip_addr(io, sd, ip_addr):
    os.system("iptables -D " + io + " -" + sd + " " + ip_addr + " -j DROP")


# view iptables
def view_iptables():
    os.system("iptables -L -nv")
    input("Press Enter to continue...")
