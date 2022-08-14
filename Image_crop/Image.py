# Importing files
from PIL import Image, ImageFilter

# open file path
img = Image.open("image.jpg")

# crop the image
img.thumbnail((600, 200))

# saving image
img.save('thumbnail.jpg')
