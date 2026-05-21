(function () {
  var KEY = 'cubox_cookie_consent';
  if (localStorage.getItem(KEY)) return;

  var css = `
#cb {
  position: fixed;
  bottom: 0;
  left: 0;
  right: 0;
  z-index: 99999;
  background: #0D2849;
  color: #fff;
  padding: 18px 24px;
  display: flex;
  align-items: center;
  gap: 20px;
  flex-wrap: wrap;
  box-shadow: 0 -4px 24px rgba(0,0,0,.22);
  font-family: Inter, system-ui, sans-serif;
  font-size: 13.5px;
  line-height: 1.55;
  animation: cb-slide .35s ease;
}
@keyframes cb-slide {
  from { transform: translateY(100%); opacity: 0; }
  to   { transform: translateY(0);    opacity: 1; }
}
#cb p {
  margin: 0;
  flex: 1 1 280px;
  color: #c8d4e6;
}
#cb p a {
  color: #fff;
  text-decoration: underline;
  text-underline-offset: 2px;
}
#cb-actions {
  display: flex;
  gap: 10px;
  flex-shrink: 0;
}
#cb-accept {
  background: #ED5E16;
  color: #fff;
  border: none;
  padding: 9px 22px;
  border-radius: 6px;
  font-size: 13.5px;
  font-weight: 600;
  cursor: pointer;
  white-space: nowrap;
  transition: background .2s;
}
#cb-accept:hover { background: #d44f08; }
#cb-refuse {
  background: transparent;
  color: #c8d4e6;
  border: 1px solid rgba(255,255,255,.25);
  padding: 9px 18px;
  border-radius: 6px;
  font-size: 13.5px;
  font-weight: 500;
  cursor: pointer;
  white-space: nowrap;
  transition: border-color .2s, color .2s;
}
#cb-refuse:hover { border-color: #fff; color: #fff; }
@media (max-width: 540px) {
  #cb { padding: 16px 16px 24px; }
  #cb-actions { width: 100%; }
  #cb-accept, #cb-refuse { flex: 1; text-align: center; }
}
`;

  var st = document.createElement('style');
  st.textContent = css;
  document.head.appendChild(st);

  var el = document.createElement('div');
  el.id = 'cb';
  el.innerHTML = `
    <p>Folosim cookie-uri necesare pentru funcționarea site-ului. Nu colectăm date de analiză sau marketing fără acordul tău. <a href="/politica-confidentialitate.html">Politică de confidențialitate</a></p>
    <div id="cb-actions">
      <button id="cb-accept">Acceptă</button>
      <button id="cb-refuse">Refuz</button>
    </div>
  `;
  document.body.appendChild(el);

  function dismiss(val) {
    localStorage.setItem(KEY, val);
    el.style.animation = 'none';
    el.style.transition = 'transform .3s ease, opacity .3s ease';
    el.style.transform = 'translateY(100%)';
    el.style.opacity = '0';
    setTimeout(function () { el.remove(); }, 320);
  }

  document.getElementById('cb-accept').addEventListener('click', function () { dismiss('accepted'); });
  document.getElementById('cb-refuse').addEventListener('click', function () { dismiss('refused'); });
})();
