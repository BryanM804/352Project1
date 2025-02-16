import socket

input_data_file = "in-proj.txt"
output_data_file = "out-proj.txt"
output_data = []
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
    # Send line by line, waiting for a response after each line
    with open(input_data_file, "r") as f:
        for line in f:
            line = line.rstrip()
            print("[C]: Sending data to server: {}".format(line))
            cs.send(line.encode('utf-8'))
            data_from_server = cs.recv(buffer_size)
            print("[C]: Data received from server: {}".format(data_from_server.decode('utf-8')))
            output_data.append(data_from_server.decode('utf-8'))

    # close the client socket
    cs.close()
    print("[C]: Connection closed")

    # Write output data to file
    with open(output_data_file, "w") as f:
        for line in output_data:
            f.write(line)
            f.write("\n")

    exit()

if __name__ == "__main__":
    client()