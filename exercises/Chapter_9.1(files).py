def length(arg):

    for word in arg:

        if len(word.strip()) >= 20:

            print(word)

def has_input(str,input):

    for i in input:

        if i in str:

            return True

        else:

            continue

    return False

def no_input(arg, input):

    counter_e = 0
    counter = 0

    for word in arg:

        if not has_input(word, input):

            print(word, sep = " ")
            counter_e += 1
            counter += 1

        else:

            counter += 1
            continue

    print("No wrong symbols = ", counter_e/counter)

def uses_only(word, str):


    for i in word:

        counter = 0

        for j in str:


            if i == j:

                counter += 1
                break

            else:

                if counter < len(str)-1:

                    counter += 1
                    continue

                else:

                    return False

    return True





file = open("word.txt", "r")
# line = file.readline()
# for word in file:
#
#     if len(word.strip()) >= 20:
#
#         print(word)
# print(length(file))
# wrong = input("Write down something: ")
# print(no_input(file, wrong))
print(uses_only("aaabbbmmmccc", "abmc"))