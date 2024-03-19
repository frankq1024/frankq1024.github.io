document.addEventListener("DOMContentLoaded", loadParticles, false);

window.addEventListener("resize", loadParticles, false);

function loadParticles() {
  particlesJS.load("particles-js", "/assets/json/particles.json", function () {
    console.log("particles.js loaded - callback");
  });
}
