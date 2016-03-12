#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import click
import socket

from sys import exit
from time import sleep

from pysockmon.common import shell_exec

import pysockmon.config as config

@click.command()
@click.option('--exit-on-error', flag_value=config.exit_on_error)
@click.option('--exit-on-warning', flag_value=config.exit_on_warning)
@click.option('--pass-read-exec', flag_value=config.pass_read_exec)
@click.option('--read-threshold', default=config.read_threshold)
@click.option('--check-delay', default=config.check_delay)
@click.option('--success-exec', default=config.success_exec)
@click.option('--warning-exec', default=config.warning_exec)
@click.option('--error-exec', default=config.error_exec)
@click.option('--timeout', default=config.client_timeout)
@click.option('--hello', default=config.hello)
@click.option('--bufsize', default=config.bufsize)
@click.argument('connection', type=click.Tuple([str, int]))
def pysockmon(exit_on_error, exit_on_warning, pass_read_exec, read_threshold,
              check_delay, success_exec, warning_exec, error_exec,
              timeout, hello, bufsize,
              connection):

    print(bufsize); exit
    sock = socket.socket()
    sock.settimeout(timeout)
    sock.connect(connection)

    config.clientside_login(sock, hello)    

    while True:
        try:
            result = sock.recv(bufsize)
            if len(result) >= read_threshold:
                cmd = success_exec
                if (pass_read_exec):
                    cmd += " %d %d" % (len(result), read_threshold)
                shell_exec(success_exec)
            else:
                cmd = warning_exec
                if (pass_read_exec):
                    cmd += " %d %d" % (len(result), read_threshold)
                shell_exec(cmd)
                if exit_on_warning:
                    break
        except socket.timeout:
            shell_exec(error_exec)
            if exit_on_error:
                break

        sleep(check_delay)

    sock.close()
    exit(1)

if '__main__' == __name__:
    pysockmon()
