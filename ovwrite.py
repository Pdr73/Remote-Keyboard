import msvcrt, sys

# Obtiene el ascii para una tecla cualquiera
char='a'
text = []

"""
while char != '0':
	print '\r',
	char = msvcrt.getch()
	text.append(char)
	print ''.join(text),
	sys.stdout.flush()
"""

char = msvcrt.getch()
# Key.backspace = '\x08'
# Key.esc		= '\x1b'
print(str(char))