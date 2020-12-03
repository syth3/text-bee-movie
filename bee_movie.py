def parse_script(movie_file, punctuation_to_strip):
    parsed_movie_script = []
    for line in movie_file:
        if line == '\n':
            continue
        line = line.strip()
        line = line.replace('\n', '')
        for word in line.split():
            for punctuation in punctuation_to_strip:
                word = word.replace(punctuation, '')
            if word != "":
                parsed_movie_script.append(word)
    return parsed_movie_script


def main():
    movie_script_filename = "bee-movie-script.txt"
    punctuation_to_strip = ["'", '?', ':', '!', ' ', ',', '-', '.', '"', '\n', '\x00']
    with open(movie_script_filename) as movie_script:
        parsed_movie_script = parse_script(movie_script, punctuation_to_strip)

    for word in parsed_movie_script:
        print(word)
    print("Number of words:", len(parsed_movie_script))


if __name__ == '__main__':
    main()
