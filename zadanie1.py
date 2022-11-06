import pytesseract as pt
import cv2

pt.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract'


def tekst_z_obrazu(nazwa):
    img = cv2.imread(nazwa)
    img_object = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    return pt.image_to_string(img_object)


print(tekst_z_obrazu('zara.jpg'))
print(tekst_z_obrazu('yt.jpg'))
print(tekst_z_obrazu('mccd.png'))
print(tekst_z_obrazu('samsung.png'))
print(tekst_z_obrazu('apteka.png'))

