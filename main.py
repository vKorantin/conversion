# Généralités.
forme_depart_valide = False
forme_arrivee_valide = False

# Fonctions.
def convertir_forme(forme):
    while forme != "1" or forme != "2" or forme != "3":
        if forme == "1":
            new_forme = "binaire"
            return new_forme
        elif forme == "2":
            new_forme = "decimal"
            return new_forme
        elif forme == "3":
            new_forme = "hexadecimal"
            return new_forme
        else:
            forme = input("Entrez le nombre correspondant : ")

# A partir du binaire.
def con_bin_dec(mot):
    print()
    mot_final = 0
    mot_depart = mot
    print("Traduction du mot binaire {} en décimal...".format(mot_depart))
    mot_a_traduire = []
    for i in range(0, len(mot_depart), 1):
        mot_a_traduire.append(int(mot_depart[i]))
    mot_a_traduire.reverse()
    for i in range(0, len(mot_a_traduire), 1):
        mot_final += mot_a_traduire[i]*2**i
    return mot_final

def con_bin_hex(mot):
    pass

# A partir du decimal.
def con_dec_bin(mot):
    print()
    mot_final = []
    mot_final_conv = ""
    mot_depart = int(mot)
    print("Traduction du mot décimal {} en binaire...".format(mot_depart))
    while mot_depart > 0:
        mot_final.append(mot_depart % 2)
        mot_depart = int(mot_depart / 2)
    mot_final.reverse()
    for elt in mot_final:
        mot_final_conv += str(elt)
    return mot_final_conv

def con_dec_hex(mot):
    pass

# A partir de l'hexadecimal.
def con_hex_bin(mot):
    pass

def con_hex_dec(mot):
    pass


###################################################################################################################

# Choix de conversion.
print("De quelle forme est le mot à traduire ?")
print()
print("1. Binaire")
print("2. Décimal")
print("3. Héxadécimal (à venir)")
print()

forme_depart = input("Entrez le nombre correspondant : ")

while forme_depart_valide == False:
    try:
        int(forme_depart)
    except ValueError:
        forme_depart = input("Entrez le nombre correspondant : ")
    else:
        forme_depart = convertir_forme(forme_depart)
        forme_depart_valide = True

print("Dans quelle forme voulez-vous le traduire ?")
print()
print("1. Binaire")
print("2. Décimal")
print("3. Héxadécimal (à venir)")
print()

forme_arrivee = input("Entrez le nombre correspondant : ")

while forme_arrivee_valide == False:
    try:
        int(forme_arrivee)
    except ValueError:
        forme_arrivee = input("Entrez le nombre correspondant : ")
    else:
        forme_arrivee = convertir_forme(forme_arrivee)
        forme_arrivee_valide = True

# Si les deux formes sont identiques.
if forme_depart == forme_arrivee:
    print("Ce sont les mêmes formes, le mot est déjà traduit.")

print()
choix_mot = input("Entrez le mot à traduire : ")
print()

# Choix de la fonction.
if forme_depart == "binaire":
    if forme_arrivee == "decimal":
        print("Le mot décimal est {}.".format(con_bin_dec(choix_mot)))
    elif forme_arrivee == "hexadecimal":
        pass
elif forme_depart == "decimal":
    if forme_arrivee == "binaire":
        print("Le mot binaire est {}.".format(con_dec_bin(choix_mot)))
    elif forme_arrivee == "hexadecimal":
        pass
elif forme_depart == "hexadecimal":
    if forme_arrivee == "binaire":
        pass
    elif forme_arrivee == "decimal":
        pass