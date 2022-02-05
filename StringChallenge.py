def StringChallenge(strParam):
    # code goes here
    list_word = list(strParam)
    list_copy = list(strParam)

    # creating a combinations of 1 to 3 with
    # all the letters of the input word

    all_combinations = []

    for n in range(1, 4):
        comb_genarate = list(itertools.combinations(range(0, len(list_word)), n))
        all_combinations += comb_genarate
    # deleting the letters of the combination until find a palindrome
    for comb in all_combinations:

        if len(comb) == 1:
            del list_word[int(comb[0])]
            letters = list_copy[int(comb[0])]

        elif len(comb) == 2:
            comb1, comb2 = comb
            del list_word[int(comb1)]
            del list_word[int(comb2) - 1]
            letters = [list_copy[int(comb1)], list_copy[int(comb2)]]
        else:
            # if the number of letter to del is greater than2, break
            print("not possible")
            break
        # checking if the result word is a palindrome
        if "".join(list_word) == "".join(list_word[::-1]):
            # checking if the word size is bigger hat 3 letters
            lenght = len(list_word)
            if lenght >= 3:
                print(letters)
                break
            else:
                print("not possible")

        try:
            del letters
        except:
            pass
        list_word = list(strParam)

    return strParam


print(StringChallenge(input()))
