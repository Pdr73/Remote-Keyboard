# SERVIDOR
import socket, sys
from pynput.keyboard import Key, Controller

keyboard = Controller()

def say(key):
	keyboard.press(key)
	keyboard.release(key)

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind(('localhost', 50000))
s.listen(1)
conn, addr = s.accept()

exit = 0
tdata=[]

while exit == 0:
	data = conn.recv(1024)		# Recibimos datos
	data = data.decode('utf-8')	# Decodificamos

	# Falta que hagas que presione las teclas

	if str(data) == '\x08':		# Borrar una letra
		tdata = tdata[:-1]
		print '\r',
		print "[+] " + "".join(tdata),
		sys.stdout.flush()
		key = Key.backspace
	
	elif str(data) == '\r':		# Intro
		tdata.append('\n')
		key = Key.space
	
	else:						# Simplemente añade una letra 
		key = tdata				# La letra en cuestion
		tdata.append(data)

	print '\r',
	print "[+] " + "".join(tdata),

	say(key)

	sys.stdout.flush()

	if data == '/e':
		exit = 1
		
conn.close()
s.close()
print("\n[-] Connection ended.")