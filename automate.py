
from params import *

def build():
    text = text_screenshot("file_name",1000, 35,500)

    fichier = text.split(" -")[0].split(".")[0] # On enlève d'abord les tirets : NSI - Vis... puis le .py
    nom_final_commande = ".\\" + fichier
    print(nom_final_commande)


    terminal_check = text_screenshot("Terminal", 75, 35, 350)
    print(terminal_check)
    if terminal_check == "Terminal":
        pyautogui.moveTo(375,0)
        pyautogui.click()
        build_check = text_screenshot("Build", 130, 35, 370, 145)
        print(build_check)
        if build_check == "Run Build Task...":
            pyautogui.moveTo(375, 155)
            pyautogui.click()
            print("Le build est en téléchargement")
            lancement(nom_final_commande)
    else:
        print("Veuillez mettre VS code en grand écran")



def lancement(nom_final_commande):
    close_terminal = text_screenshot("fermeture_term", 1915, 250, 0, 850, False)
    
    while not 'Terminal will be reused by tasks, press any key to close it.' in close_terminal:
        print("On attend que le programme soit complétement généré")
        time.sleep(1)
        close_terminal = text_screenshot("fermeture_term", 1915, 250, 0, 850, False)
        
    if not "La génération s'est achevée avec une ou plusieurs erreurs." in close_terminal:
        print("Le programme n'a pas généré d'érreur, il peut continuer")
        pyautogui.moveTo(880, 970)
        time.sleep(0.25)
        pyautogui.click()
        pyautogui.press("ENTER")

        verif_terminal = text_screenshot("verif_term", 1915, 250, 0, 700, False)

        # Mettre plutot Outpout ou problems
        if not "PROBLEMS" in verif_terminal or not "TERMINAL" in verif_terminal:
            print("Le terminal n'était pas ouvert.")
            pyautogui.moveTo(375,0)
            pyautogui.click()
            term_check = text_screenshot("new_term", 130, 35, 370, 50)
            print(term_check)
            if term_check == "New Terminal":
                pyautogui.moveTo(375, 50)
                pyautogui.click()
                time.sleep(0.5)
            
        keyboard = Controller()
        keyboard.type(nom_final_commande)

        pyautogui.press('ENTER')
    else:
        print("Le programme a généré une erreur")

build()
#print(pyautogui.position())
