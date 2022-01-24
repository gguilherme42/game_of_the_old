from print_table import print_hash_table
from player import Player

HASH_TABLE = [['-','-','-'],
            ['-','-','-'],
            ['-','-','-']]

def convert_column_letter_to_number_column(column_letter: str):
    column_converter = {'A': 0, 'B': 1, 'C': 2}

    return column_converter[column_letter]

def convert_line_number_to_valid_index_line_number(line_number: str):
    line_converter = {'1': 0, '2': 1, '3':2}
    return line_converter[line_number]

def is_position_not_ocupated(position: str):
    column = convert_column_letter_to_number_column(position[0])
    line = convert_line_number_to_valid_index_line_number(position[1])
    
    return HASH_TABLE[line][column] == "-"

def add_choice_to_hash_talbe(position: str, player_marker: str):
    column = convert_column_letter_to_number_column(position[0])
    line = convert_line_number_to_valid_index_line_number(position[1])
     
    if is_position_not_ocupated(position):
        HASH_TABLE[line][column] = player_marker

def input_hash_position(player_name: str):
    import sys
    input_pattern = 'A1B1C1A2C2B2A3B3C3'

    while True:
        try:
            result = str(input(f"{player_name} -> Posição: ")).strip().upper()
            if result in input_pattern:

                if is_position_not_ocupated(result):
                    return result
        except IndexError:
            print("POSIÇÃO INVÁLIDA!")
        
        except KeyboardInterrupt:
            sys.exit()
        else:
            print("POSIÇÃO INVÁLIDA!")


if __name__ == "__main__":
    user = Player("Guilherme")
    enemy = Player("Enemy", "O")
    print_hash_table(HASH_TABLE)
    while True:

        user_input = input_hash_position(user.name)
        user.add_choice(user_input)
        add_choice_to_hash_talbe(user_input, user.marker)
        print_hash_table(HASH_TABLE)

        enemy_input = input_hash_position(enemy.name)
        enemy.add_choice(enemy_input)
        add_choice_to_hash_talbe(enemy_input, enemy.marker)
        print_hash_table(HASH_TABLE)

        if user.status == "winner":
            print(f"Você ganhou, {user.name}!")
            break
        break