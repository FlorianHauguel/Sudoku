def Sudoku1():
	o = 0
	return [[o,o,o,o,o,5,1,o,8],
			[o,7,8,1,9,o,o,o,o],
			[o,1,o,o,3,7,9,o,5],
			[8,3,o,o,o,o,7,1,o],
			[o,o,1,o,o,o,2,o,o],
			[o,9,6,o,o,o,o,8,4],
			[6,o,7,5,2,o,o,3,o],
			[o,o,o,o,7,9,4,2,o],
			[1,o,9,4,o,o,o,o,o]]

def Sudoku2():
	test = [[y for x in range(9)] for y in range(9)]
	
	#test = [[x for x in range(9)] for x in range(9)]
	return test

def Sudoku3():
	o = 0
	return [[o,7,o,o,o,4,o,o,2],
			[o,o,1,o,3,o,o,4,o],
			[o,o,o,5,o,o,1,o,o],
			[o,4,o,o,o,3,o,o,8],
			[o,o,3,o,o,o,7,o,o],
			[1,o,o,6,o,o,o,9,o],
			[o,o,4,o,o,1,o,o,o],
			[o,2,o,o,7,o,8,o,o],
			[5,o,o,9,o,o,o,6,o]]