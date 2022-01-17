hash_talbe = [['X','O','X'],
            ['X','-','-'],
            ['-','-','-']]

def print_hash_table_columns():
    print()
    print('    A   B   C')
    print()


def print_hash_table_line(line_number: int):
    print(f'{line_number}   ', end="")


def print_hash_table():
    def is_the_final_index(index_number: int):
        return index_number == 2
    
    print_hash_table_columns()

    for line_index, line in enumerate(hash_talbe):
        print_hash_table_line(line_index + 1)
        for column_index, column in enumerate(line):
            print(f'{column}', end=f'{"  " if is_the_final_index(column_index) else " | "}')
        print()

        if not(is_the_final_index(line_index)):
            print('   ----------')
    print()


print_hash_table()