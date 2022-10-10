# https://edabit.com/challenge/j9zed4GnykS48W6vh


def maxmin(number):
    permList = []
    number = list(str(number))

    for iterable in range(0,len(number)):
        for otheriterable in range(iterable,len(number)):
            if (number[iterable] != "0" and number[otheriterable] !="0"):
                number[iterable], number[otheriterable] = number[otheriterable], number[iterable]
                permList.append(int("".join(number)))
                number[iterable], number[otheriterable] = number[otheriterable], number[iterable]
            elif (number[iterable] == "0" and number[otheriterable] != "0" and otheriterable != 0):
                number[iterable], number[otheriterable] = number[otheriterable], number[iterable]
                permList.append(int("".join(number)))
                number[iterable], number[otheriterable] = number[otheriterable], number[iterable]
            elif (number[iterable] != "0" and number[otheriterable] == "0" and iterable != 0):
                number[iterable], number[otheriterable] = number[otheriterable], number[iterable]
                permList.append(int("".join(number)))
                number[iterable], number[otheriterable] = number[otheriterable], number[iterable]
    return max(permList, key=lambda x:int(x)),min(permList, key=lambda x:int(x))

