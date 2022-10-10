#########################################################################################################################
import substring, minesweeper1, sudoku, josephus, ecg, combinations, PatternedWristband as wrist
from MaxieMinnie import maxmin
from fiscal import fiscalCode
from exactly3 import is_exactly_three
from secretagentpassword import secret_password
from atbash import atbash

def assert_equals(x,y,*args):
    if x == y:
        print("Test returns True\n")
    else:
        print("Test returns False")
        print(y, "not", x,"\n")
    thetuple = args
    for z in thetuple:
        print(z)
    print("=============================\n")


# Substring below --> Working
'''
print("substrings")
assert_equals(substring.longest_substring("844929328912985315632725682153"), "56327256")
assert_equals(substring.longest_substring("769697538272129475593767931733"), "27212947")
assert_equals(substring.longest_substring("937948289456111258444958189244"), "894561")
assert_equals(substring.longest_substring("736237766362158694825822899262"), "636")
assert_equals(substring.longest_substring("369715978955362655737322836233"), "369")
assert_equals(substring.longest_substring("345724969853525333273796592356"), "496985")
assert_equals(substring.longest_substring("548915548581127334254139969136"), "8581")
assert_equals(substring.longest_substring("417922164857852157775176959188"), "78521")
assert_equals(substring.longest_substring("251346385699223913113161144327"), "638569")
assert_equals(substring.longest_substring("483563951878576456268539849244"), "18785")
assert_equals(substring.longest_substring("853667717122615664748443484823"), "474")
assert_equals(substring.longest_substring("398785511683322662883368457392"), "98785")
assert_equals(substring.longest_substring("368293545763611759335443678239"), "76361")
assert_equals(substring.longest_substring("775195358448494712934755311372"), "4947")
assert_equals(substring.longest_substring("646113733929969155976523363762"), "76523")
assert_equals(substring.longest_substring("575337321726324966478369152265"), "478369")
assert_equals(substring.longest_substring("754388489999793138912431545258"), "545258")
assert_equals(substring.longest_substring("198644286258141856918653955964"), "2581418569")
assert_equals(substring.longest_substring("643349187319779695864213682274"), "349")
assert_equals(substring.longest_substring("919331281193713636178478295857"), "36361")
assert_equals(substring.longest_substring("2846286484444288886666448822244466688822247"), "47")
'''


# Minesweeper below ---> Working
'''
print("Minesweeper")
assert_equals(minesweeper1.num_grid([
['-', '-', '-', '-', '-'],
['-', '-', '-', '-', '-'],
['-', '-', '#', '-', '-'],
['-', '-', '-', '-', '-'],
['-', '-', '-', '-', '-']
]), [
['0', '0', '0', '0', '0'],
['0', '1', '1', '1', '0'],
['0', '1', '#', '1', '0'],
['0', '1', '1', '1', '0'],
['0', '0', '0', '0', '0']
])

assert_equals(minesweeper1.num_grid([
['-', '-', '-', '-', '#'],
['-', '-', '-', '-', '-'],
['-', '-', '#', '-', '-'],
['-', '-', '-', '-', '-'],
['#', '-', '-', '-', '-']
]), [
['0', '0', '0', '1', '#'],
['0', '1', '1', '2', '1'],
['0', '1', '#', '1', '0'],
['1', '2', '1', '1', '0'],
['#', '1', '0', '0', '0']
])

assert_equals(minesweeper1.num_grid([
['-', '-', '-', '#', '#'],
['-', '#', '-', '-', '-'],
['-', '-', '#', '-', '-'],
['-', '#', '#', '-', '-'],
['-', '-', '-', '-', '-']
]), [
['1', '1', '2', '#', '#'],
['1', '#', '3', '3', '2'],
['2', '4', '#', '2', '0'],
['1', '#', '#', '2', '0'],
['1', '2', '2', '1', '0']
])
'''


