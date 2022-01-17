hash_talbe = [['-','-','-'],
            ['-','-','-'],
            ['-','-','-']]

def print_hash_table():
    def is_the_final_index(index_number: int):
        return index_number == 2

    print('A   B   C')
    for line_index, line in enumerate(hash_talbe):
        for column_index, column in enumerate(line):
            print(f'{column}', end=f'{"   " if is_the_final_index(column_index) else " | "}')
        print('')

        if not(is_the_final_index(line_index)):
            print('---------')


print_hash_table()