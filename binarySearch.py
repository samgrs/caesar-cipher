from random import randint


def binary_search(vector, starting_position, final_position, wanted_element):
    if final_position >= starting_position:

        middle = starting_position + (final_position - starting_position) // 2

        if vector[middle] == wanted_element:
            return middle

        elif vector[middle] > wanted_element:
            return binary_search(vector, starting_position, middle - 1, wanted_element)

        else:
            return binary_search(vector, middle + 1, final_position, wanted_element)

    else:
        return -1


vector_size = 100

vector = [randint(0, vector_size) for i in range(vector_size)]
vector.sort()
wanted_element = randint(0, 100)

result = binary_search(vector, 0, len(vector) - 1, wanted_element)

print(f"{vector}")

if result != -1:
    boolean = True
    print(f"\33[32m{boolean}\033[m. O elemento \33[32m{wanted_element}\033[m está no índice {result}.")
else:
    boolean = False
    print(f"\33[31m{boolean}\033[m. O elemento \33[31m{wanted_element}\033[m não existe no vetor.")
