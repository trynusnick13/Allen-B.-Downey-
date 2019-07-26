def nested_sum(list):

    sum = 0

    for i in list:



        if type(i) == type([]):

            sum += nested_sum(i)

        else:

            sum += i

    return sum


def cumsum(list):

    new_list = []

    for i in range(len(list)):

        add = 0

        for j in range(i + 1):

            add += list[j]

        new_list.append(add)

    return new_list

def middle(list):

    return list[1:-1]

def chop(list):

    del(list[0])
    del(list[-1])

def is_sorted(list):

    a = sorted(list)

    for i in range(len(list)):

        if  list[i] != a[i]:

            return False

        else:

            continue

    return True

def is_anagram(str1,str2):

    return list(str1).sort() == list(str2).sort()

def  has_duplicates(list):

    for i in list:

        if list.count(i) > 1:

            return True

        else:

            continue

    return False

# print(nested_sum([1,[1,1],1,1]))

# print(cumsum([1,1,1]))

# print(middle([1,2,3,4]))

# a = [1,2,3,4]
# chop(a)
# print(a)

# print(is_sorted([1,5,3,4]))

# print(is_anagram("abc","cba"))

# print(has_duplicates([1,2,"d","d"]))

