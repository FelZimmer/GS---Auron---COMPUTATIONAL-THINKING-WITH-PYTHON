import streamlit as st
import json
import os
import datetime
import logging
from filelock import FileLock, Timeout
from fpdf import FPDF
import pandas as pd
import plotly.express as px
from rich.console import Console
console = Console()

# Config
BASE_DIR = os.getcwd()
EMP_FILE = os.path.join(BASE_DIR, "empresas.json")
REL_DIR = os.path.join(BASE_DIR, "relatorios")
LOGS_DIR = os.path.join(BASE_DIR, "logs")
LOCK_FILE = EMP_FILE + ".lock"
os.makedirs(REL_DIR, exist_ok=True)
os.makedirs(LOGS_DIR, exist_ok=True)

# Logger
logger = logging.getLogger("Auron.dashboard")
logger.setLevel(logging.DEBUG)
if not logger.handlers:
    fh = logging.FileHandler(os.path.join(LOGS_DIR, "dashboard.log"), encoding="utf-8")
    fh.setLevel(logging.DEBUG)
    fh.setFormatter(logging.Formatter("%(asctime)s - %(levelname)s - %(message)s"))
    logger.addHandler(fh)


def safe_rerun():
    """Tenta forçar rerun no Streamlit; se indisponível, registra e continua."""
    try:
        st.experimental_rerun()
    except Exception:
        # Alguns builds do Streamlit não expõem experimental_rerun
        logger.debug("st.experimental_rerun() indisponível — instruir usuário a atualizar a página se necessário")
        # Sem rerun, a sessão_state já será avaliada na próxima interação
        return


def with_lock_read(path, timeout=1):
    lock = FileLock(LOCK_FILE)
    try:
        with lock.acquire(timeout=timeout):
            with open(path, "r", encoding="utf-8") as f:
                return json.load(f)
    except Timeout:
        logger.warning("Timeout ao tentar ler com lock, leitura sem lock")
        with open(path, "r", encoding="utf-8") as f:
            return json.load(f)


def with_lock_write(path, data, timeout=1):
    lock = FileLock(LOCK_FILE)
    try:
        with lock.acquire(timeout=timeout):
            with open(path, "w", encoding="utf-8") as f:
                json.dump(data, f, ensure_ascii=False, indent=2)
    except Timeout:
        logger.warning("Timeout ao tentar escrever com lock, tentativa sem lock")
        with open(path, "w", encoding="utf-8") as f:
            json.dump(data, f, ensure_ascii=False, indent=2)


def load_empresas():
    if not os.path.exists(EMP_FILE):
        logger.info("empresas.json inexistente; retornando lista vazia")
        return []
    try:
        data = with_lock_read(EMP_FILE)
        return data.get("empresas", [])
    except Exception:
        logger.exception("Falha ao ler empresas.json")
        return []


def salvar_empresas(empresas):
    try:
        with_lock_write(EMP_FILE, {"empresas": empresas})
        logger.info("empresas.json salvo")
    except Exception:
        logger.exception("Falha ao gravar empresas.json")


def autenticar(usuario, senha):
    empresas = load_empresas()
    for e in empresas:
        if e.get("usuario") == usuario and e.get("senha") == senha:
            logger.info(f"Login: {usuario}")
            return e
    logger.warning(f"Falha login: {usuario}")
    return None


def calcular_kpis(empresa):
    eventos = empresa.get("eventos", [])
    total = len(eventos)
    ativos = sum(1 for ev in eventos if ev.get("auron_acionado"))
    dano = sum((ev.get("dano_potencial") or 0) for ev in eventos)
    evitado = sum((ev.get("dano_evitado") or 0) for ev in eventos)
    return total, ativos, dano, evitado


