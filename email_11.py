
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.application import MIMEApplication
import os

email_remetente = 'ayrtonsenna0110@gmail.com'
senha = 'fzro zxfk zhnq bfoq'

email_destinatario = 'wesleyfreire1707@gmail.com'

mensagem = MIMEMultipart()
mensagem['From'] = email_remetente
mensagem['To'] = email_destinatario
mensagem['Subject'] = 'Arquivo CSV em Anexo'

# Corpo do e-mail
corpo = 'Segue em anexo o arquivo CSV.'
mensagem.attach(MIMEText(corpo, 'plain'))

# Anexar arquivo CSV
caminho_arquivo = 'preços.csv'
with open(caminho_arquivo, 'rb') as file:
    anexo = MIMEApplication(file.read(), _subtype='csv')
    anexo.add_header('Content-Disposition', 'attachment', filename=os.path.basename(caminho_arquivo))
    mensagem.attach(anexo)

# Enviar e-mail
servidor = smtplib.SMTP('smtp.gmail.com', 587)
servidor.starttls()
servidor.login(email_remetente, senha)
servidor.send_message(mensagem)
servidor.quit()

print('E-mail com anexo enviado com sucesso!')