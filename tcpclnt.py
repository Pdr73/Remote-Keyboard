# CLIENTE
import socket, msvcrt, sys

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect(('localhost', 50000))

exit = 0

while exit == 0:
	print '\r',
	print '\\> ',
	char = msvcrt.getch().encode('utf-8')	# Texto a enviar codificado
	s.send(char)							# Lo envia
	print char,
	sys.stdout.flush()
	# Key.backspace	= '\x08'
	# Key.esc		= '\x1b'

	if str(char) == '\x1b':
		s.send('/e')
		exit = 1

s.close()