# Sudoku below ---> Working
'''
print("sudoku")
g1 = sudoku.Sudoku("417950030000000700060007000050009106800600000000003400900005000000430000200701580")
g2 = sudoku.Sudoku("005001000287369100416520000000700692000000000000806453843000000000930000950074200")
g3 = sudoku.Sudoku("270981006015726983869000271092678354057134829384259617730800462028407130040302798")

assert_equals(g1.board, [[4, 1, 7, 9, 5, 0, 0, 3, 0], [0, 0, 0, 0, 0, 0, 7, 0, 0], [0, 6, 0, 0, 0, 7, 0, 0, 0], [0, 5, 0, 0, 0, 9, 1, 0, 6], [8, 0, 0, 6, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 3, 4, 0, 0], [9, 0, 0, 0, 0, 5, 0, 0, 0], [0, 0, 0, 4, 3, 0, 0, 0, 0], [2, 0, 0, 7, 0, 1, 5, 8, 0]])
assert_equals(g1.get_row(0), [4, 1, 7, 9, 5, 0, 0, 3, 0])
assert_equals(g1.get_col(8), [0, 0, 0, 6, 0, 0, 0, 0, 0])
assert_equals(g1.get_sqr(1), [9, 5, 0, 0, 0, 0, 0, 0, 7])
assert_equals(g1.get_sqr(1, 8), [0, 3, 0, 7, 0, 0, 0, 0, 0])
assert_equals(g1.get_sqr(8, 3), [0, 0, 5, 4, 3, 0, 7, 0, 1])

assert_equals(g2.board, [[0, 0, 5, 0, 0, 1, 0, 0, 0], [2, 8, 7, 3, 6, 9, 1, 0, 0], [4, 1, 6, 5, 2, 0, 0, 0, 0], [0, 0, 0, 7, 0, 0, 6, 9, 2], [0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 8, 0, 6, 4, 5, 3], [8, 4, 3, 0, 0, 0, 0, 0, 0], [0, 0, 0, 9, 3, 0, 0, 0, 0], [9, 5, 0, 0, 7, 4, 2, 0, 0]])
assert_equals(g2.get_row(6), [8, 4, 3, 0, 0, 0, 0, 0, 0])
assert_equals(g2.get_col(2), [5, 7, 6, 0, 0, 0, 3, 0, 0])
assert_equals(g2.get_sqr(2), [0, 0, 0, 1, 0, 0, 0, 0, 0])
assert_equals(g2.get_sqr(5, 2), [0, 0, 0, 0, 0, 0, 0, 0, 0])
assert_equals(g2.get_sqr(8, 0), [8, 4, 3, 0, 0, 0, 9, 5, 0])

assert_equals(g3.board, [[2, 7, 0, 9, 8, 1, 0, 0, 6], [0, 1, 5, 7, 2, 6, 9, 8, 3], [8, 6, 9, 0, 0, 0, 2, 7, 1], [0, 9, 2, 6, 7, 8, 3, 5, 4], [0, 5, 7, 1, 3, 4, 8, 2, 9], [3, 8, 4, 2, 5, 9, 6, 1, 7], [7, 3, 0, 8, 0, 0, 4, 6, 2], [0, 2, 8, 4, 0, 7, 1, 3, 0], [0, 4, 0, 3, 0, 2, 7, 9, 8]])
assert_equals(g3.get_row(3), [0, 9, 2, 6, 7, 8, 3, 5, 4])
assert_equals(g3.get_col(6), [0, 9, 2, 3, 8, 6, 4, 1, 7])
assert_equals(g3.get_sqr(3), [0, 9, 2, 0, 5, 7, 3, 8, 4])
assert_equals(g3.get_sqr(1, 2), [2, 7, 0, 0, 1, 5, 8, 6, 9])
assert_equals(g3.get_sqr(4, 5), [6, 7, 8, 1, 3, 4, 2, 5, 9])
'''


