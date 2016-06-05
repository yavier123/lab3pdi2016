#! /usr/bin/python
from SimpleCV import Image, Camera, Color #nueva libreria color para los comandos de color
#cam = Camera()
#img = cam.getImage()
#img.save("lunar1.jpg")
pruebalunar=Image("lunar6nico.png") #nombre de lka imagen que quieres cargar
lunargris=pruebalunar.grayscale()
lunargris.save("fotoslunarprurba.png")
(red,green,blue)=pruebalunar.splitChannels(False) # la separo en RGB
red.save("fotoenrojo.png")
green.save("fotoenverde.png")
blue.save("fotoenazul.png")

#codigo para encontrarn manchas solo se a echo en escala de grises  
prueba69=green.binarize() #la binarizo por que se vera mejor asi 
mancha=prueba69.findBlobs() #ocupo el comando para encontrar lasmanchas (lunares)
mancha.show(Color.YELLOW)
prueba69.save("porfavorguardate3.png")


invertidos=green.invert()#se invierte la imagen para obtener manchas negras en la foto
blob=invertidos.findBlobs()#se ve si se encuentrasn las mannchas en la foto invertida
blob.show(width=2)
pruebalunar.addDrawingLayer(invertidos.dl())
pruebalunar.show()
pruebalunar.save("porfavorguardate2.png") #guardamos la imagen 


#enncontrar manchas por color especifico para el cual tenemos:
brown_distance=green.colorDistance(Color.BLACK).invert()##cmo buscamos de color negro , le pknemos black 
blobs2_=brown_distance.findBlobs()
blobs2_.draw(color=Color.PUCE ,width=3)#se va  hacer el mismo ejemplo de la guia
brown_distance.show()
green.addDrawingLayer(brown_distance.dl())
green.show()
green.save("Porfavorguaradte5.png")

#lineas=pruebalunar.findLines()
#lineas.draw(width=3)
#pruebalunar.show()
circles=pruebalunar.findCircle(canny=100,thresh=350,distance=15)
circles=circles.sortArea()
circles.draw(width=4)
img_with_circles= pruebalunar.applyLayers()
edges_in_image= pruebalunar.edges(t2=200)
final=pruebalunar.sideBySide(edges_in_image.sideBySide(img_with_circles)).scale(0.5)
final.show()
final.save("porfavorguardate.png") 
