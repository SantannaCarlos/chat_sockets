import socket
import threading

HOST = '0.0.0.0'
PORTA = 12345

clientes = {}

def enviar_para_todos(mensagem, remetente=None):
    for conexao in clientes:
        if conexao != remetente:
            try:
                conexao.sendall(mensagem.encode())
            except:
                remover_cliente(conexao)

def mensagem_privada(remetente, destino, mensagem):
    for conexao, nome in clientes.items():
        if nome == destino:
            conexao.sendall(f"[Privado de {clientes[remetente]}] {mensagem}".encode())
            return
    remetente.sendall(f"[Servidor] Usuário '{destino}' não encontrado.".encode())

def remover_cliente(conexao):
    if conexao in clientes:
        nome = clientes[conexao]
        enviar_para_todos(f"[Servidor] {nome} saiu do chat.")
        del clientes[conexao]
        conexao.close()

def lidar_com_cliente(conexao, endereco):
    try:
        conexao.sendall("Digite seu nome de usuário: ".encode())
        nome = conexao.recv(1024).decode().strip()
        clientes[conexao] = nome
        enviar_para_todos(f"[Servidor] {nome} entrou no chat.")
        conexao.sendall("Comandos: /private usuario mensagem | /online\n".encode())
    except:
        conexao.close()
        return

    while True:
        try:
            mensagem = conexao.recv(1024).decode().strip()
            if not mensagem:
                break

            if mensagem.startswith("/private"):
                partes = mensagem.split(" ", 2)
                if len(partes) == 3:
                    _, destino, conteudo = partes
                    mensagem_privada(conexao, destino, conteudo)
                else:
                    conexao.sendall("Uso correto: /private usuario mensagem".encode())

            elif mensagem == "/online":
                usuarios_online = ", ".join(clientes.values())
                conexao.sendall(f"Online: {usuarios_online}".encode())

            else:
                enviar_para_todos(f"{nome}: {mensagem}", conexao)

        except:
            break

    remover_cliente(conexao)

def iniciar_servidor():
    servidor = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    servidor.bind((HOST, PORTA))
    servidor.listen()
    print(f"Servidor iniciado em {HOST}:{PORTA}")

    while True:
        conexao, endereco = servidor.accept()
        thread = threading.Thread(target=lidar_com_cliente, args=(conexao, endereco))
        thread.start()

if __name__ == "__main__":
    iniciar_servidor()
