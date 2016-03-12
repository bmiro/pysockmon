#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import socket

from sys import exit
from time import sleep

from common import shell_exec

import config

if '__main__' == __name__:
    read_threshold = config.read_threshold
    delay = config.check_delay
    exit_on_error = config.exit_on_error
    exit_on_warning = config.exit_on_warning
    ok_cmd = config.ok_cmd
    warning_cmd = config.warning_cmd
    error_cmd = config.error_cmd
    client_timeout = config.client_timeout
    bufsize = config.bufsize

    conn = (config.server, config.server_port)

    sock = socket.socket()
    sock.settimeout(client_timeout)
    sock.connect(conn)

    config.clientside_login(sock)    

    while True:
        try:
            result = sock.recv(bufsize)
            if len(result) >= read_threshold:
                shell_exec(ok_cmd)
                print(len(result))
            else:
                shell_exec(warning_cmd)
                print("Read %d instead of %d" % (len(result), read_threshold))
                if exit_on_warning:
                    break
        except socket.timeout:
            shell_exec(error_cmd)
            if exit_on_error:
                break

        sleep(delay)

    sock.close()
    exit(1)
