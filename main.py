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


def add_choice_to_hash_talbe(position: str, player_marker: str):
    column = convert_column_letter_to_number_column(position[0])
    line = convert_line_number_to_valid_index_line_number(position[1])
    
    position_is_not_ocupated = HASH_TABLE[line][column] == "-"
    if position_is_not_ocupated:
        HASH_TABLE[line][column] = player_marker

if __name__ == "__main__":
    user = Player()
    print_hash_table(HASH_TABLE)
    while True:

        user_input = str(input("Posição: "))
        user.add_choice(user_input)
        print_hash_table(HASH_TABLE)
        if user.status == "winner":
            print(f"Você ganhou, {user.name}!")
            break
        break