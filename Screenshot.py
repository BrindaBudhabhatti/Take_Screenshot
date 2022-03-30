#Program to take Schreenshot
import pyscreenshot

#Capture screen
image = pyscreenshot.grab()

#Show screenshot
image.show()

#Save screenshot
image.save("ScrinShot.png")
