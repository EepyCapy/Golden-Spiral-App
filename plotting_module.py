import numpy as np
import matplotlib.pyplot as plt

# Function that calculates the n-th term of the fibonacci sequence
# using Binet's formula (given that 0<=n)
def fibonacci(n):
	phi = (1 + np.sqrt(5)) / 2
	F_n = (phi ** n - (-phi) ** (-n)) / np.sqrt(5)
	return int(F_n)

# Class that represents a Square
# Squares are defined by their top-left corner and the length of their sides
class Square:
	def __init__(self, x, y, sideLength):
		self.x = x                   # x-coordinate of the top-left corner of the Square
		self.y = y                   # y-coordinate of the top-left corner of the Square
		self.sideLength = sideLength # Side-length of the Square

	def drawSquare(self, axes):
		xCoords = [self.x, 
			   self.x + self.sideLength, 
			   self.x + self.sideLength,
			   self.x,
			   self.x]
		yCoords = [self.y, 
			   self.y,
			   self.y - self.sideLength,
			   self.y - self.sideLength,
			   self.y]
		axes.plot(np.array(xCoords), np.array(yCoords), color='black')

# Class that represents a Quarter Circle
# Quarter Circles are defined by their center, their radius and their orientation on the plane
# This class creates Quarter Circles that, if centered at the origin, would exist in only one
# quadrant of the plane, which will be use to specify the orientation of a Quarter Circle
class QuarterCircle:
	def __init__(self, x, y, radius, quadrant):
		self.x = x               # x-coordinate of the center of the Quarter Circle
		self.y = y               # y-coordinate of the center of the Quarter Circle
		self.radius = radius     # Radius of the Quarter Circle
		self.quadrant = quadrant # Quadrant in which the Quarter Circle would be 
					 # if it were centered at the Origin of the Coordinate System

	def drawQuarterCircle(self, axes):
		# Circle centered at Origin
		xCoords = np.linspace(0, self.radius, 60)
		yCoords = np.sqrt(self.radius ** 2 - xCoords ** 2)
		# Moving Circle to real Coordinate System
		xTranslation = self.x * np.ones(len(xCoords))
		yTranslation = self.y * np.ones(len(yCoords))
		# Plotting
		if self.quadrant == 1:
			axes.plot(xCoords + xTranslation, yCoords + yTranslation)
		if self.quadrant == 2:
			axes.plot(-np.flip(xCoords) + xTranslation, np.flip(yCoords) + yTranslation)
		if self.quadrant == 3:
			axes.plot(-np.flip(xCoords) + xTranslation, -np.flip(yCoords) + yTranslation)
		if self.quadrant == 4:
			axes.plot(xCoords + xTranslation, -yCoords + yTranslation)

# Class that represents the Golden/Fibonacci Spiral and Fibonacci Squares
class FibonacciSpiral:
	def __init__(self, n, boolVal):
		# Defining attributes
		self.n = n
		self.fibList = [fibonacci(i) for i in range(n + 1)]
		# Plotting attributes
		self.figure = plt.figure(figsize=(10, 6.1803), facecolor='#121212')
		self.axes = self.figure.add_subplot()
		self.axes.tick_params(left=False, bottom=False, labelleft=False, labelbottom=False)
		self.showSquares = boolVal

	def calculateSquareCorners(self):
		l = len(self.fibList)
		squareCounter = 1
		xCoord = -self.fibList[l - 1]
		yCoord = self.fibList[l - 1]
		corners = [[xCoord, yCoord]]
		for i in range(l - 1):
			if squareCounter == 1:
				xCoord += self.fibList[l - 1 - i]
			if squareCounter == 2:
				xCoord += self.fibList[l - 1 - i] - self.fibList[l - 2 - i]
				yCoord -= self.fibList[l - 1 - i]
			if squareCounter == 3:
				xCoord -= self.fibList[l - 2 - i]
				yCoord -= self.fibList[l - 1 - i] - self.fibList[l - 2 - i]
			if squareCounter == 4:
				yCoord += self.fibList[l - 2 - i]
				squareCounter = 0
			squareCounter += 1
			corners.append([xCoord, yCoord])
		corners.reverse()
		return corners

	def calculateCircleCenters(self):
		l = len(self.fibList)
		circleCounter = 1
		xCoord = 0
		yCoord = 0
		centers = [[xCoord, yCoord]]
		for i in range(l - 1):
			if circleCounter == 1:
				yCoord += self.fibList[l - 1 - i] - self.fibList[l - 2 - i]
			if circleCounter == 2:
				xCoord += self.fibList[l - 1 - i] - self.fibList[l - 2 - i]
			if circleCounter == 3:
				yCoord -= self.fibList[l - 1 - i] - self.fibList[l - 2 - i]
			if circleCounter == 4:
				xCoord -= self.fibList[l - 1 - i] - self.fibList[l - 2 - i]
				circleCounter = 0
			circleCounter += 1
			centers.append([xCoord, yCoord])
		centers.reverse()
		return centers

	def getSquares(self):
		corners = self.calculateSquareCorners()
		return [Square(*corners[i], self.fibList[i]) for i in range(self.n + 1)]

	def getQuarterCirlces(self):
		centers = self.calculateCircleCenters()
		quadrantNum = 3 - (self.n + 1) % 4
		if quadrantNum == 0: quadrantNum = 4
		quarterCircleList = []
		for i in range(self.n + 1):
			quarterCircleList.append(QuarterCircle(*centers[i], self.fibList[i], quadrantNum))
			if quadrantNum == 4:
				quadrantNum = 0
			quadrantNum += 1
		return quarterCircleList

	def drawFibonacciSpiral(self):
		squareList = self.getSquares()
		quarterCircleList = self.getQuarterCirlces()
		if self.showSquares:
			for square in squareList:
				square.drawSquare(self.axes)
		for quarterCircle in quarterCircleList:
			quarterCircle.drawQuarterCircle(self.axes)
