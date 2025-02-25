import socket

def server():
    try:
        ss = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        print("[S]: Server socket created")
    except socket.error as err:
        print('socket open error: {}\n'.format(err))
        exit()

    server_binding = ('', 50007)
    ss.bind(server_binding)
    ss.listen(1)
    host = socket.gethostname()
    print("[S]: Server host name is {}".format(host))
    localhost_ip = (socket.gethostbyname(host))
    print("[S]: Server IP address is {}".format(localhost_ip))
    csockid, addr = ss.accept()
    print ("[S]: Got a connection request from a client at {}".format(addr))

    # send a intro message to the client.  
    msg = "Welcome to CS 352!"
    csockid.send(msg.encode('utf-8'))

    with open("out-proj.txt", "w") as file:
        data = csockid.recv(1024).decode()
        while data:
            altered_string = data[::-1].swapcase()
            print(altered_string)
            csockid.send(altered_string.encode('utf-8'))
            file.write(altered_string)

            data = csockid.recv(1024).decode()

    # Close the server socket
    ss.close()
    exit()

server()