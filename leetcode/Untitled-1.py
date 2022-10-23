"""
x = 10 #integer
x = "print lol" #string
x = 2.2 #float

x = True #boolean
x = False #boolean
x = None #nullval

x = [1, "2", [12, True], 3.4] # list
x = x[2]
x = {
    1:"aarush",
    2:"aarvin",
    3:"raseena",
    4:"anantha",
    5:x
} # dict


"""
"""
daytime = True

while (daytime):
    x = int(input("Give me a number -> "))

    if x == 10: daytime = False

    x += 1
    x *= 5125
    x -= 5125
    x /= 5125

    print("The answer is " + str(int(x)))
"""
# print(str(x))  $$$      11.0 -> 11 -> "11"
#                         11.0 -> -> -> "11.0"s




# print(x)

jsonFilePath = "hello.json"
print(jsonFilePath[:-4]+"xml")