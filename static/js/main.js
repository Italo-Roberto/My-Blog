$(document).ready(function () {
    $('#projeto1').show();
    $('#projeto2').show();
    $('.projeto-hover').hide();

    $('#botao-menu').click(function () { 
        $('#lista').toggle('slow')
        $('#lista').css('display', 'flex');
    });
});

//Efeitos para itens dos projetos
var projetos = document.querySelectorAll('.projeto')
projetos.forEach(projeto => {
    $(projeto).mouseenter(function () { 
    //Usando this para efeito acontecer por item individual e não simultaneamente
        $('.projeto-inner', this).hide('slow');
        $('.projeto-hover', this).show('slow');
    });
    $(projeto).mouseleave(function () { 
        $('.projeto-inner', this).show('slow');
        $('.projeto-hover', this).hide('slow');
    });
});

//Efeitos de scroll
ScrollReveal().reveal('.cabecalho-descricao', {delay: 500})
ScrollReveal().reveal('.cabecalho-img', {delay: 500})
ScrollReveal().reveal('.perfil', {delay: 750})
ScrollReveal().reveal('.descricao-texto', {delay: 1000})
ScrollReveal().reveal('.titulos', {delay: 500})
ScrollReveal().reveal('#python', {delay: 700})
ScrollReveal().reveal('#django', {delay: 800})
ScrollReveal().reveal('#javascript', {delay: 900})
ScrollReveal().reveal('#mysql', {delay: 1000})
ScrollReveal().reveal('.portfolio-itens', {delay: 750})
ScrollReveal().reveal('#contato-desc', {delay: 750})
ScrollReveal().reveal('.contato-item', {delay: 850})

atual = new Date().getFullYear()
document.querySelector('#ano').innerHTML = atual

