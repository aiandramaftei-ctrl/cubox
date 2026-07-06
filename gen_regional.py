import os

SITE_PATH = r"C:\Users\HP\Desktop\CLAUDE\CUBOX\SITE"

cities = [
    {
        "slug": "containere-modulare-bacau",
        "city": "Bacău",
        "county": "Bacău",
        "county_long": "județul Bacău",
        "areaServed": "Bacău",
        "meta_title": "Containere modulare Bacău | CUBOX Modular — Livrare în 15–21 zile",
        "meta_desc": "Containere modulare în Bacău — livrare directă în județul Bacău. Modele standard, duble, cu terasă, comerciale. Prețuri de la 2.700 EUR fără TVA. Ofertă gratuită.",
        "h1": "Containere modulare Bacău",
        "hero_desc": "Livrăm containere modulare în Bacău și județul Bacău în 15–21 de zile lucrătoare. Sediu local — vino să discuți direct sau cere ofertă online.",
        "intro_title": "De ce CUBOX Modular în Bacău",
        "intro_text": "Suntem cu sediul în Bacău — cel mai scurt drum de la comandă la livrare pe care îl poți găsi în Moldova. Containere modulare standard, duble și cu terasă, containere comerciale pentru fast food și showroom — toate disponibile cu livrare în județul Bacău. Fiecare container este livrat gata montat, fără autorizație de construcție.",
        "uses": ["Birou de șantier", "Spațiu comercial fast food", "Depozit", "Studio sau birou acasă", "Cabină de pază", "Container cu terasă pentru odihnă"],
    },
    {
        "slug": "containere-modulare-suceava",
        "city": "Suceava",
        "county": "Suceava",
        "county_long": "județul Suceava",
        "areaServed": "Suceava",
        "meta_title": "Containere modulare Suceava | CUBOX Modular — Livrare în 15–21 zile",
        "meta_desc": "Containere modulare în Suceava — livrare în județul Suceava în 15–21 zile. Standard, duble, comerciale. Prețuri de la 2.700 EUR fără TVA. Cere ofertă gratuită.",
        "h1": "Containere modulare Suceava",
        "hero_desc": "Livrăm containere modulare în Suceava și județul Suceava în 15–21 de zile lucrătoare. Birou, depozit, fast food, container cu terasă — soluție rapidă fără birocrație.",
        "intro_title": "Containere modulare livrate în Suceava",
        "intro_text": "CUBOX Modular livrează containere modulare în Suceava din depozitul propriu din Moldova. Transport și montaj inclus în prețul final — nu plătești nimic extra pentru livrare în Suceava. Containerele sunt fabricate în România, livrate gata de utilizare, fără autorizație de construcție necesară.",
        "uses": ["Birou șantier", "Kiosk fast food", "Spațiu comercial", "Depozit mobil", "Container cu terasă", "Cabină de pază"],
    },
    {
        "slug": "containere-modulare-iasi",
        "city": "Iași",
        "county": "Iași",
        "county_long": "județul Iași",
        "areaServed": "Iași",
        "meta_title": "Containere modulare Iași | CUBOX Modular — Livrare în 15–21 zile",
        "meta_desc": "Containere modulare în Iași — livrare în județul Iași în 15–21 zile lucrătoare. 11 modele disponibile. Prețuri de la 2.700 EUR fără TVA. Ofertă personalizată gratuită.",
        "h1": "Containere modulare Iași",
        "hero_desc": "Livrăm containere modulare în Iași și județul Iași în 15–21 de zile lucrătoare. Fără autorizație de construcție. Livrare gata montate la locația ta.",
        "intro_title": "De ce containere modulare în Iași",
        "intro_text": "Iașul este unul dintre cele mai dinamice orașe din România din punct de vedere al construcțiilor și afacerilor. Containerele modulare CUBOX sunt soluția rapidă pentru antreprenorii din Iași care vor un spațiu funcțional fără birocrație și fără luni de așteptare. Livrăm direct la locația ta din județul Iași, gata montat.",
        "uses": ["Birou de firmă", "Fast food și kiosk", "Showroom produse", "Birou de șantier", "Depozit marfă", "Studio sau atelier"],
    },
    {
        "slug": "containere-modulare-brasov",
        "city": "Brașov",
        "county": "Brașov",
        "county_long": "județul Brașov",
        "areaServed": "Brașov",
        "meta_title": "Containere modulare Brașov | CUBOX Modular — Livrare în 15–21 zile",
        "meta_desc": "Containere modulare în Brașov — livrare în județul Brașov în 15–21 zile. Standard, duble, cu terasă, comerciale. Prețuri de la 2.700 EUR fără TVA. Ofertă gratuită.",
        "h1": "Containere modulare Brașov",
        "hero_desc": "Livrăm containere modulare în Brașov și județul Brașov în 15–21 de zile lucrătoare. Ideal pentru turism, construcții, comerț și afaceri.",
        "intro_title": "Containere modulare livrate în Brașov",
        "intro_text": "Brașovul și zona sa montană au o cerere mare de spații funcționale temporare și permanente — pentru turism, construcții, retail și afaceri mici. CUBOX Modular livrează containere modulare în Brașov gata montate, cu toate finisajele incluse. Nu ai nevoie de autorizație de construcție pentru containerele noastre standard.",
        "uses": ["Spațiu turistic sezonier", "Birou de șantier", "Fast food și cafenea", "Depozit", "Container cu terasă panoramică", "Showroom"],
    },
    {
        "slug": "containere-modulare-cluj",
        "city": "Cluj-Napoca",
        "county": "Cluj",
        "county_long": "județul Cluj",
        "areaServed": "Cluj",
        "meta_title": "Containere modulare Cluj-Napoca | CUBOX Modular — Livrare în 15–21 zile",
        "meta_desc": "Containere modulare în Cluj-Napoca — livrare în județul Cluj în 15–21 zile. Standard, duble, comerciale. Prețuri de la 2.700 EUR fără TVA. Ofertă personalizată.",
        "h1": "Containere modulare Cluj-Napoca",
        "hero_desc": "Livrăm containere modulare în Cluj-Napoca și județul Cluj în 15–21 de zile lucrătoare. Soluție rapidă pentru antreprenorii din cel mai activ hub economic din Ardeal.",
        "intro_title": "Containere modulare pentru afaceri în Cluj",
        "intro_text": "Cluj-Napoca este capitala economică a Transilvaniei — un oraș unde viteza de reacție contează. Containerele modulare CUBOX sunt soluția pentru antreprenorii clujeni care au nevoie de un spațiu funcțional rapid, fără birocrație și fără costuri mari de construcție. Livrare directă în Cluj-Napoca și județul Cluj în 15–21 de zile.",
        "uses": ["Birou startup sau firmă", "Fast food și cafenea", "Showroom și retail", "Birou de șantier", "Depozit logistică", "Container cu terasă"],
    },
    {
        "slug": "containere-modulare-bucuresti",
        "city": "București",
        "county": "București",
        "county_long": "București și Ilfov",
        "areaServed": "București",
        "meta_title": "Containere modulare București | CUBOX Modular — Livrare în 15–21 zile",
        "meta_desc": "Containere modulare în București și Ilfov — livrare în 15–21 zile lucrătoare. 11 modele, prețuri de la 2.700 EUR fără TVA. Containerele tale gata montate la adresa ta.",
        "h1": "Containere modulare București",
        "hero_desc": "Livrăm containere modulare în București și județul Ilfov în 15–21 de zile lucrătoare. Gata montate, fără autorizație de construcție.",
        "intro_title": "Containere modulare livrate în București",
        "intro_text": "Bucureștiul este cea mai mare piață din România pentru spații funcționale modulare. Construcțiile, logistica, retailul stradal, fast food-urile și birourile de șantier din Capitală au nevoie de soluții rapide. CUBOX Modular livrează containere modulare în toate sectoarele București și județul Ilfov — transport inclus, montat la locație.",
        "uses": ["Birou șantier în construcții", "Fast food și kiosk stradal", "Showroom și magazin pop-up", "Depozit logistic", "Container comercial pentru evenimente", "Birou firmă mică"],
    },
    {
        "slug": "containere-modulare-galati",
        "city": "Galați",
        "county": "Galați",
        "county_long": "județul Galați",
        "areaServed": "Galați",
        "meta_title": "Containere modulare Galați | CUBOX Modular — Livrare în 15–21 zile",
        "meta_desc": "Containere modulare în Galați — livrare în județul Galați în 15–21 zile. Standard, duble, comerciale, maritime. Prețuri de la 2.700 EUR fără TVA. Ofertă gratuită.",
        "h1": "Containere modulare Galați",
        "hero_desc": "Livrăm containere modulare în Galați și județul Galați în 15–21 de zile lucrătoare. Port, industrie, construcții — soluții complete pentru orice nevoie.",
        "intro_title": "Containere modulare în Galați",
        "intro_text": "Galațiul, cu industria sa navală, portul și activitatea industrială intensă, are nevoie de soluții de spații funcționale rapide. CUBOX Modular livrează containere modulare și maritime în Galați — pentru birouri de șantier, depozite, spații comerciale. Livrare directă în județul Galați, montat la locație.",
        "uses": ["Birou de șantier industrial", "Depozit portuar", "Kiosk fast food", "Container birou firmă", "Spațiu comercial", "Container maritim second hand"],
    },
    {
        "slug": "containere-modulare-constanta",
        "city": "Constanța",
        "county": "Constanța",
        "county_long": "județul Constanța",
        "areaServed": "Constanța",
        "meta_title": "Containere modulare Constanța | CUBOX Modular — Livrare în 15–21 zile",
        "meta_desc": "Containere modulare în Constanța — livrare în județul Constanța în 15–21 zile. Ideal pentru turism sezonier, construcții, comerț. Prețuri de la 2.700 EUR fără TVA.",
        "h1": "Containere modulare Constanța",
        "hero_desc": "Livrăm containere modulare în Constanța și județul Constanța — ideal pentru sezonul estival, construcții și comerț. Livrare în 15–21 de zile lucrătoare.",
        "intro_title": "Containere modulare pentru sezonul estival în Constanța",
        "intro_text": "Constanța și litoralul românesc au o cerere ridicată de spații funcționale sezoniere — bar de plajă, fast food estival, kiosk, depozit sezonier. Containerele modulare CUBOX sunt soluția perfectă: montezi primăvara, folosești toată vara, relocalizezi la toamnă dacă este nevoie. Livrare directă în Constanța și pe litoral.",
        "uses": ["Bar sau cafenea plajă", "Fast food sezonier", "Depozit sezonier", "Birou șantier construcții", "Container cu terasă", "Spațiu comercial litoral"],
    },
    {
        "slug": "containere-modulare-timisoara",
        "city": "Timișoara",
        "county": "Timiș",
        "county_long": "județul Timiș",
        "areaServed": "Timiș",
        "meta_title": "Containere modulare Timișoara | CUBOX Modular — Livrare în 15–21 zile",
        "meta_desc": "Containere modulare în Timișoara — livrare în județul Timiș în 15–21 zile. Standard, duble, comerciale. Prețuri de la 2.700 EUR fără TVA. Cere ofertă personalizată.",
        "h1": "Containere modulare Timișoara",
        "hero_desc": "Livrăm containere modulare în Timișoara și județul Timiș — soluție rapidă pentru antreprenorii din cel mai vestic hub industrial al României.",
        "intro_title": "Containere modulare livrate în Timișoara",
        "intro_text": "Timișoara este unul dintre cele mai active centre industriale și economice din România. Companiile din Timiș au nevoie de birouri de șantier, depozite rapide, spații comerciale relocabile. CUBOX Modular livrează containere modulare direct în Timișoara — transport inclus, montaj inclus, fără autorizație de construcție.",
        "uses": ["Birou firmă sau startup", "Birouri de șantier industrial", "Depozit rapid", "Fast food și kiosk", "Showroom produse", "Container cu terasă"],
    },
    {
        "slug": "containere-modulare-ploiesti",
        "city": "Ploiești",
        "county": "Prahova",
        "county_long": "județul Prahova",
        "areaServed": "Prahova",
        "meta_title": "Containere modulare Ploiești | CUBOX Modular — Livrare în 15–21 zile",
        "meta_desc": "Containere modulare în Ploiești — livrare în județul Prahova în 15–21 zile lucrătoare. Standard, duble, comerciale, maritime. Prețuri de la 2.700 EUR fără TVA.",
        "h1": "Containere modulare Ploiești",
        "hero_desc": "Livrăm containere modulare în Ploiești și județul Prahova în 15–21 de zile lucrătoare. Soluție rapidă pentru industrie, construcții și comerț.",
        "intro_title": "Containere modulare în Ploiești și Prahova",
        "intro_text": "Zona Ploiești-Prahova, cu activitatea sa industrială, petrochimică și comercială intensă, are nevoie constantă de spații funcționale rapide. CUBOX Modular livrează containere modulare în Ploiești și toată Prahova — birouri de șantier, depozite, spații comerciale, containere cu terasă. Livrate gata montate, fără autorizație de construcție.",
        "uses": ["Birou de șantier industrial", "Depozit rapid", "Kiosk și fast food", "Spațiu comercial relocabil", "Container cu terasă", "Birou firmă"],
    },
]

