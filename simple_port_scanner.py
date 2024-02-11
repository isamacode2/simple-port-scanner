import socket

def scan_port(ip, port):
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.settimeout(1)
    result = sock.connect_ex((ip, port))
    sock.close()
    return result == 0

def scan_ports_on_host(ip, start_port, end_port):
    open_ports = []
    for port in range(start_port, end_port + 1):
        if scan_port(ip, port):
            open_ports.append(port)
    return open_ports

# Example usage:
if __name__ == "__main__":
    target_ip = "scanme.nmap.org"  # Example target, replace with the IP you have permission to scan
    start_port = 70
    end_port = 80
    print("Scanning ports {}-{} on {}...".format(start_port, end_port, target_ip))
    open_ports = scan_ports_on_host(target_ip, start_port, end_port)
    for port in open_ports:
        print("Port {} is open on {}.".format(port, target_ip))

