document.addEventListener('DOMContentLoaded', () => {

  // ── Current date ──────────────────────────────────
  const dateEl = document.getElementById('currentDate');
  if (dateEl) {
    dateEl.textContent = new Date().toLocaleDateString('en-US', {
      weekday: 'long', year: 'numeric', month: 'long', day: 'numeric'
    });
  }

  // ── Mobile sidebar toggle ─────────────────────────
  const menuBtn = document.getElementById('menuToggle');
  const sidebar = document.getElementById('sidebar');
  if (menuBtn && sidebar) {
    menuBtn.addEventListener('click', () => {
      sidebar.classList.toggle('open');
    });
    document.addEventListener('click', (e) => {
      if (!sidebar.contains(e.target) && !menuBtn.contains(e.target)) {
        sidebar.classList.remove('open');
      }
    });
  }

  // ── Count-up animation ────────────────────────────
  document.querySelectorAll('.count-up').forEach(el => {
    const target = parseInt(el.textContent, 10);
    if (isNaN(target) || target === 0) return;
    let current = 0;
    const step = Math.ceil(target / 40);
    const timer = setInterval(() => {
      current = Math.min(current + step, target);
      el.textContent = current;
      if (current >= target) clearInterval(timer);
    }, 20);
  });

  // ── Charts ────────────────────────────────────────
  const data = window.DASHBOARD_DATA || {};
  const isDark = window.matchMedia('(prefers-color-scheme: dark)').matches;
  const gridColor = isDark ? 'rgba(255,255,255,0.06)' : 'rgba(0,0,0,0.06)';
  const tickColor = isDark ? 'rgba(255,255,255,0.35)' : 'rgba(0,0,0,0.35)';
  const labelFont = { size: 11, family: "-apple-system,BlinkMacSystemFont,'Segoe UI',sans-serif" };

  // Booking bar chart
  const bookCtx = document.getElementById('bookingChart');
  if (bookCtx) {
    new Chart(bookCtx, {
      type: 'bar',
      data: {
        labels: ['Online', 'Walk-in'],
        datasets: [{
          label: 'Bookings',
          data: [data.totalOnline || 0, data.totalOffline || 0],
          backgroundColor: ['#534AB7', '#1D9E75'],
          borderRadius: 6,
          borderSkipped: false,
          barThickness: 48,
        }]
      },
      options: {
        responsive: true,
        maintainAspectRatio: false,
        plugins: { legend: { display: false } },
        scales: {
          x: {
            grid: { display: false },
            ticks: { color: tickColor, font: labelFont }
          },
          y: {
            grid: { color: gridColor },
            ticks: { color: tickColor, font: labelFont, stepSize: 1 },
            beginAtZero: true
          }
        },
        animation: { duration: 600, easing: 'easeOutQuart' }
      }
    });
  }

  // Room type doughnut chart
  const roomCtx = document.getElementById('roomTypeChart');
  if (roomCtx && data.roomTypes && data.roomTypes.length > 0) {
    const COLORS = ['#534AB7', '#1D9E75', '#BA7517', '#D85A30', '#378ADD', '#639922'];
    new Chart(roomCtx, {
      type: 'doughnut',
      data: {
        labels: data.roomTypes.map(r => r.label),
        datasets: [{
          data: data.roomTypes.map(r => r.count),
          backgroundColor: COLORS.slice(0, data.roomTypes.length),
          borderWidth: 0,
          hoverOffset: 8
        }]
      },
      options: {
        responsive: true,
        maintainAspectRatio: false,
        cutout: '65%',
        plugins: { legend: { display: false } },
        animation: { duration: 700, easing: 'easeOutQuart' }
      }
    });
  } else if (roomCtx) {
    // Placeholder if no rooms
    new Chart(roomCtx, {
      type: 'doughnut',
      data: {
        labels: ['No rooms added'],
        datasets: [{ data: [1], backgroundColor: ['#D3D1C7'], borderWidth: 0 }]
      },
      options: {
        responsive: true, maintainAspectRatio: false, cutout: '65%',
        plugins: { legend: { display: false } }
      }
    });
  }

  // ── Progress bar entrance animation ──────────────
  const fills = document.querySelectorAll('.progress-fill');
  fills.forEach(el => {
    const target = el.style.width;
    el.style.width = '0';
    requestAnimationFrame(() => {
      requestAnimationFrame(() => { el.style.width = target; });
    });
  });

  // ── Active nav highlight ──────────────────────────
  const path = window.location.pathname;
  document.querySelectorAll('.nav-item[href]').forEach(link => {
    if (link.getAttribute('href') === path) {
      document.querySelectorAll('.nav-item.active').forEach(a => a.classList.remove('active'));
      link.classList.add('active');
    }
  });

});
