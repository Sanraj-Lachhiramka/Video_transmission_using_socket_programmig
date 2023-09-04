#10.16.160.101
import cv2,socket,pickle,struct
#socket create
server_socket=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
host_name=socket.gethostname()
host_ip=socket.gethostbyname(host_name)
print("HOST IP:",host_ip)
port=8000
socket_address=(host_ip,port)

#Socket BIND
server_socket.bind(socket_address)

#Socket listen
server_socket.listen()
print("Listening at:",socket_address)

#socket accept
while True:
    client_socket,addr=(server_socket.accept())
    print("Got connection from:",addr)
    if client_socket:
        vid=cv2.VideoCapture(0)
        img,frame=vid.read()
        a=pickle.dumps(frame)
        message=struct.pack("Q",len(a))+a
        client_socket.sendall(message)
        cv2.imshow('Transmitting video',frame)
        key=cv2.waitKey(1) & 0xFF
        if key==ord('q'):
            client_socket.close() 




