import pandas
data = pandas.read_csv("nato_phonetic_alphabet.csv")
# print(data)
nato_data = pandas.DataFrame(data)

# for (index, row) in nato_data.iterrows():
#     print(row.code)
#     print(row.letter)

nato_dict = {row.letter:row.code for (index, row) in nato_data.iterrows()}
# print(nato_dict)

word_input = input("Enter a word: ").upper()
letter_list = [letter for letter in word_input]
# print(letter_list)

#Grab the code for each letter from the dictionary of the word that has been inputted from line 13 and put it in a list
result = [nato_dict[letter] for letter in letter_list]
print(result)