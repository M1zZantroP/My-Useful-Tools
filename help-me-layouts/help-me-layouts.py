import clipboard

EN_UA = {'Q': 'Й', 'W': 'Ц', 'E': 'У', 'R': 'К', 'T': 'Е', 'Y': 'Н', 'U': 'Г', 'I': 'Ш', 'O': 'Щ', 'P': 'З', '{': 'Х',
         '}': 'Ї', 'A': 'Ф', 'S': 'І', 'D': 'В', 'F': 'А', 'G': 'П', 'H': 'Р', 'J': 'О', 'K': 'Л', 'L': 'Д', ':': 'Ж',
         '"': 'Є', "|": 'Ґ', 'Z': 'Я', 'X': 'Ч', 'C': 'С', 'V': 'М', 'B': 'И', 'N': 'Т', 'M': 'Ь', '<': 'Б', '>': 'Ю',
         '?': '.', 'q': 'й', 'w': 'ц', 'e': 'у', 'r': 'к', 't': 'е', 'y': 'н', 'u': 'г', 'i': 'ш', 'o': 'щ', 'p': 'з',
         '[': 'х', ']': 'ї', 'a': 'ф', 's': 'і', 'd': 'в', 'f': 'а', 'g': 'п', 'h': 'р', 'j': 'о', 'k': 'л', 'l': 'д',
         ';': 'ж', 'z': 'я', 'x': 'ч', 'c': 'с', 'v': 'м', 'b': 'и', 'n': 'т', 'm': 'ь', ',': 'б', '.': 'ю', '/': '.',
         "`": "'", "'": "є", '\\': 'ґ'}


def choose_translate_language(line: str) -> bool:
    if line[0] in EN_UA.keys() or line[1] in EN_UA.keys():
        return True
    return False


def make_reversed_dictionary(layout: dict) -> dict:
    return {value: key for key, value in EN_UA.items()}


def translate(line: str) -> str:
    corrected_line = ''

    if choose_translate_language(line):
        for letter in line:
            corrected_line += EN_UA.get(letter, letter)
    else:
        UA_EN = make_reversed_dictionary(EN_UA)
        for letter in line:
            corrected_line += UA_EN.get(letter, letter)
    return corrected_line


if __name__ == '__main__':
    try:
        incorrect_line = clipboard.paste()
        assert incorrect_line
        result = translate(incorrect_line)
        clipboard.copy(result)
    except AssertionError as _e:
        exit()
