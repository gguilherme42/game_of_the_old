from random import choices


def convert_list_to_string(input_list):
    result = ""
    for element in input_list:
        result += element
    return result

def valid_user_diagonal_win(user_choices, is_a_crescent_diagonal: bool):
    diagonal_pattern = 'A1B2C3' if is_a_crescent_diagonal else 'A3B2C1'
    
    result = filter(lambda user_choice: user_choice in diagonal_pattern, sorted(user_choices))
    result = convert_list_to_string(result)
    
    return result == diagonal_pattern

def validate_user_win():
    return True

class Player():
    def __init__(self, name="User 1") -> None:
        self.name = name
        self.choices = []
        self.status: str = None

    def add_choice(self, choice: str):
        def valid_user_crescent_diagonal_win():
            result = filter(lambda user_choice: user_choice in 'A1B2C3', sorted(self.choices))
            result = convert_list_to_string(result)
            return result == 'A1B2C3'
        
        def valid_user_decrescent_diagonal_win():
            result = filter(lambda user_choice: user_choice in 'A3B2C1', sorted(self.choices))
            result = convert_list_to_string(result)
            return result == 'A3B2C1'

        if choice.upper() in 'A1B1C1A2C2B2A3B3C3' and len(choice) == 2:
            self.choices.append(choice)

            if len(self.choices) >= 3 and validate_user_win():
                self.status = "winner"

        