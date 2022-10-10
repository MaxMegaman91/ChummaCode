import timeit

start = timeit.default_timer()

"""indices = []
for itr in range(len(s)): 
    if(s[itr] == "*"):
        indices.append(itr)
for i in indices:
    i -= indices.index(i)*2
    s = s.replace(s[i-1:i+1],"",1)
print(s)"""


s = "lees***dafh ja*o*p*w*ehif aw*od*kn*ca s*dpcoahe*** pofu h*s*dopk n***c**cod*e"
for i in range(s.count("*")):
    j = s.index("*")
    s = s.replace(s[j-1:j+1],"",1)
print(s)


stop = timeit.default_timer()

print('Time: ', stop - start) 

