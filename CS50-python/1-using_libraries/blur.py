from PIL import Image, ImageFilter

before = Image.open("bridgeImg.bmp")
after = before.filter(ImageFilter.BoxBlur(10))
after.save("out.bmp")
