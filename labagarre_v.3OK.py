import json
import random

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