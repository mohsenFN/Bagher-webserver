'''
The function in this script is used to get machine's local IPv4 address
'''

import socket

def get_local_ipv4():
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    
    # 11228 TATALOO
    # This connection doesn't have to be reachable
    s.connect(('1.1.22.8', 80))

    local_ipv4 = s.getsockname()[0]

    s.close()

    return local_ipv4

