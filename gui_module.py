import customtkinter as ctk
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from plotting_module import *
from os.path import isfile

class GUI(ctk.CTk):
	def __init__(self):
		super().__init__()
		self.title('Golden Spiral')
		self.geometry('1200x630')
		self.config(bg='#121212')

		self.spiral = FibonacciSpiral(6, True, True, 'purple')
		self.spiral.drawFibonacciSpiral()
		self.canvas = FigureCanvasTkAgg(figure=self.spiral.figure, master=self)
		self.canvas.draw()
		self.canvas.get_tk_widget().place(x=0, y=0)

		self.savedFiguresNum = GUI.checkForLastSavedFigure(0)

		self.redrawButton = ctk.CTkButton(self, 
										  text='Redraw Spiral', 
										  command=self.redrawSpiral,
										  height=30,
										  width=120,
										  bg_color='#121212',
										  fg_color='#8e24aa',
										  text_color='white',
										  hover_color='#6A1B9A')
		self.redrawButton.place(x=1040, y=75)
		
		self.squareVariable = ctk.BooleanVar(value=True)
		self.squareCheckbox = ctk.CTkCheckBox(self,
										text='Show Squares',
										variable=self.squareVariable,
										onvalue=True,
										offvalue=False,
										height=30,
										width=120,
										bg_color='#121212',
										fg_color='#8e24aa',
										text_color='white',
										hover_color='#6A1B9A')
		self.squareCheckbox.place(x=1040, y=125)

		self.circleVariable = ctk.BooleanVar(value=True)
		self.circleCheckbox = ctk.CTkCheckBox(self,
										text='Show Spiral',
										variable=self.circleVariable,
										onvalue=True,
										offvalue=False,
										height=30,
										width=120,
										bg_color='#121212',
										fg_color='#8e24aa',
										text_color='white',
										hover_color='#6A1B9A')
		self.circleCheckbox.place(x=1040, y=175)

		self.optionVariable = ctk.StringVar(value='6')
		self.selectN = ctk.CTkOptionMenu(self, 
						 				 values=[f'{i}' for i in range(11)],
						 				 variable=self.optionVariable,
										 height=30,
										 width=120,
										 bg_color='#121212',
										 fg_color='#8e24aa',
										 text_color='white',
										 button_color='#7B1FA2',
										 button_hover_color='#4A148C') 
		self.selectN.place(x=1040, y=225)

		self.nLabel = ctk.CTkLabel(self, 
							 	   text='n=',
								   height=30,
								   width=40,
								   bg_color='#121212',
								   fg_color='#121212',
								   text_color='white') 
		self.nLabel.place(x=1000, y=225)

		self.fnLabel = ctk.CTkLabel(self,
									text=f'F({self.spiral.n}) = {self.spiral.fibList[-1]}',
								    height=30,
								    width=120,
								    bg_color='#121212',
								    fg_color='#CE93D8',
								    text_color='black',
									corner_radius=25)
		self.fnLabel.place(x=1040, y=275)

		self.colourVariable = ctk.StringVar(value='purple')
		self.selectN = ctk.CTkOptionMenu(self, 
						 				 values=['purple', 'red', 'blue', 'green', 'yellow', 'black'],
						 				 variable=self.colourVariable,
										 height=30,
										 width=120,
										 bg_color='#121212',
										 fg_color='#8e24aa',
										 text_color='white',
										 button_color='#7B1FA2',
										 button_hover_color='#4A148C') 
		self.selectN.place(x=1040, y=325)

		self.saveButton = ctk.CTkButton(self, 
										text='Save Figure', 
										command=self.saveFigure,
										height=30,
										width=120,
										bg_color='#121212',
										fg_color='#8e24aa',
										text_color='white',
										hover_color='#6A1B9A')
		self.saveButton.place(x=1040, y=525)

	def redrawSpiral(self):
		self.spiral = FibonacciSpiral(int(self.optionVariable.get()), 
										  self.squareVariable.get(), 
										  self.circleVariable.get(),
										  self.colourVariable.get())
		self.spiral.drawFibonacciSpiral()
		self.canvas = FigureCanvasTkAgg(figure=self.spiral.figure, master=self)
		self.canvas.draw()
		self.canvas.get_tk_widget().place(x=0, y=0)
		self.fnLabel.configure(text=f'F({self.spiral.n}) = {self.spiral.fibList[-1]}')

	@staticmethod
	def checkForLastSavedFigure(start):
		i = start
		isSaved = isfile(f'golden_spiral_{i}.png')
		while isSaved:
			i += 1
			isSaved = isfile(f'golden_spiral_{i}.png')
		return i

	def saveFigure(self):
		self.savedFiguresNum = GUI.checkForLastSavedFigure(self.savedFiguresNum)
		self.spiral.figure.savefig(f'golden_spiral_{self.savedFiguresNum}.png')
		self.savedFiguresNum += 1
