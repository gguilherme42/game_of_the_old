import unittest

from player import Player


class PlayerTest(unittest.TestCase):
    def setUp(self):
        self.player_1 = Player()
        

    def test_when_the_players_input_its_out_of_range(self):
        previous_len = len(self.player_1.choices)
        self.player_1.add_choice('C4')
        last_len = len(self.player_1.choices)
    
        self.assertEqual(last_len, previous_len)
    
    def test_when_the_player_input_its_a_string_with_len_bigger_than_2_then_its_choices_are_empty(self):
        self.player_1.add_choice('C1A')
        
        self.assertFalse(self.player_1.choices)

    def test_when_the_player_input_its_not_a_string_then_its_choices_are_empty(self):
        self.player_1.add_choice(12.4)
        
        self.assertFalse(self.player_1.choices)
    
    def test_when_the_player_tries_to_input_the_same_position(self):
        self.player_1.add_choice('C1')
        previos_len = len(self.player_1.choices)
        self.player_1.add_choice('C1')
        last_len = len(self.player_1.choices)

        self.assertEqual(last_len, previos_len)
    
    def test_crescent_diagonal_win(self):
        self.player_1.add_choice('A1')
        self.player_1.add_choice('A3')
        self.player_1.add_choice('B1')
        self.player_1.add_choice('B2')
        self.player_1.add_choice('C3')

        self.assertEqual(self.player_1.status, "winner")
        

    def test_decrescent_diagonal_win(self):
        self.player_1.add_choice('A1')
        self.player_1.add_choice('A3')
        self.player_1.add_choice('B1')
        self.player_1.add_choice('B2')
        self.player_1.add_choice('C1')

        self.assertEqual(self.player_1.status, "winner")

    def test_horizontal_win(self):
        self.player_1.add_choice('A1')
        self.player_1.add_choice('C1')
        self.player_1.add_choice('A3')
        self.player_1.add_choice('B1')
        
        self.assertEqual(self.player_1.status, "winner")
    
    def test_vertical_win(self):
        self.player_1.add_choice('C2')
        self.player_1.add_choice('C1')
        self.player_1.add_choice('C3')
        self.player_1.add_choice('A3')
        self.player_1.add_choice('B1')
        
        self.assertEqual(self.player_1.status, "winner")

        


if __name__ == "__main__":
    unittest.main()