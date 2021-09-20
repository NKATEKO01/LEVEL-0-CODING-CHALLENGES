def common_character(str): #print vowel
    vowels = "a, e, i, o, u"
    words = []
    for i in str: 
        u = i.lower()
        if (u in vowels ) and (u not in words):
            words.append(u)
    print ("Vowels:",words)

common_character("Umuzi")