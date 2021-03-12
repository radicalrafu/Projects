from time import time

def solve(board, t):
    steps = 0
    solution = [[]]
    visited = []

    print("\nThis might take a while...\n")

    solution.append(board)
    while (len(solution) != 0) and (remainingBlocks(solution[-1]) > 0):
        steps += 1
        next_board = solve_helper(solution[-1], visited)
        if next_board != None:
            solution.append(next_board)
            visited.append(next_board)
        else:
            solution.pop()

    if len(solution)!= 0:
        print_board(solution[-1])
        t = (int((time()-t)*100))/100
        print("\nSolved in",steps,"steps and ",t," seconds\n")

    else:
        print(" cannot  solve :( try again ")


def solve_helper(board, visited):

    new_board = [row[:] for row in board]
    for m in range(0,9):
        for n in range(0,9):
            if board[m][n] == 0:
                for k in range(1,10):
                        if is_valid(m,n, board,k):
                            new_board[m][n] = k
                            if new_board not in visited:
                                return new_board
                            new_board = [row[:] for row in board]
                return None
    return None

def remainingBlocks(sudoku):
    count = 0
    for row in sudoku:
        for column in row:
            if column == 0:
                count += 1
    return count

def print_board(board):
    print("Boards")

    for row in board:
        check = True
        for column in row:
            if check:
                print('|  ' + str(column), end = '')
                check = False
            else:
                print("  |  "+str(column), end = '')
        print('  |\n_______________________________________________________\n')

def is_valid(y,x,board,value):
    if board[y][x] != 0:
        return False

    for row in board:
        if row[x] == value:
            return False

    if value in board[y]:
        return False

    for m in range(0,9):
        for n in range(0,9):
            if(not(m == y and n == x)):
                if((int(m/3) == int(y/3)) and (int(n/3) == int(x/3))):
                    if board[m][n] == value:
                        return False

    return True


def main():

	board = []

	filename = ""
	
	user_input = input("\n\nHello! Type in the txt filename of the sudoku you would like to solve! If you'd like to know what the file format is, type \"BRUH\"\n\n")
	
	if user_input == "BRUH":
		print("Here is an example of what a .txt file containing a sudoku would look like:")
		print("2..1.5..3\n.54...71.\n.1.2.3.8.\n6.28.73.4\n.........\n1.53.98.6\n.2.7.1.6.\n.81...24.\n7..4.2..1")
		user_input = input("\n\nIf u have the file, type the name. Otherwise, type \"exit\"\n")

	if ".txt" in user_input:
		filename = user_input.strip()
	else:
		filename = user_input.strip() + ".txt"
	
	try:
		file = open(filename, "r")
		for row in file:
			r = []
			for cell in list(row):
				if cell == '.':
					r.append(0)
				elif(cell == '\n'):
					None
				else:
					r.append(int(cell))
			board.append(r)
	except:
		print("Invalid file!")
		return
	
	solve(board, time())


if __name__ == '__main__':
    main()