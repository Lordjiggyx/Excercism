import re

VOWEL_SOUND = ('a', 'e', 'i', 'o', 'u', 'yt', 'xr')


def translate(phrase):
    return ' '.join(map(_to_pig_latin, phrase.split()))


def _to_pig_latin(word):
    if word.startswith(VOWEL_SOUND):
        return word + 'ay'

    consonant_sound = ''
    while not word.startswith(VOWEL_SOUND):
        if word.startswith('qu'):
            consonant_sound += word[0:2]
            word = word[2:]
        else:
            consonant_sound += word[0]
            word = word[1:]

    return word + consonant_sound + "ay"