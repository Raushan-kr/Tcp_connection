import socket
target_host = "127.0.0.1"
target_port = 3339
# create a socket object
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# connect the client
client.connect((target_host,target_port))
# send some data
print("*******************************")
print("enter 'exit' or 'good bye' to end this chat")
print("*******************************")
	
while True:
	
	
	data1 = raw_input("enter data1 to  send\n")
	client.send(data1)
	data2 = raw_input("enter data1 to  send\n")
	client.send(data2)

	print(" ***** data is sent ******")
	if data1=='exit':
		print("leaving chat room")
		client.send("good bye")
		exit(1)
# receive some data

	response = client.recv(1024)
	print("******_____-----data is being received ------_______*******\n")
	print (response)
	if response=='exit':
		print("leaving chat room")
		client.send("good bye")
		exit(1)
