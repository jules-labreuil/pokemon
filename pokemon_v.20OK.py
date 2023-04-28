import random # importer le module random
import json   # importer le module json
import os     # importer le module os
import sys    # importer le module sys

# Chemin vers la base de données
BASE_DIR = os.path.abspath(os.path.dirname(__file__))   # définition du chemin absolu vers le répertoire du script courant
FILENAME = "pokedex.json"                                # nom du fichier JSON qui stockera les données du pokedex
DB_PATH = os.path.join(BASE_DIR, FILENAME)               # chemin absolu vers le fichier de la base de données

# Vérifier si le fichier de la base de données existe et le créer s'il n'existe pas
if not os.path.exists(DB_PATH):
    with open(DB_PATH, "w") as f:
        json.dump({}, f)

# Charger le pokedex à partir du fichier de sauvegarde
def charger_pokedex():
    with open(DB_PATH, "r") as f:
        pokedex = json.load(f)
        return pokedex

# Fonction pour sauvegarder le pokedex dans un fichier JSON
def sauvegarder_pokedex(pokedex):
    with open(DB_PATH, "w") as f:
        json.dump(pokedex, f)

# Structure de données pour stocker les informations de chaque Pokémon
pokedex = charger_pokedex()


class Pokemon:
    # Initialise les attributs de base d'un Pokémon
    def __init__(self, name, p_type, health=100, level=1, attack_power=25, defense=25, vitesse = 25):
        self.name = name
        self.p_type = p_type
        self.health = int(health)
        self.level = max(1, int(level))
        self.attack_power = int(attack_power)
        self.defense = int(defense)
        self.vitesse = int(vitesse)
        
    def apply_level_bonus(self):
        self.health *= 1 + (self.level - 1) * 0.1
        self.attack_power *= 1 + (self.level - 1) * 0.05
        self.defense *= 1 + (self.level - 1) * 0.05
        self.vitesse *= 1 + (self.level - 1) * 0.05
        self.health = int(round(self.health))
        self.attack_power = int(round(self.attack_power))
        self.defense = int(round(self.defense))
        self.vitesse = int(round(self.vitesse))

    def apply_type_bonus(self):
        if self.p_type == "Feu":
            self.attack_power *= 1.6
            self.health *= 1.1
            self.defense *= 1.1
            self.vitesse *= 1.2
        elif self.p_type == "Eau":
            self.attack_power *= 1.3
            self.health *= 1.1
            self.defense *= 1.4
            self.vitesse *= 1.2
        elif self.p_type == "Terre":
            self.attack_power *= 1.1
            self.health *= 1.4
            self.defense *= 1.4  
            self.vitesse *= 1.1
        elif self.p_type == "Normal":
            self.attack_power *= 1.3
            self.health *= 1.3
            self.defense *= 1.3 
            self.vitesse *= 1.1
        # Ajoutez ici des conditions pour d'autres types de pokemons

    # Récupère le nom du Pokémon
    def get_name(self):
        return self.name

    # Récupère le type du Pokémon
    def get_type(self):
        return self.p_type

    # Récupère la santé du Pokémon
    def get_health(self):
        return self.health

    # Récupère le niveau du Pokémon
    def get_level(self):
        return self.level

    # Récupère la puissance d'attaque du Pokémon
    def get_attack_power(self):
        return self.attack_power

    # Récupère la défense du Pokémon
    def get_defense(self):
        return self.defense
    
     # Récupère la vitesse du Pokémon
    def get_vitesse(self):
        return self.vitesse

    # Définit la puissance d'attaque du Pokémon
    def set_attack_power(self, attack_power):
        self.attack_power = attack_power

    # Définit la défense du Pokémon
    def set_defense(self, defense):
        self.defense = defense

    # Définit la vitesse du Pokémon
    def set_vitesse(self, vitesse):
        self.vitesse = vitesse

    # Définit la santé du Pokémon
    def set_health(self, health):
        self.health = health

    # Définit le niveau du Pokémon
    def set_level(self, level):
        self.level = level

    # Définit le type du Pokémon
    def set_type(self, p_type):
        self.p_type = p_type

    # Renvoie une chaîne de caractères représentant le Pokémon
    def __str__(self):
        return f"{self.name} : Level {self.level} / Type {self.p_type}      STATS= Vie: {self.health}, Attaque: {self.attack_power}, Défense: {self.defense}, Vitesse: {self.vitesse}"



    # Renvoie une liste de tous les Pokémon dans le pokedex
    @staticmethod
    def get_all_pokemons():
        global pokedex
        pokedex = charger_pokedex()
        return [Pokemon(p["name"], p["p_type"], p["health"], p["level"], p["attack_power"], p["defense"], p["vitesse"]) for p in pokedex.values()]


    @staticmethod
    def add_pokemon(pokemon):
        global pokedex
        pokedex = charger_pokedex()
        # Vérifier si le pokemon n'est pas déjà dans la liste
        for p in pokedex.values():
            if p["name"] == pokemon.name:
                return False
        # Appliquer les bonus de type et de niveau
        pokemon.apply_type_bonus()
        pokemon.apply_level_bonus()
        # Ajouter le nouveau pokemon avec toutes les informations
        pokemon_dict = {
            "name": pokemon.name,
            "p_type": pokemon.p_type,
            "level": pokemon.level,
            "health": pokemon.health,
            "attack_power": pokemon.attack_power,
            "defense": pokemon.defense,
            "vitesse": pokemon.vitesse
        }
        pokedex[pokemon.name] = pokemon_dict
        sauvegarder_pokedex(pokedex)
        return True 
    
    