def gerar_pdf_resumo(empresa):
    try:
        pdf = FPDF()
        pdf.add_page()
        pdf.set_font("Arial", "B", 14)
        nome = empresa.get("nome", "Empresa")
        usuario = empresa.get("usuario", "user")
        pdf.cell(0, 8, f"Relatório - {nome}", ln=1, align="C")
        pdf.ln(4)
        pdf.set_font("Arial", "", 11)
        pdf.cell(0, 6, f"Usuário: {usuario}", ln=1)
        pdf.cell(0, 6, f"Data: {datetime.datetime.now().strftime('%d/%m/%Y %H:%M')}", ln=1)
        pdf.ln(4)
        eventos = empresa.get("eventos", [])
        if not eventos:
            pdf.cell(0, 6, "Nenhum evento registrado.", ln=1)
        else:
            for ev in eventos:
                pdf.set_font("Arial", "B", 12)
                pdf.cell(0, 6, ev.get("tipo_evento", "Evento"), ln=1)
                pdf.set_font("Arial", "", 10)
                pdf.cell(0, 5, f"Data/Hora: {ev.get('data_hora')}", ln=1)
                pdf.cell(0, 5, f"Nível: {ev.get('nivel_alerta')}", ln=1)
                pdf.cell(0, 5, f"Dano potencial: R$ {ev.get('dano_potencial',0):,.2f}", ln=1)
                pdf.ln(2)
        out = os.path.join(REL_DIR, f"relatorio_{usuario}_{datetime.datetime.now().strftime('%d_%m_%Y')}.pdf")
        pdf.output(out)
        logger.info(f"PDF criado: {out}")
        return out
    except Exception:
        logger.exception("Erro ao criar PDF")
        return None


def eventos_para_df(empresa):
    ev = empresa.get("eventos", [])
    if not ev:
        return pd.DataFrame()
    df = pd.DataFrame(ev)
    return df

def carregar_sessao():
    try:
        with open("sessao.json", "r", encoding="utf-8") as f:
            return json.load(f)
    except FileNotFoundError:
        return None


# Streamlit UI
st.set_page_config(page_title="Auron — Dashboard", layout="wide")
st.title("Auron — Dashboard (local)")

if "user" not in st.session_state:          # ← adicione isso
    st.session_state.user = None 

if "user" not in st.session_state or st.session_state.user is None:
    sessao = carregar_sessao()
    if sessao:
        empresas = load_empresas()
        for e in empresas:
            if e.get("usuario") == sessao["usuario"]:
                st.session_state.user = e
                break

if st.session_state.user is None:
    st.error("Sessão não encontrada. Faça login pelo terminal.")
    st.stop()

with st.sidebar:
    st.header("Sessão")
    st.markdown(f"**{st.session_state.user.get('nome', '-')}**")
    if st.button("Sair"):
        if os.path.exists("sessao.json"):
            os.remove("sessao.json")
        st.session_state.user = None
        st.stop()

empresa = st.session_state.user
total, ativos, dano, evitado = calcular_kpis(empresa)

st.subheader("Visão Geral")
cols = st.columns(4)
cols[0].metric("Eventos", total)
cols[1].metric("Alertas Ativos", ativos)
cols[2].metric("Dano Potencial (R$)", f"R$ {dano:,.2f}")
cols[3].metric("Dano Evitado (R$)", f"R$ {evitado:,.2f}")

st.markdown("---")
df = eventos_para_df(empresa)
if not df.empty:
    if 'nivel_alerta' not in df.columns:
        df['nivel_alerta'] = 'Desconhecido'
    fig = px.histogram(df, x='nivel_alerta', title='Distribuição por Nível de Alerta')
    st.plotly_chart(fig, use_container_width=True)
else:
    st.info("Nenhum evento disponível para gráficos")

st.markdown("---")
st.subheader("Alertas Ativos")
if not df.empty:
    ativos_df = df[df.get('auron_acionado', False) == True]
    if ativos_df.empty:
        st.write("Sem alertas ativos no momento.")
    else:
        st.dataframe(ativos_df[['data_hora','tipo_evento','nivel_alerta','dano_potencial']].sort_values('data_hora', ascending=False))
else:
    st.write("Sem dados de eventos.")

st.markdown("---")
st.subheader("Histórico de Eventos")
if not df.empty:
    st.dataframe(df.sort_values('data_hora', ascending=False))
    if st.button("Gerar PDF de Histórico"):
        caminho = gerar_pdf_resumo(empresa)
        if caminho:
            st.success(f"PDF salvo: {caminho}")
            with open(caminho, "rb") as f:
                st.download_button("Baixar PDF", f, file_name=os.path.basename(caminho))
        else:
            st.error("Falha ao gerar PDF")
else:
    st.write("Nenhum evento registrado.")

st.markdown("---")
st.subheader("Eventos Previstos")
prev = empresa.get('eventos_previstos', [])
if prev:
    st.table(prev)
else:
    st.write("Nenhum evento previsto.")

st.markdown("---")
st.subheader("Ações")
if st.button("Atualizar dados (recarregar empresas.json)"):
    st.session_state.user = autenticar(empresa.get('usuario'), empresa.get('senha'))
    safe_rerun()

st.caption("Aplicação local, rápida e funcional. Usa file lock simples para evitar corrupção concorrente.")
