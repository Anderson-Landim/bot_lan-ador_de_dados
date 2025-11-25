# 🧾 Bot Lançador de NF Avançado

Um **bot automatizador de lançamentos de notas fiscais simuladas** com interface gráfica moderna desenvolvida em **Python**, utilizando `tkinter` e `ttkbootstrap`.  
O sistema permite configurar clientes, produtos, impostos e gerar **notas com erros simulados**, salvando todos os dados em um banco **SQLite3**.

---

## 🚀 Funcionalidades Principais

✅ Interface moderna com tema escuro (`ttkbootstrap`)  
✅ Cadastro de até **5 produtos** com preços configuráveis  
✅ Definição de **cliente, CNPJ e impostos (ICMS, IPI, PIS, COFINS)**  
✅ Lançamento contínuo de notas fiscais com:
- Quantidade de lançamentos por ciclo  
- Intervalo entre ciclos  
- **Probabilidade de erros simulados**  

✅ Tipos de erros gerados:
- Troca de `.` por `,`  
- Inserção de letras em números  
- Soma incorreta dos valores  
- Alteração de dígitos  

✅ Exportação para gravação local no banco `SQLite3`

---

## 🧠 Tecnologias Utilizadas

| Categoria | Tecnologias |
|------------|--------------|
| Linguagem  | Python 3 |
| Interface  | tkinter, ttkbootstrap |
| Dados      | openpyxl, SQLite3 |
| Lógica e Simulação | threading, random, datetime |

---

## 📈 Estrutura do Arquivo Excel

O arquivo gerado (`notas_avancado.xlsx`) possui o seguinte formato:

| Data e Hora         | Cliente         | CNPJ               | Produto   | Preço Unitário | ICMS | IPI | PIS  | COFINS | Valor Total |
| ------------------- | --------------- | ------------------ | --------- | --------------- | ---- | --- | ---- | ------ | ----------- |
| 2025-05-19 20:01:00 | Empresa Exemplo | 12.345.678/0001-90 | Produto 1 | 100.0 | 18.0 | 5.0 | 1.65 | 7.6 | 132.25 |

---

## ⚙️ Instalação

1. Clone o repositório:
   ```bash
   git clone https://github.com/Anderson-Landim/bot_gerador_de_dados.git
