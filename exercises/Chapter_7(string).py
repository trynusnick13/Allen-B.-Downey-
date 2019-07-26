def rotate_word(st, n):

    # a = str.split()
    st.lower()
    a = ""
    for letter in st:

        if str(letter).isspace():

            continue

        else:

            temp = ord(letter) + n

            if  temp > ord("z"):

                temp %= ord("z")
                temp += ord("a")
                temp -= 1

            elif temp < ord("a"):

                temp = ord("a") - temp
                temp = ord("z") - temp
                temp += 1


        a = a + chr(temp)

    return a




st = "aa bb cc"
print(rotate_word("melon",-10))
