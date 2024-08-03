# send_mail
Sobre o Projeto

Esta solução foi desenvolvida para resolver um problema relatado pela equipe de suporte, que considerava trabalhoso informar manualmente os clientes sobre novas funcionalidades por e-mail. O objetivo do projeto é automatizar a criação e o envio desses e-mails, simplificando o processo e reduzindo o esforço manual.
Funcionalidades

    Criação Automática de E-mails: Gera e-mails contendo informações sobre novas funcionalidades.
    Envio em Massa: Envia automaticamente e-mails para uma lista de clientes.

Tecnologias Utilizadas

As seguintes tecnologias foram utilizadas para desenvolver esta solução:

    SMTP (Simple Mail Transfer Protocol): Utilizado para o envio de e-mails.
        Biblioteca: smtplib

    MIME (Multipurpose Internet Mail Extensions): Utilizado para criar e estruturar mensagens de e-mail com múltiplos tipos de conteúdo, como texto e imagens.
        Bibliotecas:
            email.mime.multipart.MIMEMultipart
            email.mime.text.MIMEText
            email.mime.image.MIMEImage

    Pandas: Biblioteca de análise de dados usada para manipulação e leitura de dados, neste caso, para ler e processar o arquivo CSV contendo dados dos clientes.
        Biblioteca: pandas