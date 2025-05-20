
## 🧾 Bot Lançador de NF Avançado

Este projeto é um **bot automatizador de lançamentos de notas fiscais simuladas** com interface gráfica desenvolvida em **Python** usando `tkinter` e `ttkbootstrap`. O sistema permite configurar cliente, produtos, impostos e gerar notas com possibilidade de  **erros simulados** , gravando tudo em um arquivo Excel.

---


### ✅ Funcionalidades

* Interface visual com tema escuro moderno (via `ttkbootstrap`)
* Cadastro de até **5 produtos com preços configuráveis**
* Definição de **cliente, CNPJ e impostos (ICMS, IPI, PIS, COFINS)**
* Lançamento contínuo de notas fiscais com:
  * Quantidade de lançamentos por ciclo
  * Intervalo entre ciclos
  * **Probabilidade de erros simulados** nas notas
* Erros possíveis:
  * Substituição de `.` por `,`
  * Inserção de letras no número
  * Soma incorreta dos valores
  * Alteração de dígito no número
* Geração de arquivo `.xlsx` com todos os lançamentos

---

### 🛠️ Tecnologias Utilizadas

* `Python 3`
* `tkinter` + `ttkbootstrap`
* `openpyxl`
* `threading`
* `random` e `datetime`

---

### 📁 Estrutura do Excel

O arquivo gerado (`notas_avancado.xlsx`) contém:

| Data e Hora         | Cliente         | CNPJ               | Produto   | Preço Unitário | ICMS | IPI | PIS  | COFINS | Valor Total |
| ------------------- | --------------- | ------------------ | --------- | ---------------- | ---- | --- | ---- | ------ | ----------- |
| 2025-05-19 20:01:00 | Empresa Exemplo | 12.345.678/0001-90 | Produto 1 | 100.0            | 18.0 | 5.0 | 1.65 | 7.6    | 132.25      |

---

### 🚀 Como Usar

1. Instale as dependências (recomenda-se usar um ambiente virtual):
   ```bash
   pip install ttkbootstrap openpyxl
   ```
2. Execute o script:
   ```bash
   python bot_nf.py
   ```
3. Configure os dados na interface:
   * Cliente e CNPJ
   * Impostos (%)
   * Nome do arquivo Excel
   * Intervalo e quantidade por ciclo
   * Probabilidade de erro (%)
   * Produtos e preços
4. Clique em **"▶ Iniciar Lançamento"** para começar.
5. Clique em **"■ Parar Lançamento"** para interromper.

---

### 📌 Exemplo de Aplicação

Este bot pode ser usado para:

* Simulações de automação contábil
* Testes em sistemas de leitura de notas
* Estudo de erros comuns em documentos fiscais
* Demonstrações educacionais de manipulação de dados com Python
* Fazer limpeza de dados

---

### 📄 Licença

Este projeto é de uso livre para fins educacionais.

---

### 📧 Contato

Se tiver dúvidas ou sugestões, sinta-se à vontade para entrar em contato.

Anderson Landim (35 997280595) anderson_landim@outlook.com.br

---
