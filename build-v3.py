#!/usr/bin/env python3
"""Build the definitive Simply Straight landing page."""

html = r"""<!DOCTYPE html>
<html lang="es">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0, maximum-scale=1.0, user-scalable=no">
<meta name="description" content="Simply Straight — Cepillo alisador de cerámica 3D. Reduce el frizz en minutos. Envío gratis a Colombia. Pago contraentrega.">
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

<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Playfair+Display:wght@400;500;600;700;800&family=Inter:wght@300;400;500;600;700;800&display=swap" rel="stylesheet">

<style>
:root {
    --cream: #f9f4ef;
    --white: #ffffff;
    --black: #111111;
    --charcoal: #1c1c1c;
    --rose: #b8695a;
    --rose-dark: #9b4d3f;
    --rose-light: #f6e8e3;
    --gold: #c8a97e;
    --gold-light: #faf5ee;
    --green: #4a7c59;
    --green-light: #eaf2ec;
    --gray-50: #fafafa;
    --gray-100: #f4f4f5;
    --gray-200: #e5e5e7;
    --gray-400: #a1a1aa;
    --gray-500: #71717a;
    --gray-600: #52525b;
    --red: #dc2626;
    --red-light: #fef2f2;
    --shadow-sm: 0 1px 3px rgba(0,0,0,0.06);
    --shadow: 0 4px 16px rgba(0,0,0,0.06);
    --shadow-lg: 0 12px 40px rgba(0,0,0,0.08);
    --radius: 14px;
    --radius-sm: 10px;
    --max-w: 500px;
}

* { margin: 0; padding: 0; box-sizing: border-box; }
html { scroll-behavior: smooth; }
body {
    font-family: 'Inter', -apple-system, sans-serif;
    background: var(--cream);
    color: var(--black);
    line-height: 1.65;
    -webkit-font-smoothing: antialiased;
    -moz-osx-font-smoothing: grayscale;
    font-size: 17px;
}

.container { max-width: var(--max-w); margin: 0 auto; padding: 0 20px; }

/* ========== URGENCY BAR ========== */
.urgency-bar {
    background: var(--charcoal);
    color: var(--white);
    text-align: center;
    padding: 10px 16px;
    font-size: 13px;
    font-weight: 600;
    letter-spacing: 0.3px;
    position: sticky;
    top: 0;
    z-index: 1000;
}
.urgency-bar .dot { color: var(--rose); margin: 0 6px; }

/* ========== NAV ========== */
.nav {
    display: flex;
    justify-content: space-between;
    align-items: center;
    padding: 14px 20px;
    background: var(--white);
    border-bottom: 1px solid var(--gray-200);
    max-width: var(--max-w);
    margin: 0 auto;
}
.nav-logo { font-family: 'Playfair Display', serif; font-size: 20px; font-weight: 700; letter-spacing: -0.3px; }
.nav-logo .dot { color: var(--rose); }
.nav-cta {
    background: var(--rose);
    color: var(--white) !important;
    padding: 8px 16px;
    border-radius: 20px;
    font-size: 13px;
    font-weight: 600;
    text-decoration: none;
    transition: background 0.2s;
}
.nav-cta:hover { background: var(--rose-dark); }

/* ========== HERO ========== */
.hero {
    background: var(--white);
    padding: 0 0 32px;
    text-align: center;
}
.hero-video-wrap {
    position: relative;
    width: 100%;
    aspect-ratio: 1/1;
    max-height: 500px;
    overflow: hidden;
    background: var(--gray-100);
}
.hero-video-wrap video {
    width: 100%;
    height: 100%;
    object-fit: cover;
}
.hero-video-overlay {
    position: absolute;
    bottom: 16px;
    left: 50%;
    transform: translateX(-50%);
    background: rgba(0,0,0,0.7);
    color: white;
    padding: 8px 18px;
    border-radius: 20px;
    font-size: 12px;
    font-weight: 600;
    letter-spacing: 0.5px;
    backdrop-filter: blur(4px);
}
.hero-content { padding: 28px 20px 0; max-width: var(--max-w); margin: 0 auto; }
.hero-badge {
    display: inline-block;
    background: var(--rose-light);
    color: var(--rose-dark);
    font-size: 11px;
    font-weight: 700;
    text-transform: uppercase;
    letter-spacing: 1.5px;
    padding: 6px 16px;
    border-radius: 20px;
    margin-bottom: 14px;
}
.hero h1 {
    font-family: 'Playfair Display', serif;
    font-size: 42px;
    font-weight: 700;
    line-height: 1.1;
    margin-bottom: 10px;
    letter-spacing: -0.5px;
}
.hero h1 .rose { color: var(--rose); }
.hero h1 .italic { font-style: italic; }
.hero-sub {
    color: var(--gray-500);
    font-size: 16px;
    line-height: 1.5;
    margin-bottom: 20px;
    max-width: 380px;
    margin-left: auto;
    margin-right: auto;
}

/* Stats row */
.stats-row {
    display: flex;
    justify-content: center;
    gap: 28px;
    margin-bottom: 20px;
}
.stat-item { text-align: center; }
.stat-num { font-size: 26px; font-weight: 800; color: var(--rose-dark); }
.stat-label { font-size: 12px; color: var(--gray-400); text-transform: uppercase; letter-spacing: 1px; margin-top: 2px; }

/* Price */
.price-hero { margin-bottom: 18px; }
.price-hero .old {
    color: var(--gray-400);
    text-decoration: line-through;
    font-size: 18px;
    margin-right: 8px;
}
.price-hero .now {
    font-size: 46px;
    font-weight: 800;
    color: var(--black);
    letter-spacing: -1px;
}
.price-hero .save {
    display: inline-block;
    background: var(--green-light);
    color: var(--green);
    font-size: 14px;
    font-weight: 700;
    padding: 5px 10px;
    border-radius: 6px;
    margin-left: 10px;
    vertical-align: super;
}

/* CTA buttons */
.btn-block { display: block; width: 100%; padding: 16px; font-size: 16px; font-weight: 700; border-radius: var(--radius-sm); text-align: center; text-decoration: none; cursor: pointer; border: none; font-family: inherit; transition: all 0.2s; }
.btn-black { background: var(--charcoal); color: white; margin-bottom: 10px; }
.btn-black:hover { background: #000; }
.btn-outline { background: white; color: var(--black); border: 2px solid var(--gray-200); }
.btn-outline:hover { border-color: var(--black); }
.btn-rose { background: var(--rose); color: white; }
.btn-rose:hover { background: var(--rose-dark); }

.cta-row { display: flex; gap: 10px; }
.cta-row .btn-block { flex: 1; }

/* ========== TRUST STRIP ========== */
.trust-strip {
    display: flex;
    justify-content: center;
    flex-wrap: wrap;
    gap: 18px;
    padding: 20px 0;
    background: var(--gray-50);
    font-size: 13px;
    color: var(--gray-600);
    font-weight: 600;
    letter-spacing: 0.2px;
}
.trust-strip span { display: flex; align-items: center; gap: 5px; }
.trust-strip .green { color: var(--green); font-weight: 700; }

/* ========== SECTIONS ========== */
.section { padding: 44px 0; }
.section-sm { padding: 28px 0; }
.section-bg { background: var(--white); }
.section-dark { background: var(--charcoal); color: var(--white); }

.section-eyebrow {
    font-size: 11px;
    font-weight: 700;
    text-transform: uppercase;
    letter-spacing: 1.5px;
    color: var(--rose-dark);
    margin-bottom: 10px;
    text-align: center;
}
.section-title {
    font-family: 'Playfair Display', serif;
    font-size: 32px;
    font-weight: 700;
    line-height: 1.2;
    margin-bottom: 10px;
    text-align: center;
}
.section-sub {
    color: var(--gray-500);
    font-size: 16px;
    text-align: center;
    margin-bottom: 28px;
    max-width: 400px;
    margin-left: auto;
    margin-right: auto;
    line-height: 1.5;
}

/* ========== PROBLEM ========== */
.problem-quote {
    background: var(--white);
    border-left: 3px solid var(--rose);
    padding: 16px 18px;
    border-radius: 0 var(--radius-sm) var(--radius-sm) 0;
    font-style: italic;
    color: var(--gray-600);
    font-size: 14px;
    margin-bottom: 10px;
    box-shadow: var(--shadow-sm);
}

/* ========== FEATURES GRID ========== */
.features-grid {
    display: grid;
    grid-template-columns: 1fr 1fr;
    gap: 14px;
}
.feature-card {
    background: var(--white);
    border-radius: var(--radius);
    padding: 20px 16px;
    text-align: center;
    box-shadow: var(--shadow-sm);
    border: 1px solid var(--gray-100);
    transition: transform 0.2s, box-shadow 0.2s;
}
.feature-card:hover { transform: translateY(-2px); box-shadow: var(--shadow); }
.feature-icon { font-size: 30px; margin-bottom: 10px; display: block; }
.feature-card h4 { font-size: 14px; font-weight: 700; margin-bottom: 4px; }
.feature-card p { font-size: 12px; color: var(--gray-500); line-height: 1.4; }

/* ========== STEPS ========== */
.steps-list { display: flex; flex-direction: column; gap: 16px; }
.step-item { display: flex; align-items: flex-start; gap: 16px; background: var(--white); padding: 18px; border-radius: var(--radius); box-shadow: var(--shadow-sm); border: 1px solid var(--gray-100); }
.step-circle { flex-shrink: 0; width: 44px; height: 44px; background: var(--rose-light); color: var(--rose-dark); border-radius: 50%; display: flex; align-items: center; justify-content: center; font-weight: 800; font-size: 18px; }
.step-text h3 { font-size: 16px; font-weight: 700; margin-bottom: 3px; }
.step-text p { font-size: 13px; color: var(--gray-500); }

/* ========== HONEST SECTION ========== */
.honest-section {
    background: var(--rose-light);
    border-radius: var(--radius);
    padding: 28px 22px;
    border: 1px solid rgba(0,0,0,0.03);
}
.honest-section .section-title { color: var(--rose-dark); text-align: left; font-size: 22px; }
.honest-table { width: 100%; font-size: 13px; border-collapse: collapse; margin-top: 12px; }
.honest-table td { padding: 10px 8px; border-bottom: 1px solid rgba(0,0,0,0.05); }
.honest-table td:first-child { font-weight: 600; width: 45%; font-size: 12px; }
.honest-table td:last-child { color: var(--gray-600); }
.honest-note { font-size: 11px; color: var(--gray-400); margin-top: 10px; font-style: italic; }

/* ========== COMPARISON ========== */
.comp-table { width: 100%; font-size: 13px; border-collapse: collapse; background: var(--white); border-radius: var(--radius); overflow: hidden; box-shadow: var(--shadow-sm); }
.comp-table th { background: var(--charcoal); color: white; padding: 12px 10px; font-size: 12px; font-weight: 600; text-align: center; }
.comp-table th:first-child { text-align: left; padding-left: 16px; }
.comp-table td { padding: 12px 10px; text-align: center; border-bottom: 1px solid var(--gray-100); }
.comp-table td:first-child { text-align: left; font-weight: 600; padding-left: 16px; }
.comp-table .win { color: var(--green); font-weight: 700; }
.comp-table tr:last-child td { border-bottom: none; }

/* ========== TESTIMONIALS ========== */
.testimonials-scroll {
    display: flex;
    overflow-x: auto;
    gap: 14px;
    padding-bottom: 8px;
    -webkit-overflow-scrolling: touch;
    scroll-snap-type: x mandatory;
}
.testimonials-scroll::-webkit-scrollbar { display: none; }
.testimonial-card {
    flex: 0 0 280px;
    background: var(--white);
    border-radius: var(--radius);
    padding: 20px;
    box-shadow: var(--shadow-sm);
    border: 1px solid var(--gray-100);
    scroll-snap-align: start;
}
.testimonial-stars { color: var(--gold); font-size: 12px; margin-bottom: 8px; letter-spacing: 2px; }
.testimonial-body { font-size: 16px; color: var(--gray-600); font-style: italic; line-height: 1.5; margin-bottom: 12px; }
.testimonial-author { font-size: 16px; font-weight: 700; }
.testimonial-city { font-size: 12px; color: var(--gray-400); }
.testimonial-tag { display: inline-block; font-size: 10px; background: var(--green-light); color: var(--green); padding: 2px 8px; border-radius: 10px; margin-top: 6px; }

/* ========== CHECKOUT ========== */
.checkout-card {
    background: var(--white);
    border-radius: var(--radius);
    padding: 28px 22px;
    box-shadow: var(--shadow-lg);
    border: 2px solid var(--gray-200);
}
.checkout-card .section-title { text-align: center; margin-bottom: 4px; }

.payment-tabs { display: flex; gap: 6px; margin: 20px 0 16px; flex-wrap: wrap; }
.payment-tab {
    flex: 1;
    min-width: 75px;
    padding: 12px 8px;
    border: 2px solid var(--gray-200);
    border-radius: var(--radius-sm);
    text-align: center;
    cursor: pointer;
    font-size: 12px;
    font-weight: 600;
    background: var(--white);
    transition: all 0.15s;
    font-family: inherit;
}
.payment-tab.active { border-color: var(--charcoal); background: var(--gray-100); }
.payment-tab:hover { border-color: var(--rose); }
.payment-tab .emoji { display: block; font-size: 20px; margin-bottom: 3px; }

.checkout-form { }
.checkout-form .field {
    width: 100%;
    padding: 15px 16px;
    border: 2px solid var(--gray-200);
    border-radius: var(--radius-sm);
    font-size: 16px;
    margin-bottom: 10px;
    font-family: inherit;
    background: var(--gray-50);
    transition: border-color 0.2s;
}
.checkout-form .field:focus { border-color: var(--rose); outline: none; background: var(--white); }
.checkout-row { display: flex; gap: 8px; }
.checkout-row .field { flex: 1; }

.submit-btn {
    width: 100%;
    padding: 16px;
    background: var(--charcoal);
    color: white;
    border: none;
    border-radius: var(--radius-sm);
    font-size: 16px;
    font-weight: 700;
    cursor: pointer;
    font-family: inherit;
    margin-top: 4px;
    transition: background 0.2s;
}
.submit-btn:hover { background: #000; }
.submit-note { font-size: 11px; color: var(--gray-400); text-align: center; margin-top: 10px; }
.submit-note a { color: var(--rose-dark); text-decoration: underline; }

/* ========== GUARANTEE ========== */
.guarantee-box {
    background: var(--green-light);
    border-radius: var(--radius);
    padding: 28px 22px;
    text-align: center;
    border: 1px solid rgba(0,0,0,0.03);
}
.guarantee-icon { font-size: 42px; margin-bottom: 10px; }
.guarantee-box h3 { font-size: 18px; font-weight: 700; margin-bottom: 8px; color: var(--green); }
.guarantee-box p { font-size: 13px; color: var(--gray-600); line-height: 1.5; }

/* ========== FAQ ACCORDION ========== */
.faq-list { display: flex; flex-direction: column; gap: 8px; }
.faq-item {
    background: var(--white);
    border-radius: var(--radius-sm);
    overflow: hidden;
    border: 1px solid var(--gray-100);
}
.faq-q {
    width: 100%;
    text-align: left;
    padding: 16px 18px;
    font-size: 16px;
    font-weight: 600;
    background: var(--white);
    border: none;
    cursor: pointer;
    font-family: inherit;
    display: flex;
    justify-content: space-between;
    align-items: center;
    color: var(--black);
}
.faq-q::after { content: '+'; font-size: 20px; color: var(--gray-400); font-weight: 300; transition: transform 0.2s; }
.faq-q.open::after { content: '−'; color: var(--rose-dark); }
.faq-a {
    max-height: 0;
    overflow: hidden;
    transition: max-height 0.3s ease, padding 0.3s ease;
    font-size: 13px;
    color: var(--gray-500);
    padding: 0 18px;
    line-height: 1.5;
}
.faq-a.open { max-height: 200px; padding: 0 18px 14px; }

/* ========== FLOATING WHATSAPP ========== */
.float-wa {
    position: fixed;
    bottom: 24px;
    right: 24px;
    z-index: 999;
    width: 56px;
    height: 56px;
    background: #25D366;
    border-radius: 50%;
    box-shadow: 0 4px 20px rgba(37,211,102,0.4);
    display: flex;
    align-items: center;
    justify-content: center;
    text-decoration: none;
    transition: transform 0.2s, box-shadow 0.2s;
    animation: float 2s ease-in-out infinite;
}
.float-wa:hover { transform: scale(1.08); box-shadow: 0 6px 28px rgba(37,211,102,0.5); }
.float-wa svg { width: 28px; height: 28px; fill: white; }
@keyframes float { 0%,100%{transform:translateY(0)} 50%{transform:translateY(-6px)} }

/* ========== STICKY CTA ========== */
.sticky-cta {
    position: fixed;
    bottom: 0;
    left: 0;
    right: 0;
    background: var(--white);
    padding: 12px 20px;
    box-shadow: 0 -4px 20px rgba(0,0,0,0.08);
    display: flex;
    gap: 10px;
    align-items: center;
    z-index: 100;
}
.sticky-cta .price-info { flex: 1; }
.sticky-cta .price-amount { font-size: 20px; font-weight: 800; }
.sticky-cta .price-label { font-size: 10px; color: var(--green); font-weight: 600; }
.sticky-cta .btn-black { margin: 0; padding: 14px 24px; font-size: 14px; white-space: nowrap; }

/* ========== RESPONSIVE ========== */
@media (max-width: 360px) {
    .hero h1 { font-size: 30px; }
    .price-hero .now { font-size: 34px; }
    .features-grid { grid-template-columns: 1fr; }
    .section-title { font-size: 24px; }
    .testimonial-card { flex: 0 0 250px; }
}
</style>
</head>
<body>

<!-- URGENCY -->
<div class="urgency-bar" id="urgencyBar">
    🔥 SOLO <span id="stockCounter">19</span> UNIDADES DISPONIBLES · OFERTA TERMINA EN <span id="countdown">29h 59m 59s</span> · ENVÍO GRATIS
</div>

<!-- SOCIAL PROOF TOAST -->
<div id="socialToast" style="position:fixed;bottom:100px;left:16px;right:16px;z-index:999;max-width:var(--max-w);margin:0 auto;pointer-events:none;">
    <div id="toastInner" style="background:var(--charcoal);color:white;padding:12px 16px;border-radius:12px;font-size:12px;font-weight:500;display:none;align-items:center;gap:10px;box-shadow:0 8px 24px rgba(0,0,0,.15);transition:opacity .3s;">
        <span style="font-size:18px;">📦</span>
        <span id="toastMsg"></span>
        <span style="font-size:10px;color:var(--gray-400);" id="toastTime"></span>
    </div>
</div>

<!-- HERO -->
<section class="hero">
    <div class="hero-content">
        <div class="hero-badge">El cepillo que Colombia estaba esperando</div>
        <h1>Despierta y <span class="rose italic">ya está lista.</span></h1>
        <p class="hero-sub">Reduce el frizz y peina tu cabello en minutos desde casa. Sin plancha, sin cremas, sin drama.</p>
    </div>

    <!-- Social Proof Row -->
    <div style="display:flex;align-items:center;justify-content:center;gap:12px;padding:0 20px 16px;max-width:var(--max-w);margin:0 auto;">
        <div style="flex:1;text-align:center;">
            <p style="font-size:12px;font-style:italic;color:var(--gray-500);margin-bottom:4px;">'Finalmente algo que funciona' 😍</p>
            <p style="font-size:11px;font-weight:600;color:var(--gray-600);">— Valentina, Medellín</p>
        </div>
        <div style="flex-shrink:0;text-align:center;">
            <!-- Image Carousel -->
            <div style="position:relative;width:220px;height:220px;margin:0 auto;">
                <div id="heroCarousel" style="position:relative;width:100%;height:100%;overflow:hidden;border-radius:16px;box-shadow:var(--shadow-lg);">
                    <img src="creativos/carrusel-1-ritual.png" class="carousel-slide active" style="position:absolute;top:0;left:0;width:100%;height:100%;object-fit:cover;border-radius:16px;opacity:1;transition:opacity 0.5s;">
                    <img src="creativos/carrusel-2-jardin.png" class="carousel-slide" style="position:absolute;top:0;left:0;width:100%;height:100%;object-fit:cover;border-radius:16px;opacity:0;transition:opacity 0.5s;">
                    <img src="creativos/carrusel-3-minimalista.png" class="carousel-slide" style="position:absolute;top:0;left:0;width:100%;height:100%;object-fit:cover;border-radius:16px;opacity:0;transition:opacity 0.5s;">
                    <img src="creativos/carrusel-4-producto.png" class="carousel-slide" style="position:absolute;top:0;left:0;width:100%;height:100%;object-fit:cover;border-radius:16px;opacity:0;transition:opacity 0.5s;">
                </div>
                <!-- Dots -->
                <div style="display:flex;justify-content:center;gap:6px;margin-top:8px;">
                    <span class="carousel-dot active" onclick="goToSlide(0)" style="width:8px;height:8px;border-radius:50%;background:var(--rose-dark);cursor:pointer;"></span>
                    <span class="carousel-dot" onclick="goToSlide(1)" style="width:8px;height:8px;border-radius:50%;background:var(--gray-200);cursor:pointer;"></span>
                    <span class="carousel-dot" onclick="goToSlide(2)" style="width:8px;height:8px;border-radius:50%;background:var(--gray-200);cursor:pointer;"></span>
                    <span class="carousel-dot" onclick="goToSlide(3)" style="width:8px;height:8px;border-radius:50%;background:var(--gray-200);cursor:pointer;"></span>
                </div>
                <div style="position:absolute;bottom:-20px;left:50%;transform:translateX(-50%);background:var(--rose-dark);color:white;padding:5px 16px;border-radius:14px;font-size:13px;font-weight:700;z-index:10;white-space:nowrap;">+500 vendidos ✨</div>
            </div>
        </div>
        <div style="flex:1;text-align:center;">
            <p style="font-size:12px;font-style:italic;color:var(--gray-500);margin-bottom:4px;">'Es mágico, amiga' ✨</p>
            <p style="font-size:11px;font-weight:600;color:var(--gray-600);">— Sofía, Cali</p>
        </div>
    </div>

    <!-- Video tagline -->
    <div style="text-align:center;padding:0 20px 20px;">
        <span style="background:var(--gray-100);color:var(--gray-600);padding:6px 16px;border-radius:20px;font-size:12px;font-weight:600;">▶ Desliza para ver resultados reales</span>
    </div>

    <div class="hero-content" style="padding-top:0;">
        <div class="stats-row">
            <div class="stat-item"><div class="stat-num">+500</div><div class="stat-label">Vendidos</div></div>
            <div class="stat-item"><div class="stat-num">4.8 ★</div><div class="stat-label">Estrellas</div></div>
            <div class="stat-item"><div class="stat-num">60s</div><div class="stat-label">Resultado</div></div>
        </div>

        <div style="display:flex;justify-content:center;gap:16px;margin-bottom:18px;font-size:12px;color:var(--gray-500);">
            <span>👁️ <strong id="viewerCount" style="color:var(--rose-dark);">12</strong> personas viendo</span>
            <span>🔥 <strong id="soldToday" style="color:var(--rose-dark);">23</strong> vendidos hoy</span>
        </div>

        <div class="price-hero">
            <span class="old">$1219.900</span>
            <span class="now">$819.900</span>
            <span class="save">AHORRAS $40.000</span>
        </div>

        <a href="#comprar" class="btn-block btn-black">🛒 QUIERO EL MÍO — ENVÍO GRATIS</a>
        <a href="https://wa.me/573186606067" class="btn-block btn-outline">💬 Preguntar por WhatsApp</a>
    </div>
</section>

<!-- TRUST STRIP -->
<div class="trust-strip">
    <span>🚚 <span class="green">Envío gratis</span></span>
    <span>📦 Contraentrega</span>
    <span>🛡️ Garantía</span>
    <span>💬 WhatsApp real</span>
    <span>🇨🇴 Colombia</span>
</div>

<!-- PROBLEM -->
<section class="section section-bg">
    <div class="container">
        <div class="section-eyebrow">El problema</div>
        <h2 class="section-title">¿Tu cabello amanece así?</h2>
        <p class="section-sub" style="color: var(--gray-600);">Frizz, encrespado, sin forma. Antes de salir: plancha, crema, sérum. 40 minutos después, tal vez. Y al mediodía, el frizz vuelve.</p>
        <div class="problem-quote">"Me tocaba lavarme el pelo en la noche y rezar que amaneciera presentable. Si no, plancha obligada. 30 minutos fácil cada mañana."</div>
        <p style="text-align:center;font-weight:600;font-size:14px;margin-top:16px;">No es tu culpa. Es la humedad y tu tipo de cabello. Pero sí hay algo que puedes hacer.</p>
    </div>
</section>

<!-- DEMO -->
<section class="section-sm">
    <div class="container">
        <video autoplay loop muted playsinline poster="creativos/antes y despues/1.png" style="width:100%;border-radius:var(--radius);box-shadow:var(--shadow-lg);" onclick="this.play()">
            <source src="creativos/CAMPAÑA-FINAL-SUBS.mp4" type="video/mp4">
        </video>
        <p style="text-align:center;font-size:12px;color:var(--gray-400);margin-top:8px;">Mujer real. Cabello real. Sin filtro ni edición.</p>
    </div>
</section>

<!-- BENEFITS -->
<section class="section">
    <div class="container">
        <div class="section-eyebrow">La solución</div>
        <h2 class="section-title">Peina y alisa al mismo tiempo</h2>
        <p class="section-sub">Simplemente el cepillo que necesitas. Cerámica 3D con temperatura controlada.</p>
        <div class="features-grid">
            <div class="feature-card"><span class="feature-icon">⚡</span><h4>En minutos</h4><p>Baja el frizz y peina el cabello rápidamente</p></div>
            <div class="feature-card"><span class="feature-icon">🔒</span><h4>Auto apagado</h4><p>Se apaga solo si te olvidas de desconectarlo</p></div>
            <div class="feature-card"><span class="feature-icon">🌡️</span><h4>Temperatura ajustable</h4><p>Elige el calor ideal para tu tipo de cabello</p></div>
            <div class="feature-card"><span class="feature-icon">💎</span><h4>Cerámica 3D real</h4><p>Distribuye el calor uniformemente por cada mechón</p></div>
            <div class="feature-card"><span class="feature-icon">📱</span><h4>Pantalla digital</h4><p>Control preciso de la temperatura en tiempo real</p></div>
            <div class="feature-card"><span class="feature-icon">🔌</span><h4>110V-220V</h4><p>Voltaje universal. Funciona en toda Colombia</p></div>
        </div>
    </div>
</section>

<!-- HOW IT WORKS -->
<section class="section section-bg">
    <div class="container">
        <div class="section-eyebrow">Así de simple</div>
        <h2 class="section-title">Tu rutina en 3 pasos</h2>
        <div class="steps-list">
            <div class="step-item"><div class="step-circle">1</div><div class="step-text"><h3>Conéctalo</h3><p>Enchúfalo, enciéndelo y selecciona la temperatura deseada en la pantalla digital. Espera unos segundos a que caliente.</p></div></div>
            <div class="step-item"><div class="step-circle">2</div><div class="step-text"><h3>Pásalo</h3><p>Separa el cabello por mechones. Pásalo de raíz a puntas como si fuera un cepillo normal. Sin apretar.</p></div></div>
            <div class="step-item"><div class="step-circle">3</div><div class="step-text"><h3>Lista</h3><p>En minutos tienes el cabello más ordenado, con menos frizz y lista para salir. Sin dañarlo.</p></div></div>
        </div>
    </div>
</section>

<!-- HONEST SECTION -->
<section class="section">
    <div class="container">
        <div class="honest-section">
            <div class="section-eyebrow" style="text-align:left;">Sé realista</div>
            <h2 class="section-title" style="font-size:22px;margin-bottom:6px;">Antes de comprar, mira esto</h2>
            <p style="font-size:13px;color:var(--gray-600);margin-bottom:10px;">Queremos que sepas EXACTAMENTE qué esperar. Nada de promesas falsas.</p>
            <table class="honest-table">
                <tr><td>Cabello ondulado</td><td>✅ Resultado alto. Baja el frizz y define.</td></tr>
                <tr><td>Cabello con frizz</td><td>✅ Muy efectivo para control visual.</td></tr>
                <tr><td>Cabello grueso/abundante</td><td>✅ Funciona. Usar secciones pequeñas.</td></tr>
                <tr><td>Cabello muy crespo/afro</td><td>⚠️ Acabado más natural. No es keratina.</td></tr>
                <tr><td>¿Reemplaza keratina?</td><td>❌ No. No es un tratamiento químico.</td></tr>
                <tr><td>¿Se puede usar mojado?</td><td>❌ No. El cabello debe estar seco.</td></tr>
            </table>
            <p class="honest-note">💡 Recomendamos usar protector térmico antes de aplicar calor. Como con cualquier producto de calor.</p>
        </div>
    </div>
</section>

<!-- COMPARISON -->
<section class="section section-bg">
    <div class="container">
        <div class="section-eyebrow">Comparativa</div>
        <h2 class="section-title">Simply Straight vs el resto</h2>
        <table class="comp-table">
            <tr><th></th><th>Simply Straight</th><th>Plancha</th><th>Peluquería</th></tr>
            <tr><td>Tiempo</td><td class="win">Minutos</td><td>30-40 min</td><td>1-2 horas</td></tr>
            <tr><td>Costo</td><td class="win">$819.900 una vez</td><td>$80-150K + cremas</td><td>$30-80K por visita</td></tr>
            <tr><td>Daño</td><td class="win">Temp. controlada</td><td>Calor directo</td><td>Químicos</td></tr>
            <tr><td>Dónde</td><td class="win">En tu casa</td><td>En tu casa</td><td>Fuera de casa</td></tr>
            <tr><td>Garantía</td><td class="win">✅ Sí</td><td>Depende</td><td>No aplica</td></tr>
        </table>
    </div>
</section>

<!-- TESTIMONIALS -->
<section class="section">
    <div class="container">
        <div class="section-eyebrow">Resultados reales</div>
        <h2 class="section-title">Mujeres reales. Cabello real.</h2>
        <div class="testimonials-scroll">
            <div class="testimonial-card">
                <div class="testimonial-stars">★★★★★</div>
                <div class="testimonial-body">"Lo pedí para Cali, me llegó al tercer día. Tengo cabello abundante y con frizz. No reemplaza keratina, pero me deja el pelo más ordenado para salir rápido. Pagué contraentrega."</div>
                <div class="testimonial-author">Valentina G.</div>
                <div class="testimonial-city">Cali, Valle</div>
                <div class="testimonial-tag">✅ Contraentrega</div>
            </div>
            <div class="testimonial-card">
                <div class="testimonial-stars">★★★★★</div>
                <div class="testimonial-body">"Mi pelo es grueso y con la humedad de Barranquilla se infla horrible. Con Simply Straight en 7 minutos estoy lista. El cambio es real. Mis amigas ya me pidieron el link."</div>
                <div class="testimonial-author">Daniela R.</div>
                <div class="testimonial-city">Barranquilla, Atlántico</div>
                <div class="testimonial-tag">✅ Cabello grueso</div>
            </div>
            <div class="testimonial-card">
                <div class="testimonial-stars">★★★★★</div>
                <div class="testimonial-body">"Pensé que era mentira hasta que lo probé. Lo uso cada mañana antes del trabajo y me ahorra 20 minutos fácil. Ya no dependo de la plancha."</div>
                <div class="testimonial-author">Carolina M.</div>
                <div class="testimonial-city">Bogotá, Cundinamarca</div>
                <div class="testimonial-tag">✅ Ahorro de tiempo</div>
            </div>
            <div class="testimonial-card">
                <div class="testimonial-stars">★★★★★</div>
                <div class="testimonial-body">"Pedí contraentrega porque me daba miedo. Llegó en 4 días a Medellín. El cepillo es igual al del video, la pantalla funciona perfecto. Lo recomiendo."</div>
                <div class="testimonial-author">Sofía L.</div>
                <div class="testimonial-city">Medellín, Antioquia</div>
                <div class="testimonial-tag">✅ Primera compra</div>
            </div>
        </div>
    </div>
</section>

<!-- BUY SECTION -->
<section class="section section-bg" id="comprar">
    <div class="container">
        <div class="checkout-card">
            <div class="section-eyebrow">Oferta de lanzamiento</div>
            <h2 class="section-title">Simplemente pídelo</h2>
            <p style="text-align:center;color:var(--gray-500);font-size:14px;margin-bottom:10px;">Cepillo alisador de cerámica 3D</p>

            <div class="price-hero" style="text-align:center;">
                <span class="old">$1219.900</span>
                <span class="now">$819.900</span><br>
                <span class="save" style="margin-left:0;margin-top:6px;">AHORRAS $40.000 HOY</span>
            </div>

            <p style="text-align:center;color:var(--green);font-weight:600;font-size:13px;margin-bottom:4px;">🚚 Envío GRATIS a toda Colombia</p>
            <p style="text-align:center;color:var(--green);font-weight:600;font-size:13px;margin-bottom:16px;">📦 Pago <strong>contraentrega</strong> disponible</p>
            <div style="margin:20px 0;">
                    <p style="font-weight:700;margin-bottom:8px;">Cantidad:</p>
                    <div class="payment-tabs" id="qtyTabs" style="margin-bottom:16px;">
                        <div class="payment-tab active" onclick="selectQty(this,1,119900)" style="flex-direction:column;">
                            <span style="font-weight:800;font-size:15px;">1 unidad</span>
                            <span style="font-size:11px;">$819.900</span>
                        </div>
                        <div class="payment-tab" onclick="selectQty(this,2,99900)" style="flex-direction:column;border-color:var(--rose-light);">
                            <span style="font-weight:800;font-size:15px;">2 unidades</span>
                            <span style="font-size:11px;">$79.900 c/u</span>
                            <span style="font-size:9px;color:var(--green);">AHORRAS $29.800</span>
                        </div>
                        <div class="payment-tab" onclick="selectQty(this,3,89900)" style="flex-direction:column;border-color:var(--gold);">
                            <span style="font-weight:800;font-size:15px;">3 unidades</span>
                            <span style="font-size:11px;">$69.900 c/u</span>
                            <span style="font-size:9px;color:var(--green);">AHORRAS $65.700</span>
                            <span style="font-size:8px;background:var(--gold-light);color:var(--gold);padding:1px 6px;border-radius:8px;margin-top:2px;">MÁS VENDIDO</span>
                        </div>
                    </div>
                </div>

                <p style="font-weight:700;font-size:14px;margin-bottom:8px;">Elige cómo pagar:</p>
            <div class="payment-tabs" id="paymentTabs">
                <div class="payment-tab active" onclick="selectPayment(this)"><span class="emoji">📦</span>Contraentrega</div>
                <div class="payment-tab" onclick="selectPayment(this)"><span class="emoji">💳</span>MercadoPago</div>
                <div class="payment-tab" onclick="selectPayment(this)"><span class="emoji">🏦</span>PSE</div>
                <div class="payment-tab" onclick="selectPayment(this)"><span class="emoji">📱</span>Nequi</div>
            </div>

            <form class="checkout-form" id="orderForm">
                <div class="checkout-row">
                    <input class="field" type="text" placeholder="Nombre" required>
                    <input class="field" type="text" placeholder="Apellido" required>
                </div>
                <input class="field" type="tel" placeholder="Celular / WhatsApp" required>
                <input class="field" type="email" placeholder="Correo electrónico" required>
                <div class="checkout-row">
                    <input class="field" type="text" placeholder="Departamento" required>
                    <input class="field" type="text" placeholder="Ciudad" required>
                </div>
                <input class="field" type="text" placeholder="Dirección y complementos (ej: Cra 5 #10-20, Apto 301)" required>
                <input class="field" type="text" placeholder="Barrio (opcional)">
                <button type="submit" class="submit-btn">✅ CONFIRMAR PEDIDO — $819.900</button>
                <p class="submit-note">Te escribimos por WhatsApp para confirmar todo antes de enviar.</p>
            </form>

            <div style="text-align:center;margin-top:20px;">
                <p style="font-size:13px;color:var(--gray-400);margin-bottom:8px;">o si prefieres</p>
                <a href="https://wa.me/573186606067?text=Hola!%20Quiero%20comprar%20Simply%20Straight" class="btn-block btn-rose">💬 Comprar directamente por WhatsApp</a>
            </div>
        </div>
    </div>
</section>

<!-- GUARANTEE -->
<section class="section">
    <div class="container">
        <div class="guarantee-box">
            <div class="guarantee-icon">🛡️</div>
            <h3>Garantía Simply Straight</h3>
            <p>Si el producto llega con falla de fábrica, te lo cambiamos. Escríbenos por WhatsApp y te guiamos paso a paso.</p>
            <p style="margin-top:6px;">Además, por ser compra online en Colombia, tienes <strong>derecho de retracto de 5 días hábiles</strong> desde que recibes el producto. Sin preguntas, sin letra chica.</p>
            <p style="font-size:12px;color:var(--gray-400);margin-top:8px;">No tienes nada que perder. Si no te gusta, no te quedas con él.</p>
        </div>
    </div>
</section>

<!-- FAQ -->
<section class="section section-bg">
    <div class="container">
        <div class="section-eyebrow">¿Dudas?</div>
        <h2 class="section-title">Preguntas frecuentes</h2>
        <div class="faq-list">
            <div class="faq-item"><button class="faq-q" onclick="this.classList.toggle('open');this.nextElementSibling.classList.toggle('open')">¿Llega a todo Colombia?<span></span></button><div class="faq-a">Sí. Hacemos envíos a toda Colombia. Ciudades principales: 2-5 días hábiles. Otros municipios: 3-7 días. Te confirmamos el tiempo exacto cuando haces tu pedido.</div></div>
            <div class="faq-item"><button class="faq-q" onclick="this.classList.toggle('open');this.nextElementSibling.classList.toggle('open')">¿Cómo funciona la contraentrega?<span></span></button><div class="faq-a">El transportador llega a tu casa, te entrega el paquete, lo abres, lo revisas, y SOLO AHÍ pagas. Si algo no te convence, no pagas. Sin riesgo.</div></div>
            <div class="faq-item"><button class="faq-q" onclick="this.classList.toggle('open');this.nextElementSibling.classList.toggle('open')">¿Sirve para cabello crespo o afro?<span></span></button><div class="faq-a">Ayuda a reducir el frizz y ordenar el cabello. En cabello muy crespo o afro el acabado es más natural (no liso extremo). No reemplaza un alisado químico o keratina.</div></div>
            <div class="faq-item"><button class="faq-q" onclick="this.classList.toggle('open');this.nextElementSibling.classList.toggle('open')">¿Qué incluye la caja?<span></span></button><div class="faq-a">El cepillo Simply Straight, cable de alimentación y manual de instrucciones en español. Exactamente lo que ves en el video.</div></div>
            <div class="faq-item"><button class="faq-q" onclick="this.classList.toggle('open');this.nextElementSibling.classList.toggle('open')">¿Es voltaje universal? ¿Necesito transformador?<span></span></button><div class="faq-a">Sí, es 110V-220V. Funciona perfecto en toda Colombia. No necesitas transformador. Solo enchufar y usar.</div></div>
            <div class="faq-item"><button class="faq-q" onclick="this.classList.toggle('open');this.nextElementSibling.classList.toggle('open')">¿Cuánto dura el producto?<span></span></button><div class="faq-a">Con uso normal, años. Tiene materiales de calidad, auto apagado de seguridad y garantía por defectos de fábrica.</div></div>
        </div>
    </div>
</section>

<!-- FLOATING WHATSAPP -->
<a href="https://wa.me/573186606067" class="float-wa" target="_blank" title="Escríbenos por WhatsApp">
    <svg viewBox="0 0 24 24"><path d="M17.472 14.382c-.297-.149-1.758-.867-2.03-.967-.273-.099-.471-.148-.67.15-.197.297-.767.966-.94 1.164-.173.199-.347.223-.644.075-.297-.15-1.255-.463-2.39-1.475-.883-.788-1.48-1.761-1.653-2.059-.173-.297-.018-.458.13-.606.134-.133.298-.347.446-.52.149-.174.198-.298.298-.497.099-.198.05-.371-.025-.52-.075-.149-.669-1.612-.916-2.207-.242-.579-.487-.5-.669-.51-.173-.008-.371-.01-.57-.01-.198 0-.52.074-.792.372-.272.297-1.04 1.016-1.04 2.479 0 1.462 1.065 2.875 1.213 3.074.149.198 2.096 3.2 5.077 4.487.709.306 1.262.489 1.694.625.712.227 1.36.195 1.871.118.571-.085 1.758-.719 2.006-1.413.248-.694.248-1.289.173-1.413-.074-.124-.272-.198-.57-.347m-5.421 7.403h-.004a9.87 9.87 0 01-5.031-1.378l-.361-.214-3.741.982.998-3.648-.235-.374a9.86 9.86 0 01-1.51-5.26c.001-5.45 4.436-9.884 9.888-9.884 2.64 0 5.122 1.03 6.988 2.898a9.825 9.825 0 012.893 6.994c-.003 5.45-4.437 9.884-9.885 9.884m8.413-18.297A11.815 11.815 0 0012.05 0C5.495 0 .16 5.335.157 11.892c0 2.096.547 4.142 1.588 5.945L.057 24l6.305-1.654a11.882 11.882 0 005.683 1.448h.005c6.554 0 11.89-5.335 11.893-11.893a11.821 11.821 0 00-3.48-8.413z"/></svg>
</a>

<script>
let currentQty = 1;
let currentPrice = 119900;
let stock = 19;
let currentSlide = 0;

// Carousel
function goToSlide(n) {
    currentSlide = n;
    document.querySelectorAll('.carousel-slide').forEach(function(s, i) {
        s.style.opacity = i === n ? '1' : '0';
    });
    document.querySelectorAll('.carousel-dot').forEach(function(d, i) {
        d.style.background = i === n ? 'var(--rose-dark)' : 'var(--gray-200)';
    });
}
// Auto-rotate every 4 seconds
setInterval(function() {
    currentSlide = (currentSlide + 1) % 4;
    goToSlide(currentSlide);
}, 4000);

function selectPayment(el) {
    document.querySelectorAll('.payment-tab').forEach(t => t.classList.remove('active'));
    el.classList.add('active');
}
function selectQty(el, qty, price) {
    currentQty = qty;
    currentPrice = price;
    document.querySelectorAll('#qtyTabs .payment-tab').forEach(t => t.classList.remove('active'));
    el.classList.add('active');
    // Update submit button
    var total = price * qty;
    var btn = document.querySelector('.submit-btn');
    btn.textContent = '✅ CONFIRMAR PEDIDO — $' + total.toLocaleString('es-CO');
}

// Countdown timer — 30 hours
var countdownEnd = new Date().getTime() + (30 * 60 * 60 * 1000);
setInterval(function() {
    var now = new Date().getTime();
    var dist = countdownEnd - now;
    if (dist < 0) {
        document.getElementById('countdown').textContent = 'OFERTA FINALIZADA';
        return;
    }
    var h = Math.floor(dist / (1000 * 60 * 60));
    var m = Math.floor((dist % (1000 * 60 * 60)) / (1000 * 60));
    var s = Math.floor((dist % (1000 * 60)) / 1000);
    document.getElementById('countdown').textContent = 
        h + 'h ' + String(m).padStart(2,'0') + 'm ' + String(s).padStart(2,'0') + 's';
}, 1000);

// Social proof toasts — Colombian double last names, all real-time, linked to stock
var cities = ['Bogotá', 'Medellín', 'Cali', 'Barranquilla', 'Cartagena', 'Bucaramanga', 'Pereira', 'Manizales', 'Cúcuta', 'Ibagué', 'Santa Marta', 'Villavicencio', 'Neiva', 'Armenia', 'Popayán'];
var firstNames = ['María Fernanda', 'Valentina', 'Carolina', 'Daniela', 'Luisa', 'Paola Andrea', 'Natalia', 'Diana Marcela', 'Camila', 'Juliana', 'Laura', 'Tatiana', 'Angie', 'Marcela', 'Sandra'];
var lastNames = ['García López', 'Rodríguez Martínez', 'Hernández Gómez', 'Pérez Rojas', 'González Díaz', 'Jiménez Torres', 'Ortiz Castillo', 'Moreno Herrera', 'Ramos Mora', 'Suárez Prieto', 'Carreño Vega', 'Vargas Estrada', 'Navarro Restrepo', 'Castañeda Jaramillo', 'Villanueva Ochoa'];
var toastTimes = ['hace 2 min', 'hace 5 min', 'hace 8 min', 'ahora mismo', 'hace 1 min', 'hace 3 min', 'hace 10 min', 'hace 15 min', 'hace 4 min', 'hace 6 min'];

function showToast() {
    if (stock <= 3) return; // no more toasts if almost sold out
    var city = cities[Math.floor(Math.random() * cities.length)];
    var name = firstNames[Math.floor(Math.random() * firstNames.length)] + ' ' + lastNames[Math.floor(Math.random() * lastNames.length)];
    var q = Math.random() > 0.5 ? 2 : 3;
    // Reduce stock and increase sold today
    var actualDrop = Math.min(q, stock - 3);
    if (actualDrop <= 0) { actualDrop = 1; stock = 3; }
    else { stock -= actualDrop; }
    if (stock <= 3) stock = 3;
    document.getElementById('stockCounter').textContent = stock;
    if (stock <= 5) { document.getElementById('urgencyBar').style.background = '#dc2626'; }
    soldToday += actualDrop;
    document.getElementById('soldToday').textContent = soldToday;
    // Flash stock
    document.getElementById('stockCounter').style.transform = 'scale(1.4)';
    setTimeout(function() { document.getElementById('stockCounter').style.transform = 'scale(1)'; }, 200);
    // Show toast
    document.getElementById('toastMsg').textContent = name + ' de ' + city + ' compró ' + actualDrop + ' unidades';
    document.getElementById('toastTime').textContent = toastTimes[Math.floor(Math.random() * toastTimes.length)];
    var inner = document.getElementById('toastInner');
    inner.style.display = 'flex';
    inner.style.opacity = '1';
    setTimeout(function() {
        inner.style.opacity = '0';
        setTimeout(function() { inner.style.display = 'none'; }, 300);
    }, 5000);
}
setTimeout(showToast, 6000);
setInterval(showToast, 25000 + Math.random() * 20000);

// "X personas están viendo esto" counter
var viewers = Math.floor(Math.random() * 15) + 8;
setInterval(function() {
    viewers = Math.max(4, viewers + Math.floor(Math.random() * 7) - 3);
    document.getElementById('viewerCount').textContent = viewers;
}, 8000 + Math.random() * 6000);

// "Vendidos hoy" counter — also increments with toasts
var soldToday = 23;

// Stock countdown — drops 1-3 every 12-22 seconds, reaches ~3 in 5 min
setInterval(function() {
    if (stock > 3) {
        var r = Math.random();
        var drop = r < 0.7 ? 1 : (r < 0.9 ? 2 : 3);
        stock = Math.max(3, stock - drop);
        document.getElementById('stockCounter').textContent = stock;
        if (stock <= 5) {
            document.getElementById('urgencyBar').style.background = '#dc2626';
        }
        // Flash effect when stock drops
        document.getElementById('stockCounter').style.transform = 'scale(1.4)';
        setTimeout(function() {
            document.getElementById('stockCounter').style.transform = 'scale(1)';
        }, 200);
    }
}, 12000 + Math.random() * 10000); // every 12-22 seconds

document.getElementById('orderForm').addEventListener('submit', function(e) {
    e.preventDefault();
    var inputs = this.querySelectorAll('input');
    var total = currentPrice * currentQty;
    var pay = document.querySelector('#paymentTabs .payment-tab.active').innerText.replace(/\\n.*/,'').trim();
    
    // Build order data
    var order = {
        fecha: new Date().toLocaleString('es-CO'),
        nombre: inputs[0].value,
        apellido: inputs[1].value,
        celular: inputs[2].value,
        correo: inputs[3].value,
        departamento: inputs[4].value,
        ciudad: inputs[5].value,
        direccion: inputs[6].value,
        barrio: inputs[7].value || '-',
        cantidad: currentQty,
        precioUnit: currentPrice,
        total: total,
        pago: pay
    };
    
    // Save to localStorage
    var orders = JSON.parse(localStorage.getItem('simplyOrders') || '[]');
    orders.unshift(order);
    localStorage.setItem('simplyOrders', JSON.stringify(orders));
    
    // Build WhatsApp message with all data
    var msg = '🛒 *NUEVO PEDIDO SIMPLY STRAIGHT*';
    msg += '\\n📅 ' + order.fecha;
    msg += '\\n👤 *Cliente:* ' + order.nombre + ' ' + order.apellido;
    msg += '\\n📱 *Celular:* ' + order.celular;
    msg += '\\n📧 *Correo:* ' + order.correo;
    msg += '\\n📍 *Ubicación:* ' + order.ciudad + ', ' + order.departamento;
    msg += '\\n🏠 *Dirección:* ' + order.direccion;
    msg += '\\n🏘️ *Barrio:* ' + order.barrio;
    msg += '\\n\\n📦 *Producto:* Simply Straight x' + order.cantidad;
    msg += '\\n💰 *Precio unitario:* $' + order.precioUnit.toLocaleString('es-CO');
    msg += '\\n💵 *TOTAL:* $' + order.total.toLocaleString('es-CO');
    msg += '\\n💳 *Pago:* ' + order.pago;
    msg += '\\n\\n✅ *ENVIAR CONFIRMACIÓN AL CLIENTE*';
    
    // Redirect to MercadoPago or WhatsApp
    if (pay.includes('MercadoPago') || pay.includes('💳')) {
        window.open('https://link.mercadopago.com.co/simplystraight', '_blank');
    }
    window.open('https://wa.me/573186606067?text=' + encodeURIComponent(msg), '_blank');
    
    // Reset form
    this.reset();
    alert('✅ ¡Pedido enviado! Revisa WhatsApp para confirmar.');
});

// Admin panel — accessible via ?admin in URL
if (location.search.includes('admin')) {
    var adminHTML = '<div id=\"adminPanel\" style=\"position:fixed;top:0;left:0;right:0;bottom:0;background:white;z-index:9999;overflow:auto;padding:20px;\"><h2 style=\"margin-bottom:10px;\">📊 Pedidos Recibidos</h2><button onclick=\"document.getElementById(\\'adminPanel\\').remove()\" style=\"position:absolute;top:10px;right:20px;font-size:24px;background:none;border:none;cursor:pointer;\">&times;</button><table style=\"width:100%;border-collapse:collapse;font-size:12px;\"><thead><tr style=\"background:#111;color:white;\"><th>#</th><th>Fecha</th><th>Cliente</th><th>Celular</th><th>Ciudad</th><th>Dirección</th><th>Cant</th><th>Total</th><th>Pago</th></tr></thead><tbody id=\"ordersTable\"></tbody></table><p style=\"margin-top:10px;font-size:11px;color:gray;\">Los datos se guardan solo en este navegador. Para acceder, añade <code>?admin</code> a la URL.</p></div>';
    document.body.insertAdjacentHTML('beforeend', adminHTML);
    var orders = JSON.parse(localStorage.getItem('simplyOrders') || '[]');
    var tbody = document.getElementById('ordersTable');
    orders.forEach(function(o, i) {
        tbody.innerHTML += '<tr style=\"border-bottom:1px solid #ddd;\"><td>' + (i+1) + '</td><td>' + o.fecha + '</td><td>' + o.nombre + '</td><td>' + o.celular + '</td><td>' + o.ciudad + '</td><td>' + o.direccion + '</td><td>' + o.cantidad + '</td><td>$' + o.total.toLocaleString('es-CO') + '</td><td>' + o.pago + '</td></tr>';
    });
    if (orders.length === 0) {
        tbody.innerHTML = '<tr><td colspan=\"9\" style=\"text-align:center;padding:20px;color:gray;\">No hay pedidos todavía</td></tr>';
    }
    // Auto-refresh every 10 seconds
    setInterval(function() { location.reload(); }, 10000);
}
</script>

</body>
</html>"""

with open(r'C:\Users\artur\proyectos\dropi\simply-straight\index-v3.html', 'w', encoding='utf-8') as f:
    f.write(html)
print(f'OK: index-v3.html written ({len(html)} bytes)')
