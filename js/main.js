// === SUNET VIDEO HERO ===
const video       = document.getElementById('hero-video');
const soundBtn    = document.getElementById('sound-toggle');
const iconMuted   = document.getElementById('icon-muted');
const iconSound   = document.getElementById('icon-sound');

if (video) {
  const tryPlay = () => {
    video.muted = true;
    const p = video.play();
    if (p) p.catch(() => {});
  };

  // Incearca imediat
  tryPlay();

  // Retry dupa 300ms (iOS are nevoie de timp dupa load)
  setTimeout(tryPlay, 300);

  // Cand video intra in viewport (iOS nu autoplay off-screen)
  if ('IntersectionObserver' in window) {
    new IntersectionObserver((entries) => {
      entries.forEach(e => { if (e.isIntersecting) tryPlay(); });
    }, { threshold: 0.1 }).observe(video);
  }

  // Fallback: primul touch pe pagina
  document.addEventListener('touchstart', tryPlay, { once: true, passive: true });
}

if (soundBtn && video) {
  soundBtn.addEventListener('click', () => {
    video.muted = !video.muted;
    iconMuted.style.display = video.muted ? '' : 'none';
    iconSound.style.display = video.muted ? 'none' : '';
    soundBtn.classList.toggle('active', !video.muted);
  });
}

// === CARD IMAGE SLIDESHOW ON HOVER ===
document.querySelectorAll('.card[data-images]').forEach(card => {
  const imgEl = card.querySelector('.card__img-wrap img');
  const images = JSON.parse(card.dataset.images);
  if (images.length <= 1) return;
  let interval = null, idx = 0;

  card.addEventListener('mouseenter', () => {
    interval = setInterval(() => {
      imgEl.style.opacity = '0';
      setTimeout(() => {
        idx = (idx + 1) % images.length;
        imgEl.src = images[idx];
        imgEl.style.opacity = '1';
      }, 320);
    }, 1300);
  });

  card.addEventListener('mouseleave', () => {
    clearInterval(interval);
    interval = null;
    imgEl.style.opacity = '0';
    setTimeout(() => {
      idx = 0;
      imgEl.src = images[0];
      imgEl.style.opacity = '1';
    }, 320);
  });
});

// === PRODUCT PAGE IMAGE GALLERY ===
document.querySelectorAll('.pg-gallery').forEach(gallery => {
  const slides = gallery.querySelectorAll('.pg-gallery__slide');
  const dots   = gallery.querySelectorAll('.pg-gallery__dot');
  if (slides.length <= 1) return;

  let current = 0;

  function goTo(idx) {
    slides[current].classList.remove('active');
    dots[current] && dots[current].classList.remove('active');
    current = (idx + slides.length) % slides.length;
    slides[current].classList.add('active');
    dots[current] && dots[current].classList.add('active');
  }

  const prevBtn = gallery.querySelector('.pg-gallery__arrow--prev');
  const nextBtn = gallery.querySelector('.pg-gallery__arrow--next');
  prevBtn && prevBtn.addEventListener('click', e => { e.preventDefault(); goTo(current - 1); });
  nextBtn && nextBtn.addEventListener('click', e => { e.preventDefault(); goTo(current + 1); });
  dots.forEach((dot, i) => dot.addEventListener('click', () => goTo(i)));
});

// === BURGER MENU ===
const burger  = document.getElementById('burger');
const navList = document.getElementById('nav-list');

burger.addEventListener('click', () => {
  navList.classList.toggle('open');
  burger.classList.toggle('open');
});
navList.querySelectorAll('a:not(.nav__dropdown a)').forEach(link => {
  link.addEventListener('click', () => {
    navList.classList.remove('open');
    burger.classList.remove('open');
  });
});

// === DROPDOWN NAV — toggle mobil ===
document.querySelectorAll('.nav__item--dropdown > a').forEach(link => {
  link.addEventListener('click', function(e) {
    if (window.innerWidth <= 1100) {
      const li = this.closest('.nav__item--dropdown');
      if (!li.classList.contains('open')) {
        e.preventDefault();
        li.classList.add('open');
      }
    }
  });
});

