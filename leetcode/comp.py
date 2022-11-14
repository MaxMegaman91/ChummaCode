import timeit

start = timeit.default_timer()

#####################################################

def myFunc(celsius):
    return [celsius+273.15, (celsius*1.8)+32.0]


#####################################################

print(myFunc(celsius = 122.11))

#####################################################
stop = timeit.default_timer()

print('Time: ', stop - start) 

