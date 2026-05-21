# CUBOX · Container Maritim 20' Standard — pagina de produs

## Structura folderului

```
cubox-container-20ft/
├── index.html              ← pagina HTML (deschide-l în browser sau integrează-l în site)
└── assets/
    ├── cubox-logo.jpg      ← logo CUBOX (44×44 în topbar)
    ├── container-side.jpg  ← container vedere laterală cu dimensiuni
    └── container-open.jpg  ← container cu uși deschise (interior)
```

## Cum integrezi în site-ul tău

### Varianta 1 — pagină de sine stătătoare
Pune tot folderul `cubox-container-20ft/` pe server, în root sau într-un subfolder.
Link către pagină: `https://cubox.ro/cubox-container-20ft/` sau `https://cubox.ro/produse/container-20ft/`.

### Varianta 2 — integrată în CMS (WordPress, Shopify etc.)
- Copiază conținutul din `<body>...</body>` în pagina de produs din CMS
- Copiază conținutul din `<style>...</style>` în CSS-ul temei sau într-un `<style>` separat
- Urcă cele 3 imagini din `assets/` în Media Library și actualizează căile (`src="..."`) către locația din CMS

### Varianta 3 — single-file (cea mai simplă)
Folosește `cubox-fisa-container-20ft.html` (din arhiva celălaltă) — un singur fișier cu imaginile încorporate în base64. Doar îl urci pe server și gata.

## Cum funcționează descărcarea PDF

Butonul „Descarcă PDF" din colțul dreapta-sus apelează `window.print()`. Browserul deschide dialogul nativ de printare, iar utilizatorul alege „Salvează ca PDF". 

CSS-ul are reguli speciale `@media print` care:
- Ascund butoanele și animațiile
- Mută secțiunea CTA pe fundal cream (în loc de navy)
- Adaugă antet/subsol pe fiecare pagină: **CUBOX** stânga, referință produs dreapta, număr pagină jos
- Forțează tabelul de specificații la o singură coloană pentru A4

## Personalizare rapidă

| Vrei să schimbi... | Caută în `index.html`... |
|---|---|
| Numărul de telefon | `tel:+40000000000` → schimbă numărul |
| Link „Trimite cerere ofertă" | `href="#"` din secțiunea CTA |
| Culoarea brand orange | variabila CSS `--c-orange: #ED5E16;` |
| Culoarea brand navy | variabila CSS `--c-navy: #0D2849;` |
| Logo | înlocuiește `assets/cubox-logo.jpg` |

## Notă tehnică

Pagina este 100% standalone, nu folosește framework-uri (React, Vue, etc.) și nu are dependențe externe în afară de fonturile Google (Bricolage Grotesque, Manrope, JetBrains Mono). Funcționează pe orice browser modern, este responsive, și are SEO-friendly meta tags.
