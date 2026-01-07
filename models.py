import random

class Konto:
    def __init__(self, iban, saldo=0.0):
        self.iban = iban
        self.saldo = saldo

    def einzahlen(self, betrag):
        self.saldo += betrag

    def auszahlen(self, betrag):
        if self.saldo > betrag:
            self.saldo -= betrag
        else:
            return "Saldo zu gering"

    def abfragen(self):
        return f"IBAN: {self.iban} Kontostand: {self.saldo}"

class Kunde:
    def __init__(self, kdnr, nachname, vorname, anschrift, email, l_pw):
        self.kundennr = kdnr
        self.nachname = nachname
        self.vorname = vorname
        self.anschrift = anschrift
        self.email = email
        self.l_pw = l_pw
        self.konten = {}

class Berater:
    def __init__(self, brid, pw, nachname, vorname):
        self.brid = brid
        self.pw = pw
        self.nachname = nachname
        self.vorname = vorname
        self.betreute = {}

    def plus_kunde(self, kunde):
        self.betreute[kunde.kundennr] = kunde

    def minus_kunde(self, kdnr):
        self.betreute.pop(kdnr, None)

    def konto_oeffnen(self, kunde=None):
        iban = "DE" + str(random.randint(100000000, 999999999))
        if not kunde:
            return "Kunde nicht betreut"
        kunde.konten[iban] = Konto(iban)
        return Konto(iban)

class Kredit:
    def __init__(self, krnm, krb, lzm, zss):
        self.kredit_nummer = krnm
        self.kredit_betrag = krb
        self.laufzeit_monate = lzm
        self.zinssatz = zss
        