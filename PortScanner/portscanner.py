import socket

target = "127.0.0.1"
open_ports = []

def port_scan(port):
    '''Scans for open ports here'''
    try:
        #AF_INET means Internet, SOCKSTREAM means TCP 
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        # Connect to target:port
        sock.connect((target, port))
        return True
    except:
        return False

for port in range(1,65535):
    result = port_scan(port)
    if result:
        print(f"Port {port} is open!")
        open_ports.append(port)
    else:
        print(f"Port {port} is closed")
        
print("All open ports are:")
for i in open_ports:
    print(i, end=", ")