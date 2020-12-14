from PIL import Image
from RequestSender import Connector

with open("res/pinya.jpg", "rb") as f:
    connector = Connector(f.read())
    f.close()
    resp = list(connector.recieveFaceCoordinates()[0]['faceRectangle'].values())
    img = Image.open("res/pinya.jpg")
    x = resp[1]
    y = resp[0]
    width = x + resp[2]
    height = y + resp[3]
    dim = (x, y, width, height)
    img = img.crop(dim)
    img.show()
    img.save("out/pinya-cropped.jpg")