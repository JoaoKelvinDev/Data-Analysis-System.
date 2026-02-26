# Criando o código atualizado com ordenação alfabética e ajustes profissionais

import pandas as pd
import tkinter as tk
from tkinter import filedialog, messagebox
import os
from datetime import datetime
from fpdf import FPDF


def carregar_planilhas():
    caminhos = filedialog.askopenfilenames(
        title="Selecione as planilhas Excel",
        filetypes=[("Planilhas Excel", "*.xlsx *.xls")]
    )
    if not caminhos:
        return None

    planilhas = []
    for caminho in caminhos:
        try:
            df = pd.read_excel(caminho, sheet_name=0, skiprows=3)
            planilhas.append(df)
        except Exception as e:
            messagebox.showerror("Erro ao ler planilha", f"Erro no arquivo:\\n{caminho}\\n\\n{str(e)}")
            return None

    if planilhas:
        return pd.concat(planilhas, ignore_index=True)
    return None


def formatar_datas(df, nomes_datas):
    df_formatado = df.copy()
    for col in nomes_datas:
        if col in df_formatado.columns:
            df_formatado[col] = pd.to_datetime(df_formatado[col], errors='coerce').dt.strftime('%d/%m/%Y').fillna('N/A')
    return df_formatado


def gerar_pdf(df, pasta, nomes_datas):
    pdf = FPDF()
    pdf.set_auto_page_break(auto=True, margin=15)
    pdf.add_page()
    pdf.set_font("Helvetica", size=12)

    total = len(df)
    pdf.cell(0, 10, f"Relatório de Alunos - {datetime.now().strftime('%d/%m/%Y')}", ln=True, align='C')
    pdf.ln(10)
    pdf.cell(0, 10, f"Total de alunos: {total}", ln=True)

    if 'Situação' in df.columns:
        situacao = df['Situação'].value_counts()
        pdf.ln(5)
        pdf.cell(0, 10, "Situação:", ln=True)
        for s, v in situacao.items():
            pdf.cell(0, 8, f" - {s}: {v} ({(v/total)*100:.2f}%)", ln=True)

    if 'Descrição' in df.columns:
        descricao = df['Descrição'].value_counts()
        pdf.ln(5)
        pdf.cell(0, 10, "Descrição:", ln=True)
        for d, v in descricao.items():
            pdf.cell(0, 8, f" - {d}: {v} ({(v/total)*100:.2f}%)", ln=True)

    if 'Status_Frequência' in df.columns:
        pdf.ln(5)
        pdf.cell(0, 10, "Status baseado na Frequência:", ln=True)
        status_freq = df['Status_Frequência'].value_counts()
        for s, v in status_freq.items():
            pdf.cell(0, 8, f" - {s}: {v} ({(v/total)*100:.2f}%)", ln=True)

    pdf.add_page()
    pdf.set_font("Helvetica", size=8)
    pdf.cell(0, 10, "Lista completa dos alunos (ordenada por nome):", ln=True)

    colunas_base = [
        "Nome", "Curso", "Modalidade", "Situação", "Descrição",
        "Frequência", "Status_Frequência"
    ]
    colunas_com_datas = colunas_base + [col for col in nomes_datas if col in df.columns]
    colunas_existentes = [c for c in colunas_com_datas if c in df.columns]

    df_formatado = formatar_datas(df, nomes_datas)
    df_formatado = df_formatado.sort_values(by="Nome", ascending=True)

    for _, row in df_formatado[colunas_existentes].iterrows():
        linha = " - ".join(str(row[col]) for col in colunas_existentes)
        pdf.multi_cell(0, 6, linha)

    caminho_pdf = os.path.join(pasta, "relatorio_alunos.pdf")
    pdf.output(caminho_pdf)


def processar():
    df = carregar_planilhas()
    if df is None or df.empty:
        messagebox.showwarning("Aviso", "Nenhuma planilha carregada ou planilha vazia.")
        return

    nomes_datas = ["Data_Início", "Data_Fim"]

    if 'Frequência' in df.columns:
        df['Frequência'] = pd.to_numeric(df['Frequência'], errors='coerce')
        df['Status_Frequência'] = df['Frequência'].apply(
            lambda x: 'Ativo' if pd.notnull(x) and x >= 75 else 'Inativo'
        )
    else:
        df['Status_Frequência'] = 'Desconhecido'

    pasta = os.path.join("exportacoes", datetime.now().strftime("%Y-%m-%d"))
    os.makedirs(pasta, exist_ok=True)

    df.to_excel(os.path.join(pasta, "todos_os_alunos.xlsx"), index=False)
    df.to_csv(os.path.join(pasta, "todos_os_alunos.csv"), index=False, encoding='utf-8-sig')

    gerar_pdf(df, pasta, nomes_datas)

    messagebox.showinfo("Concluído", f"Análise concluída!\\nArquivos exportados para:\\n{pasta}")


janela = tk.Tk()
janela.title("Analisador de Alunos")
janela.geometry("400x150")
janela.resizable(False, False)

btn = tk.Button(janela, text="Selecionar e Analisar Planilhas", command=processar, font=("Arial", 12))
btn.pack(expand=True, padx=20, pady=40)

janela.mainloop()


# Salvando o código no arquivo .py final
caminho_final = "/mnt/data/analisador_alunos_final.py"

