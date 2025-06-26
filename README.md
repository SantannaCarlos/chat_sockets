# 💬 Chat em Rede via Terminal com Sockets TCP

Este é um projeto de um sistema de comunicação (chat) em rede, utilizando sockets TCP com suporte a múltiplos usuários, mensagens públicas e privadas, desenvolvido em Python 3.

---

## ⚙️ Funcionalidades

- Conexões simultâneas de múltiplos clientes.
- Identificação por nome de usuário.
- Mensagens públicas visíveis a todos no chat.
- Mensagens privadas com o comando `/private`.
- Comando `/online` para listar os usuários conectados.
- Interface totalmente via terminal (modo texto).
- Comunicação bidirecional entre cliente e servidor.

---

## 📁 Estrutura do Projeto

chat-sockets/

├── servidor.py (código do servidor)

├── cliente.py (código do cliente)

├── README.md (este arquivo)

└── manual.pdf (manual do sistema em PDF)


---

## 🚀 Como Executar

### 1. Requisitos

- Ter Python 3 instalado na máquina.

### 2. Iniciar o servidor

Abra um terminal, vá até a pasta do projeto e execute o arquivo `servidor.py`.  
O servidor será iniciado e ficará aguardando conexões.

### 3. Iniciar os clientes

Abra um ou mais terminais em outro computador (ou na mesma máquina) e execute o arquivo `cliente.py`.  
Digite seu nome de usuário quando for solicitado.

---

## 💻 Comandos Disponíveis

- **Mensagem comum:**  
  Qualquer texto enviado será visto por todos os participantes do chat.

- **Mensagem privada:**  
/private nome_do_usuario mensagem

Envia uma mensagem privada apenas para o usuário especificado.

- **Ver quem está online:**  
/online

- **Sair do chat:**  
/quit

---

## 🎥 Vídeo Demonstração

O vídeo demonstrando o funcionamento do sistema e a explicação do código por todos os integrantes está disponível no link abaixo:  
**[Vídeo Tutorial e Explicativo](https://youtu.be/kTgasy9-Im4)**

---

## 👥 Desenvolvedor

- Carlos Henrique Fernandes Sant'Anna — SC304582X

---
