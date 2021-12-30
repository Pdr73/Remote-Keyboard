# Remote-Keyboard
Use a windows device as a remote keyboard for PC

The scripts tcpclnt.py is listening the keys and it sends to the server (tcpserv.py), that presses the keys in the remote keyboard.

Usage:
- On the pc that is going to be controlled open tcpserv.py.
- On the one that is listening for the keys open tcpclnt.py and write the ip provided by the tcpserv.py program.
- This works for pcs on the same wifi network.
