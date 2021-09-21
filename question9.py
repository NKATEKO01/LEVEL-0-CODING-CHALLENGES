def common_character(x): #print vowel
    vowels = "a, e, i, o, u"
    words = []
    for i in x: 
        u = i.lower()
        if (u in vowels ) and (u not in words):
            words.append(u)
    words =', '.join(map(str, words)) 
    
    print ("Vowels:",words)

(common_character("Umuzi"))
