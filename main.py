from subprocess import DEVNULL, STDOUT, check_call
import os

def main():
    class server_object:
        def __init__(self, name, ip, port):
            self.name = name
            self.ip = ip
            self.port = port

    server_list = [
        server_object("Glance", "192.168.178.159", 8080),
        server_object("Portainer", "192.168.178.159", 9443),
        server_object("Nextcloud", "192.168.178.159", 80),
        server_object("Gitea", "192.168.178.159", 3000),
        server_object("Adguard", "192.168.178.159", 90),
    ]
    for server in server_list:
        print(f"Checking {server.name} at {server.ip}:{server.port}")
        with open(os.devnull, "w") as devnull:
            check_call(['ping', '-c', '1', f"{server.ip}:{server.port}"], stdout=devnull, stderr=STDOUT)

if __name__ == "__main__":
    main()