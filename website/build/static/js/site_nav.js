document.addEventListener("DOMContentLoaded",handler);function handler(){console.log('Page loaded, site_nav priming')
const menuIcon=document.querySelector("nav .hamburger");const menu=document.querySelector(".site_nav ul");menuIcon.classList.remove('hidden');menu.classList.remove('open');menuIcon.addEventListener("click",function(e){menu.classList.toggle('open');});console.log('site_nav ready')}