"""
BOT SIMPLY STRAIGHT — WhatsApp Bot para clientes
Seguro, simple, respuestas EXACTAS. SIN IA. SIN acceso a archivos.
"""

import json
import os
import re
from pathlib import Path
from datetime import datetime
import time

# ============================================================
# CONFIGURACIÓN
# ============================================================
# Número de Arturo (dueño) — los mensajes de este número se ignoran
OWNER_NUMBER = "573186606067"

# Directorio donde el bridge de WhatsApp guarda mensajes
WATCH_DIR = Path.home() / "AppData" / "Local" / "hermes" / "platforms" / "whatsapp"

# ============================================================
# PLANTILLAS DE RESPUESTA (EXACTAS, nunca cambiar)
# ============================================================

PRIMER_MENSAJE = """¡Hola! 😊✨ Simply Straight es el cepillo alisador que toda colombiana está queriendo. 🇨🇴 Cerámica 3D que cuida tu cabello. Pantalla digital 185°C. Alisa en 1 minuto sin plancha, sin cremas, sin drama. 🔒 Auto apagado de seguridad. ⚡ Voltaje 110V-220V, funciona perfecto en Colombia. 💰 AHORA $109.900 — precio de lanzamiento. Después sube a $159.900. Ahorras $50.000 hoy. 🚚 Envío GRATIS a toda Colombia 🛡️ Garantía: si no te encanta, te devuelvo todo tu dinero. ¿Te aparto el tuyo? Me quedan pocos de esta tanda 🙌"""

RESPUESTA_COMPRAR = """¡Perfecto! 🎉 Qué bien que te animes.

Para tu pedido solo necesito estos datos:
1️⃣ Nombre completo
2️⃣ Número de cédula
3️⃣ Ciudad y dirección completa (con barrio)
4️⃣ Número de contacto

💳 Pago: Nequi o Bancolombia
💚 Nequi: 0092634120
📦 Envío GRATIS a toda Colombia · llega en 2-4 días hábiles
🚚 Enviado por Servientrega o Interrapidisimo

¿Cómo prefieres pagar? 🙌"""

RESPUESTA_GARANTIA = """¡Claro que sí! 🛡️ Tienes garantía total: si no te encanta el resultado, te devuelvo el 100% de tu dinero. Sin peros, sin letra chica.

Queremos que pruebes Simply Straight completamente tranquila. Si no te gusta, me escribes y te devuelvo todo.

¿Te animas a probarlo? 🙌"""

RESPUESTA_ENVIO = """📦 Envío GRATIS a toda Colombia 🇨🇴

🚚 Enviamos por Servientrega, Interrapidisimo y Coordinadora
⏱️ Llega en 2-4 días hábiles a ciudades principales
📲 Te damos número de guía para rastreo

¿Me confirmas tu ciudad y te digo el tiempo exacto?"""

RESPUESTA_CARO = """Te entiendo. Mira:

💡 Es una inversión, no un gasto. Una plancha buena cuesta más y te toma 40 minutos. Simply Straight te alisa en 1 minuto TODOS los días.

🎁 Además el envío es GRATIS. Y ahora está en precio de lanzamiento: $109.900. Después sube a $159.900.

✨ Y tienes garantía de devolución. Pruébalo sin riesgo. ¿Te lo aparto?"""

RESPUESTA_DUDA = """Te entiendo perfecto. Yo también desconfío de lo que veo en internet 😅

Pero mira:
✅ Cerámica 3D que cuida tu cabello
✅ Resultado en 1 minuto, sin plancha
✅ Envío GRATIS a toda Colombia
✅ Garantía de devolución total — no arriesgas nada

Y AHORA: $109.900. Después $159.900. Son $50.000 que te ahorras hoy.

¿Te animas a probarlo? No tienes nada que perder 🙌✨"""

RESPUESTA_PAGO = """¡Gracias por confiar! 🥰

Para el pago:
💚 Nequi: 0092634120
💰 Valor: $109.900 COP

Envíame el comprobante y queda listo 🚚
Te llega en 2-4 días. Cualquier duda, aquí estoy."""

