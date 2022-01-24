import unittest

from player import Player


hash_table = [['-','-','-'],
        ['-','-','-'],
        ['-','-','-']]

def convert_column_letter_to_number_column(column_letter: str):
    column_converter = {'A': 0, 'B': 1, 'C': 2}

    return column_converter[column_letter]

def convert_line_number_to_valid_index_line_number(line_number: str):
    line_converter = {'1': 0, '2': 1, '3':2}
    return line_converter[line_number]


def add_choice_to_hash_talbe(position: str):
    column = convert_column_letter_to_number_column(position[0])
    line = convert_line_number_to_valid_index_line_number(position[1])
    hash_table[line][column] = 'X'


class PlayerTest(unittest.TestCase):
    def setUp(self):
        self.user = Player()
    
        

    def test_when_user_adds_a_valid_position(self):
        user_choice = 'A1'
        self.user.add_choice(user_choice)
        add_choice_to_hash_talbe(user_choice)

        expected = [['X','-','-'],
            ['-','-','-'],
            ['-','-','-']]
        
        self.assertEqual(hash_table, expected)


        


if __name__ == "__main__":
    unittest.main()