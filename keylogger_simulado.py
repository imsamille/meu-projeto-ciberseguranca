import time

arquivo_log = "logs.txt"

def registrar_tecla_simulada(tecla):
    with open(arquivo_log, "a") as f:
        f.write(f"[SIMULADO] Tecla registrada: {tecla}\n")


def capturar_teclas():
    teclas_ficticias = ["A", "B", "C", "ENTER", "ESPACO"]

    print("\nIniciando keylogger SIMULADO...\n")

    for tecla in teclas_ficticias:
        registrar_tecla_simulada(tecla)
        time.sleep(0.3)

    print("Captura simulada finalizada! Logs gravados.\n")


def enviar_email_simulado():
    print("[SIMULAÇÃO] Enviando logs por e-mail...")
    time.sleep(1)
    print("[SIMULAÇÃO] Logs enviados para o servidor.\n")


print("=== KEYLOGGER SIMULADO ===")
capturar_teclas()
enviar_email_simulado()
