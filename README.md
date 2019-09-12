# Tcp_connection
basic tcp-server and tcp-client program in python 
the code is written in python 2.7 .
if you want to run it on 3.7 onward, you have to change it a little otherwise error can occur. 
tcp_serverbin.py and tcp_clientbin.py have code which implement crc.
it convert string into binary from  file then encode it and sent to client .
client then decode binary which it received  and convert them into string and store it into a file .
In this piece of code we have introduced error as well randomly. error is user independent .
so computer itself introduce the error while sending binary to client side.
then client should recognise the binary as error free or error  introduce code.
if error free sent 'ack' as acknowlegdement  else 'nack' will be sent.
if server received 'nack' it will send the same frame again until 'ack' receives ;
if server receives 'ack' the next fram will be sent.

