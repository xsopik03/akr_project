# AKR_scom
Šifrovaná komunikace mezi dvěma uživateli

Šifrovaná komunikace mezi dvěma uživateli
Vytvořte program, který bude schopen provádět šifrovanou komunikaci mezi dvěma uživateli. Zprávy budou zašifrované pomocí symetrické kryptografie a pro výměnu klíče u symetrické kryptografii využijte asymetrickou kryptografii. Veřejné klíče uživatelů budou opatřeny certifikáty, které se budou ověřovat u certifikační autority. Každá dílčí činnost programu bude vypsána do konzole.
Návrh průběhu komunikace:
1. Vytvoření klíčů asymetrické kryptografie pro certifikační autoritu a obě strany. 2. Podepsání veřejných klíčů.
3. Ověření klíčů u certifikační autority.
4. Stanovení klíče pro symetrickou komunikaci a přenos šifrovaného textu.
5. Dešifrování a zobrazení souboru.
V tomto zadání je možné použít knihovny zaměřené na symetrickou kryptografii, asymetrickou kryptografii a certifikáty.
Pro realizaci projektu je možné využít jiné metody zabezpečení, ale musí být splněny základní podmínky:
● Komunikace mezi uživateli musí být šifrována.
● Před samotnou komunikací musí proběhnout ověření komunikujících stran.


[1] RSA, https://cs.wikipedia.org/wiki/RSA

[2] AES, http://nvlpubs.nist.gov/nistpubs/FIPS/NIST.FIPS.197.pdf

[3] Digitální https://cs.wikipedia.org/wiki/Digit%C3%A1ln%C3%AD_certifik%C3%A1t
certifikát
