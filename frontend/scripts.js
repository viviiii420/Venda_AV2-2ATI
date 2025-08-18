// scripts.js
// Navegação por teclado e acessibilidade

document.addEventListener('DOMContentLoaded', () => {
  document.body.addEventListener('keydown', (e) => {
    if (e.key === 'Tab') {
      document.body.classList.add('tabbing');
    }
  });
});
