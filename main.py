#tak to tady musímě pěkně napsat aby jsme měli hodně bodíků
#JV úspěšně commitnul

#Funkce zajišťuje načtení posílané zprávy uživatelem 1
def nacteni_zpravy():
    print("Zadej zprávu, která má být přenesena:")
    uzivatel = input()
    konsole("Odesilatel: " + uzivatel)
    return uzivatel

#Funkce bude zajišťovat šifrový text.
def sifrovy_text(zprava, klic):
    #Později bude volat šifrovací funkci a jako parametr bude předávat načtený text.
    sifrovy_text = zprava
    konsole("Šifrovy text: " + sifrovy_text)
    return sifrovy_text

#Funkce zajišťuje rozšifrován posílané zprávy uživatelem 1
def rozsifrovani_sifroveho_textu(sifrovy_text,klic):
    # Později bude volat šifrovací funkci a jako parametr bude předávat načtený text.
    uzivatel2 = sifrovy_text
    konsole("Přijemce: " + uzivatel2)
    return uzivatel2

#Funkce vygeneruje symetricky klíč a uloží ho do globální proměnné.
def AES_generovani_klicu():
    klic = "TODO klic"
    konsole("Posílám klíč: " + klic)
    #TODO generovaní symetrického klíče!
    return klic

#Funkce zašifruje text pomoci symetrické šifry AES.
def AES_sifrovani(key, text):
    #TODO šifrovani!
    s_text = text
    return s_text

#Funkce dešifruje text pomoci symetrické šifry AES.
def AES_desifrovani(key, s_text):
    print("TODO")
    #TODO dešifrovani!
    text = s_text
    return text

#Funkce, které budeme předávat texty, které se mají vypsat do konsole. Text, který budeme chtít zobrazit předáme funkci konsole.
def konsole(konsol_text):
    print("Konsole: " + konsol_text)


#Komunikacni kanál zobrazuje probíhající komunikaci mezi uživately a přenášený šifrový text.
def komunikacni_kanal():
    zprava = nacteni_zpravy()
    klic = AES_generovani_klicu()
    s_text = sifrovy_text(zprava, klic)
    rozsifrovani_sifroveho_textu(s_text, klic)

#main
komunikacni_kanal()