# Wristband Below --> Working
'''
print("Wristband")
assert_equals(wrist.is_wristband( 
[['A', 'A'], 
['B', 'B'], 
['C', 'C']]), True)

assert_equals(wrist.is_wristband(
[['A', 'B'], 
['A', 'B'], 
['A', 'B']]), True)

assert_equals(wrist.is_wristband(
[['A', 'B', 'C'], 
['C', 'A', 'B'], 
['B', 'C', 'A'], 
['A', 'B', 'C']]), True)

assert_equals(wrist.is_wristband(
[['A', 'B', 'C'], 
['C', 'A', 'B'], 
['D', 'C', 'A'], 
['E', 'D', 'C']]), True)

assert_equals(wrist.is_wristband( 
[['A', 'B', 'C'], 
['B', 'A', 'B'], 
['D', 'C', 'A'], 
['E', 'D', 'C']]), False)

assert_equals(wrist.is_wristband(
[['A', 'B', 'C'], 
['B', 'C', 'A'], 
['C', 'A', 'B'], 
['A', 'B', 'A']]), True)

assert_equals(wrist.is_wristband(
[['A', 'B', 'C'], 
['B', 'C', 'D'], 
['C', 'D', 'E'], 
['D', 'E', 'F']]), True)

assert_equals(wrist.is_wristband(
[['A', 'B', 'C'], 
['B', 'C', 'D'], 
['C', 'D', 'E'], 
['D', 'E', 'E']]), True)

assert_equals(wrist.is_wristband( #this
[['A', 'B', 'C'], 
['B', 'C', 'D'], 
['C', 'D', 'E'], 
['D', 'F', 'E']]), False)

assert_equals(wrist.is_wristband( #this
[['A', 'B', 'C'], 
['B', 'D', 'A'], 
['C', 'A', 'B'], 
['A', 'B', 'A']]), False)

assert_equals(wrist.is_wristband( #this
[['A', 'B'],  
['A', 'B'], 
['A', 'C'],
['A', 'B']]), False)

assert_equals(wrist.is_wristband( #this
[['A', 'A'],
['B', 'B'],
['C', 'C'],
['D', 'B']]), False)
 
assert_equals(wrist.is_wristband(
[['A', 'A'],
['B', 'B'],
['C', 'C'],
['C', 'C']]), True)
'''


# Josephus below --> Working
'''
print("Josephus")
assert_equals(josephus.josephus(1), 1)
assert_equals(josephus.josephus(41), 19)
assert_equals(josephus.josephus(8), 1)
assert_equals(josephus.josephus(5), 3)
assert_equals(josephus.josephus(7), 7)
'''


# ECG below --> Working
'''
print("ecg")
assert_equals(ecg.ecg_seq_index(3), 4)
assert_equals(ecg.ecg_seq_index(5), 9)
assert_equals(ecg.ecg_seq_index(7), 13)
assert_equals(ecg.ecg_seq_index(18), 11)
assert_equals(ecg.ecg_seq_index(33), 20)
assert_equals(ecg.ecg_seq_index(44), 40)
assert_equals(ecg.ecg_seq_index(69), 43)
assert_equals(ecg.ecg_seq_index(75), 68)
assert_equals(ecg.ecg_seq_index(101), 188)
assert_equals(ecg.ecg_seq_index(208), 199)
assert_equals(ecg.ecg_seq_index(300), 281)
'''


# combinations below --> Working
'''
print("combinations")
assert_equals(combinations.combinations(6, 52), 20358520)
assert_equals(combinations.combinations(5, 52), 2598960)
assert_equals(combinations.combinations(10, 52), 15820024220)
assert_equals(combinations.combinations(18, 52), 42671977361650)
assert_equals(combinations.combinations(52, 52), 1)
assert_equals(combinations.combinations(7, 64), 621216192)
''' 

# Maxie Minnie below --> Working
'''
print("Max and Min")
assert_equals(maxmin(9876543210), (9876543210, 1876543290))
assert_equals(maxmin(1234567890), (9234567810, 1034567892))
assert_equals(maxmin(190015878798001), (990015878718001, 100015878798091)) 
assert_equals(maxmin(411347917692022), (911347917642022, 111347947692022))
assert_equals(maxmin(91620336331950), (99620336331150, 11620336339950))
assert_equals(maxmin(428256072523076), (824256072523076, 228256072543076))
assert_equals(maxmin(999607251369567), (999907251366567, 199607259369567))
assert_equals(maxmin(10936404093733), (90936404013733, 10036404993733))
assert_equals(maxmin(116962727585478), (916162727585478, 112962767585478))
assert_equals(maxmin(645440811595719), (945440811595716, 145440811595769))
assert_equals(maxmin(304732653285373), (804732653235373, 204732653385373))
assert_equals(maxmin(734694929081563), (934694927081563, 134694929087563))
assert_equals(maxmin(597202395684464), (997202355684464, 297205395684464))
assert_equals(maxmin(111090753368874), (911010753368874, 101091753368874))
assert_equals(maxmin(357758017083851), (857758017083351, 157758017083853))
assert_equals(maxmin(744888865698909), (944888865698907, 447888865698909))
assert_equals(maxmin(589067130451808), (985067130451808, 189067130455808))
assert_equals(maxmin(236077600527389), (936077600527382, 206077603527389))
assert_equals(maxmin(405272406161141), (705242406161141, 105272406161144))
assert_equals(maxmin(21460234556134), (61460234552134, 11460234556234))
assert_equals(maxmin(347435942637955), (947435942637355, 247435943637955))
assert_equals(maxmin(942631615759140), (992631615754140, 142631615759940))
'''

