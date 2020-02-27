import binascii
import socket
import struct

# Create a TCP/IP socket
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
server_address = ('localhost', 10000)
sock.bind(server_address)
#sock.listen(1)

unpacker = struct.Struct('I I I I')


while True:
	print('\nwaiting to receive message')
	data, address = sock.recvfrom(16)
	print('received {} bytes from {}'.format(len(data), address))
	print(data)


    #print('\nwaiting for a connection')
    #connection, client_address = sock.accept()
    #try:
    #    data = connection.recv(unpacker.size)
    #    print('received {!r}'.format(binascii.hexlify(data)))

	unpacked_data = unpacker.unpack(data)
	print('unpacked:', unpacked_data)

    #finally:
    #    connection.close()

	if data:
		sent = sock.sendto(data, address)
		print('sent {} bytes back to {}'.format(sent, address))