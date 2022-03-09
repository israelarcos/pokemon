from stats_commands_attacks import *
from classes import *

#Pokemons

pikachu = Pokemon("Pikachu", "electric", None, 35)
bulbasaur = Pokemon("Bulbasaur", "grass", "poison", 45)




#Stats

pikachu.stats = {
    HP: 35,
    ATTACK: 55,
    DEFENSE: 30,
    SPATTACK: 50,
    SPDEFENSE: 50,
    SPEED: 90
}



bulbasaur.stats = {
    HP: 45,
    ATTACK: 49,
    DEFENSE: 49,
    SPATTACK: 65,
    SPDEFENSE: 65,
    SPEED: 45
}



#Attacks
pikachu.attacks = [Attack("Thunderbolt", "electric", SPECIAL, 95, 100, 15),
                   Attack("Thunder Wave", "electric", NON_DAMAGE, 0, 100, 20),
                   Attack("Surf", "water", SPECIAL, 95, 100, 15),
                   Attack("Seismic Toss", "fighting", PHYSICAL, 1, 100, 20)]


bulbasaur.attacks = [Attack("Sleep Powder", "grass", NON_DAMAGE, 0, 75, 15),
                   Attack("Swords Dance", "normal", NON_DAMAGE, 0, 0, 30),
                   Attack("Razor Leaf", "grass", SPECIAL, 55, 95, 25),
                   Attack("Body Slam", "normal", PHYSICAL, 85, 100, 15)]







def ask_command(pokemon):
    command = None
    while not command:
        tmp_command = input("What should "+pokemon.name+" do?").split(" ")
        if len(tmp_command) == 2:
            try:
                if tmp_command[0] == DO_ATTACK and 0 <= int(tmp_command[1]) < 4:
                    command = Command({DO_ATTACK: int(tmp_command[1])})
            except Exception:
                pass
    return command

#Start battle

battle = Battle(pikachu, bulbasaur)

while not battle.is_finished():
    #Main pokemon battle loop
    #First ask for the commands
    command1 = ask_command(pikachu)
    command2 = ask_command(bulbasaur)

    #Generate new turn
    turn = Turn()
    turn.command1 = command1
    turn.command2 = command2

    if turn.can_start():
        # Execute turn
        battle.execute_turn(turn)
        battle.print_current_status()