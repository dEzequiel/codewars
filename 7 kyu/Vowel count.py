def get_count(sentence):
    vowel_counter = 0;
    vowels = 'aeiou'

    for i in sentence:
        if i in vowels:
            vowel_counter += 1;

    return vowel_counter