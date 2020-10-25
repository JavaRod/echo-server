import socket
import sys


def list_services(min_port, max_port):
    if min_port < 0:
        min_port = 0
    if min_port > 65535:
        min_port = 65535

    for port in range(min_port, max_port + 1):
        service = 'None'
        try:
            service = socket.getservbyport(port)
        except OSError:
            pass
        print(f'Port {port} Service {service}')


if __name__ == '__main__':
    if len(sys.argv) == 1:
        min_port = 0
        max_port = 1024
    elif len(sys.argv) != 3:
        usage = '\nusage: python service_list.py 0 65535\n'
        print(usage)
        sys.exit(1)
    else:
        min_port = int(sys.argv[1])
        max_port = int(sys.argv[2])

    list_services(min_port, max_port)
