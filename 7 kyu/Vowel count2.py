def get_count(sentence):
    vowel_count = 0;

    for x in sentence:
        if x == 'a' or x == 'e' or x == 'i' or x == 'o' or x == 'u':
            vowel_count += 1;

    return vowel_count;