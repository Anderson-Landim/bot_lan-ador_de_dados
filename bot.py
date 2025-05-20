import random
import tkinter as tk
from ttkbootstrap import Style
from ttkbootstrap.widgets import Entry, Label, Button, LabelFrame
from openpyxl import Workbook, load_workbook
from datetime import datetime
import os
import threading
import time

# Variável de controle
executando = False

# Produtos e preços editáveis
produtos = {
    "Produto 1": 100.0,
    "Produto 2": 200.0,
    "Produto 3": 300.0,
    "Produto 4": 400.0,
    "Produto 5": 500.0
}

def inicializar_excel(nome_arquivo):
    if not os.path.exists(nome_arquivo):
        wb = Workbook()
        ws = wb.active
        ws.title = "Notas"
        ws.append(["Data", "Cliente", "CNPJ", "Produto", "Preço Unitário", "ICMS", "IPI", "PIS", "COFINS", "Valor Total"])
        wb.save(nome_arquivo)

def salvar_linha_excel(linha, nome_arquivo):
    wb = load_workbook(nome_arquivo)
    ws = wb.active
    ws.append(linha)
    wb.save(nome_arquivo)

def erro_ocorre(probabilidade_percentual):
    return random.random() < (probabilidade_percentual / 100)

def aplicar_erro(valor):
    valor_str = str(valor)
    erro_tipo = random.choice(["virgula", "letra", "soma_errada", "numero_errado"])
    if erro_tipo == "virgula":
        return valor_str.replace('.', ',', 1)
    elif erro_tipo == "letra":
        pos = random.randint(0, len(valor_str)-1)
        return valor_str[:pos] + random.choice("abcdefghijklmnopqrstuvwxyz") + valor_str[pos:]
    elif erro_tipo == "soma_errada":
        erro = random.uniform(-10, 10)
        return round(float(valor) + erro, 2)
    elif erro_tipo == "numero_errado":
        return valor_str[:-1] + str(random.randint(0, 9))
    return valor_str

def gerar_nota(cliente, cnpj, impostos, prob_erro):
    produto = random.choice(list(produtos.keys()))
    preco_unitario = produtos[produto]
    impostos_valores = {}
    for nome, porcentagem in impostos.items():
        imposto = preco_unitario * (porcentagem / 100)
        if erro_ocorre(prob_erro):
            imposto = aplicar_erro(imposto)
        else:
            imposto = round(imposto, 2)
        impostos_valores[nome] = imposto

    valor_total = preco_unitario
    for imposto in impostos_valores.values():
        try:
            valor_total += float(imposto)
        except ValueError:
            pass  # erro proposital

    if erro_ocorre(prob_erro):
        preco_unitario = aplicar_erro(preco_unitario)

    return [
        datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        cliente,
        cnpj,
        produto,
        preco_unitario,
        impostos_valores["ICMS"],
        impostos_valores["IPI"],
        impostos_valores["PIS"],
        impostos_valores["COFINS"],
        valor_total
    ]

def loop_continuo(cliente, cnpj, impostos, intervalo, quantidade, nome_arquivo, status_label, prob_erro):
    global executando
    while executando:
        for _ in range(quantidade):
            nota = gerar_nota(cliente, cnpj, impostos, prob_erro)
            salvar_linha_excel(nota, nome_arquivo)
            status_label.config(text=f"Último lançamento: {nota[3]} R${nota[4]}")
        time.sleep(intervalo)

