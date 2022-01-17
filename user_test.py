import unittest

import player


class UserTest(unittest.TestCase):
    
    def test_when_the_user_input_its_out_of_range_then_its_choices_are_empty(self):
        user_1 = player.Player()
        user_1.add_choice('C4')
        
        def empty_choices():
            return not(user_1.choices)

        self.assertTrue(empty_choices())
    
    def test_when_the_user_input_its_not_a_string_with_len_2_then_its_choices_are_empty(self):
        user_1 = player.Player()
        user_1.add_choice('C1A')
        
        def empty_choices():
            return not(user_1.choices)

        self.assertTrue(empty_choices())
    
    def test_when_the_user_has_three_or_more_choices_and__its_a_diagonal_win_than_user_status_should_be_winner(self):
        user_1 = player.Player()
        user_1.add_choice('A1')
        user_1.add_choice('B2')
        user_1.add_choice('C3')

        self.assertTrue(user_1.status == "winner")
        



if __name__ == "__main__":
    unittest.main()