# Fiscal Passport below --> Working
'''
print("Fiscal below")
assert_equals(fiscalCode({ "name": "Brendan", "surname": "Eich", "gender": "M", "dob": "1/12/1961" }), "CHEBND61T01")
assert_equals(fiscalCode({ "name": "Helen", "surname": "Yu", "gender": "F", "dob": "1/12/1950" }), "YUXHLN50T41")
assert_equals(fiscalCode({ "name": "Al", "surname": "Capone", "gender": "M", "dob": "17/1/1899" }), "CPNLAX99A17")
assert_equals(fiscalCode({ "name": "Mickey", "surname": "Mouse", "gender": "M", "dob": "16/1/1928" }), "MSOMKY28A16")
assert_equals(fiscalCode({ "name": "Marie", "surname": "Curie", "gender": "F", "dob": "7/11/1867" }), "CRUMRA67S47")
'''

# 3 Divisors --> Working
'''
print("exactly three below")
assert_equals(is_exactly_three(4), True)
assert_equals(is_exactly_three(12), False)
assert_equals(is_exactly_three(25), True)
assert_equals(is_exactly_three(121), True)
assert_equals(is_exactly_three(48), False)
assert_equals(is_exactly_three(1), False)
assert_equals(is_exactly_three(81), False)
assert_equals(is_exactly_three(1521), False)
assert_equals(is_exactly_three(225), False)
assert_equals(is_exactly_three(27550356289), True)
assert_equals(is_exactly_three(25235235235), False)
assert_equals(is_exactly_three(10), False)
assert_equals(is_exactly_three(64), False)
assert_equals(is_exactly_three(9), True)
assert_equals(is_exactly_three(144), False)
assert_equals(is_exactly_three(3), False)
assert_equals(is_exactly_three(2), False)
assert_equals(is_exactly_three(42351351), False)
assert_equals(is_exactly_three(999966000289), True)
assert_equals(is_exactly_three(20152357681), True)
assert_equals(is_exactly_three(531625249), True)
assert_equals(is_exactly_three(264306808866), False)
assert_equals(is_exactly_three(975179493674), False)
assert_equals(is_exactly_three(49), True)
assert_equals(is_exactly_three(165983), False)
'''

# secret agent password below --> Working
'''
print("secret agent password below\n")
assert_equals(secret_password("mubashirh"), "hsajsi13u2")
assert_equals(secret_password("mattedabi"), "detbcj13a20")
assert_equals(secret_password("HeLen-eda"), "BANG! BANG! BANG!")
assert_equals(secret_password("pakistani"), "tsiboj16a11")
assert_equals(secret_password("airforce1"), "BANG! BANG! BANG!")
assert_equals(secret_password("airforces"), "rofdft1i18")
assert_equals(secret_password("Airforcee"), "BANG! BANG! BANG!")
assert_equals(secret_password("pilotmuba"), "mtovcb16i12")
assert_equals(secret_password("a_rforcee"), "BANG! BANG! BANG!")
assert_equals(secret_password("iloveherh"), "hevfsi9l15")
assert_equals(secret_password("airforcess"), "BANG! BANG! BANG!")
assert_equals(secret_password("edabit"), "BANG! BANG! BANG!")
'''

# atbash below --> Working
'''
assert_equals(atbash("abcdefghijklmnopqrstuvwxyz"), "zyxwvutsrqponmlkjihgfedcba")
assert_equals(atbash("ABCDEFGHIJKLMNOPQRSTUVWXYZ"), "ZYXWVUTSRQPONMLKJIHGFEDCBA")
assert_equals(atbash("The word 'atbash' derives from the the first and last 2 letters of the Hebrew alphabet."), "Gsv dliw 'zgyzhs' wvirevh uiln gsv gsv urihg zmw ozhg 2 ovggvih lu gsv Svyivd zokszyvg.")
assert_equals(atbash("Vmxibkgrlm zmw wvxibkgrlm ziv rwvmgrxzo uli gsv Zgyzhs xrksvi."),"Encryption and decryption are identical for the Atbash cipher.")
'''



#########################################################################################################################