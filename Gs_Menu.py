import math
import random
import matplotlib.pyplot as plt
import json
import os
from fpdf import FPDF
import datetime

ESTADOS_BRASIL = {
    "AC": "Acre", "AL": "Alagoas", "AP": "Amapá", "AM": "Amazonas",
    "BA": "Bahia", "CE": "Ceará", "DF": "Distrito Federal", "ES": "Espírito Santo",
    "GO": "Goiás", "MA": "Maranhão", "MT": "Mato Grosso", "MS": "Mato Grosso do Sul",
    "MG": "Minas Gerais", "PA": "Pará", "PB": "Paraíba", "PR": "Paraná",
    "PE": "Pernambuco", "PI": "Piauí", "RJ": "Rio de Janeiro", "RN": "Rio Grande do Norte",
    "RS": "Rio Grande do Sul", "RO": "Rondônia", "RR": "Roraima", "SC": "Santa Catarina",
    "SP": "São Paulo", "SE": "Sergipe", "TO": "Tocantins"
}
def limpar_tela():
    # nt = indentifica o Windows e executa o comando 'cls', else = clear para Linux/Mac
    os.system('cls' if os.name == 'nt' else 'clear')


def escolher_estado():    
    while True:
        print("\nEscolha o estado onde sua empresa está localizada:")
        for sigla, estado in ESTADOS_BRASIL.items():
            print(f"{sigla} - {estado}")
            
        escolha = input("\nDigite a sigla correspondente ao seu estado: ")
        
        try:
            for sigla, nome_estado in ESTADOS_BRASIL.items():
                if escolha.upper() == sigla:
                    print(f"Você selecionou: {nome_estado}")
                    return nome_estado

        except Exception as e:
            print(f"Erro encontrado: {e}")

