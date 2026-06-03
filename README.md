# Auron - Plataforma de Proteção Solar B2B
## Descrição
Auron é uma plataforma B2B de monitoramento e proteção contra anomalias solares. A aplicação simula eventos solares e demonstra como sistemas de proteção podem mitigar danos a data centers e instalações de energia solar.
## Funcionalidades
- ✅ Cadastro e Login de Empresas: Registro de empresas com autenticação segura
- ✅ Simulação de Impacto de Anomalias: Visualização gráfica do dano potencial causado por tempestades solares
- ✅ Alertas Ativos: Monitoramento em tempo real de eventos solares detectados
- ✅ Histórico de Eventos: Registro detalhado de todos os eventos solares processados
- ⏳ Previsão de Tempestades (Em desenvolvimento)
- ✅ Relatório de ROI: Geração automática de relatórios em PDF com análise de custos evitados
- ⏳ Dashboard Completo (Em desenvolvimento)
## Tecnologias Utilizadas
- Python 3.x
- Bibliotecas:
  - matplotlib: Para geração de gráficos
  - fpdf: Para geração de relatórios PDF
  - json: Para armazenamento de dados
  - os: Para operações do sistema
  - datetime: Para timestamps
  - random e math: Para simulações
## Estrutura do Projeto
```
GS---Auron---COMPUTATIONAL-THINKING-WITH-PYTHON/
│
├── Gs_Menu.py              # Arquivo principal da aplicação
├── empresas.json           # Armazena dados das empresas cadastradas
├── eventos.json            # Base de dados de eventos solares
├── README.md               # Este arquivo
│
├── images/                 # Diretório de imagens (utilizado nos relatórios)
│   └── capa.png            # Capa utilizada nos relatórios PDF
│
└── relatorios/             # Diretório onde os relatóros PDF são salvos
```
## Como Executar
1. Pré-requisitos:
- Python 3.x instalado
- Pip para gerenciamento de pacotes
2. Instalação das Dependências:
```pip install matplotlib fpdf```
3. Execução:
```python Gs_Menu.py```
## Uso
Ao executar o aplicativo:
1. Primeiro Acesso:
- Escolha "Cadastro" para criar uma nova empresa
- Preencha: nome da empresa, estado, usuário e senha
- Após o cadastro, você será redirecionado para o login
2. Login:
- Insira seu usuário e senha criados no cadastro
- Acesso ao menu principal será concedido
3. Menu Principal:
- 1. Sobre a solução Auron: Informações sobre a plataforma
- 2. Simulação de Impacto de Anomalia: Gráficos mostrando dano potencial vs. proteção Auron
- 3. Alertas Ativos: Visualização de eventos solares em tempo real
- 4. Histórico de Eventos: Detalhamento de todos os eventos processados
- 5. Previsão de Tempestades: Funcionalidade em desenvolvimento
- 6. ROI — Custos Evitados e Desempenho: Gera relatório PDF com análise financeira
- 7. Dashboard Completo: Funcionalidade em desenvolvimento
- 0. Sair: Encerra a aplicação
## Observações
- Os dados são armazenados localmente em arquivos JSON (empresas.json e eventos.json)
- Os relatórios PDF são salvos no diretório relatorios/ com nome contendo o nome da empresa e data
- A aplicação inclui simulações aleatórias de eventos solares para demonstração
- Funcionalidades marcadas como "Em desenvolvimento" estão planejadas para versões futuras
## Licença
Este projeto foi desenvolvido para fins educacionais e demonstrativos.
Desenvolvido como parte do curso de Pensamento Computacional com Python

## A fazer
 - Adicionar função de planos da plataforma (Básico, Premium, etc.)
 - Tratamento de erro/validação no login e cadastro