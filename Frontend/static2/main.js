document.addEventListener('DOMContentLoaded', function(){

    const menubutton = document.getElementById('menubutton');
    const menubutton2 = document.getElementById('menubutton2')
    const menu = document.getElementById('menu');

    menubutton.addEventListener('click', function(){
        menu.classList.toggle('open');
    });
    menubutton2.addEventListener('click', function(){
        menu.classList.remove('open');
    });

});