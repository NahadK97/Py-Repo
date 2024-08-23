from random import shuffle


def c_encrypt(word, shift):
    c_msg = ''  # empty string
    for ch in word:  # each character is checked
        if ch in "XYZxyz":  # xyz or XYZ -> abc or ABC
            j = chr(ord(ch) - (26 - shift))
        elif not ch.isalpha():  # special characters remain
            # the same
            j = ch
        else:
            j = chr(ord(ch) + shift)  # abc or ABC -> def or DEF
        c_msg += j
    return c_msg


def c_decrypt(word, shift):
    c_msg = ''  # empty string
    for ch in word:  # each character is checked
        if ch in "ABCabc":  # abc or ABC -> xyz or XYZ
            j = chr(ord(ch) + (26 - shift))
        elif not ch.isalpha():  # special characters remain the same
            j = ch
        else:
            j = chr(ord(ch) - shift)  # abc or ABC -> def or DEF
        c_msg += j
    return c_msg


def m_encrypt(word):
    c_msg = ''  # empty string
    mk = {'A': '.-', 'B': '-...', 'C': '-.-.', 'D': '-..', 'E': '.', 'F': '..-.', 'G': '--.', 'H': '....', 'I': '..',
          'J': '.---', 'K': '-.-', 'L': '.-..', 'M': '--', 'N': '-.', 'O': '---', 'P': '.--.', 'Q': '--.-', 'R': '.-.',
          'S': '...', 'T': '-', 'U': '..-', 'V': '...-', 'W': '.--', 'X': '-..-', 'Y': '-.--', 'Z': '--..'}
    for ch in word:  # each character is checked
        if ch == " ":  # space character is checked
            j = '/'
        elif ch == "\n":
            j = '//'
        elif not ch.isalpha():  # special characters remain the same
            j = ch
        else:
            j = mk[ch.upper()]  # for all alphabets
        c_msg = c_msg + " " + j
    return c_msg


def m_decrypt(word):
    c_msg = k = ''  # empty string
    mk = {'A': '.-', 'B': '-...', 'C': '-.-.', 'D': '-..', 'E': '.', 'F': '..-.', 'G': '--.', 'H': '....', 'I': '..',
          'J': '.---', 'K': '-.-', 'L': '.-..', 'M': '--', 'N': '-.', 'O': '---', 'P': '.--.', 'Q': '--.-', 'R': '.-.',
          'S': '...', 'T': '-', 'U': '..-', 'V': '...-', 'W': '.--', 'X': '-..-', 'Y': '-.--', 'Z': '--..'}
    for ln in word.split(' // '):  # each line is checked
        for w in ln.split(' / '):  # each word is checked
            for ch in w.split():  # each character is checked
                for j in mk:  # checking in dictionary for suitable fit
                    if mk[j] == ch:
                        k = j  # for all alphabets
                c_msg = c_msg + k
            c_msg += " "  # space after each word
        c_msg += "\n"  # new line after every line
    return c_msg


def jumble(word):
    word = list(word)  # convert word from string to list
    shuffle(word)  # shuffles the word in list form
    return ''.join(word)  # returns the jumbled string


def reverse(word):
    c_msg = ''  # empty string
    for ch in word:  # each character is checked
        if ch.isupper():  # ABC -> ZYX
            j = chr(155 - ord(ch))
        elif ch.islower():  # abc -> zyx
            j = chr(219 - ord(ch))
        else:
            j = ch
        c_msg += j
    return c_msg


def alph_num(word):
    c_msg = ''  # Empty String
    for ch in word:  # Checking each character
        if ch.isupper():  # For uppercase Letters
            c_msg = c_msg + str(ord(ch) - 64) + " "
        elif ch.islower():  # For lowercase letters
            c_msg = c_msg + str(ord(ch) - 96) + " "
        else:  # For other characters
            c_msg = c_msg + ch + " "
    return c_msg


def num_alph(word):
    c_msg = ''
    for ch in word.split():
        if ch.isdigit():
            c_msg = c_msg + chr(int(ch) + 64)
        elif ch == "/":
            c_msg = " "
        else:
            c_msg = c_msg + ch
    return c_msg
