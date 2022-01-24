import unittest

from player import Player
from main import HASH_TABLE, add_choice_to_hash_talbe


class PlayerTest(unittest.TestCase):
    def setUp(self):
        self.user = Player()    
        self.enemy = Player('Enemy', 'O')
    
    def tearDown(self):
        HASH_TABLE = [['-','-','-'],
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
        
        self.assertEqual(HASH_TABLE, expected)


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
        
        self.assertEqual(HASH_TABLE, expected)

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
        
        self.assertEqual(HASH_TABLE, expected)


if __name__ == "__main__":
    unittest.main()