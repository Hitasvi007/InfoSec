def pswd(text):
    letters='abcdefghijklmnopqurstxyz'
    for l_1 in letters:
        for l_2 in letters:
            for l_3 in letters:
                for l_4 in letters:
                    Crack=l_1+l_2+l_3+l_4
                    print(Crack)
                    if Crack==text:
                        print("Match found")
                        return
pd = input("Enter the password: ")
pswd(pd)
