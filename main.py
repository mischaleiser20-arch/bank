from models import Kunde, Konto, Berater
import random
from file_handler import erstell_kunde, lade_kunden_emails, lade_kunde_from_email, berater_einstellen, lade_kundennr, kunden_ohne_berater, lade_alle_berater_brid, akt_berater, lad_berater_mit_brid, lade_kunde_from_kdnr, speicher_kunde, lade_konto, erstelle_konto, speicher_konto
from auth import check_log_pw, check_log_pw_b

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
            break
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
                input("Press Enter to try again!")
        while True:
            password = input("Gebe dein Password ein: ")
            if check_log_pw(email, password) == True:
                kundedict = lade_kunde_from_email(email)
                kunde = Kunde(
                    kundedict["kundennr"],
                    kundedict["nachname"],
                    kundedict["vorname"],
                    kundedict["anschrift"],
                    kundedict["email"],
                    kundedict["l_pw"]
                )
                kunde.konten = kundedict.get("konten", [])
                return kunde
            else:
                print("Wrong Password")
                input("Press Enter to try again")

def app_k(kunde: Kunde):
    if kunde.konten == []:
        app_no_kon(kunde)
    else:
        print("Du hast ein oder mehrer Konten wähle ein Konto aus")
        for i, konto in enumerate(kunde.konten):
            print(f"{i+1}. {konto}")
        wahl_index = int(input("Deine Wahl: ")) - 1
        konto_iban = kunde.konten[wahl_index]
        kunde_konto = lade_konto(konto_iban)
        
        app_kon(kunde, kunde_konto)

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
            break
        elif wahl == 2:
            break

def app_kon(kunde: Kunde, konto: Konto):
    while True:
        konto_c = lade_konto(konto.iban)
        print(f"Du bist auf dem Konto mit der Iban: {konto_c.iban}!")
        print("Wähle eine Option aus")
        print("1. Aktueller Kontostand")
        print("2. Einzahlen")
        print("3. Auszahlen")
        print("4. kontaktiere denen Berater")
        print("5. Log out")
        wahl = int(input("Deine Wahl: "))
        if wahl == 1:
            print(f"Aktueller Kontostand beträgt: {konto_c.saldo}")
            input("Drücke Enter um zurückzukehren")
        if wahl == 2:
            print(f"Dein Kontostand beträgt: {konto_c.saldo}.")
            dep = int(input("Wie viel möchtest du einzahlen: "))
            bes = int(input(f"Du bist dabei {dep}€ einzuzahlen.\n1. Bestätigung\n2. Abbruch\nBitte drücke die 1 um zu bestätigen: ")) #irgendwas klapp hier nicht!!!
            if bes == 1:
                konto_c.einzahlen(dep)
                speicher_konto(konto_c)
                print(f"Transaktion vollendet")
            elif bes == 2:
                input("Die Transaktion Wurde abgebrochen")
        if wahl == 3:
            print(f"Dein Kontostand beträgt: {konto_c.saldo}.")
            dep = int(input("Wie viel möchtest du auszahlen: "))
            bes = int(input(
                f"Du bist dabei {dep}€ auszuzahlen.\n1. Bestätigung\n2. Abbruch\nBitte drücke die 1 um zu bestätigen: "
            ))
            if bes == 1:
                konto_c.auszahlen(dep)
                speicher_konto(konto_c)
                input("Transaktion vollendet")
            elif bes == 2:
                input("Die Transaktion Wurde abgebrochen")
                
        if wahl == 4:
            pass
        if wahl == 5:
            exit(100)

def anmeldung_b():
    while True:
        brid = lade_alle_berater_brid()
        while True:
            b_id = int(input("Gebe deine mitarbeiter_nummer ein: "))
            if b_id in brid:
                break
            else:
                print("Falsche ID")
                input("Drücke Enter um nochmal zu versuchen")
        while True:
            pw = input("Gebe dein Passwort ein: ")
            if check_log_pw_b(b_id, pw):
                berater_c = lad_berater_mit_brid(b_id)
                return berater_c
            else:
                print("Falsches passwort")
                input("Drücke Enter um erneut zu versuchen")


