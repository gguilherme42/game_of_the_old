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


def add_choice_to_hash_talbe(position: str, player_marker: str):
    column = convert_column_letter_to_number_column(position[0])
    line = convert_line_number_to_valid_index_line_number(position[1])
    
    position_is_not_ocupated = hash_table[line][column] == "-"
    if position_is_not_ocupated:
        hash_table[line][column] = player_marker


class PlayerTest(unittest.TestCase):
    def setUp(self):
        self.user = Player()    
        self.enemy = Player('Enemy', 'O')
    
    def tearDown(self):
        hash_table = [['-','-','-'],
        ['-','-','-'],
        ['-','-','-']]

        

    def test_when_an_user_adds_a_valid_position(self):
        user_choice = 'A3'
        self.user.add_choice(user_choice)
        add_choice_to_hash_talbe(user_choice, self.user.marker)

        expected = [
            # A   B    C
            ['-','-','-'], # 1
            ['-','-','-'], # 2
            ['X','-','-']] # 3
        
        self.assertEqual(hash_table, expected)


    def test_when_user_and_enemy_add_their_choices(self):
        user_choice = 'A3'
        enemy_choice = 'B2'
        
        self.user.add_choice(user_choice)
        add_choice_to_hash_talbe(user_choice, self.user.marker)
        
        self.enemy.add_choice(enemy_choice)
        add_choice_to_hash_talbe(enemy_choice, self.enemy.marker)

        expected = [
            # A   B    C
            ['-','-','-'], # 1
            ['-','O','-'], # 2
            ['X','-','-']] # 3
        
        self.assertEqual(hash_table, expected)

    def test_when_enemy_tries_an_ocupated_position(self):
        user_choice = 'A3'
        enemy_choice = 'A3'
        
        self.user.add_choice(user_choice)
        add_choice_to_hash_talbe(user_choice, self.user.marker)
        
        self.enemy.add_choice(enemy_choice)
        add_choice_to_hash_talbe(enemy_choice, self.enemy.marker)

        expected = [
            # A   B    C
            ['-','-','-'], # 1
            ['-','-','-'], # 2
            ['X','-','-']] # 3
        
        self.assertEqual(hash_table, expected)

        


if __name__ == "__main__":
    unittest.main()