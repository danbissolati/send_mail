import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.image import MIMEImage
import pandas as pd

def send_email(to_address, subject, body):
    from_address = "" # Insira o e-mail
    password = "" # Insira a senha do e-mail

    # Configurar o servidor SMTP
    server = smtplib.SMTP('', 587) # Insira o SMTP do servidor
    server.starttls()
    server.login(from_address, password)

    # Criar a mensagem
    msg = MIMEMultipart('related')
    msg['From'] = from_address
    msg['To'] = to_address
    msg['Subject'] = subject

    # Criar a parte do corpo do e-mail
    msg_alternative = MIMEMultipart('alternative')
    msg.attach(msg_alternative)

    # Anexar o corpo do e-mail
    msg_text = MIMEText(body, 'html')
    msg_alternative.attach(msg_text)

    # Anexar a imagem incorporada
    with open(image_path, 'rb') as img:
        mime_image = MIMEImage(img.read())
        mime_image.add_header('Content-ID', '<image1>')
        mime_image.add_header('Content-Disposition', 'inline', filename='assinatura.png')
        msg.attach(mime_image)

    # Enviar o e-mail
    server.send_message(msg)
    server.quit()

# Leia o arquivo CSV
try:
    df = pd.read_csv(r'') # Insira o Caminho do arquivo .CSV
    # Verifique se as colunas 'email' e 'nome' existem
    if 'email' not in df.columns or 'nome' not in df.columns:
        raise KeyError("O arquivo CSV deve conter as colunas 'email' e 'nome'.")
except FileNotFoundError:
    print("Erro: O arquivo 'CSV' não foi encontrado.")
    exit()
except pd.errors.EmptyDataError:
    print("Erro: O arquivo 'CSV' está vazio.")
    exit()
except pd.errors.ParserError:
    print("Erro: O arquivo 'CSV' está mal formatado.")
    exit()
except Exception as e:
    print(f"Erro inesperado: {e}")
    exit()

clientes = df.to_dict(orient='records')

# Caminho para a imagem
image_path = r'B:\Desktop\send_mail\ass.png'

# Enviar e-mails individualmente
for cliente in clientes:
    email = cliente["email"]
    nome = cliente["nome"]
    assunto = "" # Preencha o Assunto do E-mail
    # Descreva o corpo do e-mail
    corpo = f"""
    <p style="font-size: 15px;">Olá {nome}, tudo bem?</p>

    <p style="font-size: 15px;">Me chamo Danilo, sou da Wetok Software. Estou entrando em contato para falar sobre o Boleto Rápido.</p>
    <p style="font-size: 15px;">Temos uma funcionalidade dentro do Recash V2 que é o envio de relatório, demonstrando as faturas pagas e os clientes inadimplentes.</p>
    <p style="font-size: 15px;">Para a utilização desse recurso, gostaria de saber:</p>

    <ul>
        <li style="font-size: 15px;">Qual é o responsável da clínica?</li>
        <li style="font-size: 15px;">Qual o e-mail do responsável?</li>
        <li style="font-size: 15px;">Qual seria o número de telefone?</li>
    </ul>

    <p style="font-size: 15px;">Fico no aguarde de uma resposta.</p>
    <p style="font-size: 15px;">Desde já agradeço.</p>
    <img src="cid:image1" width="250px">
    <img src="https://i.imgur.com/GW90sq5.png" width="250px">
    """
    send_email(email, assunto, corpo, image_path)
    print(f"E-mail enviado para {email}")
