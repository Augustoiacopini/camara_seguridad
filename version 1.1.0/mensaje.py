class email:
    def __init__(self, usuario, imagen):

        self.usuario = usuario
        self.imagen = imagen

        # Importamos librerías
        import os
        import smtplib
        import mimetypes

        # Importamos los módulos necesarios
        from email.mime.multipart import MIMEMultipart
        from email.mime.image import MIMEImage
        from email.encoders import encode_base64

        # Creamos objeto Multipart, quien será el recipiente que enviaremos
        msg = MIMEMultipart()
        msg['From']="lolatay298@gmail.com"
        msg['To']=self.usuario
        msg['Subject']="ALERTA ROSTRO DETECTADO"




        # Adjuntamos Imagen
        file = open(self.imagen, "rb")
        attach_image = MIMEImage(file.read())
        attach_image.add_header('Content-Disposition', 'attachment; filename = "avatar.png"')
        msg.attach(attach_image)

        # Autenticamos
        mailServer = smtplib.SMTP('smtp.gmail.com',587)
        mailServer.ehlo()
        mailServer.starttls()
        mailServer.ehlo()
        mailServer.login("lolatay298@gmail.com","Tierra01")

        # Enviamos
        mailServer.sendmail("lolatay298@gmail.com", self.usuario, msg.as_string())

        # Cerramos conexión
        mailServer.close()
        
