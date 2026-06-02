import math
import random
import matplotlib.pyplot as plt
import json
import os

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
    nomes_estados = sorted(ESTADOS_BRASIL.values())
    
    while True:
        print("\nEscolha o estado onde sua empresa está localizada:")
        for i, estado in enumerate(nomes_estados, 1):
            print(f"{i:2}. {estado}")
            
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
        "eventos": []
})

    with open("empresas.json", "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=2)
    
    print(f"\nCadastro concluído! ")
    login()
    

            
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
            return empresa_logada["usuario"]  # Retorna o nome de usuário para uso posterior 
        else:
            print("\nUsuário ou senha incorreto(s).")
            match int(input("""Selecione uma opção:\n
1. Cadastro
2. Tentar novamente \n
                            """)):
                case 1:
                    cadastrar_empresa()
                case 2:
                    print("\nTente novamente fazer login.")
                    login()
                case _:
                    print("Opção inválida. Retornando ao menu principal.")

    except FileNotFoundError:
        print("\nErro: Arquivo 'empresas.json' não encontrado.")
        return None
    except json.JSONDecodeError:
        print("\nErro: Arquivo de dados corrompido.")
        return None



def sortear_evento():
    is_event = random.choice([True, False, False, False])
    if is_event:
        with open("eventos.json", "r") as f:
            data = json.load(f)
            evento_aleatorio = random.choice(data["eventos"])
            print(f"\n Evento Solar Detectado: {evento_aleatorio['tipo_evento']}")
            print(f" Status: {evento_aleatorio['nivel_alerta']}") # Pintar de acordo com o nível de alerta
    else:
        print(" Nenhum evento solar significativo detectado.")
        return

    try:
        with open("empresas.json", "r", encoding="utf-8") as f:
            data = json.load(f)
    except (FileNotFoundError, json.JSONDecodeError):
            data = {"empresas": []}

    for empresa in data["empresas"]:
        if empresa["usuario"] == name_login:
            empresa["eventos"].append(evento_aleatorio)

    with open("empresas.json", "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=2)
        
    
    

def menu():
    limpar_tela()
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
    try:
        with open("empresas.json", "r", encoding="utf-8") as f:
            empresas = json.load(f).get("empresas", [])
        for empresa in empresas:
            if empresa["usuario"] == name_login:
                eventos = empresa["eventos"]
                if eventos:
                    print(f"\nHistórico de Eventos da {empresa['nome']} :")
                    for evento in eventos:
                        print(f"\n  Evento #{evento['id']}")
                        print(f"  Tipo         : {evento['tipo_evento']}")
                        print(f"  Intensidade  : {evento['intensidade_nT']} nT")
                        print(f"  Duração      : {evento['duracao_min']} min")
                        print(f"  Equipamento  : {evento['equipamento_risco']}")
                        print(f"  Nível Alerta : {evento['nivel_alerta']}")
                        print(f"  Dano Potencial: R$ {evento['dano_potencial']:,.2f}")
                        print(f"  Dano Evitado : R$ {evento['dano_evitado']:,.2f}")
                        print(f"  Custo Reparo : R$ {evento['custo_reparo']:,.2f}")
                        print(f"  Auron Acionado: {'✔ Sim' if evento['auron_acionado'] else '✘ Não'}")
                        print(f"  {'-'*45}")
                    return
    except Exception as e:
        print(f"Erro encontrado: {e}")            
            
def Alertas_ativos():
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
name_login = login()

while True:
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
            Alertas_ativos()
            input("Pressione Enter para retornar ao menu...")
        case "4":
            limpar_tela()
            historico_eventos()
            input("Pressione Enter para retornar ao menu...")
        case "5":
            print("\nFuncionalidade de Previsão de Tempestades em desenvolvimento. Fique atento às próximas atualizações!")
            input("Pressione Enter para retornar ao menu...")
        case "6":
            print("\nFuncionalidade de ROI em desenvolvimento. Fique atento às próximas atualizações!")
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
            