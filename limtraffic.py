import os
import menu


def limit_rate():
    lim = menu.get_rate()
    if lim == "0":
        return " "
    command = "limit --limit" + lim
    return command


def limit_protocol():
    port = menu.get_protocol()
    if port == 80:  # HTTP
        command = "-I INPUT -p tcp --dport 80 -m string --string " + menu.get_string() + " --algo kmp"
    elif port == 443:  # HTTPS
        command = "-I INPUT -p tcp --dport 443 -m string --string " + menu.get_string() + " --algo kmp"
    elif port == 21:  # FTP
        command = "-I INPUT -p tcp --dport 21 -m string --string " + menu.get_string() + " --algo kmp"
    elif port == 67: # DHCP
        command = "-I INPUT -p udp --dport 67 -m mac --mac-source " + menu.get_macaddr() + " "
    elif port == 25: # SMTP
        command = "-I INPUT -p tcp --dport 25 -m string --string " + menu.get_string() + " --algo kmp"
    elif port == 53: # DNS
        command = "-I INPUT -p udp --dport 53 -m string --string " + menu.get_url_addr() + " --algo kmp"
    elif port == 22: # SSH
        command = "-I INPUT -p tcp --dport 22 -m string --string " + menu.get_username() + " --algo kmp"
    else:
        command = ""
    return command


def limit_traffic():
    command = "iptables " + limit_protocol() + " " + limit_rate() + " -j DROP"
    os.system(command)

