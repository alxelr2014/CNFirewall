import os


# block a URL address
def block_url_addr(io, url_addr):
    os.system("iptables -A " + io + " -m string --algo bm --string \"" + url_addr + "\" -j DROP")


# remove block from INPUT table
def remove_url_addr(io, url_addr):
    os.system("iptables -D " + io + " -m string --algo bm --string \"" + url_addr + "\" -j DROP")


# view iptables
def view_iptables():
    os.system("iptables -L -nv")
    input("Press Enter to continue...")
