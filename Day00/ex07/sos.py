# from string import ascii_lowercase, ascii_uppercase
# from string import digits, whitespace, punctuation
import sys


def main(astring):
    print(astring)
    NESTED_MORSE = {
        " ":  "/",
        "A":   ".-",
        "B":   "-.",
        "C":	"-.-.",
        "D":	"-.",
        "E":	".",
        "F":	"..-.",
        "G":	"--.",
        "H":	"....",
        "I":	"..",
        "J":	".---",
        "K":	"-.-",
        "L":	".-..",
        "M":	"--",
        "N":   "-.",
        "O":   "---",
        "P":   ".--.",
        "Q":   "--.-",
        "R":   ".-.",
        "S":   "...",
        "T":   "-",
        "U":   "..-",
        "V":   "...-",
        "W":   ".--",
        "X":   "-..-",
        "Y":   "-.--",
        "Z":   "--..",
        "0":	"-----",
        "1":	".----",
        "2":	"..---",
        "3":	"...--",
        "4":	"....-",
        "5":	".....",
        "6":	"-....",
        "7":	"--...",
        "8":	"---..",
        "9":	"----."
        }
    [print(NESTED_MORSE.get(elem), end=" ") for elem in list(astring)]
    print(end='\n')


def data_validator():
    if len(sys.argv) != 2:
        raise AssertionError('AssertionError: the arguments are bad')
    operateIn = sys.argv[1].replace(' ', '')
    if not operateIn.isalnum():
        raise AssertionError('AssertionError: the arguments are bad')
    return sys.argv[1].upper()


if __name__ == '__main__':
    try:
        validated_arg = data_validator()
        main(validated_arg)
    except Exception as e:
        print(f'{e}')
