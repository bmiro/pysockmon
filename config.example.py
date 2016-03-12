
server = 'localhost'
server_port = 6969

hello = '{"username": "fucking_strange_login", \
          "password": "onlyhilariusexample"}\r'

bufsize = 4096
read_threshold = 64

client_timeout = 2
check_delay = 1

heartbeat_interval = 1
heartbeat_msg = "Heartbeat"

exit_on_warning = False
exit_on_error = False

ok_cmd = "echo OK"
warning_cmd = "echo warning"
error_cmd = "echo error; beep" 

def serverside_login(client_sock):
    msg = client_sock.recv(len(hello))
    print("Client hellowed!")


def clientside_login(server_sock):
    from common import send
    from time import sleep

    send(server_sock, hello)

    # Read until stabilizes
    read = len(server_sock.recv(bufsize))
    sleep(0.5)

    stable = False
    while not stable:
        sleep(0.2)
        read = len(server_sock.recv(bufsize))
        stable = read != bufsize
        


