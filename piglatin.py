english_sentence = input().lower()
english_words = english_sentence.split()
latin_words = []

vowels = ['a', 'e', 'i', 'o', 'u']

for word in english_words:
    has_vowel = False

    for i in range(len(word)):

        '''
        if first letter is a vowel
        '''
        if word[0] in vowels:
            latin_words.append(word + "yay")
            break
        else:
            '''
            else get vowel position and postfix all the consonants 
            present before that vowel to the end of the word along with "ay"
            '''

            if word[i] in vowels:
                latin_words.append(word[i:] + word[:i] + "ay")
                has_vowel = True
                break

            # if the word doesn't have any vowel then simply postfix "ay"
            if has_vowel == False and i == len(word) - 1:
                latin_words.append(word + "ay")
                break

pig_latin_sentence = ' '.join(latin_words)
print(pig_latin_sentence)