def cadastrar_empresa():
    print("\nBem-vindo ao Auron — Plataforma de Proteção Solar B2B")
    nome_empresa = input("Digite o nome da sua empresa: ")
    regiao = escolher_estado()
    usuario = input("Crie um nome de usuário para acessar o dashboard: ").lower()
    senha = input("Crie uma senha para acessar o dashboard: ")
    
    
    try:
        with open("empresas.json", "r", encoding="utf-8") as f:
            data = json.load(f)
    except (FileNotFoundError, json.JSONDecodeError):
            data = {"empresas": []}

    data["empresas"].append({
        "id": len(data["empresas"]) + 1,
        "nome": nome_empresa,
        "estado": regiao,
        "usuario": usuario,
        "senha": senha,
        "tipo": "Data Center",
        "eventos": [],
        "eventos_previstos": []
})

    with open("empresas.json", "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=2)
    
    print(f"\nCadastro concluído! ")
    return login()
            
def login():
    limpar_tela()
    print("\n--- Dashboard Login ---")
    usuario_input = input("Nome de usuário: ").strip().lower()
    senha_input = input("Senha: ").strip()

    try:
        with open("empresas.json", "r", encoding="utf-8") as f:
            data = json.load(f)
            empresas = data.get("empresas", [])  # lista, não dicionário

        empresa_logada = None
        
        
        for empresa in empresas:  # percorre cada empresa
            if empresa["usuario"] == usuario_input and empresa["senha"] == senha_input:
                empresa_logada = empresa
                
                break

        if empresa_logada:
            print(f"\nLogin bem-sucedido! Bem-vindo, {empresa_logada['nome']}!")
            return empresa_logada["usuario"], empresa_logada["nome"]  # Retorna o nome de usuário para uso posterior 
        else:
            print("\nUsuário ou senha incorreto(s).")
            match int(input("""Selecione uma opção:\n
1. Cadastro
2. Tentar novamente \nDigite: """)):
                case 1:
                    return cadastrar_empresa()
                case 2:
                    print("\nTente novamente fazer login.")
                    return login()
                case _:
                    print("Opção inválida. Retornando ao menu principal.")
                    return None, None

    except FileNotFoundError:
        print("\nErro: Arquivo 'empresas.json' não encontrado.")
        return None, None
    except json.JSONDecodeError:
        print("\nErro: Arquivo de dados corrompido.")
        return None, None

def tela_inicial():
    print("\nBem-vindo ao Auron — Plataforma de Proteção Solar B2B")
    match input("\n1. Fazer Login \n2. Cadastrar sua Empresa\nDigite: "):
        case "1":
            return login()
        case "2":
            return cadastrar_empresa()

def sortear_evento():
    is_event = random.choice([True, False, False, False])
    if is_event:
        with open("eventos.json", "r", encoding="utf-8") as f:
            data = json.load(f)
            evento_aleatorio = random.choice(data["eventos"])
            evento_aleatorio["data_hora"] = datetime.datetime.now().strftime("%Y-%m-%d %H:%M")
            print(f"\n Evento Solar Detectado: {evento_aleatorio['tipo_evento']}")
            print(f" Data/Hora: {evento_aleatorio['data_hora']}")
            print(f" Status: {evento_aleatorio['nivel_alerta']}") # Pintar de acordo com o nível de alerta
    else:
        print(" Nenhum evento solar significativo detectado.")
        return

    try:
        with open("empresas.json", "r", encoding="utf-8") as f:
            data = json.load(f)
    except (FileNotFoundError, json.JSONDecodeError):
            data = {"empresas": []}

    for empresa in data.get("empresas"):
        if empresa.get("usuario") == name_login:
            empresa.get("eventos").append(evento_aleatorio)

    with open("empresas.json", "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=2)
        
    
    

def menu():
    print("="*50)
    print(""" ℙ𝕝𝕒𝕥𝕒𝕗𝕠𝕣𝕞𝕒 𝕕𝕖 ℙ𝕣𝕠𝕥𝕖𝕔̧𝕒̃𝕠 𝕊𝕠𝕝𝕒𝕣 𝔹𝟚𝔹 """)
    print("="*50)
    print()
    print(" 1. Sobre a solução Auron")
    print(" 2. Simulação de Impacto de Anomalia")
    print(" 3. Alertas Ativos")
    print(" 4. Histórico de Eventos")
    print(" 5. Previsão de Tempestades")
    print(" 6. ROI — Custos Evitados e Desempenho")
    print(" 7. Dashboard Completo")
    print(" 0. Sair")
    


def funcao_polinomial(ax):
    # Relação entre intensidade da tempestade solar (nT) e o dano causado
    # D(x) = ax² + bx + c — cresce de forma não linear com a intensidade

    a = random.uniform(0.8, 1.5)
    b = random.uniform(-120, -80)   
    c = random.uniform(-5000, 5000)
    x_max = random.randint (0, 500)

    intensidade = []
    danos = []
    

    for x in range(0, x_max + 1):
        dx = a * x**2 + b * x + c
        intensidade.append(x)
        danos.append(max(0, dx)) 

    ax.plot(intensidade, danos, color="#E8570D")
    ax.set_title("Intensidade da Tempestade Solar vs Dano")
    ax.set_xlabel("Intensidade da tempestade solar (nT)")
    ax.set_ylabel("Dano estimado (R$)")
    ax.grid(True)

    return max(danos)              


def funcao_exponencial(ax, dano_inicial):
    # Crescimento exponencial do dano sem proteção ativa
    # D(t) = D₀ · e^(kt)

    k = random.uniform(0.0, 0.12)

    tempos = []
    danos = []
    danos_com_auron = []

    for t in range(0, 121):
        dt = dano_inicial * math.exp(k * t)
        tempos.append(t)
        danos.append(dt)
        # Com Auron: automação acionada em t=15min — dano congela
        if t <= 15:
            danos_com_auron.append(dano_inicial * math.exp(k * t))
        else:
            danos_com_auron.append(danos_com_auron[-1])

    ax.plot(tempos, danos, color="#C0392B", label="Sem proteção")
    ax.plot(tempos, danos_com_auron, color="#00C2E0",linestyle="--", label="Com Auron (ação em t=15min)")
    ax.axvline(x=15, color="#F5923A", linestyle=":", label="Automação acionada")
    ax.set_title("Crescimento do Dano sem Proteção vs Com Auron")
    ax.set_xlabel("Tempo sem proteção (min)")
    ax.set_ylabel("Dano acumulado (R$)")
    ax.legend()
    ax.grid(True)

    return danos[-1]


def calcular_dano():
    try:
        fig, eixos = plt.subplots(1, 2, figsize=(14, 5))
        fig.suptitle("AURON — Simulação de Impacto de Anomalias Solares", fontsize=13, fontweight="bold")

        dano_maximo = funcao_polinomial(eixos[0])   
        print("  " + "="*50)
        print("\n  AURON — Simulação de Impacto de Anomalias Solares \n")
        print("  " + "="*50)
        print(f"\n  Intensidade máxima simulada resultou em "f"R$ {dano_maximo:.2f} de dano potencial.")

        if dano_maximo > 0:
            print("  Evento solar detectado — simulando crescimento do dano")
            dano_final = funcao_exponencial(eixos[1], dano_maximo)
            print(f"  Dano máximo sem proteção: R$ {dano_final:.2f}")
            print(f"  Com a Auron (ação em t=15min), o dano foi contido.\n")
        else:
            eixos[1].set_visible(False)
            print("\n  Simulação concluída — sem danos estimados para a intensidade atual.\n")
            print("  Nenhum evento solar significativo detectado.")
            print("  A infraestrutura está segura — monitoramento ativo.\n")

        plt.tight_layout()
        plt.show()
        input("\nPressione Enter para retornar ao menu...")

    except Exception as e:
        print(f"Erro encontrado: {e}")


def sobre():
    print("\n")
    print("              𝕊𝕠𝕓𝕣𝕖 𝕒 𝔸𝕦𝕣𝕠𝕟               ")
    print("\n" + "="*50)
    print("AURON é uma plataforma B2B de monitoramento e")
    print("proteção contra anomalias solares. Integra dados")
    print("orbitais em tempo real com IA preditiva para")
    print("acionar automações de segurança em data centers")
    print("e instalações de energia solar.")
    print("="*50)
    print()
    input("Pressione Enter para retornar ao menu...")

def historico_eventos():
    pdf = FPDF()
    pdf.add_page()
    # Adicionar a imagem no topo
    pdf.image("./images/capa.png", x=5, y=5, w=200)

    # Mover o cursor para baixo da imagem (a imagem tem ~42 de altura)
    pdf.set_y(55)

    # Definir a fonte (Arial, negrito, tamanho 16)
    pdf.set_font("Arial", "B", 16)

    # Adicionar um título (largura, altura, texto)
    pdf.cell(200, 15, f"Histórico de Eventos - {name_empresa}", ln=1, align="C")

    pdf.set_font("Arial", '' ,  12)
    pdf.cell(200, 5, f"Data: {datetime.datetime.now().strftime('%d/%m/%Y')}", ln=1, align="C")
    pdf.ln(5)

    try:    
        with open("empresas.json", "r", encoding="utf-8") as f:
            empresas = json.load(f).get("empresas", [])
            for empresa in empresas:
                if empresa["usuario"] == name_login:
                    eventos = empresa["eventos"]
                    eventos_previstos = empresa["eventos_previstos"]
                    if eventos_previstos:
                        pdf.set_font("Arial", "B", 14)
                        pdf.cell(200, 10, f"Eventos Previstos:", ln=1)
                        for evento in eventos_previstos:
                            pdf.set_font("Arial", "", 12)
                            pdf.cell(200, 5, f"Data/Hora: {evento['data_previsao']}", ln=1)
                            pdf.cell(200, 5, f"Tipo: {evento['tipo_evento']}", ln=1)
                            pdf.cell(200, 5, f"Intensidade: {evento['intensidade_nT']} nT", ln=1)
                            pdf.cell(200, 5, f"Duração: {evento['duracao_min']} min", ln=1)
                            pdf.cell(200, 5, f"Nível de Alerta: {evento['nivel_alerta']}", ln=1)
                            pdf.cell(200, 10, "-"*50, ln=1)
                            if pdf.get_y() > 200:
                                pdf.add_page()
                    if eventos:
                        pdf.set_font("Arial", "B", 14)
                        pdf.cell(200, 10, f"Eventos Anteriores:", ln=1)
                        for evento in eventos:
                            pdf.set_font("Arial", '', 12)
                            pdf.cell(200, 5, f"Data/Hora: {evento['data_hora']}", ln=1)
                            pdf.cell(200, 5, f"Tipo: {evento['tipo_evento']}", ln=1)
                            pdf.cell(200, 5, f"Intensidade: {evento['intensidade_nT']} nT", ln=1)
                            pdf.cell(200, 5, f"Duração: {evento['duracao_min']} min", ln=1)
                            pdf.cell(200, 5, f"Equipamento: {evento['equipamento_risco']}", ln=1)
                            pdf.cell(200, 5, f"Nível Alerta: {evento['nivel_alerta']}", ln=1)
                            pdf.cell(200, 5, f"Dano Potencial: R$ {evento['dano_potencial']:,.2f}", ln=1)
                            pdf.cell(200, 5, f"Dano Evitado: R$ {evento['dano_evitado']:,.2f}", ln=1)
                            pdf.cell(200, 5, f"Custo Reparo: R$ {evento['custo_reparo']:,.2f}", ln=1)
                            pdf.cell(200, 5, f"Auron Acionado: {'Sim' if evento['auron_acionado'] else 'Não'}", ln=1)
                            pdf.cell(200, 10, "-"*50, ln=1)
                            if pdf.get_y() > 200:
                                pdf.add_page()
                    pdf.output(f"./relatorios/relatorio_eventos_{name_empresa}_{datetime.datetime.now().strftime('%d_%m_%Y')}.pdf")
                    print(f"Relatório gerado com sucesso!\n")
    except Exception as e:
        print(f"Erro ao gerar relatório: {e}")


def gerar_relatorio_roi():
    
    # Variaveis
    total_eventos = 0
    eventos_com_auron = 0
    eventos_sem_protecao = 0
    total_dano_potencial = 0
    total_dano_evitado = 0
    total_custo_reparo = 0
    percentual_protecao = "0%"
    tempo_resposta_total = 0
    tempo_resposta_medio = 0
    evento_maior_intensidade = 0
    equipamentos_afetados = []
    mensalidade_auron_solar = 2990
    custo_manutencao_total = 0
    custo_total_sem_protecao = 0
    custo_total_com_protecao = 0
    economia_gerada = 0


    try:
        with open("empresas.json", "r", encoding="utf-8") as f:
            empresas = json.load(f).get("empresas", [])
        for empresa in empresas:
            if empresa.get("usuario") == name_login:
                eventos = empresa.get("eventos", [])
                if eventos:
                    total_eventos = len(eventos)
                    for e in eventos:
                        eventos_com_auron += 1 if e.get("auron_acionado") == True else 0
                        eventos_sem_protecao += 1 if e.get("auron_acionado") == False else 0
                        total_dano_potencial += e.get("dano_potencial")
                        total_dano_evitado += e.get("dano_potencial") if e.get("auron_acionado") == True else 0
                        total_custo_reparo += e.get("custo_reparo") if e.get("auron_acionado") == False else 0 
                        percentual_protecao = f"{(total_dano_evitado / total_dano_potencial) * 100:.2f}%" if total_dano_potencial > 0 else 0
                        tempo_resposta_total += e.get("tempo_resposta_min") if e.get("auron_acionado") == True else 0
                        if eventos_com_auron > 0:
                            tempo_resposta_medio = tempo_resposta_total // eventos_com_auron
                        else:
                            tempo_resposta_medio = 0
                        if e.get("auron_acionado") == True:
                            if e.get("intensidade_nT") > evento_maior_intensidade:
                                evento_maior_intensidade = e.get("intensidade_nT")
                            custo_manutencao_total += e.get("custo_manutencao_mensal")
                            
                        else:
                            if e.get("equipamento_risco") not in equipamentos_afetados:
                                equipamentos_afetados.append(e.get("equipamento_risco"))
                    custo_total_com_protecao = custo_manutencao_total + mensalidade_auron_solar
                    custo_total_sem_protecao = total_dano_potencial + total_custo_reparo + custo_manutencao_total
                    economia_gerada = custo_total_sem_protecao - custo_total_com_protecao
                    
    except Exception as e:
        print(f"Erro encontrado: {e}")
    
    # Configurar a página do PDF
    pdf = FPDF()
    pdf.add_page()
    # Adicionar a imagem no topo
    pdf.image("./images/capa.png", x=5, y=5, w=200)

    # Mover o cursor para baixo da imagem (a imagem tem ~42 de altura)
    pdf.set_y(55)

    # Definir a fonte (Arial, negrito, tamanho 16)
    pdf.set_font("Arial", "B", 16)

    # Adicionar um título (largura, altura, texto)
    pdf.cell(200, 15, f"Relatório de ROI - {name_empresa}", ln=1, align="C")

    pdf.set_font("Arial", '' ,  12)
    pdf.cell(200, 5, f"Data: {datetime.datetime.now().strftime('%d/%m/%Y')}", ln=1, align="C")
    pdf.ln(5)

    # Resumo Executivo
    pdf.set_font("Arial", "B", 14)
    pdf.cell(200, 10, "Resumo Executivo", ln=1, align="A")

    pdf.set_font("Arial", "", 12)
    pdf.cell(60, 8, f"Total de eventos monitorados: ", ln=0)
    pdf.set_font("Arial", "B", 12)
    pdf.cell(20, 8, f"{total_eventos}", ln=1)
    pdf.set_font("Arial", "", 12)
    pdf.cell(75, 8, f"Total de eventos com Auron acionado: ", ln=0)
    pdf.set_font("Arial", "B", 12)
    pdf.cell(20, 8, f"{eventos_com_auron}", ln=1)
    pdf.set_font("Arial", "", 12)
    pdf.cell(62, 8, f"Total de eventos sem proteção: ", ln=0)
    pdf.set_font("Arial", "B", 12)
    pdf.cell(20, 8, f"{eventos_sem_protecao}", ln=1)
    pdf.ln(5)

    # Analise Financeira
    pdf.set_font("Arial", "B", 14)
    pdf.cell(200, 10, "Alálise Financeira", ln=1, align="A")

    pdf.set_font("Arial", "", 12)
    pdf.cell(200, 8, f"Total de dano potencial (soma de todos eventos) :", ln=1)
    pdf.set_font("Arial", "B", 12)
    pdf.cell(200, 8, f"R${total_dano_potencial:,.2f}", ln=1)

    pdf.set_font("Arial", "", 12)
    pdf.cell(200, 8, f"Total de dano evitado :", ln=1)
    pdf.set_font("Arial", "B", 12)
    pdf.cell(200, 8, f"R${total_dano_evitado:,.2f}", ln=1)

    pdf.set_font("Arial", "", 12)
    pdf.cell(200, 8, f"Total de custo de reparo (o que não foi evitado) :", ln=1)
    pdf.set_font("Arial", "B", 12)
    pdf.cell(200, 8, f"R${total_custo_reparo:,.2f}", ln=1)

    pdf.set_font("Arial", "", 12)
    pdf.cell(200, 8, f"Percentual de proteção : ", ln=1)
    pdf.set_font("Arial", "B", 12)
    pdf.cell(200, 8, f"{percentual_protecao}", ln=1)
    pdf.ln(5)

    # Eficiencia Operacional
    pdf.set_font("Arial", "B", 14)
    pdf.cell(200, 10, "Eficiencia Operacional", ln=1, align="A")

    pdf.set_font("Arial", "", 12)
    pdf.cell(200, 8, f"Tempo médio de resposta do Auron :", ln=1)
    pdf.set_font("Arial", "B", 12)
    pdf.cell(200, 8, f"{tempo_resposta_medio} min", ln=1)
    pdf.set_font("Arial", "", 12)
    pdf.cell(200, 8, f"Evento de maior intensidade registrado :", ln=1)
    pdf.set_font("Arial", "B", 12)
    pdf.cell(200, 8, f"{evento_maior_intensidade} nT", ln=1)
    pdf.set_font("Arial", "", 12)
    pdf.cell(200, 8, f"Lista de equipamentos afetados :", ln=1)
    pdf.set_font("Arial", "B", 12)
    pdf.ln(2)
    for i, e in enumerate(equipamentos_afetados):
        pdf.cell(200, 8, f"  {i+1}. {e}", ln=1)
    pdf.ln(5)

    # Comparativo COM vs SEM
    pdf.set_font("Arial", "B", 14)
    pdf.cell(200, 10, "Comparativo COM vs SEM", ln=1, align="A")

    pdf.set_font("Arial", "", 12)
    pdf.cell(200, 8, f"Custo total SEM proteção: ", ln=1)
    pdf.set_font("Arial", "B", 12)
    pdf.cell(200, 8, f"R${custo_total_sem_protecao:,.2f}", ln=1)

    pdf.set_font("Arial", "", 12)
    pdf.cell(200, 8, f"Custo total COM proteção: ", ln=1)
    pdf.set_font("Arial", "B", 12)
    pdf.cell(200, 8, f"R${custo_total_com_protecao:,.2f}", ln=1)

    pdf.set_font("Arial", "", 12)
    pdf.cell(200, 8, f"Economia gerada: ", ln=1)
    pdf.set_font("Arial", "B", 12)
    pdf.cell(200, 8, f"R${economia_gerada:,.2f}", ln=1)
    pdf.ln(5)

    # Posicionar a 50mm do fim da página (rodapé)
    pdf.set_y(-65)
    pdf.set_font("Arial", "B", 16)
    pdf.cell(200, 10, "Recomendação", ln=1, align="C")
    pdf.set_font("Arial", "", 12)
    pdf.cell(200, 8, f"Recomendamos a manutenção do contrato", ln=1, align="C")
    pdf.cell(200, 8, f"para garantir a proteção contínua dos equipamentos", ln=1, align="C")
    pdf.cell(200, 8, f"contra futuras anomalias solares.", ln=1, align="C")
    pdf.set_font("Arial", "I", 12)
    pdf.cell(200, 8, f"A Auron custa menos que 3 minutos de downtime.", ln=1, align="C")

    pdf.ln(5)
    # Salvar o arquivo
    pdf.output(f"./relatorios/relatorio_roi_{name_empresa}_{datetime.datetime.now().strftime('%d_%m_%Y')}.pdf") # Os relatórios são armazenados por dia, não é possivel ter mais de um relatório no mesmo dia
    print(f"Relatório gerado com sucesso!\n\n")
        
def alertas_ativos():
    # colocar cor para cada tipo de alerta (verde, amarelo, vermelho) e destacar o nome da empresa
    with open("empresas.json", "r", encoding="utf-8") as f:
        empresas = json.load(f).get("empresas", [])
        print("\n" + "="*50)
        print(f"\nAlertas Ativos para {name_login}:")
        print("\n" + "="*50)
        for empresa in empresas:
            if empresa['usuario'] == name_login:
                eventos = empresa['eventos']
                for evento in eventos:
                    if evento['auron_acionado'] == True:
                        print(f"\nEvento Solar Ativo: {evento['tipo_evento']} - Nível de Alerta: {evento['nivel_alerta']}")
                    
#Login, com nome da empresa e senha, para acessar o dashboard completo, com gráficos de desempenho, ROI e alertas personalizados.
name_login, name_empresa = tela_inicial()

def prever_evento():
    evento_previsto = random.choice(["Ejeção de Massa Coronal", "Rajada de Raios Cósmicos", "Tempestade Geomagnética", "Vento Solar Intenso", "Explosão Solar de Classe M", "Explosão Solar de Classe X", "Nenhum evento solar significativo detectado"])
    if evento_previsto == "Ejeção de Massa Coronal":
        intensidade_nT = random.randint(180, 550)
        duracao_min = random.randint(30, 150)
        nivel_alerta = random.choice(["Alerta", "Crítico"])
    elif evento_previsto == "Rajada de Raios Cósmicos":
        intensidade_nT = random.randint(50, 120)
        duracao_min = random.randint(240, 480)
        nivel_alerta = random.choice(["Atenção"])
    elif evento_previsto == "Tempestade Geomagnética":
        intensidade_nT = random.randint(150, 400)
        duracao_min = random.randint(45, 180)
        nivel_alerta = random.choice(["Alerta", "Crítico"])
    elif evento_previsto == "Vento Solar Intenso":
        intensidade_nT = random.randint(80, 300)
        duracao_min = random.randint(60, 300)
        nivel_alerta = random.choice(["Alerta", "Atenção"])
    elif evento_previsto == "Explosão Solar de Classe M":
        intensidade_nT = random.randint(150, 250)
        duracao_min = random.randint(60, 120)
        nivel_alerta = random.choice(["Alerta", "Crítico"])
    elif evento_previsto == "Explosão Solar de Classe X":
        intensidade_nT = random.randint(500, 650)
        duracao_min = random.randint(120, 200)
        nivel_alerta = random.choice(["Crítico"])
    elif evento_previsto == "Nenhum evento solar significativo detectado":
        intensidade_nT = 0
        duracao_min = 0
        nivel_alerta = "Tranquilo"
    data_previsao = datetime.datetime.now() + datetime.timedelta(days=random.randint(1, 30))
    
    if intensidade_nT > 0:
        with open("empresas.json", "r", encoding="utf-8") as f:
            data = json.load(f)
            for empresa in data["empresas"]:
                if empresa['usuario'] == name_login:
                    empresa['eventos_previstos'].append({
                        "tipo_evento": evento_previsto,
                        "intensidade_nT": intensidade_nT,
                        "duracao_min": duracao_min,
                        "nivel_alerta": nivel_alerta,
                        "data_previsao": data_previsao.strftime("%d/%m/%Y %H:%M")
                    })
                    with open("empresas.json", "w", encoding="utf-8") as f:
                        json.dump(data, f, indent=2, ensure_ascii=False)

    

while True:
    limpar_tela()
    sortear_evento()
    menu()
    opcao = input("\nEscolha uma opção: ")

#1. Sobre o Auron -> Feito
#2. Simulação de Impacto de Anomalia -> Feito
#3. Alertas Ativos 
#4. Histórico de Eventos -> Feito
#5. Previsão de Tempestades
#6. ROI — Custos Evitados e Desempenho
#7. Dashboard Completo              
#0. Sair

    match opcao:
        case "1":
            limpar_tela()
            sobre()
        case "2":
            limpar_tela()
            calcular_dano()
        case "3":
            limpar_tela()
            alertas_ativos()
            input("Pressione Enter para retornar ao menu...")
        case "4":
            limpar_tela()
            historico_eventos()
            input("Pressione Enter para retornar ao menu...")
        case "5":
            limpar_tela()
            prever_evento()
            input("Pressione Enter para retornar ao menu...")
        case "6":
            gerar_relatorio_roi()
            input("Pressione Enter para retornar ao menu...")
        case "7":
            print("\nFuncionalidade de Dashboard Completo em desenvolvimento. Fique atento às próximas atualizações!")
            input("Pressione Enter para retornar ao menu...")
        case "0":
            limpar_tela()
            print(f"\nSaindo do sistema Auron. Até a próxima {name_login}!")
            break
        case _:
            print(" Opção inválida. Tente novamente.")
            
