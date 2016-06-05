#! /usr/bin/python
from SimpleCV import Image, Camera, Color #nueva libreria color para los comandos de color
#cam = Camera()
#img = cam.getImage()
#img.save("lunar1.jpg")
pruebalunar=Image("lunar5nico.png") #nombre de lka imagen que quieres cargar
lunargris=pruebalunar.grayscale()
lunargris.save("fotoslunarprurba.png")
(red,green,blue)=pruebalunar.splitChannels(False) # la separo en RGB
red.save("fotoenrojo.png")
green.save("fotoenverde.png")
blue.save("fotoenazul.png")
prueba69=lunargris.binarize() #la binarizo por que se vera mejor asi 
mancha=prueba69.findBlobs() #ocupo el comando para encontrar lasmanchas (lunares)
mancha.show(Color.YELLOW)

invertidos=pruebalunar.invert()
blob=invertidos.findBlobs()
blob.show(width=2)
pruebalunar.addDrawingLayer(invertidos.dl())
pruebalunar.show()
pruebalunar.save("porfavorguardate2.png")


brown_distance=pruebalunar.colorDistance(Color.BLACK).invert()
blobs2_=brown_distance.findBlobs()
brown_distance.show()

#lineas=pruebalunar.findLines()
#lineas.draw(width=3)
#pruebalunar.show()
circles=pruebalunar.findCircle(canny=100,thresh=250,distance=15)
circles=circles.sortArea()
circles.draw(width=2)
img_with_circles= pruebalunar.applyLayers()
edges_in_image= pruebalunar.edges(t2=200)
final=pruebalunar.sideBySide(edges_in_image.sideBySide(img_with_circles)).scale(0.5)
final.show()
final.save("porfavorguardate.png")
