def find_all_symbols():
    """
    Find all non alphanumeric symbols in the bee movie
    :return: None
    """
    non_alphanumeric_symbols = set()
    with open("bee-movie-script.txt") as bee_movie:
        while True:
            character = bee_movie.read(1)
            if not character:
                break

            if not character.isalpha() and not character.isdigit():
                non_alphanumeric_symbols.add(character)
    print(non_alphanumeric_symbols)

find_all_symbols()