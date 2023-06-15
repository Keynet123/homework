def palindrom(word):
    len_word = len(word)
    for i in range(len_word // 2):
        if word[i] != word[len_word-i-1]:
            result = False
        else:
            result = True
    print(result)
palindrom("лепсспел")
palindrom("HelloWorld")