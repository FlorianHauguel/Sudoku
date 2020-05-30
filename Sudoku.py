import numpy as np
from Examples import *

class Sudoku:
	def __init__(self, input = np.full((9, 9), ' ')):
		self.grid = np.array(input)
		self.candidates = np.zeros((9, 9), dtype=int)

	def GetSubGrid(self, number):
		row = 3 * int(number / 3)
		col = 3 * (number % 3)
		return self.grid[row : row + 3, col : col + 3]

	def GetRow(self, number):
		return self.grid[number]

	def GetColumn(self, number):
		return self.grid[:,number : number + 1]

	def Intersection(self, x, y):
		#TODO : if self.grid[x][y] != 0 result = [self.grid[x][y]] ???
		sg = int(x / 3) * 3 + int(y / 3)
		subGrid = self.GetSubGrid(sg).reshape(9)
		row = self.GetRow(x)
		column = self.GetColumn(y).reshape(9)
		result = np.unique(np.concatenate((subGrid,row, column),0))
		return result[(result > 0)]

	def Remainers(self, arr):
		complete = range(1, 10)
		remainer = np.setdiff1d(complete, arr)
		return remainer

	def AllRemainers(self, x, y):
		complete = range(1, 10)
		intersect = self.Intersection(x, y)
		remainer = np.setdiff1d(complete, intersect)
		if x == 2 and y == 6:
			print(remainer)
		return remainer

	def Complete(self):
		for i in range(9):
			for j in range(9):
				if self.grid[i][j] == 0:
					return False
		return True

	def BruteForce(self):
		#print('Let\'s solve this beast!')
		if self.Complete():
			if self.Unicity():
				#print('At least... Well done')
				print('Solution:')
				self.Render()
				return 1
			else:
				#print('Complete and... completly wrong \':(')
				return -1
		else:
			for i in range(9):
				for j in range(9):
					if self.grid[i][j] == 0:
						candidates = self.AllRemainers(i, j)
						#print(candidates)
						if len(candidates) == 0:
							#print('Dead end... no more candidates...')
							return -1
						else:
							for candidate in candidates:
								#print('Checking', candidate, 'on (', i, j, ')')
								newGrid = Sudoku(self.grid)
								newGrid.grid[i][j] = candidate

								newSolution = newGrid.BruteForce()
								if newSolution == -1:
									continue
								elif newSolution == 1:
									return 1
							#print('Go back up!')
							return -1

	def Render(self):
		for row in range(9):
			if (row != 0 and row % 3 == 0):
				print('-' * 30)
			for column in range(9):
				if (column != 0 and column % 3 == 0):
					print('| ', end ="")
				if self.grid[row][column] == 0:
					print(' ' , ' ', end = "")
				else:
						print(self.grid[row][column], ' ', end = "")
			print()
		print()

	def Unicity(self):
		for i in range(9):
			region = self.GetSubGrid(i).reshape(9)
			region = region[(region > 0)]
			unique, counts = np.unique(region, return_counts=True)
			if counts[(counts > 1)].any():
				return False

			band = self.GetRow(i)
			band = band[(band > 0)]
			unique, counts = np.unique(band, return_counts=True)
			if counts[(counts > 1)].any():
				return False

			stack = self.GetColumn(i).reshape(9)
			stack = stack[(stack > 0)]
			unique, counts = np.unique(stack, return_counts=True)
			if counts[(counts > 1)].any():
				return False
		return True

	def NakedSingles(self):
		#TODO : to rewrite using candidates grid ?
		#TODO : should return the position & the value, and leave the main solve function to modify if desired
		for i in range(9):
			subgrid = self.GetSubGrid(i).reshape(9)
			if len(subgrid[(subgrid == 0)]) == 1:
				position = np.where(subgrid == 0)[0][0]
				row = 3 * int(i / 3) + int(position / 3)
				col = 3 * (i % 3) + int(position % 3)
				print('Naked Single in subgrid', (row, col),'value', self.Remainers(subgrid)[0])
				self.grid[row][col] = self.Remainers(subgrid)[0]
				return True
			
			row = self.GetRow(i)
			if len(row[(row == 0)]) == 1:
				position = np.where(row == 0)[0][0]
				print('Naked Single in row', (i, position),'value', self.Remainers(row)[0])
				self.grid[i][position] = self.Remainers(row)[0]
				return True

			col = self.GetColumn(i).reshape(9)
			if len(col[(col == 0)]) == 1:
				position = np.where(col == 0)[0][0]
				print('Naked Single in col', (position, i),'value', self.Remainers(col)[0])
				self.grid[position][i] = self.Remainers(col)[0]
				return True
		return False

	def HiddenSingles(self):
		#TODO : to rewrite using candidates grid ?
		#TODO : should return the position & the value, and leave the main solve function to modify if desired
		for i in range(9):
			for j in range(9):
				if self.grid[i][j] == 0:
					candidates = self.AllRemainers(i, j)
					if len(candidates) == 1:
						print('Hidden Single in position', (i, j),'value', candidates[0])
						self.grid[i][j] = candidates[0]
						return True
		return False

	def SolveWithStyle(self):
		result = True
		self.FindCandidatesFirstRound()
		while result:
			self.Render()
			self.ClearObsoleteCandidates()
			result = False

			result = self.NakedSingles()
			if result:
				#apply the result if desired
				continue

			result = self.HiddenSingles()
			if result:
				#apply the result if desired
				continue

	def FindCandidatesFirstRound(self):
		for row in range(9):
			for col in range(9):
				if self.grid[row][col] == 0:
					self.candidates[row][col] = self.AllRemainers(row, col)

	def SubgridToXY(n):
		row = 3 * int(i / 3) + int(position / 3)
		col = 3 * (i % 3) + int(position % 3)
		return (row, col)

	def XYtoSubgraid(x, y):
		sg = int(x / 3) * 3 + int(y / 3)
		return sg

	def ClearObsoleteCandidates(self):
		for row in range(9):
			for col in range(9):
				val = self.grid[row][col]
				if val != 0:
					for k in range(9):
						np.delete(self.candidates[row][k], val)
						np.delete(self.candidates[k][col], val)
					for i in range(3):
						for j in range(3):
							np.delete(self.candidates[sg + i][sg + j], val)


print()
mySudoku = Sudoku(Sudoku1())
#mySudoku.Render()

#mySudoku.BruteForce()

mySudoku.SolveWithStyle()

#mySudoku.Render()

#mySudoku.NakedSingles()