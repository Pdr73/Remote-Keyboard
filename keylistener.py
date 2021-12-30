from pynput import keyboard
from pynput.keyboard import Key, Controller

kb = Controller()

def say(key):
	kd.press(key)
	kd.release(key)

global lista
lista=[]

global texto
texto = "{"

def on_press(key):
	global lista, texto
	try:
		print('alphanumeric key {} pressed'.format(key.char.decode()))
		lista.append(key.char)
		texto = texto + '{0}:{1}, '.format('"' + key.char.decode() + '"', '"' + key.char.decode() + '"')
		
	except:
		print('especial key {} pressed'.format(key))
		texto = texto + "{0}:{1}, ".format('"' + str(key) + '"', key)

		if key==keyboard.Key.space:
			lista.append(' ')
		elif key==keyboard.Key.backspace:
			lista=lista[:-1]

def on_release(key):
	print('{} released'.format(key))
	if key==keyboard.Key.esc:
		# Stops listener
		print("".join(lista))
		return False

with keyboard.Listener(on_press=on_press,on_release=on_release) as listener:
	listener.join()

listener=keyboard.Listener(on_press=on_press,on_release=on_release)
listener.start()

# We need Key.backspace, Key.space for writing and Key.esc to exit

texto = texto[0:-2] + '}'		# El [0:-1] coge todos los caracteres excepto los utlimos 2 que son ', '
print(texto)