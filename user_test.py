import unittest

import player


class UserTest(unittest.TestCase):
    def test_when_the_user_input_its_out_of_range_then_its_choices_are_empty(self):
        user_1 = player.Player()
        user_1.add_choice('C4')
    
        self.assertFalse(user_1.choices)
    
    def test_when_the_user_input_its_not_a_string_with_len_2_then_its_choices_are_empty(self):
        user_1 = player.Player()
        user_1.add_choice('C1A')
        
        self.assertFalse(user_1.choices)
    
    def test_when_the_user_has_five_choices_and__its_a_crescent_diagonal_win_than_user_status_should_be_winner(self):
        user_1 = player.Player()
        user_1.add_choice('A1')
        user_1.add_choice('A2')
        user_1.add_choice('B1')
        user_1.add_choice('B2')
        user_1.add_choice('C3')

        self.assertEqual(user_1.status, "winner")
        

    def test_when_the_user_has_five_choices_and__its_a_decrescent_diagonal_win_than_user_status_should_be_winner(self):
        user_1 = player.Player()
        user_1.add_choice('A1')
        user_1.add_choice('A3')
        user_1.add_choice('B1')
        user_1.add_choice('B2')
        user_1.add_choice('C1')

        self.assertEqual(user_1.status, "winner")
        


if __name__ == "__main__":
    unittest.main()