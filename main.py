#tak to tady musímě pěkně napsat aby jsme měli hodně bodíků
#JV úspěšně commitnul
#zkouška

import os

#Původní symetrický klíč
p_symetricky_klic = ""
#Rozšifrovaný symetrický klíč
r_symetricky_klic = ""
#Šifrovany klič pomoci RSA
s_symetricky_klic = ""
#RSA klíč 1
asymetricky_klic1 = ""
#RSA klíč 2
asymetricky_klic2 = ""
#Půvdoní zpráva
p_zprava = ""
#Rozšifrovaná zpráva
r_zprava = ""
#Sifrovaná zpráva
s_zprava = ""
#Random proměnná pro generování kníče
random = ""

#Switch class, vytvoření vlastního switch.
class switch(object):
    value = None
    def __new__(class_, value):
        class_.value = value
        return True
#Funkce spolupracující s switch.
def case(*args):
    return any((arg == switch.value for arg in args))

#Funkce zajišťuje načtení posílané zprávy uživatelem 1
def nacteni_zpravy():
    konsole("Zadej zprávu, která má být přenesena:")
    uzivatel = input()
    konsole("Odesilatel: " + uzivatel)
    global p_zprava
    p_zprava = uzivatel

#Funkce bude zajišťovat šifrový text.
def sifrovy_text():
    #Později bude volat šifrovací funkci a jako parametr bude předávat načtený text.
    sifrovy_text = s_zprava
    konsole("Šifrovy text: " + sifrovy_text)

#Funkce zajišťuje rozšifrován posílané zprávy uživatelem 1
def rozsifrovani_sifroveho_textu():
    # Později bude volat šifrovací funkci a jako parametr bude předávat načtený text.
    zprava = r_zprava
    konsole("Přijemce: " + zprava)

#Funkce vygeneruje symetricky klíč a uloží ho do globální proměnné.
def AES_generovani_klicu(key):
    # TODO generovaní symetrického klíče!
    # Slouží pro předání a uložení generovaného klíče
    global random,p_symetricky_klic, r_symetricky_klic
    #Generuje nový random klíč
    random_key = os.urandom(16)
    #Zajišťuje uložení klíče do globální proměné
    if (random == ""): random = random_key

    #Zajišťuje generování dle parametru, záleží na tom - jaké je potřeba generovat
    if key == "p":konsole("Generuji symetrický klíč.");p_symetricky_klic = random_key;print("Konsole: Generovaný klíč:");print(p_symetricky_klic);konsole("Posílám vygenerované klíče");
    if key == 'r':r_symetricky_klic = random;print("Konsole: Předaný klíč:");print(r_symetricky_klic)
    if key == 'o':konsole("Generuji symetrický klíč.");p_symetricky_klic = random_key; r_symetricky_klic = random_key;print("Konsole: Generované klíče:");print(r_symetricky_klic)

#Funkce zašifruje text pomoci symetrické šifry AES.
def AES_sifrovani():
    #TODO šifrovani!
    global s_zprava
    if p_symetricky_klic == "": AES_generovani_klicu("p")
    #Tohle nahradit šifrováním AES
    s_zprava = "TODO sifrovani zpravy"
    # Po sem

#Funkce dešifruje text pomoci symetrické šifry AES.
def AES_desifrovani():
    #TODO dešifrovani!
    if r_symetricky_klic == "": AES_generovani_klicu("r")
    #Teoreticky není potřeba, zprávu pořád máme, takže stačí vypsat zprávu, ale pro úplnost, bych dešifroval
    global r_zprava
    #Tohle nahradit dešiforováním
    r_zprava = p_zprava
    #Po sem

#Funkce na šifrování symetrického klíče.
def RSA_sifrovani():
    #TODO rsa sidrovani.
    konsole("Šifrování veřejného klíče. TODO")
    global s_symetricky_klic
    s_symetricky_klic = "TODO šifrování ss klíče pomoci RSA"
    konsole("Posílám šifrovaný klíč, TODO " + s_symetricky_klic)

#Funkce na dešifrování symetrického klíče.
def RSA_desifrovani():
    #TODO RSA desifrovani.
    konsole("Dešifrování veřejného klíče. TODO")
    global r_symetricky_klic
    r_symetricky_klic = "TODO dešifrovani ss klíče pomoci RSA"
    konsole("Dešifruji klíč, TODO " + r_symetricky_klic)

#Funkce, které budeme předávat texty, které se mají vypsat do konsole. Text, který budeme chtít zobrazit předáme funkci konsole.
def konsole(konsol_text):
    print("Konsole: " + konsol_text)

#Komunikacni kanál zobrazuje probíhající komunikaci mezi uživately a přenášený šifrový text.
def komunikacni_kanal():
    nacteni_zpravy()
    AES_sifrovani()
    sifrovy_text()
    AES_desifrovani()
    rozsifrovani_sifroveho_textu()

#Menu applikace, možné po zadání čísla vyzvat program k dané operaci.
def menu():
    print("Menu:\n1. Zahájení konverzace.\n2. Vygenerování nových symetrických klíčů.\n3. TODO něco.\n4. Konec")
    chose = input()
    while switch(chose):
        if case("1"):
            konsole("Zahájení konvezace.")
            komunikacni_kanal()
            return 1
        if case("2"):
            konsole("Generování nových AES klíčů.")
            AES_generovani_klicu("o")
            return 1
        if case("3"):
            konsole("TODO něco")
            return 1

        if case("4"):
            konsole("Konec")
            return 0
        print("Špatně zvoleno.")
        break

#main
end = 1
while end == 1:
    end = menu()