def anmeldung_a():
    while True:
        print("Wähle eine Option")
        print("1. Berater einstellen")
        print("2. Weise Kunden einen Berater zu")
        print("3. Abmelden")
        wahl = int(input("Deine Auswahl: "))
        if wahl == 1:
            brid = random.randint(10000, 99999)
            pw = "password" + str(random.randint(1000, 9999))
            nachname = input("Gebe den nachnamen des neuen Mitarbeiter ein: ")
            vorname = input("Gebe den Vornamen des neuen Mitarbeiters ein: ")
            
            newberater = Berater(brid, pw, nachname, vorname)
            berater_einstellen(newberater)
            print("Neuer Berater eingestellt")
            
        elif wahl == 2:
            k_ohne_b = kunden_ohne_berater()
            print("Wähle einen Kunden")
            for i, x in enumerate(k_ohne_b):
                print(f"{i+1}. {x}")
            choice = int(input("Wähle eine kundennr: "))
            for i, x in enumerate(k_ohne_b):
                if i+1 == choice:
                    to_be_linked_k = x
            brid_list = lade_alle_berater_brid()
            for i, x in enumerate(brid_list):
                print(f"{i+1}. {x}")
            choice = int(input("Wähle einen Berater: "))
            for i, x in enumerate(brid_list):
                if i+1 == choice:
                    to_be_linked_b = x
            berater_obj = lad_berater_mit_brid(to_be_linked_b)
            berater_obj.plus_kunde(to_be_linked_k)
            
            akt_berater(berater_obj)
            
        elif wahl == 3:
            break

def app_b(b: Berater):
    while True:
        berater = b
        print(berater.brid)
        input("Du bist in Berater App")
        print("1. Kunden verwalten")
        print("2. Logout")
        
        wahl = int(input("Wähle eine Option: "))
        if wahl == 1:
            kundenverwaltung(berater)
        elif wahl == 2:
            break

def kundenverwaltung(b: Berater):
    while True:
        berater = b
        kunden = lade_kundennr()
        for i, kunde in enumerate(kunden):
            print(f"{i+1}. {kunde}")
        wahl = int(input("Wähle einen Kunden: ")) - 1
        k_kdnr = kunden[wahl]
        for i, kunde in enumerate(kunden):
            if i == wahl:
                while True:
                    print("1. Konto öffnen")
                    print("2. Zurück")
                    
                    wahl = int(input("Wähle eine Option: "))
                    if wahl == 1:
                        b_kunde = lade_kunde_from_kdnr(k_kdnr)
                        konto_iban = berater.konto_oeffnen(b_kunde)
                        speicher_kunde(b_kunde)
                        kunde_konto = Konto(konto_iban)
                        input(f"Konto für den kunten mit der ID:{b_kunde.kundennr} wurde erstellt")
                        erstelle_konto(kunde_konto)
                        
                    if wahl == 2:
                        break
        break

def k_wahl():
    while True:
        print("1. Anmeldung")
        print("2. Registrierung")
        print("3. Zurück")
        
        wahl = int(input("Gebe eine Angabe: "))
        if wahl == 1:
            kunde = anmeldung_k()
            app_k(kunde)
        elif wahl == 2:
            register_k()
            kunde = anmeldung_k()
            app_k(kunde)
        elif wahl == 3:
            break


def menu():
    while True:
        print("1. Kunde")
        print("2. Berater")
        print("3. Admin")
        print("4. Exit")
        
        wahl = int(input("Wähle eine Option: "))
        
        if wahl == 1:
            k_wahl()
        
        if wahl == 2:
            berater = anmeldung_b()
            app_b(berater)
            
        if wahl == 3:
            anmeldung_a()
        
        if wahl == 4:
            break

menu()
