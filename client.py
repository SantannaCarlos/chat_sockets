import socket
import threading

HOST = '127.0.0.1'
PORTA = 12345

def receber_mensagens(socket_cliente):
    while True:
        try:
            dados = socket_cliente.recv(1024)
            if not dados:
                break
            print(dados.decode())
        except:
            break

def iniciar_cliente():
    cliente = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    cliente.connect((HOST, PORTA))

    resposta = cliente.recv(1024).decode()
    nome = input(resposta)
    cliente.sendall(nome.encode())

    thread = threading.Thread(target=receber_mensagens, args=(cliente,))
    thread.daemon = True
    thread.start()

    while True:
        try:
            mensagem = input()
            if mensagem.lower() == "/quit":
                break
            cliente.sendall(mensagem.encode())
            if not mensagem.startswith("/"):
                print(f"{nome}: {mensagem}")
        except:
            break

    cliente.close()

if __name__ == "__main__":
    iniciar_cliente()
