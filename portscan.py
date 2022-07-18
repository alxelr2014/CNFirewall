import os
import menu

def block_port_scanner():
    os.system("iptables -N PORTSCAN")
    os.system("iptables -A INPUT -p tcp --syn -j PORTSCAN")
    os.system("iptables -A PORTSCAN -p tcp --tcp-flags SYN,ACK,FIN,RST RST -m limit --limit 1/second -j RETURN")
    os.system("iptables -A PORTSCAN -j DROP")


def port_knocking():
    seq,conn_port = menu.get_sequence()
    # creates chains
    os.system("iptables -N STARTKNOCK")
    os.system("iptables -N FINISHKNOCK")
    for _i in range(len(seq)):
        os.system("iptables -N KNOCK"+str(_i))

    os.system("iptables -A INPUT -p tcp -j STARTKNOCK")

    for _i in range(len(seq)):
        if _i > 0:
            os.system("iptables -A KNOCK"+str(_i)+" -m recent --name AUTH"+str(_i -1) + " --remove")
        os.system("iptables -A KNOCK"+str(_i)+" -p tcp --dport " + seq[_i] + " -m recent --name AUTH"+str(_i) + "--set -j DROP")
        os.system("iptables -A KNOCK"+str(_i) + " -j DROP")

    os.system("iptables -A FINISHKNOCK -m recent --name AUTH"+str(len(seq) - 1)+" --remove")
    os.system("iptables -A FINISHKNOCK -p tcp --dport"+conn_port+" -j ACCEPT")

    os.system("iptables -A STARTKNOCK -m recent --rcheck --seconds 30 --name AUTH"+str(len(seq) - 1)+ " -j FINISHKNOCK")
    for _i in range(len(seq) - 1,0,-1):
        os.system("iptables -A STARTKNOCK -m recent --rcheck --seconds 10 --name AUTH"+str(_i - 1)+" -j KNOCK"+str(_i))

    os.system("iptables -A STARTKNOCK -j KNOCK0")