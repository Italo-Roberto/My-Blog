<h1>Blog Pessoal</h1>
<img src="https://www.djangoproject.com/m/img/logos/django-logo-negative.png" width="580px" height="275px" alt="Django Logo">

<p>A intenção com este projeto foi colocar em prática meus conhecimentos em Python e Django.</p>

<h3>Tecnologias Utilizadas:</h3>
<ul>
    <li>Python</li>
    <li>Django</li>
    <li>Mysql</li>
    <li>Jquery</li>
</ul>

<hr>

<p>
    Este projeto serve de base para qualquer blog básico que utilize o django. Neste projeto foi utilizando o módulo de autenticação padrão do django para login e cadastro de usuários, armazenamento de imagens e conexão com base de dados relacional (MySql). A página se divide nas seguinte seções: Cabeçalho com a sinformações principais sobre o autor, portfólio de projetos publicados, lista de postagens e informações de contato.
</p>

<h2>Instruções de instalação</h2>

<p>
    <strong>Pré requisitos:</strong>
    <br>
    <ul>
        <li>Python 3.10.2 (ou superior)</li>
        <li>Virtualenv 20.14.0 (ou superior)</li>
        <li>Pip 21.2.4 (ou superior)</li>
        <li>Mysql Community Server ou Workbench 8.0 (ou superior)</li>
    </ul>
</p>

  <strong>Instalação</strong>
  
  Clone este repositório para sua máquina:      
`git clone https://github.com/Italo-Roberto/myblog.git`
  
  Após realizar o clone do repositório, entre no diretório <strong>myblog</strong> e crie uma Virtualenv: <br>
 `cd myblog/`
 `virtualenv nome_veenv`

  Necessário ativar veenv após sua criação: <br>
  Linux, MacOS: `source nome_veenv/bin/activate` <br>
  Windows: `nome_veenv/Scripts/Activate`
  
  Agora iremos instalar os pacotes necessário para rodar o projeto, através do arquivo requirements.txt (incluindo o Django) <br>
 `pip install -r requirements.txt`

  Necessário criar a tabela no banco de dados por comando <br>
 `CREATE DATABASE db_name;`

  Antes de inicar o projeto, devemos fazer a migrações iniciais das tabelas no banco de dados <br>
 `python manage.py migrate`
 
  Iniciando projeto e servidor de desenvolvimento <br>
  `python manage.py runserver`

<p>
    <strong>Utilização e personalização:</strong>
    <br>
    <p>
        Este projeto e opensource, ou seja, você pode edita-lo para uso próprio, servindo de base para uma aplicação de blog pessoal.
    </p>
</p>
