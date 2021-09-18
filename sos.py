board = ['x' for x in range(36)]

def is_free(pos):
	if board[pos] == 's' or board[pos] == 'o':
		return False
	return True

def set_value(pos,letter):
	board[pos] = letter 

def print_board(board):
	count = 0
	line = 0
	print('  -------------------------------------')
	print('  |     |     |     |     |     |     |')
	for x, i in enumerate(board):
		print('  | ',i,end="")
		count = count+1
		if(count == 6):
			line = line+1
			print("  |  ",x-4,' to ',line*count)
			count = 0
			print('  |     |     |     |     |     |     |')
			print("  --------------------------------------")
			if line != 6:
				print('  |     |     |     |     |     |     |')


def is_scored(board, pos,le):

	#to check linear
	score = 0
	if le == 's':
		if (board[pos-1] == 'o' and board[pos-2] =='s'):
			score = score+1
		
		if(board[pos+1] =='o' and board[pos+2] == 's'):
			score = score+1
		
		if(board[pos-6] =='o' and board[pos-12] == 's'):
			score = score+1
		
		if(board[pos+6] =='o' and board[pos+12] == 's'):
			score = score+1
			
		if(board[pos-7] == 'o' and board[pos-14] == 's'):
			score = score+1
		if(board[pos-5] == 'o' and board[pos-10] == 's'):
			score = score+1
		if(board[pos+5] =='o' and board[pos+10] == 's'):
			score = score+1
		if(board[pos+7] =='o' and board[pos+14] == 's'):
			score = score+1
	if le == 'o':
		if(board[pos-1] == 's' and board[pos+1] == 's'):
			score = score+1
		if(board[pos-6] == 's' and board[pos+6] == 's'):
			score = score+1
		if(board[pos-5] == 's' and board[pos+5] == 's'):
			score = score+1
		if(board[pos-7] == 's' and board[pos+7] == 's'):
			score = score+1
				
	return score

total_score1 = []
total_score2 = []
session = []

def player1_move():

	run = True

	while run:
		move = input("player1 enter position : ")
		inp = input("player1 enter letter : ")

		#try:
		move = int(move)
		move = move - 1
		if (move>=0 and move<=35) and (inp.lower() =='s' or inp.lower() == 'o'):
			if is_free(move):
				run = False
				set_value(move,inp.lower())
				print_board(board)
				print("Player 1 Points : ",session)
				#print("Player 2 Points : ",total_score2)
				point = is_scored(board,move,inp.lower())
				if(point>0):
					session.append(point)
					return True
				if point == 0:	
					total_score1.append(sum(session))
					print("Player 1 Total Points : ",total_score1)
					print("Player 2 Total Points : ",total_score2)
					session.clear()
			else:
				print('not free')

		else:
			print('enter valid position')

		#except:
		#	print('enter valid info')


	return False


def player2_move():

	run = True

	while run:
		move = input("player2 enter position : ")
		inp = input("player2 enter letter : ")



		#try:
		move = int(move)
		move = move - 1
		if (move>=0 and move<=35) and (inp.lower() =='s' or inp.lower() == 'o'):
			if is_free(move):
				run = False
				set_value(move,inp.lower())
				print_board(board)
				#print("Player 1 Points : ",total_score1)
				print("Player 2 Points : ",session)
				point = is_scored(board,move,inp.lower())
				if(point>0):
					session.append(point)
					return True
				elif point == 0:
					total_score2.append(sum(session))
					print("Player 1 Total Points : ",total_score1)
					print("Player 2 Total Points : ",total_score2)
					session.clear()

			else:
				print('not free')

		else:
			print('enter valid position')

		#except:
		#	print('enter valid info')

	return False

def isfull(board):
	for i in board:
		if i=='x':
			return False
	return True

def main():
	print_board(board)

	print("\n---------Welcome to S-O-S---------")
	print("\nAbove a board is given alongside the number range of each row.\n--You just enter the count from the row to choose a position--")
	start = input('enter y to start the game ')

	if start.lower() == 'y':
		while not(isfull(board)):
			while player1_move():
				#print_board(board)
				print("Player 1 You scored, take the turn")
				#player1_move()
		
			while player2_move():
				#print_board(board)
				print("Player 1 Total Points : ",total_score1)
				print("Player 2 Total Points : ",total_score2)
				print("Player 2 You scored, take the turn")
				#player2_move()

		p1 = 0
		p2 = 0

	if isfull(board):
		for i in total_score1:
			p1 = p1 + i

		for i in total_score2:
			p2 = p2+i

		board.clear()

		print("player1 score : ",p1)
		print("player2 score : ",p2)


main()


