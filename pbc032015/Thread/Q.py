def hello(e):
	while  1 :
		if  not e.wait(3):
			logging.info("communicating......")
		else:
			logging.info("preparing to quit...")
			time.sleep(5)
			exit(1)
def showmenu(e):
	while 1:
		inp = raw_input(" enter your choice...")
		if(inp = 'q')
		e.set()
		exit(0)
e.threading.Event()
t1 = threading.Thread(target = hello, args =(e,))
t2 = threading.Thread(target = showmenu, args =(e,))
t1.start()
t1.start()