class Feu(Pokemon):
    def __init__(self, name, level=1):
        super().__init__(name, "Feu", level=level)

class Eau(Pokemon):
    def __init__(self, name, level=1):
        super().__init__(name, "Eau", level=level)

class Terre(Pokemon):
    def __init__(self, name, level=1):
        super().__init__(name, "Terre", level=level)

class Normal(Pokemon):
    def __init__(self, name, level=1):
        super().__init__(name, "Normal", level=level)
    


    
# Affichage d'un message de bienvenue
print("Bienvenue sur Pokemon edition Eclatax by Julito")

# Boucle infinie pour demander si l'utilisateur souhaite jouer
while True:
    # Demande à l'utilisateur s'il veut jouer
    jouer = input("Jouer? (oui/non) ")
    
    # Si l'utilisateur répond "oui", alors le jeu commence
    if jouer == "oui":
        # Boucle pour demander à l'utilisateur ce qu'il veut faire
        while True:
            # Demande à l'utilisateur ce qu'il veut faire
            choix = input("Choose your destiny\n1. Consulter pokedex\n2. La bagarre !\n3. Quitter\n")
            
            # Si l'utilisateur choisit l'option 1, alors il peut consulter le pokedex
            if choix == "1":
                # Boucle pour demander à l'utilisateur ce qu'il veut faire dans le pokedex
                while True:
                    # Récupération de la liste des Pokemons et affichage
                    pokedex = Pokemon.get_all_pokemons()
                    print("Liste des Pokemons:")
                    for p in pokedex:
                        print("-", p)
                        
                    # Demande à l'utilisateur ce qu'il veut faire dans le pokedex
                    choix_pokedex = input("Que voulez-vous faire ?\n1. Ajouter Nouveau Pokemon\n2. Supprimer Pokemon\n3. Retour\n")

                    # Si l'utilisateur choisit l'option 1, alors il peut ajouter un nouveau Pokemon
                    if choix_pokedex == "1":
                        # Demande à l'utilisateur le nom, le type et le niveau du Pokemon
                        name = input("Entrez le nom du Pokemon: ")
                        level = input("Entrez le niveau du Pokemon (par défaut: 1): ")
                        valid_types = ["Normal", "Feu", "Eau", "Terre"]
                        while True:
                            p_type = input("Entrez le type du Pokemon (Normal/Feu/Eau/Terre): ")
                            # Vérification de la validité du type de Pokemon
                            if p_type not in valid_types:
                                print("Réponse invalide.")
                            else:
                                # Création du Pokemon en fonction de son type et ajout au pokedex
                                if p_type == "Normal":
                                    pokemon = Normal(name, level)
                                elif p_type == "Feu":
                                    pokemon = Feu(name, level)
                                elif p_type == "Eau":
                                    pokemon = Eau(name, level)
                                elif p_type == "Terre":
                                    pokemon = Terre(name, level)

                                if Pokemon.add_pokemon(pokemon):
                                    print(f"{pokemon.name} a été ajouté au Pokedex!")
                                else:
                                    print(f"{pokemon.name} est déjà dans le Pokedex.")
                                break

                    # Si l'utilisateur choisit l'option 2, alors il peut supprimer un Pokemon
                    elif choix_pokedex == "2":
                        # Demande à l'utilisateur le nom du Pokemon à supprimer
                        name = input("Entrez le nom du Pokemon à supprimer: ")
                        pokedex = charger_pokedex()
                        
                        # Si le Pokemon est dans le pokedex, alors on le supprime
                        if name in pokedex:
                            del pokedex[name]
                            sauvegarder_pokedex(pokedex)
                            print(f"{name} a été supprimé du Pokedex.")
                        else:
                            print(f"{name} n'est pas dans le Pokedex.")
                    
                    # Si l'utilisateur choisit l'option 3, alors on sort de la boucle
                    elif choix_pokedex == "3":
                        break
                        
                    # Si l'utilisateur entre une réponse invalide, on affiche un message
                    else:
                        print("Réponse invalide") 
            
            
            # Si l'utilisateur choisit l'option 2, on affiche un message disant que cette fonctionnalité est en cours de développement
            elif choix == "2":
                class Combat:
                    def __init__(self):
                        with open("pokedex.json") as f:
                            self.pokedex = json.load(f)
                        self.player1_pokemon = None
                        self.skynet_pokemon = None
                    
                    def choose_pokemon(self):
                        # Skynet choisit un pokemon au hasard
                        self.skynet_pokemon = random.choice(self.pokedex)
                        print(f"Skynet a choisi {self.skynet_pokemon['name']}. Quel pokémon appelez vous pour combattre ?")
                        
                        # Le joueur 1 choisit son pokemon
                        player1_choice = input()
                        self.player1_pokemon = None
                        
                        # On vérifie si le pokemon choisi par le joueur existe dans le pokedex
                        for pokemon in self.pokedex:
                            if pokemon["name"].lower() == player1_choice.lower():
                                self.player1_pokemon = pokemon
                                break
                        
                        # Si le pokemon n'existe pas, on demande au joueur de saisir un nouveau nom
                        while self.player1_pokemon is None:
                            print(f"{player1_choice} n'existe pas. Veuillez saisir un nouveau nom.")
                            player1_choice = input()
                            for pokemon in self.pokedex:
                                if pokemon["name"].lower() == player1_choice.lower():
                                    self.player1_pokemon = pokemon
                                    break
                        
                        # Affichage des pokemons
                        print(f"Joueur 1\n{self.player1_pokemon['name']} : Level {self.player1_pokemon['level']} / Type {self.player1_pokemon['p_type']} STATS= Vie: {self.player1_pokemon['health']}, Attaque: {self.player1_pokemon['attack_power']}, Défense: {self.player1_pokemon['defense']}, Vitesse: {self.player1_pokemon['vitesse']}")
                        print(f"VS")
                        print(f"Skynet\n{self.skynet_pokemon['name']} : Level {self.skynet_pokemon['level']} / Type {self.skynet_pokemon['p_type']} STATS= Vie: {self.skynet_pokemon['health']}, Attaque: {self.skynet_pokemon['attack_power']}, Défense: {self.skynet_pokemon['defense']}, Vitesse: {self.skynet_pokemon['vitesse']}")
                        print("Go to war ?")
                    
                    def strike_force(self):
                        # Choix aléatoire du chosen_number
                        chosen_number = random.randint(1, 100)
                        
                        # Choix aléatoire des fail_number et critical_number
                        fail_number = random.sample(range(1, 101), 10)
                        critical_number = random.sample(list(set(range(1, 101)) - set(fail_number)), 10)
                        
                        # Si chosen_number est un fail_number
                        if chosen_number in fail_number:
                            print(f"Echec critique, {self.skynet_pokemon['name']} est pitoyable.")
                            return 0
                        
                        # Si chosen_number est un critical_number
                        elif chosen_number in critical_number:
                            print(f"Coup critique, {self.skynet_pokemon['name']} a envoyé une patate de forain.")
                            return 1.5 * self.player1_pokemon["attack_power"]
                        
                        # Si chosen_number est un normal_number
                        else:
                            print(f"Frappe normale, {self.skynet_pokemon['name']} a réussi son attaque.")
                            return self.player1_pokemon["attack_power"]
                        
                    def final_damage(self, chosen_number, critical_number, fail_number):
                        base_damage = 0
                        if chosen_number in fail_number:
                            base_damage = 0
                        elif chosen_number in critical_number:
                            base_damage = 1.5 * self.player1_pokemon["attack_power"]
                        else:
                            base_damage = self.player1_pokemon["attack_power"]

                        p_type_joueur = self.player1_pokemon["p_type"]
                        p_type_skynet = self.skynet_pokemon["p_type"]

                        if p_type_joueur == "Feu":
                            if p_type_skynet == "Terre":
                                base_damage *= 2
                            elif p_type_skynet == "Eau":
                                base_damage /= 2
                            elif p_type_skynet == "Feu":
                                base_damage *= 1
                            elif p_type_skynet == "Normal":
                                base_damage *= 0.75
                        elif p_type_joueur == "Eau":
                            if p_type_skynet == "Feu":
                                base_damage *= 2
                            elif p_type_skynet == "Terre":
                                base_damage /= 2
                            elif p_type_skynet == "Eau":
                                base_damage *= 1
                            elif p_type_skynet == "Normal":
                                base_damage *= 0.75
                        elif p_type_joueur == "Terre":
                            if p_type_skynet == "Eau":
                                base_damage *= 2
                            elif p_type_skynet == "Feu":
                                base_damage /= 2
                            elif p_type_skynet == "Terre":
                                base_damage *= 1
                            elif p_type_skynet == "Normal":
                                base_damage *= 0.75
                        elif p_type_joueur == "Normal":
                            if p_type_skynet == "Eau":
                                base_damage *= 0.75
                            elif p_type_skynet == "Feu":
                                base_damage *= 0.75
                            elif p_type_skynet == "Terre":
                                base_damage *= 0.75

                        return base_damage
                    
                    def update_skynet_pokemon_health(self, final_damage):
                        self.skynet_pokemon["health"] = round(max(0, self.skynet_pokemon["health"] - (final_damage - self.skynet_pokemon["defense"])))

                    def check_alive(self):
                        if self.player1_pokemon["health"] <= 0:
                            print(f"{self.player1_pokemon['name']} est mort. Skynet a gagné.")
                            return False
                        elif self.skynet_pokemon["health"] <= 0:
                            print(f"{self.skynet_pokemon['name']} est mort. Le joueur 1 a gagné.")
                            return False
                        else:
                            print(f"{self.player1_pokemon['name']} STATS = Vie: {self.player1_pokemon['health']}, Attaque: {self.player1_pokemon['attack_power']}, Défense: {self.player1_pokemon['defense']}, Vitesse: {self.player1_pokemon['vitesse']}")
                            print(f"{self.skynet_pokemon['name']} STATS = Vie: {self.skynet_pokemon['health']}, Attaque: {self.skynet_pokemon['attack_power']}, Défense: {self.skynet_pokemon['defense']}, Vitesse: {self.skynet_pokemon['vitesse']}")
                            return True
        



        # Si l'utilisateur choisit l'option 3, on affiche un message et on quitte le programme
            elif choix == "3":
                print("Bakayaro, Konoyaro!")
                sys.exit(0)
        
        # Si l'utilisateur entre une réponse invalide, on affiche un message
            else:
                print("Réponse invalide")  
    
    # Si l'utilisateur entre 'non', on affiche un message et on quitte le programme
    elif jouer == "non":
        print("Shine kisama!")
        sys.exit(0)

    # Si l'utilisateur entre une réponse invalide, on affiche un message
    else:
        print("Réponse invalide")