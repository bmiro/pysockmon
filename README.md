# Description

Python software to monitor a socket and execute a command depending 
on socket amout of data sent.

Imagine that you have a service at localhost port 6969. This service requires a first
hello to send from client and then server starts sending data. Initial
big amount of data is skipped.

I want to execute some monitoring command if server send less than expected
bytes in a period of time or timeout happen.

Rename config.example.py to config.py and adjust the params as you want.
The most interesting things are the command to execute depending on socket
behaviour and the `clientside_login` function.

In the config.example.py I expect server to send at least 64 bytes every
second.

Becareful because if more than bufsize bytes are send each second they
are acumulated and the script looses responsiveness.

Almost all config.py options can also be given as cli argument.

# Usage example

/pysockmon.py --success-exec "printf \"%s: OK\n\" \"$(date)\"" --warning-exec "echo 'WARNING'; beep" --error-exec "echo ERROR; beep; beep; beep;" --read-threshold 9 localhost 6969

