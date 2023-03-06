english_sentence = input()

vowels = ['a', 'e', 'i', 'o', 'u',]
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
signs = ['.', '?', '!', ';', ',', ':', '-']

last_letter = ""
if english_sentence[-1] in signs:
    last_letter = english_sentence[-1]
    english_sentence = english_sentence[:-2]

english_words = english_sentence.split()
latin_words = []

for word in english_words:
    has_vowel = False

    for i in range(len(word)):

        '''
        if first letter is a vowel
        '''
        if word[0] in "aAeEiIoOuU":
            latin_words.append(word + "-way")
            break
        elif word[0] in numbers or word[0] in signs:
            latin_words.append(word)
            break
        else:
            '''
            else get vowel position and postfix all the consonants 
            present before that vowel to the end of the word along with "ay"
            '''

            if word[i] in vowels:
                latin_words.append(word[i:] + "-" + word[:i] + "ay")
                has_vowel = True
                break

            # if the word doesn't have any vowel then simply postfix "ay"
            if has_vowel is False and i == len(word) - 1:
                latin_words.append(word + "ay")
                break

pig_latin_sentence = ' '.join(latin_words)
pig_latin_sentence += last_letter
print(pig_latin_sentence)
