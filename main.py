from models import Kunde, Konto, Berater
import random
from file_handler import erstell_kunde, lade_kunden_emails, lade_kunde_from_email, berater_einstellen, lade_kundennr, kunden_ohne_berater, lade_alle_berater_brid, akt_berater
from auth import check_log_pw

def register_k():
    while True:
        nachname = input("Gebe deinen Nachnamen ein: ")
        vorname = input("Gebe deinen Vorname ein: ")
        anschrift = input("Gebe deine Anschrift an: ")
        email = input("Gebe deine Email ein: ")
        password = input("Gebe dein Password ein: ")
        
        wahl = input("Bestätige registrierung (J/N): ").lower()
        if wahl == "j":
            kdnr = random.randint(100, 999)
            nkunde = Kunde(kdnr, nachname, vorname, anschrift, email, password)
            erstell_kunde(nkunde)
            anmeldung_k()
        else:
            pass
        
def anmeldung_k():
    while True:
        emails = lade_kunden_emails()
        while True:
            email = input("Gebe deine Email ein: ")
            if email in emails:
                break
            else:
                print("There is no account linked to this Email")
                print(emails)
                input("Press Enter to try again!")
        while True:
            password = input("Gebe dein Password ein: ")
            if check_log_pw(email, password) == True:
                kundedict = lade_kunde_from_email(email)
                kunde = Kunde(**kundedict)
                app_k(kunde)
            else:
                print("Wrong Password")
                input("Press Enter to try again")
            
def app_k(kunde: Kunde):
    if kunde.konten == {}:
        app_no_kon(kunde)
    else:
        app_kon(kunde)
        
def app_no_kon(kunde: Kunde):
    while True:
        print("Du besitzt kein Konto!")
        print("Wähle eine Option aus")
        print("1. Konto eröffnungsbeantragung")
        print("2. Log out")
        wahl = int(input("Deine Wahl: "))
        if wahl == 1:
            print("Ein Antrag wurde gesendet, es kann etwas dauern bis dieser bearbeitet wrid")
            input("Du wirst vorerst ausgeloggt")
            exit(100)
        elif wahl == 2:
            exit(100)
            
def app_kon(kunde: Kunde):
    while True:
        print("Du hast ein Konto!")
        print("Wähle eine Option aus")
        print("1. Aktueller Kontostand")
        print("2. Einzahlen")
        print("3. Auszahlen")
        print("4. kontaktiere denen Berater")
        print("5. Log out")
        wahl = int(input("Deine Wahl: "))
        if wahl == 1:
            pass
        if wahl == 2:
            pass
        if wahl == 3:
            pass
        if wahl == 4:
            pass
        if wahl == 5:
            exit(100)

def anmeldung_b():
    while True:
        b_id = int(input("Gebe deine mitarbeiter_nummer ein: "))
        passwort = input("Gebe dein Passwort ein: ")

def anmeldung_a():
    print("Wähle eine Option")
    print("1. Berater einstellen")
    print("2. Weise Kunden einen Berater zu")
    print("3. Abmelden")
    wahl = int(input("Deine Auswahl: "))
    if wahl == 1:
        brid = random.randint(10000, 99999)
        pw = "password" + str(random.randint(1000, 9999))
        nachname = input("Gebe den nachnamen des neuen Mitarbeiter ein: ")
        vorname = input("Gebe den Vornamen des neuen Mitarbeiters ein")
        
        newberater = Berater(brid, pw, nachname, vorname)
        berater_einstellen(newberater)
        print("Neuer Berater eingestellt")
        
    elif wahl == 2:
        k_ohne_b = kunden_ohne_berater()
        print("Wähle einen Kunden")
        for i, x in enumerate(k_ohne_b):
            print(f"{i+1}. {x}")
        choice = int(input("Wähle eine kundennr"))
        for i, x in enumerate(k_ohne_b):
            if i+1 == choice:
                to_be_linked_k = x
        print("Wähle einen Berater")
        brid_list = lade_alle_berater_brid()
        for i, x in enumerate(brid_list):
            print(f"{i+1}. {x}")
        choice = int(input("Wähle einen Berater"))
        for i, x in enumerate(brid_list):
            if i+1 == choice:
                to_be_linked_b = x
        to_be_linked_b: Berater
        to_be_linked_b.plus_kunde(to_be_linked_k)
        
        akt_berater(to_be_linked_b)
        
        
        
        
    elif wahl == 3:
        exit(100)
    
register_k()