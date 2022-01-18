import unittest

from player import Player


class PlayerTest(unittest.TestCase):
    def setUp(self):
        self.player_1 = Player()

    def test_when_the_player_input_its_out_of_range_then_its_choices_are_empty(self):
        self.player_1.add_choice('C4')
    
        self.assertFalse(self.player_1.choices)
    
    def test_when_the_player_input_its_a_string_with_len_bigger_than_2_then_its_choices_are_empty(self):
        self.player_1.add_choice('C1A')
        
        self.assertFalse(self.player_1.choices)

    def test_when_the_player_input_its_not_a_string_then_its_choices_are_empty(self):
        self.player_1.add_choice(12.4)
        
        self.assertFalse(self.player_1.choices)
    
    def test_when_the_player_has_five_choices_and__its_a_crescent_diagonal_win_than_player_status_should_be_winner(self):
        self.player_1.add_choice('A1')
        self.player_1.add_choice('A2')
        self.player_1.add_choice('B1')
        self.player_1.add_choice('B2')
        self.player_1.add_choice('C3')

        self.assertEqual(self.player_1.status, "winner")
        

    def test_when_the_player_has_five_choices_and__its_a_decrescent_diagonal_win_than_player_status_should_be_winner(self):
        self.player_1.add_choice('A1')
        self.player_1.add_choice('A3')
        self.player_1.add_choice('B1')
        self.player_1.add_choice('B2')
        self.player_1.add_choice('C1')

        self.assertEqual(self.player_1.status, "winner")

    def test_when_the_player_has_four_choices_and_its_a_horizontal_win_than_player_status_should_be_winner(self):
        self.player_1.add_choice('A1')
        self.player_1.add_choice('C1')
        self.player_1.add_choice('A3')
        self.player_1.add_choice('B1')
        
        self.assertEqual(self.player_1.status, "winner")
    
    def test_when_the_player_has_five_choices_and_its_a_vertical_win_then_player_status_should_be_winner(self):
        self.player_1.add_choice('C2')
        self.player_1.add_choice('C1')
        self.player_1.add_choice('C3')
        self.player_1.add_choice('A3')
        self.player_1.add_choice('B1')
        
        self.assertEqual(self.player_1.status, "winner")

        


if __name__ == "__main__":
    unittest.main()