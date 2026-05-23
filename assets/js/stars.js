// Stars background generator for 星穹梦境 theme
// Only activates on pages without wallpaper slideshow (about, message, etc.)
// Pages with wallpaper already have visual richness from the slideshow + aurora
(function() {
  // Skip if page already has wallpaper slideshow or Hero section
  if (document.getElementById('pageSlideshow') || document.getElementById('hero')) {
    return;
  }

  const canvas = document.createElement('canvas');
  canvas.className = 'stars-bg';
  canvas.style.cssText = 'position:fixed;top:0;left:0;width:100%;height:100%;z-index:-2;pointer-events:none;';
  document.body.prepend(canvas);

  const ctx = canvas.getContext('2d');
  let stars = [];
  const STAR_COUNT = 120;

  function resize() {
    canvas.width = window.innerWidth;
    canvas.height = window.innerHeight;
    initStars();
  }

  function initStars() {
    stars = [];
    for (let i = 0; i < STAR_COUNT; i++) {
      stars.push({
        x: Math.random() * canvas.width,
        y: Math.random() * canvas.height,
        r: Math.random() * 1.5 + 0.3,
        alpha: Math.random() * 0.8 + 0.2,
        speed: Math.random() * 0.005 + 0.002,
        phase: Math.random() * Math.PI * 2
      });
    }
  }

  function draw() {
    ctx.clearRect(0, 0, canvas.width, canvas.height);
    const t = Date.now() * 0.001;

    // Respect prefers-reduced-motion
    const reducedMotion = window.matchMedia('(prefers-reduced-motion: reduce)').matches;

    stars.forEach(s => {
      const flicker = reducedMotion ? 1 : (0.5 + 0.5 * Math.sin(t * s.speed * 200 + s.phase));
      ctx.beginPath();
      ctx.arc(s.x, s.y, s.r, 0, Math.PI * 2);
      ctx.fillStyle = `rgba(241, 245, 249, ${s.alpha * flicker})`;
      ctx.fill();
    });

    requestAnimationFrame(draw);
  }

  window.addEventListener('resize', resize);
  resize();
  draw();
})();
