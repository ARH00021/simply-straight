"""
SIMPLY STRAIGHT — Auto-Respondedor de Primer Contacto
=====================================================
Vigila los archivos de sesión de WhatsApp y envía el mensaje
exacto a clientes NUEVOS. SIN IA. 100% predecible.

Ejecutar una vez: python auto_responder.py
"""

import time
import re
import json
import requests
from pathlib import Path
from datetime import datetime

# Config
BRIDGE_URL = "http://localhost:3000"
SESSION_DIR = Path.home() / "AppData" / "Local" / "hermes" / "sessions"
ATENDIDOS_FILE = Path.home() / "proyectos" / "dropi" / "simply-straight" / "clientes_atendidos.txt"
OWNER_NUMBERS = ["573186606067", "573106606720"]
CHANNEL_DIR = Path.home() / "AppData" / "Local" / "hermes" / "channel_directory.json"

MENSAJE = """¡Hola! 😊✨ Simply Straight es el cepillo alisador que toda colombiana está queriendo. 🇨🇴 Cerámica 3D que cuida tu cabello. Pantalla digital 185°C. Alisa en 1 minuto sin plancha, sin cremas, sin drama. 🔒 Auto apagado de seguridad. ⚡ Voltaje 110V-220V, funciona perfecto en Colombia. 💰 AHORA $109.900 — precio de lanzamiento. Después sube a $159.900. Ahorras $50.000 hoy. 🚚 Envío GRATIS a toda Colombia 🛡️ Garantía: si no te encanta, te devuelvo todo tu dinero. ¿Te aparto el tuyo? Me quedan pocos de esta tanda 🙌"""

def log(msg):
    print(f"[{datetime.now().strftime('%H:%M:%S')}] {msg}", flush=True)

def cargar_atendidos():
    if ATENDIDOS_FILE.exists():
        return set(ATENDIDOS_FILE.read_text().strip().split('\n'))
    return set()

def guardar_atendido(chat_id):
    ATENDIDOS_FILE.parent.mkdir(parents=True, exist_ok=True)
    with open(ATENDIDOS_FILE, 'a') as f:
        f.write(f"{chat_id}\n")

def obtener_chats_clientes():
    """Lee channel_directory.json para obtener chats de clientes (no Arturo)."""
    if not CHANNEL_DIR.exists():
        return {}
    try:
        data = json.loads(CHANNEL_DIR.read_text())
        chats = {}
        for entry in data.get("platforms", {}).get("whatsapp", []):
            chat_id = entry.get("id", "")
            name = entry.get("name", "")
            # Excluir chats de Arturo o sistema
            if any(owner in name.lower() for owner in ["arturo", "simply straight colombia"]):
                continue
            chats[chat_id] = name
        return chats
    except:
        return {}

def enviar_mensaje(chat_id, texto):
    """Envía mensaje via el bridge de WhatsApp."""
    try:
        resp = requests.post(
            f"{BRIDGE_URL}/send",
            json={"chatId": chat_id, "message": texto},
            timeout=10
        )
        return resp.status_code == 200 and resp.json().get("success")
    except Exception as e:
        log(f"  ❌ Error: {e}")
        return False

def main():
    log("🟢 Simply Straight Auto-Respondedor INICIADO")
    log("📋 Mensaje exacto cargado")
    
    atendidos = cargar_atendidos()
    log(f"📁 {len(atendidos)} chats ya atendidos")
    
    while True:
        try:
            chats = obtener_chats_clientes()
            
            for chat_id, nombre in chats.items():
                if chat_id in atendidos:
                    continue
                
                log(f"🆕 Nuevo cliente: {nombre} ({chat_id})")
                
                if enviar_mensaje(chat_id, MENSAJE):
                    log(f"  ✅ Mensaje enviado a {nombre}")
                    guardar_atendido(chat_id)
                    atendidos.add(chat_id)
                else:
                    log(f"  ❌ Falló envío a {nombre}")
            
            time.sleep(5)
            
        except KeyboardInterrupt:
            log("🔴 Detenido")
            break
        except Exception as e:
            log(f"⚠️ {e}")
            time.sleep(5)

if __name__ == "__main__":
    main()
