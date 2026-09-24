/* Happexhibition — main.js
   Interactions generated from the Figma motion spec. */
(function () {
  const reduced = window.matchMedia('(prefers-reduced-motion: reduce)').matches;

  /* ---------- Header: transparent→solid + hide/show on scroll ---------- */
  const header = document.querySelector('.site-header');
  if (header) {
    const startsTransparent = header.classList.contains('transparent');
    let lastY = window.scrollY;
    const onScroll = () => {
      const y = window.scrollY;
      if (startsTransparent) {
        if (y > 80) { header.classList.add('scrolled'); header.classList.remove('transparent'); }
        else { header.classList.remove('scrolled'); header.classList.add('transparent'); }
      }
      if (y > 240 && y > lastY) header.classList.add('hidden');
      else header.classList.remove('hidden');
      lastY = y;
    };
    window.addEventListener('scroll', onScroll, { passive: true });
    onScroll();
  }

  /* ---------- Works mega dropdown (click, persists until outside click) ---------- */
  const worksBtn = document.querySelector('.nav-works');
  const mega = document.querySelector('.mega');
  if (worksBtn && mega) {
    worksBtn.addEventListener('click', (e) => {
      e.stopPropagation();
      mega.classList.toggle('open');
    });
    document.addEventListener('click', (e) => {
      if (!mega.contains(e.target)) mega.classList.remove('open');
    });
  }

  /* ---------- Mobile menu ---------- */
  const burger = document.querySelector('.burger');
  const mobileMenu = document.querySelector('.mobile-menu');
  if (burger && mobileMenu) {
    burger.addEventListener('click', () => mobileMenu.classList.add('open'));
    mobileMenu.querySelector('.close-btn').addEventListener('click', () => mobileMenu.classList.remove('open'));
    mobileMenu.querySelectorAll('a').forEach(a => a.addEventListener('click', () => mobileMenu.classList.remove('open')));
  }

  /* ---------- Hero slider: crossfade, 3s autoplay, arrows ---------- */
  const hero = document.querySelector('.hero');
  if (hero) {
    const slides = [...hero.querySelectorAll('.slide')];
    let i = 0, timer = null;
    const show = (n) => {
      slides[i].classList.remove('active');
      i = (n + slides.length) % slides.length;
      slides[i].classList.add('active');
    };
    const next = () => show(i + 1);
    const restart = () => {
      if (timer) clearInterval(timer);
      if (!reduced && slides.length > 1) timer = setInterval(next, 4000);
    };
    hero.querySelector('.arr-next')?.addEventListener('click', () => { next(); restart(); });
    hero.querySelector('.arr-prev')?.addEventListener('click', () => { show(i - 1); restart(); });
    restart();
  }

  /* ---------- Count-up stats ---------- */
  const counters = document.querySelectorAll('[data-count]');
  if (counters.length) {
    const io = new IntersectionObserver((entries) => {
      entries.forEach((en) => {
        if (!en.isIntersecting) return;
        const el = en.target;
        io.unobserve(el);
        const target = parseFloat(el.dataset.count.replace(/,/g, ''));
        const suffix = el.dataset.suffix || '';
        if (reduced) { el.textContent = el.dataset.count + suffix; return; }
        const t0 = performance.now(), dur = 1400;
        const tick = (t) => {
          const p = Math.min(1, (t - t0) / dur);
          const eased = 1 - Math.pow(1 - p, 3);
          el.textContent = Math.round(target * eased).toLocaleString() + suffix;
          if (p < 1) requestAnimationFrame(tick);
        };
        requestAnimationFrame(tick);
      });
    }, { threshold: 0.4 });
    counters.forEach((c) => io.observe(c));
  }

  /* ---------- Reveal on scroll ---------- */
  const reveals = document.querySelectorAll('.reveal');
  if (reveals.length && !reduced) {
    const io2 = new IntersectionObserver((entries) => {
      entries.forEach((en) => { if (en.isIntersecting) { en.target.classList.add('in'); io2.unobserve(en.target); } });
    }, { threshold: 0.18 });
    reveals.forEach((r) => io2.observe(r));
  } else {
    reveals.forEach((r) => r.classList.add('in'));
  }

  /* ---------- Works category filter ---------- */
  const chips = document.querySelectorAll('.filter-bar .chip[data-filter]');
  const workCards = document.querySelectorAll('.work-grid [data-cat]');
  if (chips.length && workCards.length) {
    chips.forEach((chip) => chip.addEventListener('click', () => {
      chips.forEach((c) => c.classList.remove('active'));
      chip.classList.add('active');
      const f = chip.dataset.filter;
      let visible = 0;
      workCards.forEach((card) => {
        const show = f === 'all' || card.dataset.cat === f;
        card.style.display = show ? '' : 'none';
        if (show) visible++;
      });
      const count = document.querySelector('[data-result-count]');
      if (count) count.textContent = visible + ' project' + (visible === 1 ? '' : 's');
      const empty = document.querySelector('[data-empty]');
      if (empty) empty.style.display = visible ? 'none' : 'block';
    }));
  }

  /* ---------- Services sticky-nav active state ---------- */
  const svcLinks = document.querySelectorAll('.svc-nav a[href^="#"]');
  if (svcLinks.length) {
    const blocks = [...svcLinks].map((a) => document.querySelector(a.getAttribute('href'))).filter(Boolean);
    const io3 = new IntersectionObserver((entries) => {
      entries.forEach((en) => {
        if (en.isIntersecting) {
          svcLinks.forEach((a) => a.classList.toggle('active', a.getAttribute('href') === '#' + en.target.id));
        }
      });
    }, { rootMargin: '-30% 0px -60% 0px' });
    blocks.forEach((b) => io3.observe(b));
  }

  /* ---------- EN/TH language toggle ---------- */
  const langBtns = document.querySelectorAll('.lang-btn');
  if (langBtns.length) {
    let note = null;
    langBtns.forEach((b) => b.addEventListener('click', () => {
      langBtns.forEach((x) => x.classList.remove('active'));
      b.classList.add('active');
      if (b.dataset.lang === 'th') {
        if (!note) {
          note = document.createElement('div');
          note.className = 'lang-note';
          note.textContent = 'เวอร์ชันภาษาไทยเร็ว ๆ นี้ — Thai version coming soon';
          document.body.appendChild(note);
        }
        note.classList.add('show');
        setTimeout(() => note.classList.remove('show'), 2400);
      }
    }));
  }
})();
