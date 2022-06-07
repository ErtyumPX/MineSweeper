from tkinter import *
from random import sample

root = Tk()
root.resizable(False, False)
root.title('Mine Sweeper')


class MineField():
	def __init__(self, mapLength, row, mineAmount):
		self.mapLength = mapLength
		self.row = row
		self.nodesInLine = int(mapLength/row)
		self.mineAmount = mineAmount
		self.mines = []
		self.grid = []
		for i in range(mapLength):
			node = Node(i, self.nodesInLine)
			self.grid.append(node)

		for node in sample(self.grid, mineAmount):
			node.isMine = True
			#node.button.configure(text='M')
			self.mines.append(node)

		for node in (set(self.grid) - set(self.mines)):
			node.number = self.Count(node)
			#node.button.configure(text=node.number)
		n = 0
		for node in self.grid:
			if(node.isMine):
				print('M', end=' ')
			else:
				print(node.number, end=' ')
			n += 1
			if(n % self.nodesInLine == 0):
				print()

	def Count(self, node):
		neighbourMineCount = 0
		rightSide = [node.place-self.nodesInLine+1, node.place+1, node.place+self.nodesInLine+1]
		leftSide = [node.place-self.nodesInLine-1, node.place-1, node.place+self.nodesInLine-1]
		upDown = [node.place-self.nodesInLine, node.place+self.nodesInLine]

		if((node.place+1) % self.nodesInLine == 0):
			rightSide.clear()
		if(node.y == 0):
			leftSide.clear()

		for nodeList in rightSide, leftSide, upDown:
			for index in nodeList:
				if(self.mapLength > index >= 0):
					if(self.grid[index].isMine):
						neighbourMineCount += 1
					else:
						node.neighbours.append(self.grid[index])
		return neighbourMineCount
		
 
class Node():
	def __init__(self, place, nodesInLine, isMine = False, number = 0):
		self.place = place
		self.nodesInLine = nodesInLine
		self.x, self.y = divmod(self.place, self.nodesInLine)

		self.isMine = isMine #boolean
		self.number = number

		self.revealed = False
		self.neighbours = []

		self.button = Button(root,width=2,height=1, command=lambda:self.Reveal())
		self.button.grid(row=self.x, column=self.y)

	def Reveal(self):
		self.revealed = True
		if(self.isMine):
			self.button.configure(text='M')
		else:
			self.button.configure(text=self.number)
			if(self.number == 0):
				for neighbour in self.neighbours:
					if(not neighbour.revealed):
						neighbour.Reveal()

gameOver = False

gridX = 10
gridY = 10
mineField = MineField(100, 10, 10)

root.mainloop()