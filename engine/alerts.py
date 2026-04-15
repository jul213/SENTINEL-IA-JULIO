import requests

def send_telegram_alert(message):
    # Esto es un ejemplo de cómo conectaríamos un Bot de Telegram
    # Un As automatiza las alertas de ataques críticos
    print(f"🚨 ALERTA DE SEGURIDAD ENVIADA: {message}")
    # En producción usarías: requests.post(f"https://api.telegram.org/bot{token}/sendMessage", data={...})

def analyze_critical_threats(df):
    # Si hay más de 5 bloqueos de la misma IP en un minuto, es un ataque serio
    stats = df[df['action'] == 'BLOCK']['source_ip'].value_counts()
    for ip, count in stats.items():
        if count > 5:
            send_telegram_alert(f"Posible ataque de Fuerza Bruta desde IP: {ip}. {count} intentos bloqueados.")