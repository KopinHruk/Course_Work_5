# NOT WORKING / IN PROGRESS
# Module to correct wrong-parsed words.

from spellchecker import SpellChecker

spell = SpellChecker()
spell.word_frequency.load_text_file('ru_full.txt')

# TODO dynamic dictionary for goods

# find those words that may be misspelled
misspelled = spell.unknown(['СПОЙКА', 'БАБЧШКИН', 'пфжилой', 'ВАОЛИ'])

for word in misspelled:
    # Get the one `most likely` answer
    print(spell.correction(word))

    # Get a list of `likely` options
    print(spell.candidates(word))

print(spell.correction('СПОЙКА'))
