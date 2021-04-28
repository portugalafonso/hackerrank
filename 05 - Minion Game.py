#Minion Game


def minion_game(string):
    vowel_list = ['A','E','I','O','U']
    length_word = len(string)
    score_stuart = 0
    score_kevin = 0
    
    #Loop through the string in range(length)
    for index in range(length_word):
        #If the letter is a vowel add (length-index)
        if string[index] not in vowel_list:
            score_stuart += length_word - index
        #If the letter is not a vowel add (length-index)
        else:
            score_kevin += length_word - index
    #Check winner and print
    if score_stuart > score_kevin:
        print("Stuart", score_stuart)
    elif score_stuart < score_kevin:
        print("Kevin", score_kevin)
    else:
        print("Draw")
    
print(minion_game("BANANA"))
    #Substrings with one letter
    # for letter in string:
    #     if letter in vowel:
    #         kevin_list.append(letter)
    #     else:
    #         stuart_list.append(letter)