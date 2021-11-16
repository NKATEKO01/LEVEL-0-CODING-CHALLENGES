def common_letter(str1,str2):
    file = []
    for i in str1:
        for k in str2:
            if i.lower() == k.lower():
                if i not in file:
                    file.append(i)

    return ",".join(file)


print("common letters: " + common_letter("house", "computers"))
