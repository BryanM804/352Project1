import socket

input_data_file = "in-proj.txt"
buffer_size = 200

def client():

    # Attempt to create a client socket
    try:
        cs = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        print("[C]: Client socket created")
    except socket.error as err:
        print('socket open error: {} \n'.format(err))
        exit()
        
    # Connect to server
    port = 50007
    localhost_addr = socket.gethostbyname(socket.gethostname())
    server_binding = (localhost_addr, port)
    cs.connect(server_binding)

    # Send data to server
    # Send line by line, waiting for a ACK response after each line
    # Send next line only if ACK response is received
    with open(input_data_file, "r") as f:
        for line in f:
            line = line.rstrip()
            cs.send(line.encode('utf-8'))
            print("[C]: Data sent to server: {}".format(line))
            ack = cs.recv(buffer_size)
            print("[C]: ACK received from server: {}".format(ack.decode('utf-8')))
    
    # close the client socket
    cs.close()
    print("[C]: Connection closed")

    exit()

if __name__ == "__main__":
    client()