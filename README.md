pygame-site
===========



CONFIGURAÇÃO DO APACHE + PYTHON + FLASK
========================================

UBUNTU 14.04

PRIMEIRAMENTE VAMOS INSTALAR  E ABILITA O MODULO mod_wsgi

Abra um terminal e digita o comando:

sudo apt-get install libapache2-mod-wsgi 

Agora precisamos abilita o modulo novamente no terminal:

sudo a2enmod wsgi

Criando a Flask App
-------------------

Com o terminal aberto digita

    cd /var/www

em seguida vamos criar o diretorio do flask

    sudo mkdir FlaskApp

vamos entra no diretorio que acabamos de criar

    cd FlaskApp

dentro deste diretorio vamos criar mais 2 

    sudo mkdir static templates


e nossa arvore de diretorios deve esta assim:

|----FlaskApp

|---------FlaskApp

|--------------static

|--------------templates

Agora vamos criar um aquivo de texto com o nome de \__init__.py

abra o mesmo com seu editor preferido no meu caso estou usando o nano

    sudo nano \__init__.py


e escreva o conteudo abaixo

    from flask import Flask
    app = Flask(__name__)
    @app.route("/")
    def hello():
    return "Hello, I love Digital Ocean!"   
    if \__name__ == "__main__":
    app.run()
