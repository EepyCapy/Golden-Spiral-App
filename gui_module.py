import customtkinter as ctk
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from plotting_module import *

class GUI(ctk.CTk):
	def __init__(self):
		super().__init__()
		self.title('Golden Spiral')
		self.geometry('1200x630')
		self.config(bg='#121212')

		self.spiral = FibonacciSpiral(6, True)
		self.spiral.drawFibonacciSpiral()
		self.canvas = FigureCanvasTkAgg(figure=self.spiral.figure, master=self)
		self.canvas.draw()
		self.canvas.get_tk_widget().place(x=0, y=0)

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
		self.selectN.place(x=1040, y=175)
		self.nLabel = ctk.CTkLabel(self, 
							 	   text='n =',
								   height=30,
								   width=40,
								   bg_color='#121212',
								   fg_color='#121212',
								   text_color='white') 
		self.nLabel.place(x=1000, y=175)
		self.checkboxVariable = ctk.BooleanVar(value=True)
		self.checkbox = ctk.CTkCheckBox(self,
										text='Show Squares',
										#command=self.displaySquares,
										variable=self.checkboxVariable,
										onvalue=True,
										offvalue=False,
										height=30,
										width=120,
										bg_color='#121212',
										fg_color='#8e24aa',
										text_color='white',
										hover_color='#6A1B9A')
		self.checkbox.place(x=1040, y=125)

	def redrawSpiral(self):
		self.spiral = FibonacciSpiral(int(self.optionVariable.get()), self.checkboxVariable.get())
		self.spiral.drawFibonacciSpiral()
		self.canvas = FigureCanvasTkAgg(figure=self.spiral.figure, master=self)
		self.canvas.draw()
		self.canvas.get_tk_widget().place(x=0, y=0)

	#def displaySquares(self):
	#	self.spiral.showSquares = self.checkboxVariable.get()
	#	print(self.spiral.showSquares)

