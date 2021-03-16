# Playing with % to try out his capabilities.

def is_even(num):
    return num % 2 == 0


def is_odd(num):
    return num % 2 != 0


def split_names_into_rows(name_list, modulus=3):
    for index, name in enumerate(name_list, start=1):
        print(f"{name:-^15} ", end="")
        if index % modulus == 0:
            print()
    print()


names = ["Anna", "Graham", "Buck", "Rick", "Monty", "Marvin"]

split_names_into_rows(names)