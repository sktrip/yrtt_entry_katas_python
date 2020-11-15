# Move the first letter of each word to the end of it, then add "ay"
# to the end of the word. Leave punctuation marks untouched.

def pig_it(text):
    import string

    words = text.split()
    letters_start = ""
    new_text = ""
    first_word = text.split()[0]

    def punctuation_at_end(sample):
        sample_letters = ""
        k = -1
        while sample[k] in string.punctuation:
            sample_letters = sample[k]+sample_letters
            k = k-1
        return [k, sample_letters]

    for word in words:
        if word[0] in string.punctuation:
            i = 0
            while word[i] in string.punctuation:
                letters_start = letters_start+word[i]
                i = i+1
                if word[-1] in string.punctuation:
                    x = punctuation_at_end(word)
                    with_punctuation = lambda c, d : letters_start+word[i+1:x[0]+1]+word[i]+'ay'+x[1] if c == d else ' '+letters_start+word[i+1:x[0]+1]+word[i]+'ay'+x[1]
                    start_punctuation = with_punctuation(word, first_word)
                else:
                    punctuation_at_start = lambda m, n: letters_start+word[i+1:]+word[i]+'ay' if m == n else ' '+letters_start+word[i+1:]+word[i]+'ay'
                    start_punctuation = punctuation_at_start(word, first_word)
            new_text = new_text + start_punctuation
            letters_start = ''
        elif word[-1] in string.punctuation:
            x = punctuation_at_end(word)
            word_punctuation = lambda a, b: word[1:x[0]+1]+word[0]+'ay'+x[1] if a ==b else ' '+word[1:x[0]+1]+word[0]+'ay'+x[1]
            end_punctuation = word_punctuation(word, first_word)
            new_text = new_text + end_punctuation
        else:
            word_position = lambda u, v: word[1:]+word[0:1]+'ay' if u == v else " "+word[1:]+word[0:1]+'ay'
            no_punctuation = word_position(word, first_word)
            new_text = new_text + no_punctuation
    return new_text