TEMPLATE = '''<!DOCTYPE html>
<html lang="ro">
<head>
<!-- Google tag (gtag.js) -->
<script async src="https://www.googletagmanager.com/gtag/js?id=G-ETB5ED006N"></script>
<script>
  window.dataLayer = window.dataLayer || [];
  function gtag(){{dataLayer.push(arguments);}}
  gtag('js', new Date());
  gtag('config', 'G-ETB5ED006N');
</script>
  <meta charset="UTF-8">
  <link rel="icon" type="image/x-icon" href="favicon.ico">
  <link rel="icon" type="image/png" sizes="32x32" href="favicon-32x32.png">
  <link rel="apple-touch-icon" sizes="180x180" href="apple-touch-icon.png">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <meta name="description" content="{meta_desc}">
  <meta property="og:type" content="website">
  <meta property="og:site_name" content="CUBOX Modular">
  <meta property="og:title" content="{meta_title}">
  <meta property="og:description" content="{meta_desc}">
  <meta property="og:image" content="https://cuboxmodular.ro/assets/og-image.jpg">
  <meta property="og:image:width" content="1200">
  <meta property="og:image:height" content="630">
  <meta property="og:image:alt" content="CUBOX Modular — Containere modulare {city}">
  <meta name="twitter:card" content="summary_large_image">
  <meta name="twitter:image" content="https://cuboxmodular.ro/assets/og-image.jpg">
  <title>{meta_title}</title>
  <script type="application/ld+json">
{{
  "@context": "https://schema.org",
  "@type": "LocalBusiness",
  "name": "CUBOX Modular",
  "url": "https://cuboxmodular.ro",
  "telephone": "+40728873857",
  "email": "contact@cuboxmodular.ro",
  "image": "https://cuboxmodular.ro/assets/cubox-modular-logo.png",
  "address": {{
    "@type": "PostalAddress",
    "streetAddress": "Strada 1 Mai",
    "addressLocality": "Bacău",
    "postalCode": "600001",
    "addressCountry": "RO"
  }},
  "areaServed": ["{areaServed}", "România"],
  "description": "Containere modulare personalizate livrate în {county_long}. Livrare în 15-21 zile lucrătoare.",
  "priceRange": "2700-9500 EUR"
}}
  </script>
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700;800;900&display=swap" rel="stylesheet">
  <link rel="stylesheet" href="css/style.css?v=8">
  <style>
    .uses-list {{
      list-style: none;
      padding: 0;
      margin: 0 0 32px 0;
      display: grid;
      grid-template-columns: 1fr 1fr;
      gap: 10px;
    }}
    .uses-list li {{
      display: flex;
      align-items: center;
      gap: 10px;
      font-size: 15px;
      font-weight: 500;
      color: #2c3140;
    }}
    .uses-list svg {{
      width: 16px;
      height: 16px;
      flex-shrink: 0;
      color: #1448a0;
    }}
    @media (max-width: 600px) {{
      .uses-list {{ grid-template-columns: 1fr; }}
    }}
    .regional-info {{
      background: #f8f9fb;
      border: 1px solid #e4e7ed;
      border-radius: 14px;
      padding: 36px 40px;
      margin-bottom: 40px;
    }}
    .regional-info h2 {{
      font-size: 26px;
      font-weight: 800;
      color: #0D2849;
      margin-bottom: 16px;
    }}
    .regional-info p {{
      font-size: 16px;
      line-height: 1.7;
      color: #4a5060;
      margin-bottom: 24px;
    }}
    .regional-info h3 {{
      font-size: 18px;
      font-weight: 700;
      color: #0D2849;
      margin-bottom: 12px;
    }}
    .regional-cta-row {{
      display: flex;
      gap: 16px;
      flex-wrap: wrap;
      margin-top: 16px;
    }}
    .model-card {{
      display: block;
      background: #fff;
      border: 1px solid #e4e7ed;
      border-radius: 12px;
      padding: 24px;
      text-decoration: none;
      color: inherit;
      transition: box-shadow 0.2s, border-color 0.2s;
    }}
    .model-card:hover {{
      box-shadow: 0 4px 18px rgba(13,40,73,0.1);
      border-color: #1448a0;
    }}
    .model-card__tag {{
      font-size: 12px;
      font-weight: 700;
      border-radius: 4px;
      padding: 3px 10px;
      display: inline-block;
      margin-bottom: 12px;
    }}
    .model-card__tag--modular {{ color: #1448a0; background: #dce8fb; }}
    .model-card__tag--comercial {{ color: #c47a00; background: #fff3cd; }}
    .model-card__title {{
      font-size: 17px;
      font-weight: 700;
      color: #0D2849;
      margin-bottom: 8px;
    }}
    .model-card__desc {{
      font-size: 14px;
      color: #4a5060;
      margin-bottom: 12px;
      line-height: 1.5;
    }}
    .model-card__price {{
      font-size: 15px;
      font-weight: 800;
      color: #0D2849;
    }}
    .model-card__price span {{
      font-size: 12px;
      font-weight: 500;
      color: #6b7280;
    }}
    .models-grid {{
      display: grid;
      grid-template-columns: repeat(auto-fill, minmax(260px, 1fr));
      gap: 20px;
      margin-bottom: 40px;
    }}
    @media (max-width: 600px) {{
      .regional-info {{ padding: 24px 20px; }}
      .regional-cta-row {{ flex-direction: column; }}
    }}
  </style>
</head>
<body>

  <div class="topbar">
    <div class="topbar__inner">
      <a href="tel:+40728873857" class="topbar__item">
        <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M22 16.92v3a2 2 0 01-2.18 2 19.79 19.79 0 01-8.63-3.07A19.5 19.5 0 013.07 8.81 19.79 19.79 0 010 .18 2 2 0 012 2h3a2 2 0 012 1.72c.127.96.361 1.903.7 2.81a2 2 0 01-.45 2.11L6.09 9.91a16 16 0 006 6l1.27-1.27a2 2 0 012.11-.45c.907.339 1.85.573 2.81.7A2 2 0 0122 16.92z"/></svg>
        <span>0728873857</span>
      </a>
      <div class="topbar__divider"></div>
      <a href="mailto:contact@cuboxmodular.ro" class="topbar__item">
        <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M4 4h16c1.1 0 2 .9 2 2v12c0 1.1-.9 2-2 2H4c-1.1 0-2-.9-2-2V6c0-1.1.9-2 2-2z"/><polyline points="22,6 12,13 2,6"/></svg>
        <span>contact@cuboxmodular.ro</span>
      </a>
    </div>
  </div>

  <header class="header" id="header">
    <div class="header__inner">
      <a href="index.html" class="header__logo">
        <img src="assets/cubox-modular-logo.png" alt="CUBOX Modular Logo">
      </a>
      <nav class="nav">
        <ul class="nav__list" id="nav-list">
          <li class="nav__item--dropdown"><a href="containere-modulare.html">Containere modulare <svg class="nav__chevron" width="12" height="12" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5"><polyline points="6 9 12 15 18 9"/></svg></a><ul class="nav__dropdown"><li><a href="containere-modulare.html#standard">Standard</a></li><li><a href="containere-modulare.html#duble">Duble</a></li><li><a href="containere-modulare.html#terasa">Cu terasă</a></li></ul></li>
          <li class="nav__item--dropdown"><a href="containere-comerciale.html">Containere comerciale <svg class="nav__chevron" width="12" height="12" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5"><polyline points="6 9 12 15 18 9"/></svg></a><ul class="nav__dropdown"><li><a href="containere-comerciale.html#showroom">Showroom</a></li><li><a href="containere-comerciale.html#fastfood">Fast food</a></li></ul></li>
          <li class="nav__item--dropdown"><a href="containere-maritime.html">Containere maritime <svg class="nav__chevron" width="12" height="12" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5"><polyline points="6 9 12 15 18 9"/></svg></a><ul class="nav__dropdown"><li><a href="containere-maritime.html#noi">Noi</a></li><li><a href="containere-maritime.html#sh">Second Hand</a></li></ul></li>
          <li><a href="inchiriere.html">Închiriere containere</a></li>
          <li><a href="proiecte.html">Proiecte</a></li>
          <li><a href="#cerere-oferta" class="nav__cta">Cere ofertă</a></li>
          <li><a href="contact.html">Contact</a></li>
        </ul>
        <button class="nav__burger" id="burger" aria-label="Meniu">
          <span></span><span></span><span></span>
        </button>
      </nav>
    </div>
  </header>

  <div class="page-hero">
    <div class="container">
      <nav class="breadcrumb">
        <a href="index.html">Acasă</a>
        <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><polyline points="9 18 15 12 9 6"/></svg>
        <a href="containere-modulare.html">Containere modulare</a>
        <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><polyline points="9 18 15 12 9 6"/></svg>
        <span>{city}</span>
      </nav>
      <h1 class="page-hero__title">{h1}</h1>
      <p class="page-hero__desc">{hero_desc}</p>
    </div>
  </div>

  <section class="section section--gray">
    <div class="container">

      <div class="regional-info">
        <h2>{intro_title}</h2>
        <p>{intro_text}</p>
        <h3>Utilizări frecvente în {county_long}</h3>
        <ul class="uses-list">
{uses_html}
        </ul>
        <div class="regional-cta-row">
          <a href="containere-modulare.html" class="btn btn--primary">
            Vezi toate modelele
            <svg class="btn__arrow" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5"><path d="M5 12h14M12 5l7 7-7 7"/></svg>
          </a>
          <a href="#cerere-oferta" class="btn btn--outline">
            Cere ofertă pentru {city}
            <svg class="btn__arrow" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5"><path d="M5 12h14M12 5l7 7-7 7"/></svg>
          </a>
        </div>
      </div>

      <div class="product-group-header reveal">
        <span class="product-group-header__tag">Disponibile</span>
        <h2 class="product-group-header__title">Modele cu livrare în {city}</h2>
        <span class="product-group-header__count">11 modele</span>
      </div>

      <div class="models-grid">
        <a href="containere-modulare/container-modular-6x24-alb.html" class="model-card">
          <div class="model-card__tag model-card__tag--modular">Standard</div>
          <p class="model-card__title">Container modular 6×2,4m — Alb</p>
          <p class="model-card__desc">Birou, depozit sau spațiu comercial. Fără autorizație de construcție. Livrat gata montat.</p>
          <div class="model-card__price">de la 2.700 € <span>fără TVA</span></div>
        </a>
        <a href="containere-modulare/container-modular-6x24-gri.html" class="model-card">
          <div class="model-card__tag model-card__tag--modular">Standard</div>
          <p class="model-card__title">Container modular 6×2,4m — Gri antracit</p>
          <p class="model-card__desc">Design modern, finisaj gri antracit. Ideal birou sau depozit. Livrare în {city}.</p>
          <div class="model-card__price">de la 3.000 € <span>fără TVA</span></div>
        </a>
        <a href="containere-modulare/container-modular-dublu-6x48-alb.html" class="model-card">
          <div class="model-card__tag model-card__tag--modular">Dublu</div>
          <p class="model-card__title">Container modular dublu 6×4,8m</p>
          <p class="model-card__desc">28,8 m² — spațiu dublu față de standard. Ideal showroom sau birou mai mare.</p>
          <div class="model-card__price">de la 5.300 € <span>fără TVA</span></div>
        </a>
        <a href="containere-modulare/container-modular-terasa-gri-riflaj-3m.html" class="model-card">
          <div class="model-card__tag model-card__tag--modular">Cu terasă</div>
          <p class="model-card__title">Container modular cu terasă 3m</p>
          <p class="model-card__desc">Spațiu interior + terasă acoperită de 3m. Ideal pentru vacanță, cafenea sau birou.</p>
          <div class="model-card__price">de la 5.900 € <span>fără TVA</span></div>
        </a>
        <a href="containere-comerciale/container-comercial-fastfood-oblon.html" class="model-card">
          <div class="model-card__tag model-card__tag--comercial">Comercial</div>
          <p class="model-card__title">Container fast food cu oblon</p>
          <p class="model-card__desc">Kiosk fast food complet echipat. Gata de vânzare în 15–21 zile lucrătoare.</p>
          <div class="model-card__price">de la 2.850 € <span>fără TVA</span></div>
        </a>
        <a href="containere-comerciale/container-comercial-showroom-vitrina-alb.html" class="model-card">
          <div class="model-card__tag model-card__tag--comercial">Comercial</div>
          <p class="model-card__title">Container showroom cu vitrină</p>
          <p class="model-card__desc">Vitrină panoramică, finisaj premium. Ideal pentru showroom sau magazin stradal.</p>
          <div class="model-card__price">de la 4.500 € <span>fără TVA</span></div>
        </a>
      </div>

      <div style="text-align:center; margin-bottom:20px;">
        <a href="containere-modulare.html" class="btn btn--primary" style="display:inline-flex;">
          Vezi toate cele 11 modele
          <svg class="btn__arrow" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5"><path d="M5 12h14M12 5l7 7-7 7"/></svg>
        </a>
      </div>

    </div>
  </section>

  <section class="section section--blue" id="cerere-oferta">
    <div class="container">
      <div class="form-split">
        <div class="form-split__left reveal">
          <span class="eyebrow" style="color:rgba(245,161,0,0.85)">Livrare în {city}</span>
          <h2 class="section__title section__title--white">Cere ofertă pentru<br>containere în {city}</h2>
          <p class="section__desc section__desc--white" style="margin-bottom:32px">Lasă-ne numărul de telefon și te sunăm în maximum 48 de ore cu detalii complete și prețul final pentru livrare în {county_long}.</p>
          <div class="contact-info">
            <div class="contact-item">
              <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M22 16.92v3a2 2 0 01-2.18 2 19.79 19.79 0 01-8.63-3.07A19.5 19.5 0 013.07 8.81 19.79 19.79 0 010 .18 2 2 0 012 2h3a2 2 0 012 1.72c.127.96.361 1.903.7 2.81a2 2 0 01-.45 2.11L6.09 9.91a16 16 0 006 6l1.27-1.27a2 2 0 012.11-.45c.907.339 1.85.573 2.81.7A2 2 0 0122 16.92z"/></svg>
              <span>Te sunăm în 48 de ore</span>
            </div>
            <div class="contact-item">
              <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><rect x="1" y="3" width="15" height="13"/><polygon points="16 8 20 8 23 11 23 16 16 16 16 8"/><circle cx="5.5" cy="18.5" r="2.5"/><circle cx="18.5" cy="18.5" r="2.5"/></svg>
              <span>Livrare în 15–21 de zile lucrătoare</span>
            </div>
            <div class="contact-item">
              <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M12 22s8-4 8-10V5l-8-3-8 3v7c0 6 8 10 8 10z"/></svg>
              <span>Ofertă fără angajament</span>
            </div>
            <div class="contact-item">
              <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><circle cx="12" cy="12" r="10"/><polyline points="12 6 12 12 16 14"/></svg>
              <span>Răspuns rapid garantat</span>
            </div>
          </div>
        </div>
        <div class="form-split__right reveal reveal-d2">
          <form class="form" id="contact-form">
            <input type="hidden" name="produs" value="Containere modulare {city}">
            <div class="form__row">
              <div class="form__group">
                <label for="nume">Nume și prenume *</label>
                <input type="text" id="nume" name="nume" required placeholder="Ion Popescu">
              </div>
              <div class="form__group">
                <label for="telefon">Telefon *</label>
                <input type="tel" id="telefon" name="telefon" required placeholder="07xx xxx xxx">
              </div>
            </div>
            <div class="form__group">
              <label for="locatie">Locație livrare *</label>
              <input type="text" id="locatie" name="locatie" required placeholder="ex: {city}, str. ...">
            </div>
            <div class="form__group">
              <label for="mesaj">Mesaj (opțional)</label>
              <textarea id="mesaj" name="mesaj" rows="3" placeholder="Spune-ne ce model te interesează sau alte detalii..."></textarea>
            </div>
            <button type="submit" class="btn btn--primary btn--full">
              Trimite cererea
              <svg class="btn__arrow" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5"><path d="M5 12h14M12 5l7 7-7 7"/></svg>
            </button>
            <p class="form__status" id="form-status"></p>
          </form>
        </div>
      </div>
    </div>
  </section>

  <footer class="footer">
    <div class="container">
      <div class="footer__inner">
        <div class="footer__brand">
          <img src="assets/cubox-modular-logo.png" alt="CUBOX Modular" class="footer__logo">
          <p>Containere modulare personalizate.<br>Fabricate în România.</p>
        </div>
        <div class="footer__col">
          <h4>Produse</h4>
          <div class="footer__links">
            <a href="containere-modulare.html">Containere modulare</a>
            <a href="containere-comerciale.html">Containere comerciale</a>
            <a href="containere-maritime.html">Containere maritime</a>
            <a href="inchiriere.html">Închiriere containere</a>
          </div>
        </div>
        <div class="footer__col">
          <h4>Contact &amp; Legal</h4>
          <div class="footer__links">
            <a href="#cerere-oferta">Cere ofertă</a>
            <a href="index.html#cum-functioneaza">Cum funcționează</a>
            <a href="politica-confidentialitate.html">Politică de confidențialitate</a>
            <a href="termeni-si-conditii.html">Termeni și condiții</a>
          </div>
        </div>
      </div>
      <div class="footer__bottom">
        <p>&copy; 2026 CUBOX Modular</p>
      </div>
    </div>
  </footer>

  <div class="sticky-cta" id="sticky-cta">
    <a href="#cerere-oferta" class="btn btn--primary btn--full">Cere ofertă</a>
  </div>
  <script src="js/main.js?v=9"></script>
  <script src="js/cookie-consent.js"></script>
</body>
</html>'''

def make_page(d):
    uses_html = "\n".join([
        f'          <li><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5"><polyline points="20 6 9 17 4 12"/></svg>{u}</li>'
        for u in d["uses"]
    ])
    return TEMPLATE.format(
        meta_title=d["meta_title"],
        meta_desc=d["meta_desc"],
        city=d["city"],
        county=d["county"],
        county_long=d["county_long"],
        areaServed=d["areaServed"],
        h1=d["h1"],
        hero_desc=d["hero_desc"],
        intro_title=d["intro_title"],
        intro_text=d["intro_text"],
        uses_html=uses_html,
    )

for city_data in cities:
    filepath = os.path.join(SITE_PATH, city_data["slug"] + ".html")
    content = make_page(city_data)
    with open(filepath, "w", encoding="utf-8") as f:
        f.write(content)
    print(f"Created: {city_data['slug']}.html")

print("\nDone! All 10 regional pages created.")
