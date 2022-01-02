def disemvowel(string_):
    vowel_minus_list = ['a', 'e', 'i', 'o', 'u'];
    vowel_mayus_list = [];

    for x in vowel_minus_list:
        vowel_mayus_list.append(x.upper())

    vowel_list = vowel_minus_list + vowel_mayus_list

    vowels = ""

    for i in vowel_list:
        vowels += i;

    print(vowels)

    for i in vowels:
        string_ = string_.replace(i, "")

    return string_