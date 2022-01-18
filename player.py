from random import choices


def convert_list_to_string(input_list):
    result = ""
    for element in input_list:
        result += element
    return result


def valid_user_crescent_diagonal_win(user_choices):
    crescent_pattern = 'A1B2C3' 
    result = filter(lambda user_choice: user_choice in crescent_pattern, sorted(user_choices))
    result = convert_list_to_string(result)
    return result == crescent_pattern
        

def valid_user_decrescent_diagonal_win(user_choices):
    decrescent_pattern = 'A3B2C1'
    result = filter(lambda user_choice: user_choice in decrescent_pattern, sorted(user_choices))
    result = convert_list_to_string(result)
    return result == decrescent_pattern




class Player():
    def __init__(self, name="User 1") -> None:
        self.name = name
        self.choices = []
        self.status: str = None

    def add_choice(self, choice: str):
        def validate_user_win():
            return True

        if choice.upper() in 'A1B1C1A2C2B2A3B3C3' and len(choice) == 2:
            self.choices.append(choice)

            if len(self.choices) >= 3 and validate_user_win():
                self.status = "winner"

        