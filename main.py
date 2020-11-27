#tak to tady musímě pěkně napsat aby jsme měli hodně bodíků
#JV úspěšně commitnul
#zkouška

import os
from cryptography.fernet import Fernet
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC
import base64
from cryptography.hazmat.primitives.ciphers import (
    Cipher, algorithms, modes
)
#TODO udělat kládání konverzace + klíče do souboru a jejich načtení
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
#bytová verze zprávy
b_zprava = ""
#Kontrola, zda byla zahájena konverzace
zapocata_komunikace = 0
#pomocna p
p = ""
# globální iv = z klíče - předat returnem z šifrování do dešifrování AES
global_iv = ""

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
    konsole("Uživatel1: " + uzivatel)
    global p_zprava
    p_zprava = uzivatel

def nacteni_zpravy_odpoved():
    konsole("Zadej zprávu, která má být přenesena:")
    uzivatel = input()
    konsole("Uživatel2: " + uzivatel)
    global p_zprava
    p_zprava = uzivatel

#Funkce bude zajišťovat šifrový text.
def sifrovy_text():
    #Později bude volat šifrovací funkci a jako parametr bude předávat načtený text.
    sifrovy_text = s_zprava
    #sifrovy_text = Decode(sifrovy_text)
    #s_zprava = Decode(s_zprava)
    #print("sifrovy text")
    konsole("Šifrový text: " + str(sifrovy_text))

#Funkce zajišťuje rozšifrován posílané zprávy uživatelem 1
def rozsifrovani_sifroveho_textu():
    # Později bude volat šifrovací funkci a jako parametr bude předávat načtený text.
    zprava = r_zprava
    zprava = Decode(zprava)
    konsole("Přijemce: " + zprava)

#Funkce vygeneruje symetricky klíč a uloží ho do globální proměnné.
def AES_generovani_klicu(key_G):
    # Slouží pro předání a uložení generovaného klíče
    global random,p_symetricky_klic, r_symetricky_klic
    #Generuje nový random klíč
    passw = os.urandom(16)
    kdf = PBKDF2HMAC(
        algorithm=hashes.SHA256(),
        length=12,                      #delka klíče
        salt=os.urandom(16),
        iterations=100000,
        backend=default_backend()
    )
    key = base64.urlsafe_b64encode(kdf.derive(passw))
    #print(len(key))
    #key = os.urandom(16)
    #Zajišťuje uložení klíče do globální proměné
    if (random == ""): random = key

    #Zajišťuje generování dle parametru, záleží na tom - jaké je potřeba generovat
    #TODO pepík předělání
    if key_G == "p":konsole("Generuji symetrický klíč.");p_symetricky_klic = key;print("Konsole: Generovaný klíč:");print(Decode(p_symetricky_klic));konsole("Posílám vygenerované klíče");
    if key_G == 'r':r_symetricky_klic = random;print("Konsole: Předaný klíč:");print(Decode(r_symetricky_klic))
    if key_G == 'o':konsole("Generuji symetrický klíč.");p_symetricky_klic = key; r_symetricky_klic = key;print("Konsole: Generovaný klíč:");print(Decode(r_symetricky_klic))

#Funkce zašifruje text pomoci symetrické šifry AES.
def AES_sifrovani():
    global s_zprava, b_zprava, p, global_iv
    if p_symetricky_klic == "": AES_generovani_klicu("p")
    #Tohle nahradit šifrováním AES
    b_zprava = Encode(p_zprava)
    #f = Fernet(p_symetricky_klic)
    #s_zprava = f.encrypt(b_zprava)
    iv = os.urandom(12)

    sifrovani_AES = Cipher(
        algorithms.AES(p_symetricky_klic),
        modes.GCM(iv),
        backend=default_backend()
    ).encryptor()

    #autorita - asi :/
    sifrovani_AES.authenticate_additional_data(b"authenticated but not encrweweweweypted payload")
    # kvůli gcmku malá zpráva
    s_zprava = sifrovani_AES.update(b_zprava) + sifrovani_AES.finalize()
    #print(s_zprava)

    p = sifrovani_AES.tag
    global_iv = iv
    # Po sem

#převedení zprávy do bytové formy
def Encode(zprava):
    #global b_zprava
    return zprava.encode()

#převedení bytové zpráva do normální formy
def Decode(zprava):
    #global r_zprava
    return zprava.decode()

#Funkce dešifruje text pomoci symetrické šifry AES.
def AES_desifrovani():
    if r_symetricky_klic == "": AES_generovani_klicu("r")
    #Teoreticky není potřeba, zprávu pořád máme, takže stačí vypsat zprávu, ale pro úplnost, bych dešifroval
    global r_zprava
    #Tohle nahradit dešiforováním
    #f = Fernet(p_symetricky_klic)
    #r_zprava = f.decrypt(s_zprava)
    #r_zprava = Decode(r_zprava)
    decryptor = Cipher(
        algorithms.AES(p_symetricky_klic),
        modes.GCM(global_iv, p),
        backend=default_backend()
    ).decryptor()

    decryptor.authenticate_additional_data(b"authenticated but not encrweweweweypted payload")

    r_zprava = decryptor.update(s_zprava) + decryptor.finalize()
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
    global zapocata_komunikace
    zapocata_komunikace = zapocata_komunikace + 1
    nacteni_zpravy()
    AES_sifrovani()
    sifrovy_text()
    AES_desifrovani()
    rozsifrovani_sifroveho_textu()

def komunikacni_kanal_odpoved():
    nacteni_zpravy_odpoved()
    AES_sifrovani()
    sifrovy_text()
    AES_desifrovani()
    rozsifrovani_sifroveho_textu()

def komunikacni_kanal_pokracovani():
    global r_zprava
    end = 1
    while end == 1:
        print("Konverzační menu:\n1. Uživatel1 zpráva.\n2. Uživatel2 zpráva.\n3. Zobrazit poslední posílanou zprávu.\n4. Vrácení do hlavního menu.")
        chose = input()
        while switch(chose):
            if case("1"):
                komunikacni_kanal()
            if case("2"):
                komunikacni_kanal_odpoved()
            if case("3"):
                konsole("Poslední posílaná zpráva.")
                rozsifrovani_sifroveho_textu()
            if case("4"):
                konsole("Vracíme se do hlavního menu.")
                end = 0
            #if(chose != 1 && chose != 2 && chose != 3 && chose != 4): print("Špatně zvoleno.")
            break


#Menu applikace, možné po zadání čísla vyzvat program k dané operaci.
def menu():
    print("Menu:\n1. Zahájení konverzace.\n2. Pokračovat v započaté konverzaci.\n3. Vygenerování nových symetrických klíčů.\n4. Konec")
    chose = input()
    while switch(chose):
        if case("1"):
            konsole("Zahájení konvezace.")
            komunikacni_kanal()
            return 1
        if case("2"):
            konsole("Pokračování v započaté konverzaci.")
            if zapocata_komunikace == 1: komunikacni_kanal_pokracovani()
            else: konsole("Žádná konverzace nebyla započatá.")
            return 1
        if case("3"):
            konsole("Generování nových AES klíčů.")
            AES_generovani_klicu("o")
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
