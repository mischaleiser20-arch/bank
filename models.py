import random

class Kredit:
    def __init__(self, krnm, krb, lzm, zss, zubzahlen=None):
        self.kredit_nummer = krnm
        self.kredit_betrag = krb
        self.laufzeit_monate = lzm
        self.zinssatz = zss
        if zubzahlen == None:
            self.zubezahlen = self.kredit_betrag
        else:
            self.zubezahlen = zubzahlen
        
    def laufzeit_update(self, w_monat=1):
        self.laufzeit_monate -= w_monat
        self.zubezahlen += (self.zinssatz / 100) * self.kredit_betrag
    
    def rate_tilgen(self, wert):
        self.zubezahlen -= wert

class Konto:
    def __init__(self, iban, saldo=0.0):
        self.iban = iban
        self.saldo = saldo
        self.gesperrt = False
        self.kredite = []

    def einzahlen(self, betrag):
        self.saldo += betrag

    def auszahlen(self, betrag):
        if self.saldo > betrag:
            self.saldo -= betrag
        else:
            return "Saldo zu gering"

    def abfragen(self):
        return f"IBAN: {self.iban} Kontostand: {self.saldo}"
    
    def add_kredite(self, kredit: Kredit):
        self.kredite.append(kredit.kredit_nummer)
        self.saldo += kredit.kredit_betrag
        
    def remove_kredit(self, kredit: Kredit):
        if kredit.kredit_nummer in self.kredite:
            self.kredite.remove(kredit.kredit_nummer)
        else:
            print("Kredit nicht vorhanden")
        
    def konto_sperren(self):
        self.gesperrt = True
        
    def konto_entsperren(self):
        self.gesperrt = False

class Kunde:
    def __init__(self, kundennr, nachname, vorname, anschrift, email, l_pw):
        self.kundennr = kundennr
        self.nachname = nachname
        self.vorname = vorname
        self.anschrift = anschrift
        self.email = email
        self.l_pw = l_pw
        self.konten = []

class Berater:
    def __init__(self, brid, pw, nachname, vorname):
        self.brid = brid
        self.pw = pw
        self.nachname = nachname
        self.vorname = vorname
        self.betreute = []

    def plus_kunde(self, kundennr):
        self.betreute.append(kundennr)

    def minus_kunde(self, kdnr):
        self.betreute.pop(kdnr, None)

    def konto_oeffnen(self, kunde=None):
        iban = "DE" + str(random.randint(100000000, 999999999))
        if not kunde:
            return "Kunde nicht betreut"
        kunde.konten.append(iban)
        return iban
    
    def kredit_genemigen(self, kunde=None):
        pass


        
        
