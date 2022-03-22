import random

from termcolor import cprint

from classes import Ataque, Grid, Player, Pokemon, TipoAtaque
from helpers import (clear_and_print_map, get_temporal_coords,
                     interact_with_map, is_valid_move, print_color_for_pokemon)

# Tipos Ataques
fuego = TipoAtaque('fuego', ['agua'])
agua = TipoAtaque('agua', ['fuego'])
electrico = TipoAtaque('electrico', ['agua'])
fuerza = TipoAtaque('fuerza', ['fuego', 'agua', 'electrico'])
        
# Ataques
ataque_rayo = Ataque('rayo', 600, 'electrico')
ataque_colazo = Ataque('cola de hierro', 400, 'fuerza')
lista_Ataques_1 = [ataque_colazo, ataque_rayo]

ataque_bola_fuego = Ataque('bola de fuego', 800, 'fuego')
ataque_garrazo = Ataque('garrazo', 250, 'fuerza')
lista_Ataques_2 = [ataque_bola_fuego, ataque_garrazo]

ataque_hidrobomba = Ataque('hidrobomba', 1000, 'agua')
ataque_mordida = Ataque('mordida', 700, 'fuerza')
lista_Ataques_3 = [ataque_mordida, ataque_hidrobomba]
 
# Pokes  
pikachu = Pokemon('Pikachu', 'electrico', 1000, lista_Ataques_1)
charizard = Pokemon('Charizard', 'fuego', 3000, lista_Ataques_2)
eevee = Pokemon('Eevee', 'agua', 1500, lista_Ataques_3)

lista_pokemons = [pikachu, charizard, eevee]

# Player
cprint('Welcome to Pokemon Game!!!', 'green')
player_name = str(input('Type the name of your player: '))

cprint('Please, select one of the following Pokemons', 'green')
for index, poke in enumerate(lista_pokemons):
    cprint(f'{index}: {poke.name}', print_color_for_pokemon(poke))

chosen_poke = int(input('Type the ID of the pokemon you choose: '))

if chosen_poke == 0:
    player = Player(player_name, [pikachu])
elif chosen_poke == 1:
    player = Player(player_name, [charizard])
elif chosen_poke == 2:
    player = Player(player_name, [eevee])

# Map
map = Grid()
size = 5
map.build_map(size)
initial_rand_x = random.randint(0, size - 1)
initial_rand_y = random.randint(0, size - 1)
current_coordinates = [initial_rand_x, initial_rand_y]
map.paint_map(current_coordinates)

while player.get_num_captured_pokes() < 4 and player.number_of_pokemons_alive() > 0:
    clear_and_print_map(map, current_coordinates)
    
    movement = str(input('Please, enter a movement: '))
    
    if movement == 'w':
        temporal_coords = get_temporal_coords(movement, current_coordinates)
        if is_valid_move(size, temporal_coords):
            current_coordinates[0] -= 1
            clear_and_print_map(map, current_coordinates)
        else:
            print('Not valid move!!!!!!!')

    elif movement == 's':
        temporal_coords = get_temporal_coords(movement, current_coordinates)
        if is_valid_move(size, temporal_coords):
            current_coordinates[0] += 1
            clear_and_print_map(map, current_coordinates)
        else:
            print('Not valid move!!!!!!!')
        
    elif movement == 'd':
        temporal_coords = get_temporal_coords(movement, current_coordinates)
        if is_valid_move(size, temporal_coords):
            current_coordinates[1] += 1
            clear_and_print_map(map, current_coordinates)
        else:
            print('Not valid move!!!!!!!')
        
    elif movement == 'a':
        temporal_coords = get_temporal_coords(movement, current_coordinates)
        if is_valid_move(size, temporal_coords):
            current_coordinates[1] -= 1
            clear_and_print_map(map, current_coordinates)
        else:
            print('Not valid move!!!!!!!')
            
    elif movement == 'p':
        print('Your pokemons are: ')
        for poke in player.lista_pokes:
            cprint(f'Name: {poke.name}', print_color_for_pokemon(poke))
            cprint(f'Tipo: {poke.tipo}', print_color_for_pokemon(poke))
            cprint(f'Life Points: {poke.salud}', print_color_for_pokemon(poke))
            
    elif movement == 'b':
        print('Your bag has the following items: ')
        cprint(f'Coins: {player.money}', 'yellow')
        cprint(f'Pokeballs: {player.pokeballs}', 'red')
        cprint(f'Potions to cure: {player.potions_cure}', 'green')
        cprint(f'Potions to increase damage: {player.potions_damage}', 'blue')
            
            
    interact_with_map(map.map, player, current_coordinates, lista_pokemons)
        
