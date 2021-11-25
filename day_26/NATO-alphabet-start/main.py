student_dict = {
    "student": ["Angela", "James", "Lily"], 
    "score": [56, 76, 98]
}

#Looping through dictionaries:
for (key, value) in student_dict.items():
    print(key, value)


import pandas as pd
student_data_frame = pd.DataFrame(student_dict)

#Loop through rows of a data frame
for (index, row) in student_data_frame.iterrows():
   
    #Access index and row
    print(index, end=' ---- ')
    #Access row.student or row.score
    print(row.student, row.score)


# Keyword Method with iterrows()
dict_pairs =  {row.student:row.score for (index, row) in student_data_frame.iterrows()}
print(dict_pairs)
#TODO 1. Create a dictionary in this format:
#{"A": "Alfa", "B": "Bravo"}
codes_df = pd.read_csv('day_twenty_six/NATO-alphabet-start/nato_phonetic_alphabet.csv')
codes_dict = codes_df.to_dict(orient='list')
code_letter_dict = {l:c for l, c in zip(codes_dict['letter'], codes_dict['code'])}

print(code_letter_dict)
#TODO 2. Create a list of the phonetic code words from a word that the user inputs.

def to_phonetic(word:str) -> list:
    letters = [letter.upper() for letter in word]
    phonems = [code_letter_dict.get(letter, 'BLAH') for letter in letters]
    return(phonems)


def user_input() -> str:
    a = input('Enter a word: ').upper()
    return(a)


def convert_to_phonetic():
    word = user_input()
    print(* to_phonetic(word))
    
    
convert_to_phonetic()