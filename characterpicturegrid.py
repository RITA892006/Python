
print("name:BINDU SHREE")


grid = [['.', '.', '.', '.', '.', '.'],		# x0
        ['.', 'O', 'O', '.', '.', '.'],		# x1
        ['O', 'O', 'O', 'O', '.', '.'],		# x2
        ['O', 'O', 'O', 'O', 'O', '.'],		# x3
        ['.', 'O', 'O', 'O', 'O', 'O'],		# x4
        ['O', 'O', 'O', 'O', 'O', '.'],		# x5
        ['O', 'O', 'O', 'O', '.', '.'],		# x6
        ['.', 'O', 'O', '.', '.', '.'],		# x7
        ['.', '.', '.', '.', '.', '.']]		# x8
		# y0, y1, y2, y3, y4, y5

heart = ''

# j will become the future y
for j in range(len(grid[3])):

	# i will become the future x
	for i in reversed(range(len(grid))):

		heart += grid[i][j]

		if i == 0:
		
			heart += '\n'

print(heart)
