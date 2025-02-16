import socket

buffer_size = 200

def server():

    # Attempt to create a server socket
    try:
        ss = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        print("[S]: Server socket created")
    except socket.error as err:
        print('socket open error: {}\n'.format(err))
        exit()

    # Bind the server socket
    server_binding = ('', 50007)
    ss.bind(server_binding)

    # Start listening on the server socket
    ss.listen(1)
    host = socket.gethostname()
    print("[S]: Server host name is {}".format(host))
    localhost_ip = (socket.gethostbyname(host))
    print("[S]: Server IP address is {}".format(localhost_ip))

    # Accept an incoming connection request (client socket)
    csockid, addr = ss.accept() # get details of client socket
    print ("[S]: Got a connection request from a client at {}".format(addr))

    # Whenever data is received from client, process it and send it back. Repeat until client closes connection.
    while True:
        data_from_client = csockid.recv(buffer_size) # receive data from client

        # if client closes connection, data_from_client will be empty
        if not data_from_client:
            break

        print("[S]: Data received from client: {}".format(data_from_client.decode('utf-8')))
        data_to_client = process_data(data_from_client.decode('utf-8')) # process data
        print("[S]: Data to be sent to client: {}".format(data_to_client))
        csockid.send(data_to_client.encode('utf-8')) # send processed data back to client

    # Close the server socket
    ss.close()
    exit()

def process_data(data: str) -> str:
    return data[::-1].swapcase() # Reverse the string and swap the case of each character

if __name__ == "__main__":
    server()