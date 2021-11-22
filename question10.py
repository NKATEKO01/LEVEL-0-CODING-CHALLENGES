def common_letter(str1,str2):
    common_letter_list = []
    for i in str1:
        for k in str2:
            if i.lower() == k.lower():
                if i not in common_letter_list:
                    common_letter_list.append(i)
    return ", ".join(common_letter_list)


print("common letters: " + common_letter("house", "computers"))
