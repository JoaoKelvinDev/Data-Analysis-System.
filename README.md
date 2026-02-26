# 📊 Data Analysis System

O **Data Analysis System** é uma solução robusta desenvolvida em **Python** para automação de processos educacionais e análise de dados. O sistema foi projetado para eliminar o trabalho manual de consolidar múltiplas planilhas, realizando o processamento inteligente de dados, aplicação de regras de negócio (frequência e status) e geração automática de relatórios gerenciais profissionais.

## 🚀 Principais Funcionalidades

* **Consolidação Inteligente:** Unifica diversos arquivos `.xlsx` e `.xls` de uma única vez, tratando automaticamente cabeçalhos e formatações inconsistentes.
* **Regras de Negócio Automatizadas:** Calcula automaticamente o status do aluno (Ativo/Inativo) com base na métrica de **75% de frequência mínima**.
* **Tratamento de Dados:** Realiza a conversão de tipos, formatação de datas e **ordenação alfabética** rigorosa para garantir relatórios limpos e organizados.
* **Exportação Multiformato:** Gera uma pasta estruturada por data contendo:
    * **Relatório Executivo em PDF:** Com resumo estatístico, porcentagens e lista detalhada.
    * **Base de Dados Master:** Arquivos consolidado em Excel (.xlsx) e CSV (UTF-8) para integração com outras ferramentas.
* **Interface Desktop (GUI):** Interface gráfica amigável desenvolvida em Tkinter para facilitar a operação por qualquer usuário.

## 📁 Estrutura do Projeto

```text
Data Analysis System/
├── py/
│   ├── main.py           # Core do sistema (Processamento, Lógica e GUI)
│   └── gerar_testes.py   # Script utilitário para criação de massa de dados
├── projeto/              # Interface Web / Assets
│   ├── index.html        # Estrutura visual da interface
│   └── script.js         # Lógica de interação front-end
├── samples/              # Pasta para armazenamento de arquivos de exemplo
├── .gitignore            # Configuração de arquivos ignorados pelo Git
└── README.md             # Documentação completa do projeto
