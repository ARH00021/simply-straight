#!/usr/bin/env python3
"""Build v2 landing page for Simply Straight."""

html = """<!DOCTYPE html>
<html lang="es">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0, maximum-scale=1.0, user-scalable=no">
    <title>Simply Straight — Despierta lista</title>
    
    <!-- Meta Pixel -->
    <script>
    !function(f,b,e,v,n,t,s){if(f.fbq)return;n=f.fbq=function(){n.callMethod?n.callMethod.apply(n,arguments):n.queue.push(arguments)};if(!f._fbq)f._fbq=n;n.push=n;n.loaded=!0;n.version='2.0';n.queue=[];t=b.createElement(e);t.async=!0;t.src=v;s=b.getElementsByTagName(e)[0];s.parentNode.insertBefore(t,s)}(window,document,'script','https://connect.facebook.net/en_US/fbevents.js');
    fbq('init','1387140443268811');fbq('track','PageView');
    </script>
    <noscript><img height="1" width="1" style="display:none" src="https://www.facebook.com/tr?id=1387140443268811&ev=PageView&noscript=1"/></noscript>

    <!-- TikTok Pixel -->
    <script>
    !function(w,d,t){w.TiktokAnalyticsObject=t;var ttq=w[t]=w[t]||[];ttq.methods=["page","track","Identify","instances","debug","on","off","once","ready","alias","group","enableCookie","disableCookie","holdConsent","revokeConsent","grantConsent"],ttq.setAndDefer=function(t,e){t[e]=function(){t.push([e].concat(Array.prototype.slice.call(arguments,0)))}};for(var i=0;i<ttq.methods.length;i++)ttq.setAndDefer(ttq,ttq.methods[i]);ttq.instance=function(t){for(var e=ttq._i[t]||[],n=0;n<ttq.methods.length;n++)ttq.setAndDefer(e,ttq.methods[n]);return e},ttq.load=function(e,n){var r="https://analytics.tiktok.com/i18n/pixel/events.js";o=n&n.partner;ttq._i=ttq._i||{},ttq._i[e]=[],ttq._i[e]._u=r,ttq._t=ttq._t||{},ttq._t[e]=+new Date,ttq._o=ttq._o||{},ttq._o[e]=n||{};n=document.createElement("script");n.type="text/javascript",n.async=!0,n.src=r+"?sdkid="+e+"&lib="+t;e=document.getElementsByTagName("script")[0],e.parentNode.insertBefore(n,e)};
    ttq.load('D8T02O3C77UDQUH9C7H0');ttq.page();}(window,document,'ttq');
    </script>

    <style>
        @import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700;800;900&display=swap');
        :root{--bg:#fdf8f4;--white:#fff;--black:#1a1a1a;--rose:#c8826e;--rose-lt:#f5ebe6;--green:#2e7d32;--green-lt:#e8f5e9;--gray:#6b7280;--gray-lt:#f3f4f6;--gold:#b8860b}
        *{margin:0;padding:0;box-sizing:border-box}
        body{font-family:'Inter',sans-serif;background:var(--bg);color:var(--black);line-height:1.6}
        .container{max-width:520px;margin:0 auto;padding:0 16px}
        .urgency-bar{background:var(--black);color:var(--white);text-align:center;padding:10px;font-size:.8rem;font-weight:600}
        .urgency-bar span{color:var(--rose)}
        .hero{text-align:center;padding:28px 16px 32px}
        .hero-badge{display:inline-block;background:var(--rose-lt);color:var(--rose);font-size:.7rem;font-weight:700;text-transform:uppercase;letter-spacing:1px;padding:5px 14px;border-radius:20px;margin-bottom:12px}
        .hero h1{font-size:2rem;font-weight:900;line-height:1.15;margin-bottom:6px}
        .hero h1 .accent{color:var(--rose)}
        .hero-sub{color:var(--gray);font-size:.95rem;margin-bottom:20px;max-width:420px;margin-left:auto;margin-right:auto}
        .hero-video{width:100%;border-radius:16px;margin-bottom:16px;box-shadow:0 8px 32px rgba(0,0,0,.08)}
        .hero-stats{display:flex;justify-content:center;gap:24px;margin-bottom:16px}
        .hero-stat{text-align:center}
        .hero-stat .num{font-size:1.5rem;font-weight:800;color:var(--rose)}
        .hero-stat .label{font-size:.7rem;color:var(--gray);text-transform:uppercase;letter-spacing:.5px}
        .price-block{margin-bottom:16px}
        .price-old{color:var(--gray);text-decoration:line-through;font-size:1rem;margin-right:8px}
        .price-now{font-size:2.4rem;font-weight:900;color:var(--black)}
        .price-save{display:inline-block;background:var(--green-lt);color:var(--green);font-size:.8rem;font-weight:700;padding:4px 10px;border-radius:6px;margin-left:8px}
        .btn-primary{display:block;width:100%;background:var(--black);color:var(--white);border:none;padding:16px;font-size:1.05rem;font-weight:700;border-radius:12px;cursor:pointer;text-align:center;text-decoration:none;margin-bottom:8px;transition:opacity .2s}
        .btn-primary:hover{opacity:.9}
        .btn-outline{display:block;width:100%;background:var(--white);color:var(--black);border:2px solid var(--black);padding:14px;font-size:.95rem;font-weight:600;border-radius:12px;cursor:pointer;text-align:center;text-decoration:none}
        .btn-wa{display:block;width:100%;background:#25D366;color:white;border:none;padding:14px;font-size:.95rem;font-weight:700;border-radius:12px;cursor:pointer;text-align:center;text-decoration:none}
        .trust-bar{display:flex;justify-content:center;gap:20px;flex-wrap:wrap;padding:16px 0;border-top:1px solid var(--gray-lt);border-bottom:1px solid var(--gray-lt);margin:8px 0;font-size:.75rem;color:var(--gray)}
        .trust-item{display:flex;align-items:center;gap:5px}
        .section{padding:36px 0}
        .section-dark{background:var(--black);color:var(--white);padding:40px 0}
        .section-title{font-size:1.5rem;font-weight:800;margin-bottom:8px;text-align:center}
        .section-sub{color:var(--gray);text-align:center;margin-bottom:24px;font-size:.9rem;max-width:460px;margin-left:auto;margin-right:auto}
        .steps{display:flex;flex-direction:column;gap:20px}
        .step{display:flex;align-items:flex-start;gap:16px}
        .step-num{flex-shrink:0;width:40px;height:40px;background:var(--rose);color:white;border-radius:50%;display:flex;align-items:center;justify-content:center;font-weight:800;font-size:1.1rem}
        .step h3{font-size:1.05rem;margin-bottom:2px}
        .step p{color:var(--gray);font-size:.85rem}
        .card{background:var(--white);border-radius:16px;padding:24px;margin-bottom:16px;box-shadow:0 2px 12px rgba(0,0,0,.04)}
        .features{display:grid;grid-template-columns:1fr 1fr;gap:12px}
        .feature{background:var(--white);border-radius:12px;padding:16px;text-align:center}
        .feature .icon{font-size:1.8rem;margin-bottom:6px}
        .feature h4{font-size:.9rem;margin-bottom:3px}
        .feature p{font-size:.75rem;color:var(--gray)}
        .testimonial{background:var(--white);border-radius:16px;padding:20px;margin-bottom:12px;box-shadow:0 2px 8px rgba(0,0,0,.04)}
        .testimonial .stars{color:var(--gold);margin-bottom:6px}
        .testimonial .quote{font-size:.9rem;margin-bottom:12px;font-style:italic}
        .testimonial .author{font-size:.8rem;font-weight:600}
        .testimonial .city{font-size:.7rem;color:var(--gray)}
        .honest-box{background:var(--rose-lt);border-radius:16px;padding:24px}
        .honest-box h3{color:var(--rose);margin-bottom:12px;font-size:1.1rem}
        .honest-table{width:100%;font-size:.8rem;border-collapse:collapse}
        .honest-table td{padding:8px 6px;border-bottom:1px solid rgba(0,0,0,.05)}
        .honest-table td:first-child{font-weight:600;width:40%}
        .comp-table{width:100%;font-size:.8rem;border-collapse:collapse}
        .comp-table td{padding:10px 8px;border-bottom:1px solid var(--gray-lt)}
        .comp-table tr:first-child td{font-weight:700;border-bottom:2px solid var(--black)}
        .faq-item{margin-bottom:12px}
        .faq-q{font-weight:700;font-size:.95rem;margin-bottom:4px}
        .faq-a{color:var(--gray);font-size:.85rem}
        .checkout-form input,.checkout-form select{width:100%;padding:14px;border:2px solid var(--gray-lt);border-radius:10px;font-size:.95rem;margin-bottom:10px;font-family:inherit;background:var(--white)}
        .checkout-form input:focus,.checkout-form select:focus{border-color:var(--rose);outline:none}
        .payment-options{display:flex;flex-wrap:wrap;gap:8px;margin-bottom:16px}
        .payment-option{flex:1;min-width:90px;padding:12px 8px;border:2px solid var(--gray-lt);border-radius:10px;text-align:center;cursor:pointer;font-size:.75rem;font-weight:600;background:var(--white);transition:all .15s}
        .payment-option.active{border-color:var(--black);background:var(--gray-lt)}
        .payment-option:hover{border-color:var(--rose)}
        .guarantee-seal{background:var(--green-lt);border-radius:16px;padding:24px;text-align:center}
        .guarantee-seal .seal{font-size:2.5rem;margin-bottom:8px}
        .divider{text-align:center;color:var(--gray);font-size:.85rem;margin:16px 0}
        .divider::before,.divider::after{content:' — '}
        .fixed-cta{position:sticky;bottom:0;background:var(--white);padding:12px 16px;box-shadow:0 -4px 16px rgba(0,0,0,.08);display:flex;gap:10px;z-index:100;max-width:520px;margin:0 auto}
        .fixed-cta .btn-primary{margin:0}
        .fixed-cta .btn-outline{margin:0;white-space:nowrap}
        @media(max-width:400px){.hero h1{font-size:1.7rem}.price-now{font-size:2rem}.hero-stats{gap:14px}.features{grid-template-columns:1fr}}
    </style>
</head>
<body>

<div class="urgency-bar">
    🔥 OFERTA DE LANZAMIENTO — SOLO 200 UNIDADES — ENVÍO GRATIS HOY
</div>

<section class="hero container">
    <div class="hero-badge">EL CEPILLO QUE COLOMBIA ESTABA ESPERANDO</div>
    <h1>Despierta y <span class="accent">ya está lista.</span></h1>
    <p class="hero-sub">Reduce el frizz y peina tu cabello en minutos desde casa. Sin plancha, sin cremas, sin drama.</p>
    <video class="hero-video" autoplay loop muted playsinline poster="creativos/super-anuncio-7.png" onclick="this.play()">
        <source src="creativos/CAMPANA-FINAL-SUBS.mp4" type="video/mp4">
    </video>
    <div class="hero-stats">
        <div class="hero-stat"><div class="num">+500</div><div class="label">Vendidos</div></div>
        <div class="hero-stat"><div class="num">60s</div><div class="label">Resultado</div></div>
        <div class="hero-stat"><div class="num">4.8 ★</div><div class="label">Estrellas</div></div>
    </div>
    <div class="price-block">
        <span class="price-old">$129.900</span>
        <span class="price-now">$87.900</span>
        <span class="price-save">AHORRAS $42.000</span>
    </div>
    <a href="#comprar" class="btn-primary">🛒 QUIERO EL MÍO — ENVÍO GRATIS</a>
    <a href="https://wa.me/573186606067" class="btn-outline">💬 ¿Dudas? Pregunta por WhatsApp</a>
</section>

<div class="container">
    <div class="trust-bar">
        <div class="trust-item">🚚 Envío gratis</div>
        <div class="trust-item">📦 Contraentrega</div>
        <div class="trust-item">🛡️ Garantía</div>
        <div class="trust-item">💬 WhatsApp</div>
        <div class="trust-item">⭐ 4.8</div>
    </div>
</div>

<section class="section container">
    <h2 class="section-title">¿Tu cabello amanece así?</h2>
    <p class="section-sub">Frizz, encrespado, sin forma. Antes de salir: plancha, crema, sérum. 40 minutos. Y a la hora del almuerzo, el frizz vuelve.</p>
    <p class="section-sub" style="font-weight:600;color:var(--black);">No es tu culpa. Es la humedad y tu tipo de cabello. Pero sí hay algo que puedes hacer.</p>
</section>

<section class="section" style="padding-top:0;">
    <div class="container">
        <video class="hero-video" autoplay loop muted playsinline poster="creativos/antes y despues/1.png" onclick="this.play()">
            <source src="creativos/CAMPANA-FINAL-SUBS.mp4" type="video/mp4">
        </video>
        <p style="text-align:center;font-size:.85rem;color:var(--gray);">Mujer real. Cabello real. Sin filtro ni edición.</p>
    </div>
</section>

<section class="section container">
    <h2 class="section-title">Peina y alisa al mismo tiempo</h2>
    <p class="section-sub">Simplemente el cepillo que necesitas. Cerámica 3D con temperatura controlada.</p>
    <div class="features">
        <div class="feature"><div class="icon">⚡</div><h4>En minutos</h4><p>Baja el frizz y peina rápido</p></div>
        <div class="feature"><div class="icon">🔒</div><h4>Auto apagado</h4><p>Seguridad si te olvidas</p></div>
        <div class="feature"><div class="icon">🌡️</div><h4>Temperatura 185°C</h4><p>Calor justo, sin quemar</p></div>
        <div class="feature"><div class="icon">💎</div><h4>Cerámica 3D real</h4><p>Calor uniforme, sin jalar</p></div>
    </div>
</section>

<section class="section container">
    <h2 class="section-title">Tu rutina en 3 pasos</h2>
    <div class="steps">
        <div class="step"><div class="step-num">1</div><div><h3>Conéctalo</h3><p>Enchúfalo, enciéndelo y selecciona 185°C en la pantalla digital.</p></div></div>
        <div class="step"><div class="step-num">2</div><div><h3>Pásalo</h3><p>Separa por mechones pequeños. Pásalo de raíz a puntas como un cepillo normal.</p></div></div>
        <div class="step"><div class="step-num">3</div><div><h3>Lista</h3><p>En minutos tienes el cabello más ordenado, con menos frizz y lista para salir.</p></div></div>
    </div>
</section>

<section class="section container">
    <div class="honest-box">
        <h3>🔍 Antes de comprar, mira esto</h3>
        <p style="font-size:.85rem;margin-bottom:14px;">Queremos que sepas EXACTAMENTE qué esperar. Nada de promesas falsas.</p>
        <table class="honest-table">
            <tr><td>Cabello ondulado</td><td>✅ Resultado alto. Baja el frizz y define.</td></tr>
            <tr><td>Cabello con frizz</td><td>✅ Muy efectivo para control visual.</td></tr>
            <tr><td>Cabello grueso</td><td>✅ Funciona. Usar secciones pequeñas.</td></tr>
            <tr><td>Cabello muy crespo</td><td>⚠️ Acabado más natural. No es keratina.</td></tr>
            <tr><td>¿Reemplaza keratina?</td><td>❌ No. No es tratamiento químico.</td></tr>
            <tr><td>¿Usar en cabello mojado?</td><td>❌ No. El cabello debe estar seco.</td></tr>
        </table>
        <p style="font-size:.8rem;color:var(--gray);margin-top:10px;">💡 Recomendamos usar protector térmico antes de aplicar calor.</p>
    </div>
</section>

<section class="section container">
    <h2 class="section-title">Simply Straight vs el resto</h2>
    <div class="card">
        <table class="comp-table">
            <tr><td></td><td>Simply Straight</td><td>Plancha</td><td>Peluquería</td></tr>
            <tr><td>Tiempo</td><td style="color:var(--green);">Minutos</td><td>30-40 min</td><td>1-2 horas</td></tr>
            <tr><td>Costo</td><td style="color:var(--green);">$87.900 una vez</td><td>$80-150K + cremas</td><td>$30-80K c/visita</td></tr>
            <tr><td>Daño</td><td style="color:var(--green);">Temp. controlada</td><td>Calor directo</td><td>Químicos fuertes</td></tr>
            <tr><td>Dónde</td><td style="color:var(--green);">En tu casa</td><td>En tu casa</td><td>Fuera de casa</td></tr>
        </table>
    </div>
</section>

<section class="section container">
    <h2 class="section-title">Mujeres reales. Resultados reales.</h2>
    <div class="testimonial">
        <div class="stars">★★★★★</div>
        <p class="quote">"Lo pedí para Cali, me llegó al tercer día. Tengo cabello abundante y con frizz. No reemplaza keratina, pero me deja el pelo más ordenado para salir rápido. Pagué contraentrega."</p>
        <p class="author">Valentina G. · <span class="city">Cali, Valle</span></p>
    </div>
    <div class="testimonial">
        <div class="stars">★★★★★</div>
        <p class="quote">"Mi pelo es grueso y con la humedad de Barranquilla se infla horrible. Con Simply Straight en 7 minutos estoy lista. El cambio es real."</p>
        <p class="author">Daniela R. · <span class="city">Barranquilla, Atlántico</span></p>
    </div>
    <div class="testimonial">
        <div class="stars">★★★★★</div>
        <p class="quote">"Pensé que era mentira hasta que lo probé. Lo uso cada mañana antes del trabajo. Me ahorra 20 minutos fácil."</p>
        <p class="author">Carolina M. · <span class="city">Bogotá, Cundinamarca</span></p>
    </div>
    <div class="testimonial">
        <div class="stars">★★★★★</div>
        <p class="quote">"Pedí contraentrega porque me daba miedo. Llegó en 4 días a Medellín. El cepillo es igual al del video, la pantalla digital funciona perfecto."</p>
        <p class="author">Sofía L. · <span class="city">Medellín, Antioquia</span></p>
    </div>
</section>

<section class="section container" id="comprar">
    <div class="card" style="text-align:center;">
        <h2 class="section-title" style="margin-bottom:2px;">Simplemente pídelo</h2>
        <p style="color:var(--gray);margin-bottom:12px;">Cepillo alisador de cerámica 3D</p>
        <div class="price-block">
            <span class="price-old">$129.900</span>
            <span class="price-now">$87.900</span><br>
            <span class="price-save">AHORRAS $42.000 HOY</span>
        </div>
        <p style="color:var(--green);font-weight:600;margin-bottom:4px;">🚚 Envío GRATIS a toda Colombia</p>
        <p style="color:var(--green);font-weight:600;margin-bottom:16px;">📦 Pago contraentrega disponible</p>

        <div style="margin:20px 0;">
            <p style="font-weight:700;margin-bottom:8px;">Elige cómo pagar:</p>
            <div class="payment-options" id="paymentOptions">
                <div class="payment-option active" onclick="selectPayment(this)">📦<br>Contraentrega</div>
                <div class="payment-option" onclick="selectPayment(this)">💳<br>MercadoPago</div>
                <div class="payment-option" onclick="selectPayment(this)">🏦<br>PSE</div>
                <div class="payment-option" onclick="selectPayment(this)">📱<br>Nequi</div>
            </div>
        </div>

        <form class="checkout-form" id="orderForm">
            <input type="text" placeholder="Nombre completo" required>
            <input type="tel" placeholder="WhatsApp / Celular" required>
            <input type="text" placeholder="Ciudad" required>
            <input type="text" placeholder="Dirección" required>
            <input type="text" placeholder="Barrio (opcional)">
            <button type="submit" class="btn-primary">✅ CONFIRMAR PEDIDO — $87.900</button>
            <p style="font-size:.75rem;color:var(--gray);margin-top:8px;">Te contactaremos por WhatsApp para confirmar cobertura y tiempo de entrega.</p>
        </form>

        <div class="divider">o si prefieres</div>
        <a href="https://wa.me/573186606067?text=Hola!%20Quiero%20comprar%20Simply%20Straight" class="btn-wa">💬 Comprar directamente por WhatsApp</a>
    </div>
</section>

<section class="section container">
    <div class="guarantee-seal">
        <div class="seal">🛡️</div>
        <h3 style="margin-bottom:8px;">Garantía Simply Straight</h3>
        <p style="font-size:.85rem;">Si el producto llega con falla de fábrica, te lo cambiamos. Solo escríbenos por WhatsApp con foto o video y te guiamos paso a paso.</p>
        <p style="font-size:.85rem;margin-top:6px;">Además, por ser compra online en Colombia, tienes derecho de retracto de 5 días hábiles desde que lo recibes. Sin preguntas.</p>
        <p style="font-size:.8rem;color:var(--gray);margin-top:8px;">No tienes nada que perder. Si no te gusta, no te quedas con él.</p>
    </div>
</section>

<section class="section container">
    <h2 class="section-title">Preguntas frecuentes</h2>
    <div class="faq-item"><p class="faq-q">¿Llega a todo Colombia?</p><p class="faq-a">Sí. Ciudades principales: 2-5 días hábiles. Otros municipios: 3-7 días. Te confirmamos el tiempo exacto al hacer tu pedido.</p></div>
    <div class="faq-item"><p class="faq-q">¿Cómo funciona la contraentrega?</p><p class="faq-a">Recibes el producto en tu casa, lo abres, lo revisas, y SOLO AHÍ pagas. Si algo no te convence, no pagas y listo. Sin riesgo.</p></div>
    <div class="faq-item"><p class="faq-q">¿Sirve para cabello crespo o afro?</p><p class="faq-a">Ayuda a reducir el frizz y ordenar. En cabello muy crespo o afro el acabado es más natural que liso extremo. No reemplaza un alisado químico.</p></div>
    <div class="faq-item"><p class="faq-q">¿Qué incluye la caja?</p><p class="faq-a">El cepillo Simply Straight, cable de alimentación y manual de uso en español.</p></div>
    <div class="faq-item"><p class="faq-q">¿Es voltaje universal?</p><p class="faq-a">Sí. 110V-220V. Funciona en toda Colombia sin necesidad de transformador.</p></div>
    <div class="faq-item"><p class="faq-q">¿Cuánto dura?</p><p class="faq-a">Con uso normal, años. Tiene auto apagado de seguridad y materiales de calidad.</p></div>
</section>

<div class="fixed-cta">
    <a href="#comprar" class="btn-primary" style="flex:2;">$87.900 — PEDIR AHORA</a>
    <a href="https://wa.me/573186606067" class="btn-outline" style="flex:1;font-size:.8rem;">💬 WhatsApp</a>
</div>

<script>
function selectPayment(el) {
    document.querySelectorAll('.payment-option').forEach(o => o.classList.remove('active'));
    el.classList.add('active');
}
document.getElementById('orderForm').addEventListener('submit', function(e) {
    e.preventDefault();
    var inputs = this.querySelectorAll('input');
    var msg = 'Hola! Quiero comprar Simply Straight.\\nNombre: ' + inputs[0].value + '\\nCelular: ' + inputs[1].value + '\\nCiudad: ' + inputs[2].value + '\\nDireccion: ' + inputs[3].value + '\\nBarrio: ' + (inputs[4].value || '-');
    var payEl = document.querySelector('.payment-option.active');
    var pay = payEl ? payEl.innerText.trim().split('\\n')[0] : 'Contraentrega';
    msg += '\\nPago: ' + pay;
    window.open('https://wa.me/573186606067?text=' + encodeURIComponent(msg), '_blank');
});
</script>

</body>
</html>"""

with open(r'C:\Users\artur\proyectos\dropi\simply-straight\index-v2.html', 'w', encoding='utf-8') as f:
    f.write(html)
print('OK: index-v2.html written')
