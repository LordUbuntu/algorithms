# Jacobus Burger (2024-11-23)
# ROT13, ROTate 13 Cypher
# A simple rotational cypher algorithm that rotates the values of symbols (letters) within a symbol space (alphabet) over by 13 symbols within that order. Imagine arranging the alphabet in a ring, then take any letter and move 13 in a chosen direction. To decypher, rotate all the letters back the other way.


# A basic and common example using something similar to Cesarian cypher
def rot13(plaintext: str) -> str:
    # convert letters to numbers (Python)
    cyphertext = [ord(letter) for letter in plaintext.upper()]
    # rotate letters in cypher, bewaring wraparound
    # upper letters are dec 65 - 90
    for i in range(len(cyphertext)):
        number = cyphertext[i]
        if 65 <= number <= 90:
            if number + 13 > 90:
                number = 65 + ((number + 13) - 91)
            else:
                number = number + 13
        cyphertext[i] = number
    # convert numbers to letters (Python)
    cyphertext = [chr(number) for number in cyphertext]
    return cyphertext
