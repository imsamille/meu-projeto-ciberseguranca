import os
import base64

PASTA = "arquivos"

def criptografar():
    for arquivo in os.listdir(PASTA):
        caminho = os.path.join(PASTA, arquivo)

        with open(caminho, "rb") as f:
            conteudo = f.read()

        criptografado = base64.b64encode(conteudo)

        with open(caminho + ".locked", "wb") as f:
            f.write(criptografado)

    print("\n[SIMULAÇÃO] Arquivos 'criptografados'.")
    print("Mensagem de resgate: Seus arquivos foram trancados! Use a chave para restaurar.\n")


def descriptografar():
    for arquivo in os.listdir(PASTA):
        if not arquivo.endswith(".locked"):
            continue

        caminho = os.path.join(PASTA, arquivo)

        with open(caminho, "rb") as f:
            conteudo = f.read()

        original = base64.b64decode(conteudo)

        novo_nome = caminho.replace(".locked", "")

        with open(novo_nome, "wb") as f:
            f.write(original)

    print("\n[SIMULAÇÃO] Arquivos restaurados com sucesso!\n")


print("=== RANSOMWARE SIMULADO ===")
print("1 - Criptografar arquivos")
print("2 - Descriptografar arquivos")

escolha = input("Escolha: ")

if escolha == "1":
    criptografar()
elif escolha == "2":
    descriptografar()
else:
    print("Opção inválida.")
