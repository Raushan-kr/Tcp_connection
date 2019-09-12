import socket
import threading
target_host = "127.0.0.1"
target_port = 3343
# create a socket object
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# connect the client
client.connect(('',target_port))
# send some data
def binaryToDecimal(binary): 
      
    binary1 = binary 
    decimal, i, n = 0, 0, 0
    while(binary != 0): 
        dec = binary % 10
        decimal = decimal + dec * pow(2, i) 
        binary = binary//10
        i += 1
    #print(decimal)
	
    #print(chr(decimal))
    return(chr(decimal))

def xor(a, b): 

	# initialize result 
	result = [] 

	# Traverse all bits, if bits are 
	# same, then XOR is 0, else 1 
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
def decodeData(data, key,): 

	l_key = len(key) 

	# Appends n-1 zeroes at end of data 
	appended_data = data + '0'*(l_key-1) 
	remainder = mod2div(appended_data, key) 
	if remainder =='00000000':
		codeword = int(data)/100000000
		
		
		return str(codeword) 
	else:

		codeword = ''
		return codeword

divisor=client.recv(1024)
print("crc8:")
print(divisor)	
a=open('text1.txt','w+')
dic={}
i=0
frame=1

response = client.recv(1024)
print("<-------DOWNLOADING-------->")
	
print("******_____-----data is being received ------_______*******\n")
print("******please wait*****")
while True:
   r=''	
   if response=="":	
	break
   else:
#def receiver()
	
	
	
	
	l=response.split()
	
	

	
	
	for j in l:
		p=decodeData(j, divisor)
		
		
		if (p == ""):
			
			r= ''
						
			break 
		else:		
			if(len(p)>15):
				
				print(p)
				a=int(p)%1000000000000000
				c=int(p)/10000000000000000
				b=binaryToDecimal(int(c))
				
				r = r + b
				b=binaryToDecimal(int(a))
				
				r = r + b
			
			else:
				if(p==' '):
					continue
				else:
	
					
					b=binaryToDecimal(int(p))
					r = r + b
   if(r == ''):
	 i = i+1
	 frame = frame
	 ack= 'nack'
   else:
	 i=0
	 
	 ack='ack'
   	
	 frame =frame +1
   dic[frame] = i+1
  
   client.send(ack)
   response=" "
   response = client.recv(1024)
   #print(r)
   a.writelines(r) 
count = 0
for i in dic:
	if (dic[i] == 1):
		count=count
	else:
		count = count+1
print("number of frame which were in error")

print(count)
print("number of tries attempt on each frame")			
print(dic)


