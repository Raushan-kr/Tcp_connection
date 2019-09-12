import socket
import threading
bind_ip = "127.0.0.1"
bind_port = 3344
BUFSIZ = 1024
ADDR = ('',bind_port)
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((bind_ip,bind_port))

server.listen(5)


# this is our client-handling thread
def msg(client_sockett):
	while True:
		print("***---- receiving -----****")
		request1 = client_sockett.recv(1024)
		print ("[*] Received: %s" % request1)
		request2 = client_sockett.recv(1024)
		print ("[*] Received: %s" % request2)
		if request1 == "good bye" or request1 == "exit" or request2 == "good bye" or request2 == "exit":
			return(1)
		x=int(input("if addition press 1 else0"))
		if (x == 1):
			data1 = int(request1)+int(request2)
			print("*******-----sending----*****")
			print(data1) 
			client_sockett.send(str(data1))
		else:
			data1 = int(request1)-int(request2)
			print("*******-----sending----*****") 
			print(data1)			
			client_sockett.send(str(data1))



def handle_client(client_socket):
	# print out what the client sends
	#request = client_socket.recv(1024)
	#print "[*] Received: %s" % request
	# send back a packet
	print("*******************************")
	print("enter 'exit' to end this chat")
	print("*******************************")
	msg(client_socket)
	client_socket.close()


        
while True:
	
	print "[*] Listening on %s:%d" % (bind_ip,bind_port)

	client,addr = server.accept()
	print "[*] Accepted connection from: %s:%d" % (addr[0],addr[1])
	#client_handler = handle_client(client)
	client_handler = threading.Thread(target=handle_client,args=(client,))
	client_handler.start()

