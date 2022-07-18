import os

import menu
import ip
import url
import port
import limtraffic
import header
import portscan


def main():
    while True:
        input_code = menu.main_menu()
        if input_code == 0:
            return
        elif input_code == 1:
            second_input = menu.io_menu()
            if second_input == 1:
                io, sd, addr = menu.get_ip_addr()
                ip.block_ip_addr(io, sd, addr)
            elif second_input == 2:
                io, sd, addr = menu.get_ip_addr()
                ip.remove_ip_addr(io, sd, addr)
            elif second_input == 3:
                ip.view_iptables()
            else:
                pass
        elif input_code == 2:
            second_input = menu.io_menu()
            if second_input == 1:
                io, addr = menu.get_url_addr()
                url.block_url_addr(io, addr)
            elif second_input == 2:
                io, sd, addr = menu.get_url_addr()
                url.remove_url_addr(io, addr)
            elif second_input == 3:
                url.view_iptables()
            else:
                pass
        elif input_code == 3:
            second_input = menu.io_menu()
            if second_input == 1:
                io, proto, sd, portnum = menu.get_port()
                port.block_port(io, proto, sd, portnum)
            elif second_input == 2:
                io, proto, sd, portnum = menu.get_port()
                port.remove_port(io, proto, sd, portnum)
            elif second_input == 3:
                port.view_iptables()
            else:
                pass
        elif input_code == 4:
            limtraffic.limit_traffic()
        elif input_code == 5:
            header.block_header(menu.get_header())
        elif input_code == 6:
            portscan.block_port_scanner()
        elif input_code == 7:
            portscan.port_knocking()
        elif input_code == 8:
            os.system("iptables -F")
        else:
            pass


main()
