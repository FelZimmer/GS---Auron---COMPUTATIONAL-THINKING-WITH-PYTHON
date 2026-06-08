# 🌞 AURON — Plataforma de Proteção Solar B2B

> Solução tecnológica integrada de monitoramento e proteção contra anomalias solares, desenvolvida para a **Global Solution 2026 — FIAP**.

---

## 📋 Descrição do Projeto

O **Auron** é uma plataforma B2B de monitoramento e proteção contra anomalias solares voltada para empresas que operam **data centers**. A solução combina dados orbitais, inteligência artificial preditiva e automações de segurança para minimizar danos causados por tempestades solares, explosões solares, ejeções de massa coronal e outras anomalias espaciais.

A plataforma oferece um sistema completo de login por empresa, simulação de impacto de anomalias, histórico de eventos, alertas ativos, relatório de ROI em PDF e um dashboard interativo em tempo real.

---

## 🎯 Objetivo da Solução

Proteger a infraestrutura tecnológica de empresas brasileiras contra eventos solares que podem causar:

- Surtos elétricos e superaquecimento em servidores
- Falhas em no-breaks e inversores
- Perda de dados e horas de inatividade
- Prejuízos financeiros de milhões de reais por evento

O diferencial está na **narrativa de impacto em cadeia**:
> **"Empresas protegidas → Serviços disponíveis → Usuários protegidos"**

---

## ✅ Funcionalidades

- ✅ **Cadastro e Login de Empresas** — Registro de empresas com autenticação segura
- ✅ **Simulação de Impacto de Anomalias** — Visualização gráfica do dano potencial causado por tempestades solares
- ✅ **Alertas Ativos** — Monitoramento em tempo real de eventos solares detectados
- ✅ **Histórico de Eventos** — Registro detalhado de todos os eventos solares processados
- ⏳ **Previsão de Tempestades** — Em desenvolvimento
- ✅ **Relatório de ROI** — Geração automática de relatórios em PDF com análise de custos evitados
- ⏳ **Dashboard Completo** — Em desenvolvimento

---

## 🛰️ Conexão com a Indústria Espacial

A solução utiliza dados inspirados nos satélites de monitoramento solar:
- **DSCOVR** (NOAA) — monitoramento de vento solar
- **SOHO** (NASA/ESA) — observação da atividade solar
- **ACE** (NASA) — medição de partículas solares

---

## 🧰 Tecnologias e Bibliotecas Utilizadas

| Biblioteca       | Uso                                              |
|------------------|--------------------------------------------------|
| `streamlit`      | Dashboard interativo web                         |
| `plotly.express` | Gráficos interativos no dashboard                |
| `matplotlib`     | Gráficos de simulação de dano no terminal        |
| `fpdf2`          | Geração de relatórios em PDF                     |
| `pandas`         | Manipulação de dados no dashboard                |
| `filelock`       | Controle de acesso concorrente ao JSON           |
| `math`           | Cálculos de funções exponenciais e polinomiais   |
| `random`         | Geração de parâmetros aleatórios para simulações |
| `json`           | Leitura e escrita dos arquivos de dados          |
| `logging`        | Registro de eventos e erros do sistema           |
| `datetime`       | Controle de datas nos relatórios                 |
| `os`             | Manipulação de arquivos e diretórios             |
| `subprocess`     | Abertura do dashboard em novo terminal           |

---

## ⚙️ Explicação do Funcionamento

### Fluxo principal

```
1. Usuário executa Gs_Menu.py
2. Realiza login ou cadastro da empresa
3. Navega pelo menu com as opções do dashboard
4. Pode abrir o dashboard Streamlit diretamente pelo menu
5. O dashboard carrega automaticamente os dados da sessão ativa
```

### Opções do Menu

| Opção | Funcionalidade |
|-------|---------------|
| 1 | Sobre a solução Auron |
| 2 | Simulação de impacto de anomalia (gráficos polinomial + exponencial) |
| 3 | Alertas ativos da empresa logada |
| 4 | Histórico de eventos solares registrados |
| 5 | Previsão de tempestades solares |
| 6 | ROI — Geração de relatório PDF com custos evitados |
| 7 | Dashboard completo (abre Streamlit no navegador) |
| 0 | Sair |

### Simulação Matemática

A simulação de impacto utiliza dois modelos matemáticos:

- **Função Polinomial** `D(x) = ax² + bx + c` — relação entre intensidade da tempestade (nT) e dano potencial
- **Função Exponencial** `D(t) = D₀ · e^(kt)` — crescimento do dano sem proteção ao longo do tempo, com comparativo do Auron acionado em t=15min

### Tipos de Eventos Monitorados

