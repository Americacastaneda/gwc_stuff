from PIL import Image

img = Image.open("photo.jpg")
img.show()

im = Image.new("RGB", (250,250), color = 5)
im.show()