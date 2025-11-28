# Import seznamu filmů (v reálné situaci by byl v externím souboru)
filmy = [
    ("Christopher Nolan", "Interstellar", 8.6),
    ("Christopher Nolan", "Inception", 8.8),
    ("Wachowski", "The Matrix", 8.7),
    ("Quentin Tarantino", "Pulp Fiction", 8.9),
    ("Robert Zemeckis", "Forrest Gump", 8.8),
    ("Christopher Nolan", "The Dark Knight", 9.0),
    ("David Fincher", "Fight Club", 8.8),
    ("Frank Darabont", "Shawshank Redemption", 9.3),
    ("Ridley Scott", "Gladiator", 8.5),
    ("Bong Joon-ho", "Parasite", 8.5),
    ("Denis Villeneuve", "Dune", 8.0),
    ("Steven Spielberg", "Schindler's List", 9.0),
    ("Peter Jackson", "The Lord of the Rings", 8.9),
    ("Francis Ford Coppola", "The Godfather", 9.2),
    ("Martin Scorsese", "Goodfellas", 8.7)
]

print(len(filmy))
print(filmy[:5])

# ===== PŘIDÁNÍ NOVÉHO FILMU =====
filmy.append(("Greta Gerwig", "Barbie", 7.2))
print(filmy[-1])

# ===== ODEBRÁNÍ FILMŮ REŽISÉRA =====
filmy_filtered = [film for film in filmy if film[0] != "Christopher Nolan"]
print(filmy_filtered[0:5])

# Alternativní způsob - odebrání ze seznamu
for i in range(len(filmy) - 1, -1, -1):
    if filmy[i][0] == "Greta Gerwig":
        del filmy[i]

print("Počet filmů po odebrání:", len(filmy))
print("Aktuální seznam:", filmy)

# ===== CELKOVÉ HODNOCENÍ =====
total_rating = 0
for film in filmy:
    total_rating += film[2]

print(f"Průměrné hodnocení: {total_rating/len(filmy):.2f}")

# ===== UNIKÁTNÍ REŽISÉŘI =====
unique_directors = set()
for film in filmy:
    unique_directors.add(film[0])

print("Unikátní režiséři:")
for director in unique_directors:
    print(director, end=", ")

# ===== SEŘAZENÍ PODLE HODNOCENÍ =====
filmy.sort(key=lambda film: film[2])

print("\n5 filmů s nejnižším hodnocením:")
for film in filmy[:5]:
    print(f"{film[0]} – {film[1]} ({film[2]})")