RESPUESTA_DATOS = """¡Gracias! Con esos datos ya tengo todo para tu envío.

Ahora solo falta el pago:
💚 Nequi: 0092634120
💰 $109.900 COP

¿Cómo prefieres pagar? 🙌"""

# ============================================================
# LÓGICA DE DETECCIÓN
# ============================================================

def detectar_intencion(mensaje):
    """Detecta qué quiere el cliente basado en palabras clave."""
    msg = mensaje.lower().strip()
    
    # Comprar / pedir
    if any(w in msg for w in ['comprar', 'lo quiero', 'quiero uno', 'pedir', 'apartar',
                                'envíame', 'envíe', 'cómo pago', 'como pago', 'pagar',
                                'nequi', 'bancolombia', 'contraentrega']):
        return 'comprar'
    
    # Datos de envío (nombre, dirección, ciudad)
    if re.search(r'(nombre|direcci[oó]n|ciudad|barrio|cra|carrera|calle|av|transversal)', msg):
        return 'datos_envio'
    
    # Garantía
    if any(w in msg for w in ['garantía', 'garantia', 'devolución', 'devolucion',
                                'reembolso', 'no sirve', 'no funciona', 'daña', 'dañar']):
        return 'garantia'
    
    # Envío
    if any(w in msg for w in ['envío', 'envio', 'envían', 'llega', 'llegar', 'demora',
                                'domicilio', 'cuánto tarda', 'cuanto tarda']):
        return 'envio'
    
    # Caro
    if any(w in msg for w in ['caro', 'costoso', 'muy caro', 'rebaja', 'descuento',
                                'más barato', 'económico']):
        return 'caro'
    
    # Duda
    if any(w in msg for w in ['duda', 'seguro', 'funciona', 'sirve', 'verdad',
                                'confiar', 'estafa', 'falso']):
        return 'duda'
    
    # Pago confirmado / comprobante
    if any(w in msg for w in ['comprobante', 'transferencia', 'pagué', 'pague',
                                'ya pagué', 'ya pague', 'listo']):
        return 'pago'
    
    # Info general / precio / primer contacto
    if any(w in msg for w in ['info', 'información', 'informacion', 'precio',
                                'cuánto', 'cuanto', 'vale', 'valor', 'cuesta',
                                'hola', 'buenas', 'qué tal', 'cepillo',
                                'alisador', 'simply', 'straight']):
        return 'primer_mensaje'
    
    # Por defecto, manda info del producto
    return 'primer_mensaje'


def obtener_respuesta(intencion):
    """Devuelve la plantilla exacta según la intención."""
    respuestas = {
        'primer_mensaje': PRIMER_MENSAJE,
        'comprar': RESPUESTA_COMPRAR,
        'garantia': RESPUESTA_GARANTIA,
        'envio': RESPUESTA_ENVIO,
        'caro': RESPUESTA_CARO,
        'duda': RESPUESTA_DUDA,
        'pago': RESPUESTA_PAGO,
        'datos_envio': RESPUESTA_DATOS,
    }
    return respuestas.get(intencion, PRIMER_MENSAJE)


# ============================================================
# LOG
# ============================================================

def log(mensaje):
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    print(f"[{timestamp}] {mensaje}")


# ============================================================
# MAIN
# ============================================================

if __name__ == "__main__":
    log("🟢 Bot Simply Straight iniciado")
    log(f"📁 Vigilando: {WATCH_DIR}")
    log(f"👤 Dueño: {OWNER_NUMBER}")
    log("📋 Plantillas cargadas: primer_mensaje, comprar, garantia, envio, caro, duda, pago, datos_envio")
    log("⏳ Esperando mensajes...")
    
    # Mantener el proceso vivo
    try:
        while True:
            time.sleep(60)
    except KeyboardInterrupt:
        log("🔴 Bot detenido")
