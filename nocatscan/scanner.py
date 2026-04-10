import socket

def scan_port(target, port):
    try:
        s = socket.socket()
        s.settimeout(0.5)
        s.connect((target, port))

        try:
            banner = s.recv(1024).decode().strip()
        except:
            banner = "Unknown"

        print(f"[OPEN] {port} | {banner}")

        s.close()
        return (port, banner)

    except:
        return None