import pandas as pd

# Dados de exemplo para o Teste 1
dados1 = {
    "Nome": ["Ana Silva", "Bruno Costa", "Carlos Souza"],
    "Curso": ["Python Dev", "Data Science", "Python Dev"],
    "Modalidade": ["EAD", "Presencial", "EAD"],
    "Situação": ["Matriculado", "Matriculado", "Trancado"],
    "Descrição": ["Regular", "Bolsista", "Regular"],
    "Frequência": [85, 92, 60],
    "Data_Início": ["2023-01-10", "2023-01-15", "2023-02-01"],
    "Data_Fim": ["2023-12-10", "2023-12-15", "2023-11-01"]
}

# Dados de exemplo para o Teste 2
dados2 = {
    "Nome": ["Zeca Urubu", "Daniela Lima", "Eduardo Meirelles"],
    "Curso": ["Data Science", "Python Dev", "Data Science"],
    "Modalidade": ["Presencial", "EAD", "EAD"],
    "Situação": ["Matriculado", "Evadido", "Matriculado"],
    "Descrição": ["Regular", "Regular", "Bolsista"],
    "Frequência": [78, 45, 95],
    "Data_Início": ["2023-01-20", "2023-03-01", "2023-01-15"],
    "Data_Fim": ["2023-12-20", "2023-10-01", "2023-12-15"]
}

def criar_planilha(nome_arquivo, dados):
    # Cria um DataFrame vazio para simular o cabeçalho de 3 linhas que seu código pula (skiprows=3)
    df_vazio = pd.DataFrame([[""] * len(dados.keys())] * 3, columns=dados.keys())
    df_real = pd.DataFrame(dados)
    
    # Concatena o vazio com os dados reais
    df_final = pd.concat([df_vazio, df_real], ignore_index=True)
    
    # Salva como Excel
    df_final.to_excel(nome_arquivo, index=False)
    print(f"✅ Arquivo {nome_arquivo} criado com sucesso!")

criar_planilha("teste_alunos_A.xlsx", dados1)
criar_planilha("teste_alunos_B.xlsx", dados2)