# Move the first letter of each word to the end of it, then add "ay" 
# to the end of the word. Leave punctuation marks untouched.

def pig_it(text):
    punctuation_marks = ['.', ',', '!', "'", '*', '?', '-', ':', ';']
    letter_new = ""
    words = text.split()
    for word in words:
        for i in word:
            if word[0] in punctuation_marks:
                new_word = word[0]+word[2:]+word[1:2]+'ay'
                break
            else:
                new_word = word[1:] + word[0:1]
        letter_new = letter_new + ' ' + new_word
    return letter_new.strip()

