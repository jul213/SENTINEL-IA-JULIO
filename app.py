import streamlit as st
import pandas as pd
import plotly.express as px
from transformers import pipeline

# Configuración de nivel Enterprise
st.set_page_config(page_title="SENTINEL-AI | Security Hub", layout="wide")

@st.cache_resource
def load_ai():
    return pipeline("summarization", model="sshleifer/distilbart-cnn-12-6")

summarizer = load_ai()

st.title("🛡️ SENTINEL-AI: Security Intelligence Hub")
st.markdown("---")

# SIMULACIÓN DE BIG DATA: Carga de logs
# En un entorno real, esto vendría de una base de datos o un S3 de AWS
try:
    df = pd.read_csv("network_traffic.csv")
except:
    st.error("¡Falta el archivo de Big Data! Ejecuta primero el generador de logs.")
    st.stop()

# --- SECCIÓN 1: BIG DATA ANALYTICS ---
col1, col2 = st.columns(2)

with col1:
    st.subheader("📊 Análisis de Tráfico Masivo")
    fig = px.pie(df, names='threat_type', title='Distribución de Amenazas Detectadas', hole=0.4)
    st.plotly_chart(fig, use_container_width=True)

with col2:
    st.subheader("🚩 Alertas Críticas (Filtrado de Datos)")
    critical_events = df[df['action'] == 'BLOCK'].head(10)
    st.table(critical_events[['source_ip', 'threat_type', 'destination_port']])

# --- SECCIÓN 2: INTELIGENCIA ARTIFICIAL (SecOps) ---
st.markdown("---")
st.subheader("🧠 Análisis Predictivo de la IA")

selected_event = st.selectbox("Selecciona una IP bloqueada para análisis profundo:", critical_events['source_ip'].unique())

if st.button("Generar Reporte de Mitigación"):
    # Preparamos los datos para la IA
    contexto = f"El sistema detectó múltiples ataques de tipo {critical_events['threat_type'].iloc[0]} " \
               f"desde la IP {selected_event}. El firewall de Fortinet ha bloqueado el tráfico."
    
    with st.spinner('IA analizando vector de ataque...'):
        reporte = summarizer(contexto, max_length=50, min_length=20, do_sample=False)
        st.info(f"**Recomendación de la IA:** {reporte[0]['summary_text']}")
        st.success("Sugerencia: Aplicar regla de IPS en FortiGate para esta subred.")