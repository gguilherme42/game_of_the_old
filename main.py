from xmlrpc.client import UNSUPPORTED_ENCODING
from print_table import print_hash_table
from player import Player

hash_table = [['-','-','-'],
            ['-','-','-'],
            ['-','-','-']]



if __name__ == "__main__":
    user = Player()
    print_hash_table(hash_table)
    while True:

        user_input = str(input("Posição: "))
        user.add_choice(user_input)
        print_hash_table(hash_table)
        if user.status == "winner":
            print(f"Você ganhou, {user.name}!")
            break
        break