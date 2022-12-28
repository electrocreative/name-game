"""
Module for "The Name Game" string translator.

Rules based on the lyrics from the 1964 song "The Name Game" by Shirley Ellis.
https://en.wikipedia.org/wiki/The_Name_Game

Unless your name string begins with either a vowel (A, E, I, O, U), OR begins
with the letters 'B', 'F' or 'M', the 'regular verse' rules will apply.

REGULAR VERSE:
Begin by dropping all leading consonants. At the end of every line, the name
then gets repeated without the first letter.

    Example: The verse for the name 'Gary' would be:
        Gary!
        Gary, Gary, bo-bary
        Banana-fana fo-fary
        Fee-fi-mo-mary
        Gary!

EXCEPTION 1: Vowel is first letter of the name:
If you have a vowel ('A', 'E', 'I', 'O', or 'U') as the first letter of your
name (e.g. 'Earl') you do not truncate the name.
    - NOTE: 'Y' in the first position is NOT considered a vowel.
    - NOTE: 'Y' in the second position IS considered a vowel, so it remains.

    Example: The verse for the name 'Earl' would be:
        Earl!
        Earl, Earl, bo-bearl
        Banana-fana fo-fearl
        Fee-fi-mo-mearl
        Earl!

EXCEPTION 2: 'B', 'F' or 'M' as first letter of the name:
If you have a 'B', an 'F' or an 'M' as the first letter of the name, (e.g.
'Billy', 'Felix', 'Mary'), in addition to the regular verse rules we also
subtract the prefix char in the matching "bo-(b), fo-(f), mo-(m)" verse line.

    Example: The verse for the name 'Billy' would be (note line #2:
        Billy!
        Billy, Billy, bo-illy
        Banana-fana fo-filly
        Fee-fi-mo-milly
        Billy!
    Example: The verse for the name 'Felix' would be (note line #3:
        Felix!
        Felix, Felix, bo-belix
        Banana-fana fo-elix
        Fee-fi-mo-melix
        Felix!
    Example: The verse for the name 'Mary' would be (note line #4:
        Mary!
        Mary, Mary, bo-bary
        Banana-fana fo-fary
        Fi-Fi mo-ary
        Mary!

Author: SCOTT R. HENZ
Date: 11/11/2022
"""
import introcs


def first_vowel(s):
    """
    Returns the position of the first vowel in s; it returns -1 if there are no
    vowels.

    We define the vowels to be the letters 'a','e','i','o', and 'u'.  The letter
    'y' counts as a vowel only if it is not the first letter in the string.

    Examples:
        first_vowel('hat') returns 1
        first_vowel('grrm') returns -1
        first_vowel('sky') returns 2
        first_vowel('year') returns 1

    Parameter s: the string to search
    Precondition: s is a nonempty string with only lowercase letters
    """

    result = len(s)  # In case there is no 'a'
    a = introcs.find_str(s, 'a')
    e = introcs.find_str(s, 'e')
    i = introcs.find_str(s, 'i')
    o = introcs.find_str(s, 'o')
    u = introcs.find_str(s, 'u')
    y = introcs.find_str(s[1:], 'y')

    if a > -1:
        result = a
    if e > -1 and e < result:
        result = e
    if i > -1 and i < result:
        result = i
    if o > -1 and o < result:
        result = o
    if u > -1 and u < result:
        result = u
    if y > -1 and y < result:
        result = y + 1

    return result if result != len(s) else -1


def name(s):
    """
    Returns the translated name as a formatted string in the form of a verse.

    REGULAR VERSE: No vowels, or 'B', 'F' or 'M' in pos 1: Strip all chars up to
    first vowel.

    Example: name('Scott') returns:
        Scott!
        Scott, Scott, bo-bott
        Banana-fana fo-fott
        Fi-Fi mo-mott
        Scott!
        
    EXCEPTION 1: A, E, I, O, U in pos1 - Do not strip anything.

    Example: name('Evan') returns:
        Evan!
        Evan, Evan, bo-bevan
        Banana-fana fo-fevan
        Fi-Fi mo-mevan
        Evan!

    EXCEPTION 2: 'B', 'F' or 'M' in pos 1: Same as Case 1, PLUS also subtract
    prefix char in the matching "bo-(b), fo-(f), mo-(m)" verse line.

    Example: name('Fred') returns:
        Fred!
        Fred, Fred, bo-bed
        Banana-fana fo-ed
        Fi-Fi mo-med
        Fred!

    Parameter s: the string (name) to translate
    Precondition: s is a string.
    """

    bananarama = ''
    b = ''
    f = ''
    m = ''

    # EXCEPTION 1
    if s[0] == 'A' or s[0] == 'E' or s[0] == 'I' or s[0] == 'O' or s[0] == 'U':
        case = 1
        b, f, m = 'b', 'f', 'm'
        bananarama = s.lower()

    # EXCEPTION 2
    elif s[0] == 'B' or s[0] == 'F' or s[0] == 'M':
        case = 2
        if s[0] == 'B':
            b, f, m = '', 'f', 'm'
        elif s[0] == 'F':
            b, f, m = 'b', '', 'm'
        else:
            b, f, m = 'b', 'f', ''
        bananarama = s.lower()[first_vowel(s):]

    # REGULAR VERSE
    else:
        case = 3
        b, f, m = 'b', 'f', 'm'
        bananarama = s.lower()[first_vowel(s):]

    # Concatenate the verse
    verse = (s + '!\n' +
             s + ', ' + s + ', ' + 'bo-' + b + bananarama + '\n' +
             'Banana-fana fo-' + f + bananarama + '\n' +
             'Fi-Fi mo-' + m + bananarama + '\n' +
             s + '!')

    # Print the result to terminal
    print(verse)
