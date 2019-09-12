import socket
import threading
import random
bind_ip=''
bind_port = 3343

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((bind_ip,bind_port))

server.listen(5)
crc8="100000111"


def xor(a, b): 

	 
	result = []  
	for i in range(1, len(b)): 
		if a[i] == b[i]: 
			result.append('0') 
		else: 
			result.append('1') 
	return ''.join(result) 


# Performs Modulo-2 division 
def mod2div(divident, divisor): 
	# Number of bits to be XORed at a time. 
	pick = len(divisor) 
	# Slicing the divident to appropriate 
	# length for particular step 
	tmp = divident[0 : pick] 
	while pick < len(divident): 
		if tmp[0] == '1': 
			# replace the divident by the result 
			# of XOR and pull 1 bit down 
			tmp = xor(divisor, tmp) + divident[pick] 

		else: # If leftmost bit is '0' 
			# If the leftmost bit of the dividend (or the 
			# part used in each step) is 0, the step cannot 
			# use the regular divisor; we need to use an 
			# all-0s divisor. 
			tmp = xor('0'*pick, tmp) + divident[pick] 

		# increment pick to move further 
		pick += 1

	# For the last n bits, we have to carry it out 
	# normally as increased value of pick will cause 
	# Index Out of Bounds. 
	if tmp[0] == '1': 
		tmp = xor(divisor, tmp) 
	else: 
		tmp = xor('0'*pick, tmp) 

	checkword = tmp 
	return checkword 

# Function used at the sender side to encode 
# data by appending remainder of modular divison 
# at the end of data. 
def encodeData(data, key): 

	l_key = len(key) 

	# Appends n-1 zeroes at end of data 
	appended_data = data + '0'*(l_key-1) 
	remainder = mod2div(appended_data, key) 

	# Append remainder in the original data 
	codeword = data + remainder 
	#print("Remainder : ", remainder) 
	#print("Encoded Data (Data + Remainder) : ", codeword) 
	return codeword
#introducing error
def error(p,i):
	
	if(p[i]==' '):
		m=p[:i+5]
		if p[i+5]=='0':
			x='1'
			m=m+x
		else:
			x='0'
			m=m+x
		m=m+p[i+1:len(p)]
				
		return m
		
	elif p[i]=='0':
		m=p[:i]
		x='1'
		m=m+x
	else:
		m=p[:i]
		x='0'
		m=m+x
	m=m+p[i+1:len(p)]
	return m




#sending data to client
def send(l,client_sockett):
	r1 = random.randint(10,1000)
	if(r1%2==0):
		p = ' '.join(encodeData(j, crc8) for j in l)
		client_sockett.send(str(p))
		acknowledge = client_sockett.recv(1024)
		if acknowledge == 'nack':
			send(l,client_sockett)
		else:
			
			return		
		return
	else:
		r2 = random.randint(100,1000)
		
		
		p = ' '.join(encodeData(j, crc8) for j in l)
		ith = r2%(len(p))
		j=error(p,ith)
		
		client_sockett.send(str(j))
		acknowledge = client_sockett.recv(1024)
				
		if acknowledge == 'nack':
			send(l,client_sockett)
		else:
			return
		return
		
		

# this is our client-handling thread
def msg(client_sockett):
		
	
	a = open('text.txt','r')
	for i in a:
		
		b=' '.join(format(ord(x), 'b') for x in i)
		l=b.split()
		send(l,client_sockett)
		
	return (1)
		

def handle_client(client_socket):
	
	print("*******************************\n")
	print("data is being sent ")
	print("*******************************")
	client_socket.send(str(crc8))
	msg(client_socket)
	client_socket.close()
	


        
while True:
	
	print ("[*] Listening on %s:%d" % (bind_ip,bind_port))

	client,addr = server.accept()
	print ("[*] Accepted connection from: %s:%d" % (addr[0],addr[1]))
	#client_handler = handle_client(client)
	client_handler = threading.Thread(target=handle_client,args=(client,))
	client_handler.start()

