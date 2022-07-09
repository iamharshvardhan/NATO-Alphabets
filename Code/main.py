import pandas

data = pandas.read_csv("nato_phonetic_alphabet.csv")
# Create a dictionary in this format:
phonetic_data = {row.letter:row.code for (index, row) in data.iterrows()}
print(phonetic_data)

# Create a list of the phonetic code words from a word that the user inputs.
word = input("Enter the word: ").upper()
word_nato = [phonetic_data[letter] for letter in word]
print(word_nato)
