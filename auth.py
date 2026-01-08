import json
from models import Kunde, Berater, Konto


def lade_json(datei):
    try:
        with open(datei, "r") as f:
            return json.load(f)
    except FileNotFoundError:
        return []


def speichere_json(datei, daten):
    with open(datei, "w") as f:
        json.dump(daten, f, indent=4)


KUNDEN_DATEI = "kunden.json"

def check_log_pw(email, pw, datei=KUNDEN_DATEI):
    kundendb = lade_json(datei)
    lpw = None
    for kunde in kundendb:
        if kunde.get("email") == email:
            lpw = kunde.get("l_pw")
    if lpw == pw:
        return True
    else:
        return False
    
BERATER_DATEI = "berater.json"    

def check_log_pw_b(brid, pw, datei=BERATER_DATEI):
    beraterdb = lade_json(datei)
    lpw = None
    for berater in beraterdb:
        if berater.get("brid") == brid:
            lpw = berater.get("pw")
    if lpw == pw:
        return True
    else:
        return False