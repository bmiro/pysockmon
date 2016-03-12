import subprocess

def shell_exec(cmd):
    return subprocess.run(cmd, shell=True)

def send(sock, data, encoding='utf-8'):
    return sock.sendall(data.encode(encoding))
