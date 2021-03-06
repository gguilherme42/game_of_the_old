def print_hash_table_columns():
    print()
    print('\033[1;1;97m    A   B   C\033[0;0m')
    print()

def print_hash_table_line(line_number: int):
    print(f'\033[1;1;97m{line_number}   \033[0;0m', end="")


def print_hash_table(hash_table: list[list[str]]):
    def is_the_final_index(index_number: int):
        return index_number == 2
    
    print_hash_table_columns()

    for line_index, line in enumerate(hash_table):
        print_hash_table_line(line_index + 1)
        for column_index, column in enumerate(line):
            print(f'{column}', end=f'{"  " if is_the_final_index(column_index) else " | "}')
        print()

        if not(is_the_final_index(line_index)):
            print('   ----------')
    print()