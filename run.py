import datetime
import os
import platform
import socket

def ping():
	# to ping a particular IP
	try:
		socket.setdefaulttimeout(3)# if data interruption occurs for 3
		# seconds, <except> part will be executed
		s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		# AF_INET: address family
		# SOCK_STREAM: type for TCP

		host = "12.0.0.1"
		port = 80

		server_address = (host, port)
		s.connect(server_address)

	except OSError as error:
		return False
		# function returns false value
		# after data interruption

	else:
		s.close()
		# closing the connection after the
		# communication with the server is completed
		return True

def first_check():
    if ping():
        print("\nConnection Acquired\n")
        connection_acquired_time = datetime.datetime.now()
        acquiring_message = "connection acquired at: " + \
			str(connection_acquired_time).split(".")[0]
        print(acquiring_message)
    else:
        print("\nConnection Failed\n")

username=os.getlogin() #to get username
detail=platform.uname() # ('Windows', 'name', 'XP', '5.1.2600', 'x86', 'x86 Family 6 Model 15 Stepping 6, GenuineIntel')
print(username,detail)
first_check()