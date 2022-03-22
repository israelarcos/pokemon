import os
import random
import copy
import time

from termcolor import cprint

class TrainerCPU():
    def __init__(self, name, lista_pokes, money):
        self.name = name
        self.lista_pokes = lista_pokes
        self.money = money
        self.main_poke = 0
        self.potions_cure = 5
        self.potions_damage = 5
        
    def give_reward(self):
        award = self.money * 0.1
        self.money -= award
        return award
    
    def recieve_reward(self, amount):
        self.money += amount
    
    def add_new_poke(self, poke):
        self.lista_pokes.append(poke)
        
    def lose_main_poke(self):
        main_poke = copy.deepcopy(self.lista_pokes[self.main_poke])
        main_poke_name = main_poke.name
        self.lista_pokes = list(filter(lambda poke: poke.name != main_poke_name, self.lista_pokes))
        return main_poke
    
    def number_of_pokemons_alive(self):
        num_pokemons_alive = 0
        for poke in self.lista_pokes:
            if poke.salud > 0:
                num_pokemons_alive += 1
        return num_pokemons_alive
    
    def main_poke_recieves_damage(self, damage_amount):
        salud_main_poke = self.lista_pokes[self.main_poke].salud
        self.lista_pokes[self.main_poke].salud = salud_main_poke - damage_amount
        
    def damage_of_main_poke(self):
        main_poke = self.lista_pokes[self.main_poke]
        id_attack = random.randint(0, 1)
        attack_main_poke = main_poke.ataques[id_attack]
        attack_main_poke_damage = attack_main_poke.damage
        return attack_main_poke_damage
    
    def heal_main_poke(self):
        main_poke = self.lista_pokes[self.main_poke]
        if self.potions_cure > 0:
            main_poke.salud += 100
            self.potions_cure -= 1
            
    def main_poke_recieves_damage(self, damage_amount):
        salud_main_poke = self.lista_pokes[self.main_poke].salud
        self.lista_pokes[self.main_poke].salud = salud_main_poke - damage_amount
        
        
def print_battle_life(cpu, player):
    cpu_main_poke = cpu.lista_pokes[cpu.main_poke]
    player_main_poke = player.lista_pokes[player.main_poke]
    cprint(f'Your poke life is: {player_main_poke.salud}', 'green')
    cprint(f'CPU main poke life is: {cpu_main_poke.salud}', 'red')


def print_intro(map):
    cprint('\nOn \U0001F335 you could find potions for your pokemons', 'green')
    cprint('On \U0001F47E you can find wild pokemons to capture', 'yellow')
    cprint('On \U0001F93A you can fight with other trainers', 'red')
    print('Your Player: \U0001F9B9')
    print('\n')
    print('*' + '-'*(len(map)*4-2) + '*')
    

def print_end(map):
    print('*' + '-'*(len(map)*4-2) + '*')    
    print('\n')
    print('Press to move -> w: \U00002B06  s: \U00002B07   a: \U00002B05   d: \U000027A1')
    print('Press b \U0001F392 to see the items in your backpack')
    print('Press p \U0001F47E to see your available pokemons')

def print_color_for_pokemon(pokemon):
    if pokemon.tipo == 'electrico':
        return 'yellow'
    elif pokemon.tipo == 'fuego':
        return 'red'
    elif pokemon.tipo == 'agua':
        return 'blue'


def is_valid_move(matrix_size, coordinates):
    x = coordinates[0]
    y = coordinates[1]
    
    if (x >= 0 and x <= matrix_size -1) and (y >= 0 and y <= matrix_size - 1):
        return True
    elif x < 0 or x > matrix_size - 1:
        return False
    elif y < 0 or y > matrix_size - 1:
        return False
    

def clear_and_print_map(map, current_coordinates):
    os.system('clear')
    map.paint_map(current_coordinates)


def get_temporal_coords(movement, current_coordinates):
    if movement == 'w':
        temporal_x = current_coordinates[0] - 1
        temporal_y = current_coordinates[1]
        temporal_coords = [temporal_x, temporal_y]
        return temporal_coords
    
    elif movement == 's':
        temporal_x = current_coordinates[0] + 1
        temporal_y = current_coordinates[1]
        temporal_coords = [temporal_x, temporal_y]
        return temporal_coords
    
    elif movement == 'd':
        temporal_x = current_coordinates[0]
        temporal_y = current_coordinates[1] + 1
        temporal_coords = [temporal_x, temporal_y]
        return temporal_coords
    
    elif movement == 'a':
        temporal_x = current_coordinates[0]
        temporal_y = current_coordinates[1] - 1
        temporal_coords = [temporal_x, temporal_y]
        return temporal_coords
    
    
