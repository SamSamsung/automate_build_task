import pyautogui # Prendre la capture et le reste
import pytesseract # Extraire le texte de la photo
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'
import cv2
import time
from pynput.keyboard import Controller


def text_screenshot(nom_fichier, x2, y2, x1=0, y1=0, sans_saut= True):
    image = pyautogui.screenshot(region=(x1,y1,x2,y2)) # Première valeures x et y: d'ou on commence. Deuxièmes valeures x et y: taille du screenshot 
    image.save(r'.\\{}.png'.format(nom_fichier))


    img = cv2.imread(".\\{}.png".format(nom_fichier))

    text = pytesseract.image_to_string(img)
    if sans_saut:
        return text.split("\n")[0] # On enlève le saut à la ligne
    else:
        return text