def iniciar():
    global executando
    executando = True

    cliente = cliente_entry.get()
    cnpj = cnpj_entry.get()
    nome_arquivo = nome_entry.get() or "notas_avancado.xlsx"
    intervalo = int(intervalo_entry.get())
    quantidade = int(quantidade_entry.get())
    prob_erro = float(erro_entry.get())

    impostos = {
        "ICMS": float(icms_entry.get()),
        "IPI": float(ipi_entry.get()),
        "PIS": float(pis_entry.get()),
        "COFINS": float(cofins_entry.get())
    }

    for i in range(5):
        nome_produto = produto_entries[i].get()
        preco_produto = float(preco_entries[i].get())
        produtos[nome_produto] = preco_produto

    inicializar_excel(nome_arquivo)
    status_label.config(text="Bot rodando...", foreground="green")
    thread = threading.Thread(target=loop_continuo, args=(cliente, cnpj, impostos, intervalo, quantidade, nome_arquivo, status_label, prob_erro), daemon=True)
    thread.start()

def parar():
    global executando
    executando = False
    status_label.config(text="Bot parado.", foreground="orange")

# === INTERFACE BONITA ===
root = tk.Tk()
root.title("Bot Lançador de NF Avançado")
style = Style("cyborg")
root.geometry("650x1000")
style.configure('TLabel', font=('Segoe UI', 10))
style.configure('TEntry', font=('Segoe UI', 10))

def criar_label_entry(container, texto, entry_default=""):
    Label(container, text=texto).pack(anchor="w", padx=10, pady=(10, 0))
    entry = Entry(container)
    entry.insert(0, entry_default)
    entry.pack(fill="x", padx=10)
    return entry

cliente_frame = LabelFrame(root, text="🧾 Dados do Cliente")
cliente_frame.pack(fill="x", padx=20, pady=10)
cliente_entry = criar_label_entry(cliente_frame, "Cliente:", "Empresa Exemplo")
cnpj_entry = criar_label_entry(cliente_frame, "CNPJ:", "12.345.678/0001-90")

impostos_frame = LabelFrame(root, text="💰 Impostos (%)")
impostos_frame.pack(fill="x", padx=20, pady=10)
icms_entry = criar_label_entry(impostos_frame, "ICMS (%):", "18")
ipi_entry = criar_label_entry(impostos_frame, "IPI (%):", "5")
pis_entry = criar_label_entry(impostos_frame, "PIS (%):", "1.65")
cofins_entry = criar_label_entry(impostos_frame, "COFINS (%):", "7.6")

config_frame = LabelFrame(root, text="⚙️ Configurações")
config_frame.pack(fill="x", padx=20, pady=10)
nome_entry = criar_label_entry(config_frame, "Nome do Arquivo Excel:", "notas_avancado.xlsx")
intervalo_entry = criar_label_entry(config_frame, "Intervalo entre ciclos (segundos):", "5")
quantidade_entry = criar_label_entry(config_frame, "Quantidade de notas por ciclo:", "2")
erro_entry = criar_label_entry(config_frame, "Probabilidade de Erro (%):", "10")

produtos_frame = LabelFrame(root, text="📦 Produtos e Preços")
produtos_frame.pack(fill="x", padx=20, pady=10)
produto_entries = []
preco_entries = []

for i in range(5):
    linha = tk.Frame(produtos_frame)
    linha.pack(fill="x", padx=10, pady=2)
    produto_entry = Entry(linha, width=30)
    produto_entry.insert(0, f"Produto {i+1}")
    produto_entry.pack(side="left", padx=(0, 10))
    preco_entry = Entry(linha, width=15)
    preco_entry.insert(0, str(produtos[f"Produto {i+1}"]))
    preco_entry.pack(side="left")
    produto_entries.append(produto_entry)
    preco_entries.append(preco_entry)

botoes_frame = tk.Frame(root)
botoes_frame.pack(pady=15)
Button(botoes_frame, text="▶ Iniciar Lançamento", bootstyle="success", command=iniciar).pack(side="left", padx=10)
Button(botoes_frame, text="■ Parar Lançamento", bootstyle="danger", command=parar).pack(side="left", padx=10)

status_label = Label(root, text="", anchor="center", font=("Segoe UI", 10, "bold"))
status_label.pack(pady=10)

root.mainloop()