| Tipo de Evento | Intensidade (nT) | Nível de Alerta |
|----------------|-----------------|-----------------|
| Rajada de Raios Cósmicos | 50 – 120 | Atenção |
| Explosão Solar Classe M | 150 – 250 | Atenção |
| Vento Solar Intenso | 80 – 300 | Atenção / Alerta |
| Tempestade Geomagnética | 150 – 400 | Alerta / Crítico |
| Ejeção de Massa Coronal | 180 – 550 | Alerta / Crítico |
| Explosão Solar Classe X | 500 – 650 | Crítico |

---

## 🗂️ Estrutura do Projeto

```
GS---Auron---COMPUTATIONAL-THINKING-WITH-PYTHON/
│
├── Gs_Menu.py              # Arquivo principal da aplicação
├── dashboard.py            # Dashboard interativo com Streamlit
├── empresas.json           # Armazena dados das empresas cadastradas
├── eventos.json            # Base de dados de eventos solares
├── sessao.json             # Guarda os dados da sessão ativa
├── requirements.txt        # Dependências do projeto
├── README.md               # Este arquivo
│
├── images/                 # Imagens utilizadas nos relatórios
│   └── capa.png            # Capa dos relatórios PDF
│
├── logs/                   # Logs gerados pelo sistema
│
└── relatorios/             # Relatórios PDF gerados
    └── relatorios.md       # Não apagar — mantém a pasta no repositório
```

---

## 🚀 Instruções de Instalação e Execução

### 1. Clone o repositório

```bash
git clone https://github.com/seu-usuario/GS---Auron---COMPUTATIONAL-THINKING-WITH-PYTHON.git
cd GS---Auron---COMPUTATIONAL-THINKING-WITH-PYTHON
```

### 2. Instale as dependências

```bash
pip install -r requirements.txt
```

Ou instale manualmente:

```bash
pip install streamlit plotly filelock fpdf2 pandas matplotlib
```

### 3. Execute o sistema

```bash
python Gs_Menu.py
```

> ⚠️ **Não é necessário executar o `dashboard.py` manualmente.** Ele é aberto automaticamente pela opção **7 — Dashboard Completo** dentro do menu.

---

## 💡 Exemplos de Uso

### Login no sistema
```
Bem-vindo ao Auron — Plataforma de Proteção Solar B2B

1. Fazer Login
2. Cadastrar sua Empresa
Digite: 1

--- Dashboard Login ---
Nome de usuário: nexcore
Senha: ********

Login bem-sucedido! Bem-vindo, NexCore Tecnologia!
```

### Empresas pré-cadastradas para teste

| Usuário | Senha | Empresa | Estado |
|---------|-------|---------|--------|
| `nexcore` | `Nex@2026` | NexCore Tecnologia | SP |
| `maretech` | `Mare@2026` | MareTech Infraestrutura | RJ |
| `sultech` | `Sul@2026` | SulTech Infraestrutura | PR |
| `capitalserver` | `Cap@2026` | CapitalServer | DF |

### Abrindo o Dashboard
```
Escolha uma opção: 7
Dashboard aberto no navegador!
→ Acesse: http://localhost:8501
```

---

## 🌍 ODS Alinhados

| ODS | Descrição |
|-----|-----------|
| **ODS 7** | Energia limpa e acessível — proteção da infraestrutura solar |
| **ODS 9** | Indústria, inovação e infraestrutura — proteção de data centers |
| **ODS 11** | Cidades e comunidades sustentáveis — continuidade de serviços urbanos |
| **ODS 13** | Ação climática — uso de dados espaciais para resiliência |

---

## 📌 Observações

- Os dados são armazenados localmente em arquivos JSON (`empresas.json` e `eventos.json`)
- Os relatórios PDF são salvos no diretório `relatorios/` com nome contendo o nome da empresa e data
- A aplicação inclui simulações aleatórias de eventos solares para demonstração
- Funcionalidades marcadas como ⏳ **Em desenvolvimento** estão planejadas para versões futuras

---

## 📄 Licença

Este projeto foi desenvolvido para fins educacionais e demonstrativos.
Desenvolvido como parte do curso de **Pensamento Computacional com Python — FIAP**.

---

## 👥 Integrantes

| RM | Nome |
|----|------|
| 570860 | Esther Tozzo |
| 570316 | Izabela Pordeus |
| 569949 | João Victor Santos Souza |
| 571458 | Matheus Lopes Lima |
| 570863 | Felipe de Oliveira Zimmermann |

---

> Desenvolvido para a **Global Solution 2026 — 1º Semestre**
> Curso: Engenharia de Software — 1º Ano | FIAP