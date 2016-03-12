hello = '{"username": "dummy", "password": "example"}'

bufsize = 4096
read_threshold = 4096
initial_read = bufsize * 4

client_timeout = 2
check_delay = 1

heartbeat_interval = 1
heartbeat_msg = "Heartbeat"

exit_on_warning = False
exit_on_error = False

pass_read_exec = False

success_exec = "echo OK"
warning_exec = "echo warning; beep"
error_exec = "echo error; beep" 

def serverside_login(client_sock, hello):
    msg = client_sock.recv(len(hello))
    print("Client hellowed!")


def clientside_login(server_sock, hello):
    from pysockmon.common import send
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
