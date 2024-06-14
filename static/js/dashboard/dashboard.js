document.addEventListener('DOMContentLoaded', function() {
  const menuToggle = document.getElementById('menu-toggle');
  const sidepanel = document.querySelector('.sidepanel');

  menuToggle.addEventListener('click', function() {
      sidepanel.classList.toggle('open');
  });
});
