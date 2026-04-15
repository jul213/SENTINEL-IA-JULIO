# 🛡️ SENTINEL-AI: Security Intelligence Hub

**SENTINEL-AI** es una plataforma avanzada de **SecOps** que integra Inteligencia Artificial, análisis de Big Data y contenedores Docker para la detección y mitigación de amenazas en redes empresariales.

Este proyecto simula un entorno de monitoreo de seguridad (tipo Fortinet/SOC) donde los logs masivos son procesados, visualizados y analizados por modelos de lenguaje natural (NLP) para generar reportes de respuesta inmediata.

---

## 🚀 Tecnologías y Pilares del Proyecto

* **IA (Brain):** Procesamiento de Lenguaje Natural con `Hugging Face Transformers` para análisis de vectores de ataque.
* **Big Data (Muscle):** Procesamiento y limpieza de miles de logs de tráfico con `Pandas` y `NumPy`.
* **Data Viz:** Dashboard interactivo desarrollado en `Streamlit` con gráficas de `Plotly`.
* **DevOps & Cloud:** Contenedorización completa mediante `Docker` y orquestación con `Docker Compose`.
* **Cybersecurity:** Lógica de filtrado basada en eventos de red (Blocking, Brute Force, Port Scanning).

---

## 📦 Arquitectura del Sistema

```text
SENTINEL-AI/
├── engine/             # Lógica de procesamiento de Big Data
├── data/               # Almacenamiento de logs (Dataset)
├── app.py              # Interfaz de usuario y núcleo de la IA
├── Dockerfile          # Definición de la imagen del contenedor
├── docker-compose.yml  # Orquestación de microservicios
└── requirements.txt    # Dependencias de grado industrial