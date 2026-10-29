// Marchează imaginile și filmul generate cu AI (Regulamentul (UE) 2024/1689, art. 50 alin. (4)).
// Eticheta „AI" e text simplu, alb sau negru după cât de deschisă e zona din poză aflată sub ea.
(function () {
  var EXCLUSE = 'header, footer, .topbar, .demo-notice, .cat-header, .anpc-sal, .sale-card, .sticky-cta';

  var st = document.createElement('style');
  st.textContent =
    '.ai-eticheta{position:absolute;z-index:3;pointer-events:none;margin:0;' +
    'font:700 12px/1 Inter,"Segoe UI",system-ui,sans-serif;letter-spacing:.08em;white-space:nowrap;' +
    'color:#fff;text-shadow:0 0 2px rgba(0,0,0,.55),0 0 6px rgba(0,0,0,.3);transition:color .25s,text-shadow .25s}' +
    '.ai-eticheta--inchis{color:#0f1117;text-shadow:0 0 2px rgba(255,255,255,.75),0 0 6px rgba(255,255,255,.4)}' +
    '.ai-eticheta--mica{font-size:11px}' +
    '@media (prefers-reduced-motion:reduce){.ai-eticheta{transition:none}}';
  document.head.appendChild(st);

  var panza = document.createElement('canvas');
  panza.width = 16;
  panza.height = 8;
  var ctx = panza.getContext('2d', { willReadFrequently: true });

  function exclusa(el) {
    var src = (el.getAttribute('src') || '') + ' ' + (el.currentSrc || '');
    return /logo|sigla|\.svg/i.test(src) || el.closest(EXCLUSE);
  }

  function liniar(c) {
    c /= 255;
    return c <= 0.03928 ? c / 12.92 : Math.pow((c + 0.055) / 1.055, 2.4);
  }
  function luminanta(r, g, b) {
    return 0.2126 * liniar(r) + 0.7152 * liniar(g) + 0.0722 * liniar(b);
  }

  // luminanța fundalului din spatele elementului (pentru zonele fără imagine sau transparente)
  function luminantaParinte(el) {
    for (var n = el; n && n.nodeType === 1; n = n.parentElement) {
      var m = getComputedStyle(n).backgroundColor.match(/[\d.]+/g);
      if (m && (m.length < 4 || +m[3] > 0.5)) return luminanta(+m[0], +m[1], +m[2]);
    }
    return 1;
  }

  function fractie(v, liber) {
    if (/%$/.test(v)) return { f: parseFloat(v) / 100 };
    if (/px$/.test(v)) return { px: parseFloat(v) };
    return { f: 0.5 };
  }

  // true = zona de sub etichetă e deschisă la culoare (scrisul trebuie să fie negru)
  function fundalDeschis(media, et) {
    var a = media.getBoundingClientRect();
    var q = et.getBoundingClientRect();
    var natW = media.naturalWidth || media.videoWidth;
    var natH = media.naturalHeight || media.videoHeight;
    if (!natW || !natH || !q.width) return null;
    var cs = getComputedStyle(media);
    var fit = cs.objectFit || 'fill';
    var sx = a.width / natW, sy = a.height / natH, ox = 0, oy = 0;
    if (fit !== 'fill') {
      var s = fit === 'cover' ? Math.max(sx, sy) : fit === 'none' ? 1 : Math.min(sx, sy);
      if (fit === 'scale-down') s = Math.min(1, s);
      var poz = (cs.objectPosition || '50% 50%').split(' ');
      var px = fractie(poz[0]), py = fractie(poz[1] || '50%');
      ox = px.px !== undefined ? px.px : (a.width - natW * s) * px.f;
      oy = py.px !== undefined ? py.px : (a.height - natH * s) * py.f;
      sx = sy = s;
    }
    var nx = (q.left - a.left - ox) / sx, ny = (q.top - a.top - oy) / sy;
    var nw = q.width / sx, nh = q.height / sy;
    var x0 = Math.max(0, nx), y0 = Math.max(0, ny);
    var x1 = Math.min(natW, nx + nw), y1 = Math.min(natH, ny + nh);
    var Lfundal = luminantaParinte(media.parentElement);
    var L;
    if (x1 - x0 < 1 || y1 - y0 < 1) {
      L = Lfundal;
    } else {
      try {
        ctx.clearRect(0, 0, 16, 8);
        ctx.drawImage(media, x0, y0, x1 - x0, y1 - y0, 0, 0, 16, 8);
        var d = ctx.getImageData(0, 0, 16, 8).data, suma = 0;
        for (var i = 0; i < d.length; i += 4) {
          var al = d[i + 3] / 255;
          suma += al * luminanta(d[i], d[i + 1], d[i + 2]) + (1 - al) * Lfundal;
        }
        L = suma / (d.length / 4);
      } catch (e) {
        return null;
      }
    }
    // alege culoarea cu contrastul mai mare (formula WCAG)
    return (L + 0.05) / 0.05 > 1.05 / (L + 0.05);
  }

  function vizibil(media) {
    var cs = getComputedStyle(media);
    return cs.visibility !== 'hidden' && parseFloat(cs.opacity) >= 0.5;
  }

  function pozitioneaza(media, et) {
    var par = et.parentElement;
    var a = media.getBoundingClientRect();
    var c = par.getBoundingClientRect();
    if (a.width < 2 || a.height < 2 || !vizibil(media)) { et.style.display = 'none'; return; }
    et.style.display = '';
    var mica = a.width < 220;
    if (et.classList.contains('ai-eticheta--mica') !== mica) et.classList.toggle('ai-eticheta--mica', mica);
    // colțul din dreapta-sus: jos-stânga e ocupat des de texte și numerotări peste poze
    var stanga = a.right - c.left - par.clientLeft + par.scrollLeft - et.offsetWidth - 10;
    var sus = a.top - c.top - par.clientTop + par.scrollTop + 10;
    et.style.left = Math.round(stanga) + 'px';
    et.style.top = Math.round(sus) + 'px';
    coloreaza(media, et);
  }

  function coloreaza(media, et) {
    var deschis = fundalDeschis(media, et);
    if (deschis === null) return;
    if (et.classList.contains('ai-eticheta--inchis') !== deschis) et.classList.toggle('ai-eticheta--inchis', deschis);
  }

  var perechi = [];
  function marcheaza(media, text) {
    if (media.dataset.aiMarcat || exclusa(media)) return;
    media.dataset.aiMarcat = '1';
    if (media.tagName === 'IMG') {
      var alt = media.getAttribute('alt') || '';
      if (!/generat[ăa] cu AI/i.test(alt)) media.setAttribute('alt', (alt ? alt + ' — ' : '') + 'imagine generată cu AI');
    } else if (!media.getAttribute('aria-label')) {
      media.setAttribute('aria-label', 'Video generat cu AI');
    }
    var par = media.parentElement;
    if (getComputedStyle(par).position === 'static') par.style.position = 'relative';
    var et = document.createElement('span');
    et.className = 'ai-eticheta';
    et.textContent = text;
    et.setAttribute('aria-hidden', 'true');
    par.appendChild(et);
    perechi.push([media, et]);
    pozitioneaza(media, et);
    media.addEventListener('load', function () { pozitioneaza(media, et); });
    media.addEventListener('transitionend', function () { pozitioneaza(media, et); });
    if (media.tagName === 'VIDEO') {
      // filmul își schimbă scena: recalculez culoarea cât timp rulează
      setInterval(function () {
        if (!media.paused && et.style.display !== 'none') coloreaza(media, et);
      }, 600);
    }
    if (window.ResizeObserver) {
      var ro = new ResizeObserver(function () { pozitioneaza(media, et); });
      ro.observe(media);
      ro.observe(par);
    }
  }

  function toate() {
    document.querySelectorAll('img').forEach(function (im) { marcheaza(im, 'AI'); });
    document.querySelectorAll('video').forEach(function (v) { marcheaza(v, 'AI'); });
  }

  var asteapta = false;
  function repozitioneaza() {
    if (asteapta) return;
    asteapta = true;
    requestAnimationFrame(function () {
      asteapta = false;
      perechi.forEach(function (p) { pozitioneaza(p[0], p[1]); });
    });
  }

  toate();
  window.addEventListener('load', function () { toate(); repozitioneaza(); });
  window.addEventListener('resize', repozitioneaza);
  // galeriile își schimbă imaginea activă prin clase: repoziționez la orice schimbare de clasă
  function aEticheta(n) {
    return n && n.nodeType === 1 ? n.classList.contains('ai-eticheta') : !!(n && n.parentElement && n.parentElement.classList.contains('ai-eticheta'));
  }
  new MutationObserver(function (m) {
    var straine = m.filter(function (x) {
      if (aEticheta(x.target)) return false;
      if (x.type === 'childList') {
        var toateEtichete = [].slice.call(x.addedNodes).concat([].slice.call(x.removedNodes)).every(aEticheta);
        return !toateEtichete;
      }
      return true;
    });
    if (!straine.length) return;
    if (straine.some(function (x) { return x.type === 'childList'; })) toate();
    repozitioneaza();
  }).observe(document.body, { subtree: true, childList: true, attributes: true, attributeFilter: ['class', 'src'] });
})();
