import base64


def decodeImage(img_string,filename):    # we are giving image_string in postman
    with open(filename, 'wb') as f:
        f.write(base64.b64decode(img_string))
        f.close()

def encodeImageIntoBase64(croppedImagePath):
    with open(croppedImagePath, "rb") as f:
        return base64.b64encode(f.read())