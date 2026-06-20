document.addEventListener('DOMContentLoaded', () => {
  // ── Mobile navbar menu ────────────────────────────
  const menuBtn = document.getElementById('pubMenu');
  const mobileMenu = document.getElementById('pubMobileMenu');
  if (menuBtn && mobileMenu) {
    menuBtn.addEventListener('click', () => {
      mobileMenu.classList.toggle('open');
    });
    // Close on link click
    mobileMenu.querySelectorAll('a').forEach(link => {
      link.addEventListener('click', () => {
        mobileMenu.classList.remove('open');
      });
    });
  }

  // ── Admin sidebar mobile toggle ───────────────────
  const adminMenu = document.getElementById('menuToggle');
  const sidebar = document.getElementById('sidebar');
  if (adminMenu && sidebar) {
    adminMenu.addEventListener('click', () => {
      sidebar.classList.toggle('open');
    });
    // Close sidebar on link click
    document.addEventListener('click', (e) => {
      if (!sidebar.contains(e.target) && !adminMenu.contains(e.target)) {
        sidebar.classList.remove('open');
      }
    });
  }

  // ── Set current date ──────────────────────────────
  const dateEl = document.getElementById('currentDate');
  if (dateEl) {
    dateEl.textContent = new Date().toLocaleDateString('en-US', {
      weekday: 'long', year: 'numeric', month: 'long', day: 'numeric'
    });
  }

  // ── Image upload preview ──────────────────────────
  document.querySelectorAll('input[type="file"]').forEach(input => {
    const preview = document.getElementById(input.dataset.preview);
    if (!preview) return;
    input.addEventListener('change', (e) => {
      const file = e.target.files[0];
      if (file) {
        const reader = new FileReader();
        reader.onload = (evt) => {
          preview.src = evt.target.result;
          preview.classList.add('show');
        };
        reader.readAsDataURL(file);
      }
    });
  });

});
