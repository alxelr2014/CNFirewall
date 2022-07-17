import os


# block port
def block_port(io, proto, sd, port):
    os.system("iptables -A " + io + " -p " + proto + " --" + sd + " " + port + " -j DROP")


# remove block port
def remove_port(io, proto, sd, port):
    os.system("iptables -D " + io + " -p " + proto + " --" + sd + " " + port + " -j DROP")


# view iptables
def view_iptables():
    os.system("iptables -L -nv")
    input("Press Enter to continue...")
