#

def feven_row(number):
    return (number**2) * 2 - number

def fodd_row(number):
    return (number**2) * 2 + number

def flipped_row(number):
    ans = (number**2)*2 
    return ans + number if number % 2 else ans - number

def even_sum(number):
    answer = 0
    for x in range(0,number//2+1):
        answer += feven_row(x)
    return answer

def odd_sum(number):
    answer = 0
    for x in range(0,number//2+1):
        answer += fodd_row(x)
    return answer

def aflippedsum(number):
    answer = 0
    for x in range(0,number//2+1):
        answer += flipped_row(x)
    return answer

def flippedsum(number):
    if number % 2 == 0:
        return even_sum(number)
    return odd_sum(number)

def alltriangles(layers):
    return int(1/6 * layers * (layers+1) * (layers+2)) + flippedsum(layers)

print(alltriangles(-2))