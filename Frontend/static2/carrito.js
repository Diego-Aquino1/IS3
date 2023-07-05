document.addEventListener('DOMContentLoaded', function(){

const envioInput = document.getElementById("envio");
const recojoInput = document.getElementById("recojo");
const formEnvio = document.getElementById("envio_main");
const formRecojo = document.getElementById("recojo_main");
const cenvio = document.getElementsByClassName("envio1");
const crecojo = document.getElementsByClassName("recojo1");

recojoInput.checked = true;
formEnvio.style.display = "none";
formRecojo.style.display = "block";
cenvio[0].classList.remove("activo");
crecojo[0].classList.add("activo");

function activarEnvio() {
  formEnvio.style.display = "block";
  formRecojo.style.display = "none";
  cenvio[0].classList.add("activo");
  crecojo[0].classList.remove("activo");
  envioInput.checked = true;
  recojoInput.checked = false;
}

function activarRecojo() {
  formEnvio.style.display = "none";
  formRecojo.style.display = "block";
  cenvio[0].classList.remove("activo");
  crecojo[0].classList.add("activo");
  envioInput.checked = false;
  recojoInput.checked = true;
}

cenvio[0].addEventListener("click", activarEnvio);
crecojo[0].addEventListener("click", activarRecojo);

envioInput.addEventListener("change", activarEnvio);
recojoInput.addEventListener("change", activarRecojo);

});