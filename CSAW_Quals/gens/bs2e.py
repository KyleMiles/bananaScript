#BananaScript to English
from __future__ import print_function

traslateList = {}
traslateList["BANANAS"] = 'a'
traslateList["BANANAs"] = 'b'
traslateList["BANANaS"] = 'c'
traslateList["BANANas"] = 'd'
traslateList["BANAnAS"] = 'e'
traslateList["BANAnAs"] = 'f'
traslateList["BANAnaS"] = 'g'
traslateList["BANAnas"] = 'h'
traslateList["BANaNAS"] = 'i'
traslateList["BANaNAs"] = 'j'
traslateList["BANaNaS"] = 'k'
traslateList["BANaNas"] = 'l'
traslateList["BANanAS"] = 'm'
traslateList["BANanAs"] = 'n'
traslateList["BANanaS"] = 'o'
traslateList["BANanas"] = 'p'
traslateList["BAnANAS"] = 'q'
traslateList["BAnANAs"] = 'r'
traslateList["BAnANaS"] = 's'
traslateList["BAnANas"] = 't'
traslateList["BAnAnAS"] = 'u'
traslateList["BAnAnAs"] = 'v'
traslateList["BAnAnaS"] = 'w'
traslateList["BAnAnas"] = 'x'
traslateList["BAnaNAS"] = 'y'
traslateList["BAnaNAs"] = 'z'
traslateList["BAnaNaS"] = 'A'
traslateList["BAnaNas"] = 'B'
traslateList["BAnanAS"] = 'C'
traslateList["BAnanAs"] = 'D'
traslateList["BAnanaS"] = 'E'
traslateList["BAnanas"] = 'F'
traslateList["BaNANAS"] = 'G'
traslateList["BaNANAs"] = 'H'
traslateList["BaNANaS"] = 'I'
traslateList["BaNANas"] = 'J'
traslateList["BaNAnAS"] = 'K'
traslateList["BaNAnAs"] = 'L'
traslateList["BaNAnaS"] = 'M'
traslateList["BaNAnas"] = 'N'
traslateList["BaNaNAS"] = 'O'
traslateList["BaNaNAs"] = 'P'
traslateList["BaNaNaS"] = 'Q'
traslateList["BaNaNas"] = 'R'
traslateList["BaNanAS"] = 'S'
traslateList["BaNanAs"] = 'T'
traslateList["BaNanaS"] = 'U'
traslateList["BaNanas"] = 'V'
traslateList["BanANAS"] = 'W'
traslateList["BanANAs"] = 'X'
traslateList["BanANaS"] = 'Y'
traslateList["BanANas"] = 'Z'
traslateList["BanAnAS"] = ' '
traslateList["BanAnAs"] = '-1'
traslateList["BanAnaS"] = '0'
traslateList["BanAnas"] = '1'
traslateList["BanaNAS"] = '2'
traslateList["BanaNAs"] = '3'
traslateList["BanaNaS"] = '4'
traslateList["BanaNas"] = '5'
traslateList["BananAS"] = '6'
traslateList["BananAs"] = '7'
traslateList["BananaS"] = '8'
traslateList["Bananas"] = '9'

traslateList["bANANAS"] = ','
traslateList["bANANAs"] = '.'
traslateList["bANANaS"] = '/'
traslateList["bANANas"] = ';'
traslateList["bANAnAS"] = '\''
traslateList["bANAnAs"] = '['
traslateList["bANAnaS"] = ']'
traslateList["bANAnas"] = '='
traslateList["bANaNAS"] = '-'
traslateList["bANaNAs"] = '`'
traslateList["bANaNaS"] = '~'
traslateList["bANaNas"] = '!'
traslateList["bANanAS"] = '@'
traslateList["bANanAs"] = '#'
traslateList["bANanaS"] = '$'
traslateList["bANanas"] = '%'
traslateList["bAnANAS"] = '^'
traslateList["bAnANAs"] = '&'
traslateList["bAnANaS"] = '*'
traslateList["bAnANas"] = '('
traslateList["bAnAnAS"] = ')'
traslateList["bAnAnAs"] = '_'
traslateList["bAnAnaS"] = '+'
traslateList["bAnAnas"] = '{'
traslateList["bAnaNAS"] = '}'
traslateList["bAnaNAs"] = '|'
traslateList["bAnaNaS"] = '\\'
traslateList["bAnaNas"] = ':'
traslateList["bAnanAS"] = '"'
traslateList["bAnanAs"] = '?'
traslateList["bAnanaS"] = '>'
traslateList["bAnanas"] = '<'

inputString = raw_input()
while (inputString != "exit"):
    for word in inputString.split():
        try:
            print(traslateList[word], end='')
        except:
            print("Word \"" + word + "\" not found")
    print()

    inputString = raw_input()
