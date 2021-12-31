# SERVER
import socket, msvcrt
from pynput.keyboard import Key, Controller

dicsionario = {"Key.enter":Key.enter, "Key.delete":Key.delete, "Key.insert":Key.insert, "Key.right":Key.right, "Key.down":Key.down, "Key.left":Key.left, "Key.ctrl_r":Key.ctrl_r, "Key.cmd":Key.cmd, "Key.ctrl_l":Key.ctrl_l, "Key.alt_gr":Key.alt_gr, "<":"<", "Key.space":Key.space, "Key.alt_l":Key.alt_l, "Key.ctrl_l":Key.ctrl_l, "Key.page_down":Key.page_down, "Key.down":Key.down, "Key.end":Key.end, "Key.up":Key.up, "Key.shift_r":Key.shift_r, "-":"-", ".":".", ",":",", "m":"m", "n":"n", "b":"b", "v":"v", "c":"c", "x":"x", "z":"z", "Key.shift":Key.shift, "+":"+", "Key.right":Key.right, "Key.left":Key.left, "Key.enter":Key.enter, "[u'\xb4']":u'\xb4', "u'\xf1'":u'\xf1', "l":"l", "k":"k", "j":"j", "h":"h", "g":"g", "f":"f", "d":"d", "s":"s", "a":"a", "Key.caps_lock":Key.caps_lock, "Key.page_up":Key.page_up, "Key.up":Key.up, "Key.home":Key.home, "u'\xe7'":u'\xe7', "+":"+", "`":"`", "p":"p", "o":"o", "i":"i", "u":"u", "y":"y", "t":"t", "r":"r", "e":"e", "w":"w", "q":"q", "Key.tab":Key.tab, "-":"-", "*":"*", "-":"-", "Key.num_lock":Key.num_lock, "Key.backspace":Key.backspace, "u'\xa1'":u'\xa1', "'":"'", "0":"0", "9":"9", "8":"8", "7":"7", "6":"6", "5":"5", "4":"4", "3":"3", "2":"2", "1":"1", "u'\xba'":u'\xba', "Key.page_down":Key.page_down, "Key.page_up":Key.page_up, "Key.delete":Key.delete, "Key.insert":Key.insert, "Key.pause":Key.pause, "Key.scroll_lock":Key.scroll_lock, "Key.print_screen":Key.print_screen, "Key.f12":Key.f12, "Key.f11":Key.f11, "Key.f10":Key.f10, "Key.f9":Key.f9, "Key.f8":Key.f8, "Key.f7":Key.f7, "Key.f6":Key.f6, "Key.f5":Key.f5, "Key.f4":Key.f4, "Key.f3":Key.f3, "Key.f2":Key.f2, "Key.f1":Key.f1, "Key.esc":Key.esc}

keybd = Controller()

pcname = socket.gethostname()
ip = socket.gethostbyname(pcname)

print("This is the IP you have to share: {}?".format(ip))

print("[*] Creating connection...")
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((ip, 50000))
s.listen(1)
conn, addr = s.accept()
print("[+] Connected to {}! Program is ready to send keys!".format(addr))


def funcionrec(keyspressed):
	keypressed = keyspressed[0]

	if len(keyspressed) > 2:
		with keybd.pressed(keypressed):
			funcionrec(keyspressed[1:len(keyspressed)])
	elif len(keyspressed) == 2:
		with keybd.pressed(keypressed):
			keybd.press(keyspressed[-1])
			keybd.release(keyspressed[-1])


exit = 0
tdata=[]

while exit == 0:
	data = conn.recv(1024)		# Recieve the data
	data = data.decode('ascii')	# Decode
	print(data)

	if data.startswith('press.'):
		keybd.press(dicsionario[data.split('press.')[1]])

	elif data.startswith('release.'):
		keybd.release(dicsionario[data.split('release.')[1]])

	elif data.startswith('pressed.'):
		keyspressed = data.split('pressed.')[1].split('.pressedwith.')
		for i in range(len(keyspressed)):
			keyspressed[i] = dicsionario[keyspressed[i]]

		funcionrec(keyspressed)

	if data == '/e':
		keybd.release(dicsionario[data.split('press.')[1]])
		exit = 1

conn.close()
s.close()
print("\n[-] Connection ended.")  