class email:
    def __init__(self, usuario, imagen):

        self.usuario = usuario
        self.imagen = imagen


        import os
        import smtplib
        import mimetypes

 
        from email.mime.multipart import MIMEMultipart
        from email.mime.image import MIMEImage
        from email.encoders import encode_base64

     
        msg = MIMEMultipart() 
        msg['From']="xxxxxxx@gmail.com" #correo para enviar imagenes
        msg['To']=self.usuario
        msg['Subject']="ALERTA ROSTRO DETECTADO"




     
        file = open(self.imagen, "rb")
        attach_image = MIMEImage(file.read())
        attach_image.add_header('Content-Disposition', 'attachment; filename = "avatar.png"')
        msg.attach(attach_image)

     
        mailServer = smtplib.SMTP('smtp.gmail.com',587)
        mailServer.ehlo()
        mailServer.starttls()
        mailServer.ehlo()
        mailServer.login("xxxxx@gmail.com","******")

     
        mailServer.sendmail("xxxxxxxx@gmail.com", self.usuario, msg.as_string())
        mailServer.close()
        
