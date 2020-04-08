import binascii
import socket
import struct
import time

# Create a TCP/IP socket
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
#server_address = ('192.168.0.1', 5001)
#server_address = ('128.61.18.161', 5001)
server_address = ('127.0.0.1', 5099)
#server_address = ('128.61.18.161', 5099)
sock.bind(server_address)
#sock.listen(1)

packer = struct.Struct('= I H I I I')
unpacker = struct.Struct('= I H I I I')

file1 = open("server_time.txt","a") 

while True:
	print('\nwaiting to receive message')
	data, address = sock.recvfrom(18)
	start_time = time.time()
	print('received {} bytes from {}'.format(len(data), address))

    #print('\nwaiting for a connection')
    #connection, client_address = sock.accept()
    #try:
    #    data = connection.recv(unpacker.size)
    #    print('received {!r}'.format(binascii.hexlify(data)))

	unpacked_data = unpacker.unpack(data)
	print('unpacked:', unpacked_data)	

	l = list(unpacked_data)
	end_time = time.time()
	elapsed_time = end_time - start_time

	l[3] = elapsed_time*1000000
	#t = tuple(l)
	print('modified:', l)

	packed_data = packer.pack(*l)

    #finally:
    #    connection.close()

	if packed_data:
		end_time = time.time()
		sent = sock.sendto(packed_data, address)
		elapsed_time = (end_time - start_time)*1000000
		file1.write(str(elapsed_time))
		file1.write("\n")
		print('Elapsed Time: ', elapsed_time)
		print('sent {} bytes back to {}'.format(sent, address))
file1.close()