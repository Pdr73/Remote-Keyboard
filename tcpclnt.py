# CLIENT
import socket, sys
from pynput.keyboard import Key, Controller
from pynput import keyboard

# Dictionary with the keys
dicsionario = {"Key.enter":Key.enter, "Key.delete":Key.delete, "Key.insert":Key.insert, "Key.right":Key.right, "Key.down":Key.down, "Key.left":Key.left, "Key.ctrl_r":Key.ctrl_r, "Key.cmd":Key.cmd, "Key.ctrl_l":Key.ctrl_l, "Key.alt_gr":Key.alt_gr, "<":"<", "Key.space":Key.space, "Key.alt_l":Key.alt_l, "Key.ctrl_l":Key.ctrl_l, "Key.page_down":Key.page_down, "Key.down":Key.down, "Key.end":Key.end, "Key.up":Key.up, "Key.shift_r":Key.shift_r, "-":"-", ".":".", ",":",", "m":"m", "n":"n", "b":"b", "v":"v", "c":"c", "x":"x", "z":"z", "Key.shift":Key.shift, "+":"+", "Key.right":Key.right, "Key.left":Key.left, "Key.enter":Key.enter, "[u'\xb4']":u'\xb4', "u'\xf1'":u'\xf1', "l":"l", "k":"k", "j":"j", "h":"h", "g":"g", "f":"f", "d":"d", "s":"s", "a":"a", "Key.caps_lock":Key.caps_lock, "Key.page_up":Key.page_up, "Key.up":Key.up, "Key.home":Key.home, "u'\xe7'":u'\xe7', "+":"+", "`":"`", "p":"p", "o":"o", "i":"i", "u":"u", "y":"y", "t":"t", "r":"r", "e":"e", "w":"w", "q":"q", "Key.tab":Key.tab, "-":"-", "*":"*", "-":"-", "Key.num_lock":Key.num_lock, "Key.backspace":Key.backspace, "u'\xa1'":u'\xa1', "'":"'", "0":"0", "9":"9", "8":"8", "7":"7", "6":"6", "5":"5", "4":"4", "3":"3", "2":"2", "1":"1", "u'\xba'":u'\xba', "Key.page_down":Key.page_down, "Key.page_up":Key.page_up, "Key.delete":Key.delete, "Key.insert":Key.insert, "Key.pause":Key.pause, "Key.scroll_lock":Key.scroll_lock, "Key.print_screen":Key.print_screen, "Key.f12":Key.f12, "Key.f11":Key.f11, "Key.f10":Key.f10, "Key.f9":Key.f9, "Key.f8":Key.f8, "Key.f7":Key.f7, "Key.f6":Key.f6, "Key.f5":Key.f5, "Key.f4":Key.f4, "Key.f3":Key.f3, "Key.f2":Key.f2, "Key.f1":Key.f1, "Key.esc":Key.esc}
dicsionariodos = dict(map(reversed, dicsionario.items()))  	# inverted dicsionario to access the str from value (i.e.: dicsionariodos[Key.space] --> "Key.space")

global s, nkeys, lastkey, pressdkey, keyspressed
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

ip = str(raw_input("IP: "))
s.connect((ip, 50000))

nkeys = 0  	# number of keys pressed
keyspressed = []     # this will contain the keys pressed in the moment

def on_press(key):
	global s, nkeys, lastkey, pressdkey, keyspressed
	if key != lastkey
		nkeys += 1
	if key not in keyspressed:
		keyspressed.append(key)
	
	try:
		print(key)
		if key != keyboard.Key.esc:
			if len(keyspressed) == 1:	
				s.send("press." + dicsionariodos[key]) 	# sends str, i.e.: "pressKey.delete" if it is no the esc key
			else:
				# Revisa que no de error al pulsar un caracter: key.char.decode()
				try:	
					send = "pressed." + dicsionariodos[[keyspressed][0]]
				except:
					send = "pressed." + dicsionariodos[[keyspressed][0].char.decode()]
				for n in keyspressed:
					if n != keyspressed[0]:
						try:	
							send += ".pressedwith." + dicsionariodos[[n]]
						except:
							send += ".pressedwith." + dicsionariodos[[n.char.decode()]]
				s.send(send)
			
	except:
		if key != keyboard.Key.esc:
			s.send("press." + dicsionariodos[key.char.decode()])
	lastkey = key

def on_release(key):
	global s, nkeys, pressdkey, keyspressed
	nkeys -= 1
	keyspressed.remove(key)
	try:
		s.send("release." + dicsionariodos[key])  	# sends str, i.e.: "releaseKey.delete" if it is no the esc key
	except:
		s.send("release." + dicsionariodos[key.char.decode()])

	if key==keyboard.Key.esc:
		# Stops listener
		s.send('/e')
		s.close()
		return False

with keyboard.Listener(on_press=on_press,on_release=on_release) as listener:
	listener.join()

listener=keyboard.Listener(on_press=on_press,on_release=on_release)
listener.start()
