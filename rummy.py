i=1
list1=[]
deck = ["H1", "H2", "H3", "H4", "H5", "H6", "H7", "H8", "H9", "H10", "H11", "H12", "H13", 
"D1", "D2", "D3", "D4", "D5", "D6", "D7", "D8", "D9", "D10", "D11", "D12", "D13",
"S1", "S2", "S3", "S4", "S5", "S6", "S7", "S8", "S9", "S10", "S11", "S12", "S13",
"C1", "C2", "C3", "C4", "C5", "C6", "C7", "C8", "C9", "C10", "C11", "C12", "C13",
"BJ", "BJ", "RJ", "RJ"
]
while i <= 13:
    input = input("Card", i + "?")
    if input in deck: 
        list1.append(input)
        i+=1
    else: continue

def sortcards():
    list2 = []
    k=0
    while k <13:
        j = int(deck.index(list1[k]))
        list2.append(j)
    list2.sort()

def rummycheckad():
    while i < 13:
