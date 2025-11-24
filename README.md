# 🔐 Projeto – Simulação de Malware em Ambiente Seguro

Este repositório apresenta uma **simulação educativa** de dois tipos de malware:  
**Ransomware** e **Keylogger**, ambos implementados em Python de forma totalmente segura (sem qualquer comportamento malicioso real).

---

## 🎯 Objetivos

- Demonstrar, de forma controlada, como ransomwares e keyloggers funcionam.  
- Simular técnicas de criptografia, captura de teclas e exfiltração de dados.  
- Documentar boas práticas de defesa e prevenção em cibersegurança.  
- Utilizar o GitHub como portfólio técnico.

---

# 🕵️ Ransomware Simulado

Script: **`ransomware_simulado.py`**  

Este script:

- Lê arquivos da pasta `/arquivos`
- “Criptografa” usando Base64 (simulação inofensiva)
- Gera arquivos com extensão `.locked`
- Exibe mensagem de “resgate” fictícia
- Restaura os arquivos com a opção de descriptografia

**Obs.:** A criptografia é apenas ilustrativa e totalmente reversível.

---

# ⌨️ Keylogger Simulado

Script: **`keylogger_simulado.py`**

O keylogger simulado:

- Registra teclas fictícias em `logs.txt`
- Simula comportamento furtivo
- Simula envio de e-mail com os dados coletados
- Gera um fluxo completo de demonstração sem capturar teclas reais

---

# 🛡️ Medidas de Defesa

Principais práticas aprendidas:

- Uso de antivírus e firewall
- Sandboxing para análise segura de arquivos
- Controle de acessos e MFA
- Backups regulares para mitigar ransomware
- Conscientização do usuário contra phishing e engenharia social

---

# 📁 Estrutura do Repositório

```
/README.md
/ransomware_simulado.py
/keylogger_simulado.py
/arquivos
/images
```

A pasta `/images` contém prints demonstrativos, e `/arquivos` contém arquivos de teste para a simulação.

---

# ✅ Conclusão

Este projeto demonstra, de forma prática e segura, o funcionamento básico de malwares comuns e como podemos nos proteger deles por meio de boas práticas de segurança e análise preventiva.

