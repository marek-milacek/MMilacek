def vypocitaj_prumer():
    """
    Program pro výpočet váženého průměru školních známek.
    Známky: 1-5, váhy: 1-10
    """
    znamky = []
    vahy = []
    
    print("=" * 50)
    print("VÝPOČET VÁŽENÉHO PRŮMĚRU ZNÁMEK")
    print("=" * 50)
    print("\nZadávejte známky (1-5) a jejich váhy (1-10)")
    print("Pro ukončení zadávání stiskněte Enter bez zadání známky\n")
    
    while True:
        # Zadání známky
        znamka_input = input("Zadejte známku (1-5) nebo Enter pro ukončení: ").strip()
        
        if znamka_input == "":
            break
            
        try:
            znamka = float(znamka_input)
            
            # Kontrola rozsahu známky
            if znamka < 1 or znamka > 5:
                print("❌ Chyba: Známka musí být v rozsahu 1-5!")
                continue
            
            # Zadání váhy
            vaha_input = input("Zadejte váhu této známky (1-10): ").strip()
            vaha = float(vaha_input)
            
            # Kontrola rozsahu váhy
            if vaha < 1 or vaha > 10:
                print("❌ Chyba: Váha musí být v rozsahu 1-10!")
                continue
            
            # Přidání platných hodnot
            znamky.append(znamka)
            vahy.append(vaha)
            print(f"✓ Přidáno: známka {znamka}, váha {vaha}\n")
            
        except ValueError:
            print("❌ Chyba: Zadejte platné číslo!\n")
    
    # Výpočet a zobrazení výsledků
    if len(znamky) == 0:
        print("\n⚠ Nebyly zadány žádné známky!")
        return
    
    print("\n" + "=" * 50)
    print("PŘEHLED ZNÁMEK:")
    print("=" * 50)
    for i, (z, v) in enumerate(zip(znamky, vahy), 1):
        print(f"{i}. Známka: {z}, Váha: {v}")
    
    # Výpočet váženého průměru
    soucet_vazenych = sum(z * v for z, v in zip(znamky, vahy))
    soucet_vah = sum(vahy)
    vazeny_prumer = soucet_vazenych / soucet_vah
    
    # Výpočet prostého průměru pro srovnání
    prosty_prumer = sum(znamky) / len(znamky)
    
    print("\n" + "=" * 50)
    print("VÝSLEDKY:")
    print("=" * 50)
    print(f"Počet známek: {len(znamky)}")
    print(f"Prostý průměr: {prosty_prumer:.2f}")
    print(f"Vážený průměr: {vazeny_prumer:.2f}")
    print("=" * 50)
    
    # Slovní hodnocení
    if vazeny_prumer <= 1.5:
        hodnoceni = "Výborný 👏"
    elif vazeny_prumer <= 2.5:
        hodnoceni = "Chvalitebný 👍"
    elif vazeny_prumer <= 3.5:
        hodnoceni = "Dobrý"
    elif vazeny_prumer <= 4.5:
        hodnoceni = "Dostatečný"
    else:
        hodnoceni = "Nedostatečný"
    
    print(f"\nCelkové hodnocení: {hodnoceni}")


if __name__ == "__main__":
    vypocitaj_prumer()
    
    # Možnost opakování
    while True:
        znovu = input("\nChcete provést další výpočet? (ano/ne): ").strip().lower()
        if znovu in ["ano", "a", "y", "yes"]:
            print("\n")
            vypocitaj_prumer()
        else:
            print("\nDěkuji za použití programu!")
            break
