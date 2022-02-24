"""detencion facial"""



class face_detect:
   def __init__(self, imagen_detectada):
       self.imagen_detectada =  imagen_detectada
       #IMPORTAMOS "opencv".
       
       import cv2
       import mensaje
       import time
       import datetime
       timestamp = datetime.datetime.now()
       ts = timestamp.strftime("%d %B %Y %I:%M:%S%p")
       #INTRODUCIMOS RUTA A LA IMAGEN Y EL ARCHIVO "xml".
       imagePath = self.imagen_detectada #<ruta a la imagen fuente>
       cascPath = "haarcascade_frontalface_default.xml"
       cascPath2 = "haarcascade_profileface.xml" 
       #CARGAMOS CLASIFICADOR.
       faceCascade = cv2.CascadeClassifier(cascPath)
       profile_cascade = cv2.CascadeClassifier(cascPath2)
       #LEEMOS IMAGEN
       image = cv2.imread(imagePath)
       #CONVERTIMOS IMAGEN A ESCALA DE GRISES
       gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
       #DETECTAMOS ROSTROS EN LA IMAGEN
       faces = faceCascade.detectMultiScale(
           gray,
           scaleFactor=1.3,
           minNeighbors=4)
       perfil = profile_cascade.detectMultiScale( 
           gray, scaleFactor=1.3, minNeighbors=1)

       #NÚMERO DE ROSTROS ENCONTRADOS
       rostro = len(faces)
       profile = len(perfil)
       if rostro == 0 and profile == 0:
          print('sin rostros encontrados: ')
        #print("Found {0} faces!".format(rostro))
       if rostro >= 1:
           #MOSTRAMOS CONTENIDO DE "faces":
           print ('ROSTROS ENCONTRADOS:', rostro)
           #MARCAMOS LOS ROSTROS CON UN RECTANGULO
           for (x, y, w, h) in faces:
               cv2.rectangle(image, (x, y), (x+w, y+h), (0, 255, 0), 2)
               print("frente") 

           #mostramos resultados

           ruta = '/'.join(['/','home','augusto','Escritorio','oraculo', 'version 1.1.0','rostros',ts + '.jpg'])
           cv2.imwrite(ruta, image)
           mensaje.email("adiacopini@gmail.com", ruta)     
           mensaje.email("ejcolman3@gmail.com", ruta)   
       if profile >= 1:
           print("rostro encontrado: ", profile)
           for (x, y, w, h) in perfil:
               cv2.rectangle(image, (x, y), (x+w, y+h), (0, 255, 255), 2)       
               print("perfil")

            #MOSTRAMOS RESULTADO.

           ruta = '/'.join(['/','home','augusto','Escritorio','oraculo', 'version 1.1.0','rostros',ts + '.jpg'])
           cv2.imwrite(ruta, image)
           mensaje.email("adiacopini@gmail.com", ruta)  
           mensaje.email("ejcolman3@gmail.com", ruta)
               