// === SMOOTH SCROLL cu offset header ===
document.querySelectorAll('a[href^="#"]').forEach(anchor => {
  anchor.addEventListener('click', function(e) {
    const href = this.getAttribute('href');
    if (href === '#') return;
    const target = document.querySelector(href);
    if (!target) return;
    e.preventDefault();
    const header  = document.querySelector('.header');
    const topbar  = document.querySelector('.topbar');
    const offset  = (header ? header.offsetHeight : 0)
                  + (topbar && topbar.offsetHeight > 0 ? topbar.offsetHeight : 0)
                  + 16;
    const top = target.getBoundingClientRect().top + window.pageYOffset - offset;
    window.scrollTo({ top: Math.max(0, top), behavior: 'smooth' });
  });
});

// === SCROLL REVEAL ===
const revealObserver = new IntersectionObserver((entries) => {
  entries.forEach(entry => {
    if (entry.isIntersecting) {
      entry.target.classList.add('visible');
      revealObserver.unobserve(entry.target);
    }
  });
}, { threshold: 0.1, rootMargin: '0px 0px -40px 0px' });

document.querySelectorAll('.reveal').forEach(el => revealObserver.observe(el));

// === SITE DEMONSTRATIV — formularul nu mai trimite nimic; contact UNOMATEC ===
const SALE_MAIL = 'unomatec90@gmail.com';
const SALE_HREF = 'mailto:' + SALE_MAIL + '?subject=' + encodeURIComponent('Site personalizat (model CUBOX Modular)');
const MAIL_ICON = '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" aria-hidden="true"><path d="M4 4h16c1.1 0 2 .9 2 2v12c0 1.1-.9 2-2 2H4c-1.1 0-2-.9-2-2V6c0-1.1.9-2 2-2z"/><polyline points="22,6 12,13 2,6"/></svg>';

const contactGrid = document.querySelector('.contact-grid');
const saleHost = document.querySelector('#cerere-oferta .container')
  || (contactGrid && contactGrid.closest('.container'));

if (saleHost) {
  saleHost.innerHTML = `
    <div class="sale-card">
      <div class="sale-card__body">
        <p class="sale-card__eyebrow">Site demonstrativ</p>
        <h2 class="sale-card__title">Acest site este un model de prezentare.</h2>
        <p class="sale-card__text">Produsele și prețurile sunt exemple și nu se vând. Realizăm un site personalizat pentru afacerea ta.</p>
      </div>
      <a href="${SALE_HREF}" class="btn btn--primary sale-card__cta" data-sale-cta="card">${MAIL_ICON}${SALE_MAIL}</a>
    </div>
  `;
}

let stickyCta = document.getElementById('sticky-cta');
if (!stickyCta) {
  stickyCta = document.createElement('div');
  stickyCta.id = 'sticky-cta';
  stickyCta.className = 'sticky-cta';
  document.body.appendChild(stickyCta);
}
stickyCta.classList.add('sticky-cta--sale');
stickyCta.innerHTML = `
  <p class="sale-sticky__text"><strong>Containerele nu se vând.</strong> Vrei un site ca acesta?</p>
  <a href="${SALE_HREF}" class="btn btn--primary sale-sticky__cta" data-sale-cta="mobil">${MAIL_ICON}Scrie-ne</a>
`;

const saleCard = document.querySelector('.sale-card');
if (saleCard) {
  new IntersectionObserver((entries) => {
    entries.forEach(entry => {
      stickyCta.style.display = entry.isIntersecting ? 'none' : '';
    });
  }, { threshold: 0.1 }).observe(saleCard);
}

// === GA4 EVENTS ===
function trackEvent(name, params) {
  if (typeof gtag === 'function') gtag('event', name, params);
}

document.querySelectorAll('a[href^="tel:"]').forEach(el => {
  el.addEventListener('click', () => trackEvent('click_telefon', { event_category: 'contact' }));
});

document.querySelectorAll('a[href^="mailto:"]').forEach(el => {
  el.addEventListener('click', () => trackEvent('click_email', { event_category: 'contact' }));
});

document.addEventListener('click', (e) => {
  const cta = e.target.closest('[data-sale-cta]');
  if (cta) trackEvent('click_site_de_vanzare', { event_category: 'vanzare_site', pozitie: cta.dataset.saleCta });
});

if (saleCard) {
  const fvObs = new IntersectionObserver((entries) => {
    entries.forEach(e => {
      if (e.isIntersecting) {
        trackEvent('view_site_de_vanzare', { event_category: 'vanzare_site' });
        fvObs.disconnect();
      }
    });
  }, { threshold: 0.3 });
  fvObs.observe(saleCard);
}
