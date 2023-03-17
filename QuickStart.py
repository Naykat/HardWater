import HardWater

filename = "Images/HardWater.jpg" #File to place watermark on
watermark = "HardWater" #Watermark that will be placed on image

#Add watermark
image = HardWater.watermark(filename, watermark)
image.save("Images/example.png") #Image preservation
image.show() #Image opening

#Watermark reveal
secret_message = HardWater.reveal("Images/example.png")
print(secret_message)


