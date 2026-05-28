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

// === STICKY MOBILE CTA — două butoane: sună + ofertă ===
const stickyCta      = document.getElementById('sticky-cta');
const contactSection = document.getElementById('cerere-oferta');

if (stickyCta) {
  stickyCta.innerHTML = `
    <a href="tel:+40700000000" class="sticky-cta__call">
      <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" width="18" height="18"><path d="M22 16.92v3a2 2 0 01-2.18 2 19.79 19.79 0 01-8.63-3.07A19.5 19.5 0 013.07 8.81 19.79 19.79 0 010 .18 2 2 0 012 2h3a2 2 0 012 1.72c.127.96.361 1.903.7 2.81a2 2 0 01-.45 2.11L6.09 9.91a16 16 0 006 6l1.27-1.27a2 2 0 012.11-.45c.907.339 1.85.573 2.81.7A2 2 0 0122 16.92z"/></svg>
      Sună acum
    </a>
    <a href="#cerere-oferta" class="sticky-cta__offer btn btn--primary">Cere ofertă</a>
  `;
}

if (stickyCta && contactSection) {
  const hideObserver = new IntersectionObserver((entries) => {
    entries.forEach(entry => {
      stickyCta.style.display = entry.isIntersecting ? 'none' : '';
    });
  }, { threshold: 0.1 });
  hideObserver.observe(contactSection);
}

// === FORMSUBMIT CONFIG ===
const FORM_ENDPOINT = 'https://formsubmit.co/ajax/84f6b09d1213e2b05eadb73b2c4d0a86';

// === BADGE PRODUS SELECTAT ÎN FORMULAR ===
const form   = document.getElementById('contact-form');
const status = document.getElementById('form-status');

if (form) {
  const produsInput = form.querySelector('[name="produs"]');
  if (produsInput && produsInput.value) {
    const badge = document.createElement('div');
    badge.className = 'form__product-badge';
    badge.innerHTML = `
      <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" width="16" height="16"><path d="M20 7H4a2 2 0 00-2 2v6a2 2 0 002 2h16a2 2 0 002-2V9a2 2 0 00-2-2z"/><path d="M16 21V5a2 2 0 00-2-2h-4a2 2 0 00-2 2v16"/></svg>
      <span><strong>Produs selectat:</strong> ${produsInput.value}</span>
    `;
    form.insertBefore(badge, form.firstChild);
  }
}

if (form) {
  form.addEventListener('submit', async (e) => {
    e.preventDefault();
    const submitBtn = form.querySelector('button[type="submit"]');
    const originalText = submitBtn.innerHTML;
    submitBtn.textContent = 'Se trimite...';
    submitBtn.disabled = true;
    status.textContent = '';
    status.className = 'form__status';

    const formData = {
      nume:     form.querySelector('[name="nume"]')?.value || '',
      telefon:  form.querySelector('[name="telefon"]')?.value || '',
      locatie:  form.querySelector('[name="locatie"]')?.value || '',
      mesaj:    form.querySelector('[name="mesaj"]')?.value || '',
      produs:   form.querySelector('[name="produs"]')?.value || '',
      _subject: 'Cerere nouă — cuboxmodular.ro',
      _template: 'table',
    };

    try {
      const res = await fetch(FORM_ENDPOINT, {
        method: 'POST',
        headers: { 'Content-Type': 'application/json', 'Accept': 'application/json' },
        body: JSON.stringify(formData)
      });
      const json = await res.json();
      if (json.success === 'true' || json.success === true) {
        status.textContent = '✓ Cererea a fost trimisă! Te contactăm în cel mult 48 de ore.';
        status.className = 'form__status success';
        form.reset();
      } else {
        throw new Error(json.message);
      }
    } catch {
      status.textContent = '✗ Eroare la trimitere. Sună-ne direct la 0728873857.';
      status.className = 'form__status error';
    } finally {
      submitBtn.innerHTML = originalText;
      submitBtn.disabled = false;
    }
  });
}
