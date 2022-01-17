import unittest

import player


class UserTest(unittest.TestCase):
    
    def test_when_the_user_inputs_its_out_of_range_then_its_choices_are_empty(self):
        user_1 = player.Player()
        user_1.add_choice('C4')
        
        def empty_choices():
            return not(user_1.choices)

        self.assertTrue(empty_choices())



if __name__ == "__main__":
    unittest.main()