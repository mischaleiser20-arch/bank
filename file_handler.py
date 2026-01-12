import json
from models import Kunde, Berater, Konto, Kredit

def lade_json(datei):
    try:
        with open(datei, "r") as f:
            return json.load(f)
    except FileNotFoundError:
        return []

def speichere_json(datei, daten):
    with open(datei, "w") as f:
        json.dump(daten, f, indent=4)

# Kunde
KUNDEN_DATEI = "kunden.json"
def erstell_kunde(kunde: Kunde, datei=KUNDEN_DATEI):
    kunden = lade_json(datei)
    kunden.append({"kundennr": kunde.kundennr,
                   "nachname": kunde.nachname,
                   "vorname": kunde.vorname,
                   "anschrift": kunde.anschrift,
                   "email": kunde.email,
                   "l_pw": kunde.l_pw,
                   "konten": kunde.konten
                   })
    speichere_json(datei, kunden)

def lade_kundennr(datei=KUNDEN_DATEI):
    kundendb = lade_json(datei)
    kundennrlist = []
    for kunde in kundendb:
        if "kundennr" in kunde:
            kundennrlist.append(kunde["kundennr"])
            return kundennrlist

def kunden_ohne_berater(datei=KUNDEN_DATEI):
    kundendb = lade_json(datei)
    kundenliste = []
    for kunde in kundendb:
        if kunde.get("konten") == []:
            kundenliste.append(kunde.get("kdnr") or kunde.get("kundennr"))
    return kundenliste

def lade_kunden_emails(datei=KUNDEN_DATEI):
    kundendb = lade_json(datei)
    emaillist = []
    for kunde in kundendb:
        if "email" in kunde:
            emaillist.append(kunde["email"])
    return emaillist

def lade_kunde_from_email(email ,datei=KUNDEN_DATEI):
    kundendb = lade_json(datei)
    for kunde in kundendb:
        if kunde.get("email") == email:
            return kunde

def lade_kunde_from_kdnr(kdnr, datei=KUNDEN_DATEI):
    kundendb = lade_json(datei)
    for kunde in kundendb:
        if kunde.get("kundennr") == kdnr:
            k = Kunde(
                kunde["kundennr"],
                kunde["nachname"],
                kunde["vorname"],
                kunde["anschrift"],
                kunde["email"],
                kunde["l_pw"]
            )
            k.konten = kunde.get("konten", [])
            return k

def speicher_kunde(kunde: Kunde, datei=KUNDEN_DATEI):
    kundendb = lade_json(datei)
    updated = False
    for i,k in enumerate(kundendb):
        if k.get("kundennr") == kunde.kundennr:
            kundendb[i] = {
                "kundennr": kunde.kundennr,
                "nachname": kunde.nachname,
                "vorname": kunde.vorname,
                "anschrift": kunde.anschrift,
                "email": kunde.email,
                "l_pw": kunde.l_pw,
                "konten": kunde.konten
            }
            updated = True
            break
        
    if not updated:
        raise ValueError(f"Kunde mit Kundennr {kunde.kundennr} nicht gefunden")
    speichere_json(datei, kundendb)


# Berater
BERATER_DATEI = "berater.json"

def berater_einstellen(berater: Berater, datei=BERATER_DATEI):
    beraterdb = lade_json(datei)
    beraterdb.append({"brid": berater.brid,
                      "pw": berater.pw,
                      "nachname": berater.nachname,
                      "vorname": berater.vorname,
                      "betreute": berater.betreute})
    speichere_json(datei, beraterdb)

def lade_alle_berater_brid(datei=BERATER_DATEI):
    beraterdb = lade_json(datei)
    listofbrid = []
    for berater in beraterdb:
        listofbrid.append(berater.get("brid"))
    return listofbrid

def lad_berater_mit_brid(brid, datei=BERATER_DATEI):
    beraterdb = lade_json(datei)
    for berater in beraterdb:
        if berater.get("brid") == brid:
            b = Berater(
                berater["brid"],
                berater["pw"],
                berater["nachname"],
                berater["vorname"]
            )
            b.betreute = berater.get("betreute", [])
            return b

def lad_berater_mit_kunde(kunde: Kunde, datei=BERATER_DATEI):
    beraterdb = lade_json(datei)
    for berater in beraterdb:
        for kundenr in berater.get("betreute", []):
            if kundenr == kunde.kundennr:
                b = Berater(
                    berater["brid"],
                    berater["pw"],
                    berater["nachname"],
                    berater["vorname"]
                )
                b.betreute = berater.get("betreute", [])
                return b


def akt_berater(berater: Berater, datei=BERATER_DATEI):
    beraterdb = lade_json(datei)
    for berater_ob in beraterdb:
        if berater_ob.get("brid") == berater.brid:
            berater_ob["betreute"] = berater.betreute
        speichere_json(datei, beraterdb)


# Konto

KONTO_DATEI = "konto.json"

def erstelle_konto(konto: Konto, datei=KONTO_DATEI):
    kontodb = lade_json(datei)
    kontodb.append({
        "iban": konto.iban,
        "saldo": konto.saldo,
        "kredite": konto.kredite
    })
    speichere_json(datei, kontodb)


def lade_konto(Iban_k, datei=KONTO_DATEI):
    kontodb = lade_json(datei)
    for konto in kontodb:
        if konto.get("iban") == Iban_k:
            k = Konto(
                konto["iban"],
                konto["saldo"]
            )
            k.kredite = konto.get("kredite", [])
            return k


def speicher_konto(konto: Konto, datei=KONTO_DATEI):
    kontodb = lade_json(datei)
    for konto_ob in kontodb:
        if konto_ob.get("iban") == konto.iban:
            konto_ob["saldo"] = konto.saldo
            konto_ob["kredite"] = konto.kredite
    speichere_json(datei, kontodb)


# Kredit
KREDIT_DATEI = "kredite.json"

def save_kredit(kredit: Kredit, datei=KREDIT_DATEI):
    kreditedb = lade_json(datei)
    kreditedb.append({
        "kredit_nummer": kredit.kredit_nummer,
        "kredit_betrag": kredit.kredit_betrag,
        "laufzeit_monate": kredit.laufzeit_monate,
        "zinssatz": kredit.zinssatz,
        "zubezahlen": kredit.zubezahlen
    })
    speichere_json(datei, kreditedb)

def lade_kredit(konto: Konto, datei=KREDIT_DATEI):
    kreditedb = lade_json(datei)
    for kredit in kreditedb:
        if kredit.get("kredit_nummer") == konto.kredite[0]:
            k = Kredit(
                kredit["kredit_nummer"],
                kredit["kredit_betrag"],
                kredit["laufzeit_monate"],
                kredit["zinssatz"],
                kredit["zubezahlen"]
            )
            return k


def akt_kredit(kredit: Kredit, datei=KREDIT_DATEI):
    kreditedb = lade_json(datei)
    for kredit_ob in kreditedb:
        if kredit_ob.get("kreditnummer") == kredit.kredit_nummer:
            kredit_ob["zubezahlen"] = kredit.zubezahlen
        speichere_json(datei, kreditedb)