def handle_interaction_items(player):
    prize_type = random.randint(0, 2)
    
    if prize_type == 0:
        player.pokeballs += 1
        print('\nCongrats, you found one pokeball')
    
    elif prize_type == 1:
        potion_type = random.randint(0, 1)
    
        if potion_type == 0:
            player.potions_cure += 1
            print('\nCongrats, you found one postion to cure your pokemons')
    
        if potion_type == 1:
            player.potions_damage += 1
            print('\nCongrats, you found one postion to increase the damage of your pokemons')
    
    elif prize_type == 2:
        player.money += 10
        print('\nCongrats, you found some poke-coins')
        

def handle_interaction_wild_pokes(player, lista_pokemons):
    random_pokemon_id = random.randint(0, 2)
    random_pokemon = lista_pokemons[random_pokemon_id]
    poke_rand_number = random.randint(1, 3)
    player_guess_number = None
    
    if player.pokeballs == 0:
        print('\nSorry, you dont have enough pokeballs.')
    
    print(f'\nTo catch the wild {random_pokemon.name} guess a number from 1 - 3')
    
    while player.pokeballs > 0 and player_guess_number != 0 and poke_rand_number != player_guess_number:
        player_guess_number = int(input('Ingrese su numero (1-3) o 0 para salir'))
        
        player.pokeballs -= 1
        
        if poke_rand_number == player_guess_number:
            player.lista_pokes.append(random_pokemon)
            print('Congrats!! You catch a new Pokemon\n')
        
        if player.pokeballs == 0:
            print('Sorry, you run out of tries. You dont have more pokeballs available.\n')


def handle_interaction_trainer(player, lista_pokemons):
    random_pokemon_id = random.randint(0, 2)
    random_money_amount = random.randint(50, 100)
    copy_lista_pokemons = copy.deepcopy(lista_pokemons)
    random_pokemon = copy_lista_pokemons[random_pokemon_id]
    cpu_name = 'CPU_' + str(random.randint(0, 100))
    cpu = TrainerCPU(cpu_name, [random_pokemon], random_money_amount)
    
    player_action = None

    while player_action != 'x' and player.number_of_pokemons_alive() > 0 and cpu.number_of_pokemons_alive() > 0:
        os.system('clear')
        print_battle_life(cpu, player)
        player_action = str(input('\nPress a \U0001F525 to attack, h \U0001F3E5 to heal your main poke, or x \U0001F6D1 to finish battle: '))
        
        if player_action == 'a':
            damage = player.damage_of_main_poke()
            cpu.main_poke_recieves_damage(damage)
            
            random_cpu_action = random.randint(0, 1)
            
            if random_cpu_action == 0:
                damage = cpu.damage_of_main_poke()
                player.main_poke_recieves_damage(damage)
                cprint('\nCPU attacked your pokemon\n', 'red')
                
            elif random_cpu_action == 1:
                cpu.heal_main_poke()
                cprint('\nCPU cured its pokemon\n', 'red')
                
        elif player_action == 'h':
            player.heal_main_poke()
            
            random_cpu_action = random.randint(0, 1)
            
            if random_cpu_action == 0:
                damage = cpu.damage_of_main_poke()
                player.main_poke_recieves_damage(damage)
                cprint('\nCPU attacked your pokemon\n', 'red')
                
            elif random_cpu_action == 1:
                cpu.heal_main_poke()
                cprint('\nCPU cured its pokemon\n', 'red')
                
        elif player_action == 'x':
            cprint('\nBattle finished!!', 'red')
            
        if player.number_of_pokemons_alive() == 0:
            print('\nYou lost')
            print('You lost your main pokemon')
            poke = player.lose_main_poke()
            cpu.add_new_poke(poke)
            print('You lost poke-coins')
            reward = player.give_reward()
            cpu.recieve_reward(reward)
            
        if cpu.number_of_pokemons_alive() == 0:
            cprint('\nYou won!!!!', 'yellow')
            print('You recieves a new poke')
            poke = cpu.lose_main_poke()
            player.add_new_poke(poke)
            print('You recieves aome poke-coins')
            reward = cpu.give_reward()
            player.recieve_reward(reward)
            
        time.sleep(2)
                


def interact_with_map(map, player, current_coordinates, lista_pokemons):
    x = current_coordinates[0]
    y = current_coordinates[1]

    if map[x][y] == 0 or map[x][y] == 1 or map[x][y] == 2:
        print('\nYou found an item: \U0001F335.') 
        interact = str(input('Press i to interact with it, or c to continue: '))
        if interact == 'i':
            handle_interaction_items(player)
            
    elif map[x][y] == 3:
        print('You found a wild Pokemon: \U0001F47E.')
        interact = str(input('Press i to interact with it, or c to continue: '))
        if interact == 'i':
            handle_interaction_wild_pokes(player, lista_pokemons)
        
    elif map[x][y] == 4:
        print('You found a trainer: \U0001F93A.')
        interact = str(input('Press i to interact with it, or c to continue: '))
        if interact == 'i':
            handle_interaction_trainer(player, lista_pokemons)
    
