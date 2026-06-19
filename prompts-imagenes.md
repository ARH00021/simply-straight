# 🖼️ Prompts para Imágenes — Simply Straight

> Generados para ComfyUI con SD 1.5 (Realistic Vision V6) + IPAdapter
> Si no usas IPAdapter: genera primero la imagen 1, luego úsala como referencia

---

## 1. PRODUCTO PRINCIPAL
**Uso:** Ficha de producto, foto principal
**Ratio:** 1:1

**Prompt:**
```
ultra-realistic 4K product photography of the "Simply Straight" hair straightening brush, professional studio shot. The brush is positioned at a slight 3/4 angle to show depth, on an immaculate pure white background. The brush body is a sleek matte black plastic. The 3D ceramic bristles are vibrant hot pink, perfectly arranged. A small built-in digital LCD screen is clearly visible and illuminated, displaying the temperature "450°F" in crisp blue font. Studio lighting is soft and diffused, eliminating harsh shadows, with a key light creating subtle elegant highlights along the brush's curves. The 6ft black power cord is artfully coiled and placed neatly behind the brush. Impeccable focus, every detail sharp, commercial quality, shot on hasselblad, ISO 100.
```

**Negative:**
```
shadows, reflections, fingerprints, dust, scratches, blurry, out of focus, text, watermark, logo, warped, deformed, poor lighting, distracting elements
```

**Settings:** Steps: 35, CFG: 7, Sampler: DPM++ 2M Karras

---

## 2. LIFESTYLE RESULTADO
**Uso:** Redes sociales, WhatsApp, stories
**Ratio:** 4:5

**Prompt:**
```
beautiful Colombian latina woman, 25 years old, warm brown skin, long dark brown hair incredibly smooth and pin-straight with glossy shine. She is smiling confidently, looking slightly down at a Simply Straight hair brush she's holding in her hand in front of a mirror. The brush has a black body and hot pink ceramic bristles, with a digital LCD display. Natural daylight coming from a large window on the left, soft golden hour glow. She wears a simple white tank top. The mood is effortless, happy, "I just discovered this" vibe. Shot on 85mm f1.4 lens, bokeh background showing a modern clean bedroom. Editorial lifestyle photography, warm tones.
```

**Negative:**
```
ugly, deformed face, extra fingers, bad anatomy, disfigured, plastic skin, harsh lighting, studio lighting, angry, sad, text, watermark, logo, curly hair, messy hair, wet hair
```

**Settings:** Steps: 30, CFG: 7, Sampler: DPM++ 2M Karras

---

## 3. ANTES Y DESPUÉS
**Uso:** Meta Ads, TikTok, feed
**Ratio:** 1:1

**Prompt:**
```
split screen comparison photograph. LEFT SIDE: same Colombian latina woman with dark brown hair looking messy, frizzy, uncontrollable, dry, and frustrated, slight frown, unflattering bathroom lighting. RIGHT SIDE: same woman with incredibly smooth, pin-straight, glossy, flowing dark brown hair, looking relieved and confident, holding a Simply Straight ceramic brush with black body and hot pink bristles and LCD display, clean bathroom lighting. Sharp vertical split down the middle. Professional haircare before-and-after advertisement style, clean composition, no text. The contrast is dramatic and inspiring.
```

**Negative:**
```
text, watermark, logo, different person, inconsistent face, deformed, ugly, blurry, extra limbs, bad composition, cartoon, drawing
```

**Settings:** Steps: 30, CFG: 7, Sampler: DPM++ 2M Karras

---

## 4. META ADS
**Uso:** Anuncios Facebook/Instagram
**Ratio:** 4:5

**Prompt:**
```
confident young Colombian latina woman with long straight glossy brown hair, looking directly at camera with a warm genuine smile. She holds a Simply Straight black and hot pink ceramic hair brush near her chest, LCD display visible. Soft blurred tropical background suggesting Colombia (palm tree, warm light, bokeh). Golden hour sunlight from the right creating a rim light on her hair. She wears a casual elegant cream blouse. The vibe is aspirational, confident, "this changed my life". Professional portrait photography, 85mm lens, f1.8, natural skin texture, subtle makeup, editorial quality.
```

**Negative:**
```
ugly, deformed, plastic skin, too much makeup, angry, sad, studio lighting, cold tones, text, watermark, logo, extra fingers, bad anatomy, looking away
```

**Settings:** Steps: 30, CFG: 7, Sampler: DPM++ 2M Karras

---

## 5. UNBOXING / EMPAQUE
**Uso:** Stories, TikTok, WhatsApp
**Ratio:** 9:16

**Prompt:**
```
top-down flat lay unboxing photograph. A white hair straightening brush box with purple and black accents is open, the Simply Straight ceramic brush (black body with hot pink bristles, LCD display) is partially lifted out of the box, held by female hands with natural nails. The box features the text "The Brush That Straightens Hair!" in purple font. White marble table surface. Soft natural overhead lighting. Clean, minimal aesthetic. The viewer feels like they're about to discover something amazing. Product unboxing photography, flat lay style.
```

**Negative:**
```
messy, cluttered, dark, shadows, blurry, dirty nails, text overlay, watermark, deformed hands, extra fingers, bad anatomy, low quality
```

**Settings:** Steps: 30, CFG: 7, Sampler: DPM++ 2M Karras

---

## ⚙️ Configuración Técnica ComfyUI

| Parámetro | Valor |
|-----------|-------|
| **Modelo** | Realistic Vision V6 (SD 1.5) |
| **Steps** | 30-35 |
| **CFG Scale** | 7 |
| **Sampler** | DPM++ 2M Karras |
| **IPAdapter** | Usar imagen 1 como referencia para consistencia |
| **Resolución** | 512x512 (SD 1.5 nativa, luego upscale 2x) |

### 🎯 Recomendación para consistencia:
1. Genera la **imagen 1** primero hasta que el cepillo se vea perfecto
2. Usa esa imagen en un nodo **IPAdapter** de ComfyUI
3. Genera las imágenes 2, 4, 5 con IPAdapter para que el cepillo sea idéntico
4. La imagen 3 (antes/después) no necesita IPAdapter — el enfoque es el cabello

---

## 🆓 Alternativas gratis si ComfyUI falla:
- **Leonardo.ai** — 150 créditos gratis/día
- **Bing Image Creator** — ilimitado con DALL-E 3
- **Playground AI** — 500 imágenes gratis/día
