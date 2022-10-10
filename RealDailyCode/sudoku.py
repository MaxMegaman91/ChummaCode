# https://edabit.com/challenge/CMDy4pvnTZkFwJmmx

class Sudoku:
	def __init__(self,input):
		self.board = [[],[],[],[],[],[],[],[],[]]
		whichlist = 0
		x=0
		for i in input:
			if x >= 9:
				whichlist +=1
				x = 0
			self.board[whichlist].append(int(i))
			x +=1
	
	def printboard(self):
		for i in self.board:
			print(i)

	def get_row(self, rownumber):
		return self.board[rownumber]

	def get_col(self, colnumber):
		thelist = []
		for index in range(0,9):
			thelist.append(self.board[index][colnumber])
		return thelist
			
	def get_sqr(self, *m):
		thelist = []
		startcolumn = m[0] // 3 * 3
		if len(m) == 1:
			#the code to return a square
			startrow = m[0] % 3 * 3
		elif len(m) == 2:
			#the code to return the square of a position
			startrow = m[1] // 3 * 3
		for i in range(0,3):
				for j in range(0,3):
					thelist.append(self.board[startcolumn+i][startrow+j])
		return thelist
