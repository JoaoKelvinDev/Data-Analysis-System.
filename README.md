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

🛠️ Tecnologias Utilizadas
Python 3.x: Linguagem principal para o backend.

Pandas: Biblioteca de alta performance para manipulação e análise de dados.

FPDF: Biblioteca para geração dinâmica de documentos PDF.

Tkinter: Framework nativo para criação de interfaces gráficas desktop.

OpenPyXL: Engine para leitura e escrita de arquivos Excel modernos.

HTML5 & JavaScript: Tecnologias de front-end integradas à estrutura do projeto.

🧪 Como Testar o Sistema
O projeto já inclui um script gerador de dados para que você possa testar as funcionalidades imediatamente:

Clone o repositório:

Bash

git clone [https://github.com/SEU_USUARIO/data-analysis-system.git](https://github.com/SEU_USUARIO/data-analysis-system.git)
Instale as dependências necessárias:

Bash

pip install pandas fpdf openpyxl
Gere a massa de dados de teste:

Bash

python py/gerar_testes.py
Inicie o sistema:

Bash

python py/main.py
No programa, clique em "Selecionar e Analisar Planilhas" e escolha os arquivos gerados (ex: teste_alunos_A.xlsx).

📂 Organização da Saída
Ao processar os dados, o sistema cria automaticamente o diretório de exportação:
exportacoes/AAAA-MM-DD/

relatorio_alunos.pdf (Documento formatado para impressão)

todos_os_alunos.xlsx (Planilha mestre unificada)

todos_os_alunos.csv (Base de dados leve para sistemas terceiros)

Desenvolvido por João Kelvin Desenvolvedor focado em automação de processos e análise de dados.

https://www.linkedin.com/in/joaokelvindev | jkelvindev@gmail.com


 