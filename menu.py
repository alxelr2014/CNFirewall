import os


def main_menu():
    os.system("clear")
    ans = int(input("1- IP address\n2- Block Domain Regex URL\n3- Port\n4- Limit Traffic\n5- Header\n6- Port Scanning "
                    "and Knocking\n0- Exit\n"))
    return ans


def io_menu():
    os.system("clear")
    ans = int(input("1- Add Rule\n2- Remove Rule\n3- View Table\n0- Back\n"))
    return ans


def get_ip_addr():
    os.system("clear")
    iio = int(input("1- Block Incoming\n2- Block Outgoing\n"))
    if iio == 1:
        io = "INPUT"
    elif iio == 2:
        io = "OUTPUT"
    else:
        return
    isd = int(input("1- Block Based on Source IP\n2- Block Based on Destination IP\n"))
    if isd == 1:
        sd = "s"
    elif isd == 2:
        sd = "d"
    else:
        return
    addr = input("Enter an IP address\n")
    return io, sd, addr


def get_url_addr():
    os.system("clear")
    iio = int(input("1- Block Incoming\n2- Block Outgoing\n"))
    if iio == 1:
        io = "INPUT"
    elif iio == 2:
        io = "OUTPUT"
    else:
        return
    addr = input("Enter an URL regex address\n")
    return io, addr


def get_port():
    os.system("clear")
    iio = int(input("1- Block Incoming\n2- Block Outgoing\n"))
    if iio == 1:
        io = "INPUT"
    elif iio == 2:
        io = "OUTPUT"
    else:
        return
    proto = input("Enter a Protocol\n")
    isd = int(input("1- Block Based on Source IP\n2- Block Based on Destination IP\n"))
    if isd == 1:
        sd = "s"
    elif isd == 2:
        sd = "d"
    else:
        return
    port = input("Enter a port\n")
    return io, proto, sd, port


def get_rate():
    os.system("clear")
    ans = input("Enter a rate e.g. 5/minute, Enter 0 for no limit\n")
    return ans


def get_protocol():
    os.system("clear")
    ans = int(input("1- HTTP\n2- HTTPS\n3- FTP\n4- DHCP\n5- SMTP\n6- DNS\n7- SSH\n0- Back\n"))
    if ans == 1:
        protocol = 80
    elif ans == 2:
        protocol = 443
    elif ans == 3:
        protocol = 21
    elif ans == 4:
        protocol = 67
    elif ans == 5:
        protocol = 25
    elif ans == 6:
        protocol = 53
    elif ans == 7:
        protocol = 22
    else:
        protocol = 0
    return protocol


def get_string():
    os.system("clear")
    ans = input("Enter a string\n")
    return ans


def get_macaddr():
    os.system("clear")
    ans = input("Enter a MAC address\n")
    return ans


def get_username():
    os.system("clear")
    ans = input("Enter a username\n")
    return ans


def get_sequence():
    os.system("clear")
    ans = input("Enter a space separated sequnce of port number\n").split(" ")
    return ans
