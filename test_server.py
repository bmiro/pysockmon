#!/usr/bin/env python3
# -*- coding: utf-8 -*-
                  
import socket     
from time import sleep

from common import send

import config

if '__main__' == __name__:

    conn = (config.server, config.server_port)

    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    server.bind(conn)
    server.listen(1)

    print("Waiting client")

    (client, address) = server.accept()

    config.serverside_login(client)

    while True:        
        msg = config.heartbeat_msg
        print("Sending: " + msg)
        send(client, msg)
        sleep(config.heartbeat_interval)
