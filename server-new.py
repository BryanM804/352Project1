import socket

output_file = "out-proj.txt"
output_data = []
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

    # Whenever data is received from client, process it and add it to output_data
    # Send an ACK response after processing each, to tell client to send next line
    while True:
        data_from_client = csockid.recv(buffer_size) # receive data from client

        # if client closes connection, data_from_client will be empty
        if not data_from_client:
            break

        print("[S]: Data received from client: {}".format(data_from_client.decode('utf-8')))
        processed_data = process_data(data_from_client.decode('utf-8'))
        output_data.append(processed_data)
        print("[S]: Data processed: {}".format(processed_data))

        ack = "ACK"
        csockid.send(ack.encode('utf-8')) # send ACK to client
    
    # Write output_data to output_file
    with open(output_file, "w") as f:
        for line in output_data:
            f.write(line + "\n")

    # Close the server socket
    ss.close()
    exit()

def process_data(data: str) -> str:
    return data[::-1].swapcase() # Reverse the string and swap the case of each character

if __name__ == "__main__":
    server()