pygame-site
===========

### Rodando localmente

    git clone https://github.com/pygamebrasil/pygame-site.git

Instalando  Mysql e dependencias

	sudo apt-get install mysql-server mysql-client
	sudo apt-get install libmysqlclient-dev
	sudo apt-get install python-dev

*quando você instalar ele vai te pedir uma senha, é necessário que você também coloque essa senha*
*no arquivo models/db_init.py*
    
Instale o pip e virtualenv

    [sudo] apt-get install python-pip && pip install virtualenv

Crie um ambiente com virtualenv

    cd pygame-site/FlaskApp
    virtualenv venv

Ative o ambiente

    source venv/bin/activate
    
E instale as dependencias

    venv/bin/pip install -r requirements.txt


Rodando o servidor

    python FlaskApp/main.py
    

Se tudo ocorrer bem devera aparecer alguma mensagem parecida com isso daqui

    It should display “Running on http://localhost:5000/” or "Running on http://127.0.0.1:5000/". 

CONFIGURAÇÃO DO APACHE + PYTHON + FLASK
----------------------------------------

Esse projeto roda dentro do apache, se voce quer testar localmente dentro do apache é necessário que você siga esses passos:


UBUNTU 14.04

PRIMEIRAMENTE VAMOS INSTALAR  E ABILITA O MODULO mod_wsgi

Abra um terminal e digita o comando:

    sudo apt-get install libapache2-mod-wsgi 

Agora precisamos abilita o modulo novamente no terminal:

    sudo a2enmod wsgi


Agora aperte as teclas Ctrl + C para encerra o servidor e vamos configura o apache

Edite o arquivo 000-default do apache que esta na pasta

    /etc/apache2/sites-enable
    
Dexe Desta forma

    <VirtualHost *:80>
        # The ServerName directive sets the request scheme, hostname and port that
        # the server uses to identify itself. This is used when creating
        # redirection URLs. In the context of virtual hosts, the ServerName
        # specifies what hostname must appear in the request's Host: header to
        # match this virtual host. For the default virtual host (this file) this
        # value is not decisive as it is used as a last resort host regardless.
        # However, you must set it for any further virtual host explicitly.
        #ServerName www.example.com
        ServerName mywebsite.com
        ServerAdmin webmaster@localhost
        WSGIScriptAlias / /var/www/FlaskApp/flaskapp.wsgi
        DocumentRoot /var/www
    
        <Directory /var/www/FlaskApp/FlaskApp/>
            Options Indexes FollowSymLinks MultiViews ExecCGI
            DirectoryIndex index.html index.cgi index.pl index.php index.xhtml index.htm index.wsgi index.py
            AddHandler cgi-script .cgi
            AddHandler wsgi-script .wsgi .py
            AllowOverride All
            Order allow,deny
            allow from all
        </Directory>
        Alias /static /var/www/FlaskApp/FlaskApp/static
    
        <Directory /var/www/FlaskApp/FlaskApp/static/>
                Order allow,deny
                Allow from all
            </Directory>
    
    
        # Available loglevels: trace8, ..., trace1, debug, info, notice, warn,
        # error, crit, alert, emerg.
        # It is also possible to configure the loglevel for particular
        # modules, e.g.
        #LogLevel info ssl:warn
    
        ErrorLog ${APACHE_LOG_DIR}/error.log
        CustomLog ${APACHE_LOG_DIR}/access.log combined
    
        # For most configuration files from conf-available/, which are
        # enabled or disabled at a global level, it is possible to
        # include a line for only one particular virtual host. For example the
        # following line enables the CGI configuration for this host only
        # after it has been globally disabled with "a2disconf".
        #Include conf-available/serve-cgi-bin.conf
    </VirtualHost>
    
    # vim: syntax=apache ts=4 sw=4 sts=4 sr noet
    

So resta agora reiniciar o apache


    sudo service apache2 restart
    
Acesso o seu site agora e veja se esta funcionando 

se estiver ok a mensagem 
    
    Ola Mundo eu Amo Python
    
Devera aparecer é o sinal de que o seu servidor esta pronto para trabalhar com python





