# https://edabit.com/challenge/grorumaEjyFDmZQCx


#wristband =[['A', 'A'],['B', 'B'],['C', 'C'],['D', 'B']]

def is_wristband(wristband):
    if is_horizontal(wristband) or is_vertical(wristband) or is_r_diagonal(wristband) or is_l_diagonal(wristband): return True
    else: return False

def is_horizontal(wristband):
    for indey in range(0,len(wristband)):
        for index in range(0,len(wristband[0])):
            if wristband[indey][index-1] != wristband[indey][index]: return False
    return True

def is_vertical(wristband):
    for index in range(0,len(wristband[0])):
        for indey in range(0,len(wristband)):
            if wristband[indey-1][index] != wristband[indey][index]: return False
    return True

def is_r_diagonal(wristband):
    for index in range(0,len(wristband[0])-1):
        for indey in range(1,len(wristband)):
            if wristband[indey][index] != wristband[indey-1][index+1]: return False
    return True

def is_l_diagonal(wristband):
    for index in range(1,len(wristband[0])):
        for indey in range(1,len(wristband)):
            if wristband[indey][index] != wristband[indey-1][index-1]: return False
    return True
