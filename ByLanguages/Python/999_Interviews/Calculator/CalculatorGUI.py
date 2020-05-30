"""
@Author: Rahul Vats
@AuthorEmail: vats.rahul@gmail.com
@Note: This program creates a GUI calculator using tkinter library
"""
#-*-coding: utf-8-*-
try:
    # for Python2
    from Tkinter import *   ## notice capitalized T in Tkinter 
except ImportError:
    # for Python3
    from tkinter import *   ## notice lowercase 't' in tkinter here
import math

class calc:
	def getandreplace(self):
		"""replace x with * and ÷ with /"""
		
		self.expression = self.e.get()
		self.newtext=self.expression.replace(self.newdiv,'/')
		self.newtext=self.newtext.replace('x','*')

	def equals(self):
		"""when the equal button is pressed"""

		self.getandreplace()
		try: 
			self.value= eval(self.newtext) #evaluate the expression using the eval function
		except SyntaxError or NameErrror:
			self.e.delete(0,END)
			self.e.insert(0,'Invalid Input!')
		else:
			self.e.delete(0,END)
			self.e.insert(0,self.value)
	
	def squareroot(self):
		"""squareroot method"""
		
		self.getandreplace()
		try: 
			self.value= eval(self.newtext) #evaluate the expression using the eval function
		except SyntaxError or NameErrror:
			self.e.delete(0,END)
			self.e.insert(0,'Invalid Input!')
		else:
			self.sqrtval=math.sqrt(self.value)
			self.e.delete(0,END)
			self.e.insert(0,self.sqrtval)

	def square(self):
		"""square method"""
		
		self.getandreplace()
		try: 
			self.value= eval(self.newtext) #evaluate the expression using the eval function
		except SyntaxError or NameErrror:
			self.e.delete(0,END)
			self.e.insert(0,'Invalid Input!')
		else:
			self.sqval=math.pow(self.value,2)
			self.e.delete(0,END)
			self.e.insert(0,self.sqval)
	
	def clearall(self): 
		"""when clear button is pressed,clears the text input area"""
		self.e.delete(0,END)
	
	def clear1(self):
		self.txt=self.e.get()[:-1]
		self.e.delete(0,END)
		self.e.insert(0,self.txt)

	def action(self,argi): 
		"""pressed button's value is inserted into the end of the text area"""
		self.e.insert(END,argi)
	
	def __init__(self,master):
		"""Constructor method"""
		master.title('Graphical Scientific Calulator By Rahul Vats') 
		master.geometry()
		self.e = Entry(master)
		self.e.grid(row=0,column=0,columnspan=30,pady=5)
		self.e.focus_set() #Sets focus on the input text area
				
		self.div='÷'
		# self.newdiv=self.div.decode('utf-8')
		self.newdiv=self.div

		#Generating Buttons

		# Row 1 Items
		Button(master,text="7",width=3,command=lambda:self.action('7')).grid(row=1, column=0)
		Button(master,text="8",width=3,command=lambda:self.action(8)).grid(row=1, column=1)
		Button(master,text="9",width=3,command=lambda:self.action(9)).grid(row=1, column=2)
		Button(master,text="÷",width=3,command=lambda:self.action(self.newdiv)).grid(row=1, column=3) 
		Button(master,text='AC',width=3,command=lambda:self.clearall()).grid(row=1, column=4)
		Button(master,text='C',width=3,command=lambda:self.clear1()).grid(row=1, column=5)
		
		# Row 2 Items
		Button(master,text="4",width=3,command=lambda:self.action(4)).grid(row=2, column=0)
		Button(master,text="5",width=3,command=lambda:self.action(5)).grid(row=2, column=1)
		Button(master,text="6",width=3,command=lambda:self.action(6)).grid(row=2, column=2)
		Button(master,text="x",width=3,command=lambda:self.action('x')).grid(row=2, column=3)
		Button(master,text="(",width=3,command=lambda:self.action('(')).grid(row=2, column=4)
		Button(master,text=")",width=3,command=lambda:self.action(')')).grid(row=2, column=5)
		
		# Row 3 Items
		Button(master,text="1",width=3,command=lambda:self.action(1)).grid(row=3, column=0)
		Button(master,text="2",width=3,command=lambda:self.action(2)).grid(row=3, column=1)
		Button(master,text="3",width=3,command=lambda:self.action(3)).grid(row=3, column=2)
		Button(master,text="-",width=3,command=lambda:self.action('-')).grid(row=3, column=3)
		Button(master,text="√",width=3,command=lambda:self.squareroot()).grid(row=3, column=4)
		Button(master,text="x²",width=3,command=lambda:self.square()).grid(row=3, column=5)
		
		# Row 4 Items
		Button(master,text="0",width=3,command=lambda:self.action(0)).grid(row=4, column=0)
		Button(master,text=".",width=3,command=lambda:self.action('.')).grid(row=4, column=1)
		Button(master,text="%",width=3,command=lambda:self.action('%')).grid(row=4, column=2)
		Button(master,text="+",width=3,command=lambda:self.action('+')).grid(row=4, column=3)
		Button(master,text="=",width=10,command=lambda:self.equals()).grid(row=4, column=4,columnspan=2)
		
		# Row 5 Items
		Button(master,text="This is Awesome.",width=10)
		
#Main
root = Tk()
obj=calc(root) #object instantiated
root.mainloop()
