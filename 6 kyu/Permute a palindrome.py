def permute_a_palindrome (input):

    #dicc para key:value de char repetidos
    counter = {}

    for char in input:
        if char in counter:
            counter[char] += 1
        else:
            counter[char] = 1

    #for key in counter:
     #   if counter[key] >= 1:
      #      print(key, counter[key])

    total = 0
    for value in counter.values():
        total += value % 2
        print("total =", total, "value = ", value)

    print(total)

    if total < 2:
        return True
    else:
        return False