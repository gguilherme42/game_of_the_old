from random import choices


def convert_list_to_string(input_list):
    result = ""
    for element in input_list:
        result += element
    return result


def valid_player_crescent_diagonal_win(player_choices):
    crescent_pattern = 'A1B2C3' 
    result = filter(lambda player_choice: player_choice in crescent_pattern, sorted(player_choices))
    result = convert_list_to_string(result)
    return result == crescent_pattern
        

def valid_player_decrescent_diagonal_win(player_choices):
    decrescent_pattern = 'A3B2C1'
    result = filter(lambda player_choice: player_choice in decrescent_pattern, sorted(player_choices))
    result = convert_list_to_string(result)
    return result == decrescent_pattern




class Player():
    def __init__(self, name="player 1") -> None:
        self.name = name
        self.choices = []
        self.status: str = None

    def add_choice(self, choice: str):
        valid_input_options = 'A1B1C1A2C2B2A3B3C3'

        choice = str(choice)

        
        def validate_player_choice():
            return choice.upper() in valid_input_options and len(choice) == 2
        
        
        def validate_player_win():
            return valid_player_crescent_diagonal_win(self.choices) \
                or valid_player_decrescent_diagonal_win(self.choices)

        if validate_player_choice():
            self.choices.append(choice)

            if len(self.choices) >= 3 and validate_player_win():
                self.status = "winner"

        