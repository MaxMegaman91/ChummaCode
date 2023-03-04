def editDistance(string1, string2):
    len1, len2 = len(string1), len(string2)
    array = [[0 for i in range(len2 + 1)] for j in range(len1 + 1)]

    for j in range(len2 + 1):
        array[0][j] = j
        
    for i in range(len1 + 1):
        array[i][0] = i
        
    for i in range(1, len1 + 1):
        for j in range(1, len2 + 1):
            if string1[i - 1] == string2[j - 1]:
                array[i][j] = array[i-1][j-1]
            else:
                array[i][j] = 1 + min(
                    array[i-1][j], # Insertion
                    array[i][j-1], # Deletion
                    array[i-1][j-1] # Replacement
                )

    return array[len1][len2]

if __name__ == '__main__':
    string1 = input()
    string2 = input()
    print(editDistance(string1, string2))
