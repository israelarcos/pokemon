import random
import copy

from termcolor import cprint

from helpers import print_intro, print_end


class TipoAtaque():
    def __init__(self, name, counters):
        self.name = name
        self.counters = counters
      
  
class Ataque():
    def __init__(self, name, damage, tipo):
        self.name = name
        self.damage = damage
        self.tipo = tipo
        
        
class Pokemon():
    def __init__(self, name, tipo, salud, ataques):
        self.name = name
        self.tipo = tipo
        self.salud = salud
        self.ataques = ataques
        
    def recibir_damage(self, damage):
        self.salud = self.salud - damage


class Player():
    def __init__(self, name, lista_pokes):
        self.name = name
        self.main_poke = 0
        self.lista_pokes = lista_pokes
        self.money = 0
        self.pokeballs = 0
        self.potions_cure = 0
        self.potions_damage = 0
        
    def get_num_captured_pokes(self):
        return len(self.lista_pokes)
    
    def give_reward(self):
        award = self.money * 0.1
        self.money -= award
        return award
    
    def recieve_reward(self, amount):
        self.money += amount
    
    def number_of_pokemons_alive(self):
        num_pokemons_alive = 0
        for poke in self.lista_pokes:
            if poke.salud > 0:
                num_pokemons_alive += 1
        return num_pokemons_alive
    
    def change_main_poke(self, index_new_main_poke):
        self.main_poke = index_new_main_poke
        
    def add_new_poke(self, poke):
        self.lista_pokes.append(poke)
        
    def lose_main_poke(self):
        main_poke = copy.deepcopy(self.lista_pokes[self.main_poke])
        main_poke_name = main_poke.name
        self.lista_pokes = list(filter(lambda poke: poke.name != main_poke_name, self.lista_pokes))
        return main_poke
        
    def main_poke_recieves_damage(self, damage_amount):
        salud_main_poke = self.lista_pokes[self.main_poke].salud
        self.lista_pokes[self.main_poke].salud = salud_main_poke - damage_amount
        
    def add_pokeballs(self, amount):
        self.pokeballs += amount
        
    def damage_of_main_poke(self):
        main_poke = self.lista_pokes[self.main_poke]
        print('Select the ID attack of the main pokemon:')
        for index, attack in enumerate(main_poke.ataques):
            print(f'{index}: {attack.name}')
        id_attack = int(input('Type an ID attack: '))
        attack_main_poke = main_poke.ataques[id_attack]
        attack_main_poke_damage = attack_main_poke.damage
        return attack_main_poke_damage
    
    def heal_main_poke(self):
        main_poke = self.lista_pokes[self.main_poke]
        if self.potions_cure > 0:
            main_poke.salud += 100
            self.potions_cure -= 1
        

class Grid():
    def __init__(self):
        self.map = None
        
    def build_map(self, size):
        rows = []
        for _ in range(size):
            columns = []
            for _ in range(size):
               value = random.randint(0, 4)
               columns.append(value)
            rows.append(columns)
        self.map = rows
        
    def paint_map(self, player_position):    
        print_intro(self.map)
        
        for i in range(len(self.map)):
            for j in range(len(self.map)):
                if player_position[0] == i and player_position[1] == j:
                    print('\U0001F9B9  ', end = '')
                elif self.map[i][j] == 0 or self.map[i][j] == 1 or self.map[i][j] == 2:
                    print('\U0001F335  ', end = '')
                elif self.map[i][j] == 3:
                    cprint('\U0001F47E  ', end = '')
                elif self.map[i][j] == 4:
                    cprint('\U0001F93A  ', end = '')
            print('\n')
            
        print_end(self.map)
