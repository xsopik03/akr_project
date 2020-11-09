#tak to tady musímě pěkně napsat aby jsme měli hodně bodíků
#JV úspěšně commitnul
#Funkce zajišťuje načtení posílané zprávy uživatelem 1
def nacteni_zpravy():
    print("Zadej zprávu, která má být přenesena:")
    uzivatel = input()
    return uzivatel

#Funkce bude zajišťovat šifrový text.
def sifrovy_text(zprava):
    #Později bude volat šifrovací funkci a jako parametr bude předávat načtený text.
    sifrovy_text = zprava
    return sifrovy_text

#Funkce zajišťuje rozšifrován posílané zprávy uživatelem 1
def rozsifrovani_sifroveho_textu(sifrovy_text):
    # Později bude volat šifrovací funkci a jako parametr bude předávat načtený text.
    uzivatel2 = sifrovy_text
    return uzivatel2

#Funkce vygeneruje symetricky klíč a uloží ho do globální proměnné.
def AES_generovani_klicu():
    print("TODO generovani klíče.")
    #TODO generovaní symetrického klíče!

#Funkce zašifruje text pomoci symetrické šifry AES.
def AES_sifrovani(key, text):
    print("TODO")
    #TODO šifrovani!
    s_text = text
    return s_text

#Funkce dešifruje text pomoci symetrické šifry AES.
def AES_desifrovani(key, s_text):
    print("TODO")
    #TODO dešifrovani!
    text = s_text
    return text

#Komunikacni kanál zobrazuje probíhající komunikaci mezi uživately a přenášený šifrový text.
def komunikacni_kanal():
    zprava = nacteni_zpravy()
    s_text = sifrovy_text(zprava)
    vystup = rozsifrovani_sifroveho_textu(s_text)
    print("Odesilatel -> Uživatel2: " + zprava)
    print("Šifrový text: " + s_text)
    print("Uživatel 1 -> Příjemce: " + vystup)

print("Pokus!")
komunikacni_kanal()



