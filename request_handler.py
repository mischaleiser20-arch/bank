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



REQUEST_DATEI = "request.json"
def kredit_request(brid, kontonummer, krb, lzm, datei=REQUEST_DATEI):
    r_type = "kredit"
    berater_id = brid
    iban = kontonummer
    kredit_betrag = krb
    laufzeit_monate = lzm
    
    requestsdb = lade_json(datei)
    requestsdb.append({
        "type": r_type,
        "brid": berater_id,
        "iban": iban,
        "betrag": kredit_betrag,
        "laufzeit": laufzeit_monate
    })
    speichere_json(datei, requestsdb)

def load_request(berater: Berater, datei=REQUEST_DATEI):
    requestdb = lade_json(datei)
    requestlist = []
    for request in requestdb:
        if request.get("brid") == berater.brid:
            requestlist.append(request)
    return requestlist

