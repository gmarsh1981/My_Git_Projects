from tkinter import *
from tkinter import filedialog
from PIL import Image, ImageTk
import tkinter.messagebox
from time import sleep
import os.path
import csv
import datetime
import shutil
import sys
from decimal import Decimal

#create popup window class
class popupWindow(object):
	def __init__(self, rootWindow):
		self.top=Toplevel(rootWindow)
		self.l=Label(self.top, text= "Enter Goal Amount", justify='center', font=('Arial Rounded MT Bold','22'))
		self.l.pack(pady=10, padx=5)
		self.e = Entry(self.top, justify='center', font=('Arial Rounded MT Bold','22'))
		self.e.pack(pady=10, padx=5)
		self.b = Button(self.top, text="Done", font=('Arial Rounded MT Bold','22'), command=self.cleanup_func)
		self.b.pack(pady=10, padx=5)
		
	def cleanup_func(self):
		self.goal_value = self.e.get()
		self.top.destroy()

class BankingApp(object):
	def __init__(self, rootWindow):
		self.rootWindow = rootWindow
		rootWindow.title('THE PIGGY BANK')
		
		self.enter_name = StringVar()
		self.enter_name.set('Enter your name: ')
		
		self.date = datetime.date.today()
		
		#Create frame 1
		self.frame1 = Frame(self.rootWindow)
		self.frame1.grid(row=0, column=0, sticky=N+S+E+W)
		
		
		#Create menu elements
		self.mainMenu = Menu(self.rootWindow)
		self.rootWindow.configure(menu = self.mainMenu)
		self.subMenu1 = Menu(self.mainMenu)
		self.mainMenu.add_cascade(label = 'File', menu = self.subMenu1)
		self.subMenu1.add_command(label = 'Export Balance', command = self.export_balance)
		self.subMenu1.add_command(label = 'Exit', command = self.end_func)
		#submenu2
		self.subMenu2 = Menu(self.mainMenu)
		self.mainMenu.add_cascade(label = 'Goal', menu = self.subMenu2)
		self.subMenu2.add_command(label = 'Make A Goal', command= self.create_goal_func)
		self.subMenu2.add_command(label = 'See A Goal', command= self.view_goal_func)
		self.subMenu2.add_command(label = 'End A Goal', command= self.end_goal_func)
		
		
		#Elements frame1
		self.go_btn = Button(self.frame1, text='Go', font=('Arial Rounded MT Bold','22'), command=self.go_func)
		self.login_btn = Button(self.frame1, text='Login', font=('Arial Rounded MT Bold','22'), command=self.user_choices_func)
		self.view_btn = Button(self.frame1, text="Balance", font=('Arial Rounded MT Bold','22'), command=self.view_balance_func)
		self.deposit_btn = Button(self.frame1, text='Deposit', font=('Arial Rounded MT Bold','22'), command=self.what_to_do_func)
		self.withdraw_btn = Button(self.frame1, text = "Withdraw", font=('Arial Rounded MT Bold','22'), command=self.what_to_do_func)
		self.exit_bth = Button(self.frame1, text="Exit", font=('Arial Rounded MT Bold','22'), command= self.rootWindow.quit)
		self.name_entry = Entry(self.frame1, textvariable = self.enter_name, justify='center', font=('Arial Rounded MT Bold','24'), fg= 'gray')
		self.name_entry.bind('<Button-1>', self.clear_entry_func)
		self.screen_lbl = Text(self.frame1, height= 0, width = 0, font = ('Consolas','16'), fg = 'green', bg = 'black')
		#add image
		#self.img = ImageTk.PhotoImage(Image.open(''))
		#self.img_panel = Label(self.frame1, image = self.img) 
		self.img1 = ImageTk.PhotoImage(Image.open('piggybanklogo.png'))
		self.img_panel1 = Label(self.frame1, image = self.img1) 
		#Create scrollbar for textbox
		self.scrollbar = Scrollbar(self.frame1, command=self.screen_lbl.yview)
		self.scrollbar.grid(row=1, column=3, sticky=N+S+E+W)
		self.screen_lbl['yscrollcommand'] = self.scrollbar.set
		
		##################################################################
		#Element Grid
		for i in range(3):
			Grid.rowconfigure(self.frame1, i, weight= 1)
		for i in range(3):
			Grid.columnconfigure(self.frame1, i, weight= 1)
			
		self.go_btn.grid(row=0, column=0, sticky=N+S+E+W, pady=5, padx=5)
		self.login_btn.grid(row=0, column=1, sticky=N+S+E+W, pady=5, padx=5)
		self.name_entry.grid(row=0, column=2, columnspan=2, sticky=N+S+E+W, pady=5, padx=5)
		self.view_btn.grid(row=1, column =0, sticky=N+S+E+W, pady=5, padx=5)
		self.deposit_btn.grid(row=1, column =1, sticky=N+S+E+W, pady=5, padx=5)
		self.screen_lbl.grid(row=1, column=2, sticky=N+S+E+W, ipady=20, padx=5)
		self.withdraw_btn.grid(row=2, column =0, sticky=N+S+E+W, pady=5, padx=5)
		self.exit_bth.grid(row=2, column =1, sticky=N+S+E+W, pady=5, padx=5)
		self.img_panel1.grid(row=2, column=2, sticky=W+E, pady=5, padx=5)
		
		
			

	def add_goal_bar_func(self):	
		
		#Create Frame 2
		self.frame2 = Frame(self.rootWindow)
		self.frame2.grid(row=0, column=3, padx=30, sticky=N+S+E+W)
	    
		
		if os.path.exists(self.username+'_goal.txt'):
			f = open(self.username+'_goal.txt', 'r')
			known_value_amount = f.read()
			known_value_amount = float(known_value_amount)
			#Algorithm to identify the amount of cells to color
			balance = self.get_balance_func()
			balance = float(balance)
			one_thirtyth = float(known_value_amount) * .0333
			counter = float(known_value_amount) * .0333
			x = 1
			while balance % one_thirtyth != balance and one_thirtyth != balance:
				one_thirtyth += counter
				x +=1
		else:
			#Algorithm to identify the amount of cells to color
			balance = self.get_balance_func()
			balance = float(balance)
			one_thirtyth = float(self.value_amount) * .0333
			counter = float(self.value_amount) * .0333
			x = 1
			while balance % one_thirtyth != balance and one_thirtyth != balance:
				one_thirtyth += counter
				x +=1
			
		
		if x <= 1:	
			self.a = '#e3d2d5'
		else:
			self.a = '#894450'
		if x < 2:
			self.b = '#e3d2d5'
		else:
			self.b = '#894450'
		if x < 3:
			self.c = '#e3d2d5'
		else:
			self.c = '#894450'
		if x < 4:	
			self.d = '#e3d2d5'
		else: 
			self.d = '#894450'
		if x < 5:	
			self.e = '#e3d2d5'
		else: 
			self.e = '#894450'
		if x < 6:	
			self.f = '#e3d2d5'
		else: 
			self.f = '#894450'
		if x < 7:	
			self.g = '#e3d2d5'
		else: 
			self.g = '#894450'
		if x < 8:	
			self.h = '#e3d2d5'
		else: 
			self.h = '#894450'
		if x < 9:	
			self.i = '#e3d2d5'
		else: 
			self.i = '#894450'
		if x < 10:	
			self.j = '#e3d2d5'
		else: 
			self.j = '#894450'
		if x < 11:	
			self.k = '#e3d2d5'
		else: 
			self.k = '#894450'
		if x < 12:	
			self.l = '#e3d2d5'
		else: 
			self.l = '#894450'
		if x < 13:	
			self.m = '#e3d2d5'
		else: 
			self.m = '#894450'
		if x < 14:	
			self.n = '#e3d2d5'
		else: 
			self.n = '#894450'
		if x < 15:	
			self.o = '#e3d2d5'
		else: 
			self.o = '#894450'
		if x < 16:	
			self.p = '#e3d2d5'
		else: 
			self.p = '#894450'
		if x < 17:	
			self.q = '#e3d2d5'
		else: 
			self.q = '#894450'
		if x < 18:	
			self.r = '#e3d2d5'
		else: 
			self.r = '#894450'
		if x < 19:	
			self.s = '#e3d2d5'
		else: 
			self.s = '#894450'
		if x < 20:	
			self.t = '#e3d2d5'
		else: 
			self.t = '#894450'
		if x < 21:	
			self.u = '#e3d2d5'
		else: 
			self.u = '#894450'
		if x < 22:	
			self.v = '#e3d2d5'
		else: 
			self.v = '#894450'
		if x < 23:	
			self.w = '#e3d2d5'
		else: 
			self.w = '#894450'
		if x < 24:	
			self.x = '#e3d2d5'
		else: 
			self.x = '#894450'
		if x < 25:	
			self.y = '#e3d2d5'
		else: 
			self.y = '#894450'			
		if x < 26:	
			self.z = '#e3d2d5'
		else: 
			self.z = '#894450'
		if x < 27:	
			self.aa = '#e3d2d5'
		else: 
			self.aa = '#894450'
		if x < 28:	
			self.bb = '#e3d2d5'
		else: 
			self.bb = '#894450'
		if x < 29:	
			self.cc = '#e3d2d5'
		else: 
			self.cc = '#894450'
		if x <= 30:	
			self.dd = '#e3d2d5'
		else: 
			self.dd = '#894450'
					
				
			
		#Frame 2 Elements
		self.img2 = ImageTk.PhotoImage(Image.open('goal.png'))
		self.img_panel2 = Label(self.frame2, image = self.img2) 
		self.screen_lbl1 = Label(self.frame2, height= 1, width = 5,   bg = self.dd)
		self.screen_lbl2 = Label(self.frame2, height= 1, width = 5,   bg = self.cc)
		self.screen_lbl3 = Label(self.frame2, height= 1, width = 5,   bg = self.bb)
		self.screen_lbl4 = Label(self.frame2, height= 1, width = 5,   bg = self.aa)
		self.screen_lbl5 = Label(self.frame2, height= 1, width = 5,   bg = self.z)
		self.screen_lbl6 = Label(self.frame2, height= 1, width = 5,   bg = self.y)
		self.screen_lbl7 = Label(self.frame2, height= 1, width = 5,   bg = self.x)
		self.screen_lbl8 = Label(self.frame2, height= 1, width = 5,   bg = self.w)
		self.screen_lbl9 = Label(self.frame2, height= 1, width = 5,   bg = self.v)
		self.screen_lbl10 = Label(self.frame2, height= 1, width = 5,   bg = self.u)
		self.screen_lbl11 = Label(self.frame2, height= 1, width = 5,   bg = self.t)
		self.screen_lbl12 = Label(self.frame2, height= 1, width = 5,   bg = self.s)
		self.screen_lbl13 = Label(self.frame2, height= 1, width = 5,   bg = self.r)
		self.screen_lbl14 = Label(self.frame2, height= 1, width = 5,   bg = self.q)
		self.screen_lbl15 = Label(self.frame2, height= 1, width = 5,   bg = self.p)
		self.screen_lbl16 = Label(self.frame2, height= 1, width = 5,   bg = self.o)
		self.screen_lbl17 = Label(self.frame2, height= 1, width = 5,   bg = self.n)
		self.screen_lbl18 = Label(self.frame2, height= 1, width = 5,   bg = self.m)
		self.screen_lbl19 = Label(self.frame2, height= 1, width = 5,   bg = self.l)
		self.screen_lbl20 = Label(self.frame2, height= 1, width = 5,   bg = self.k)
		self.screen_lbl21 = Label(self.frame2, height= 1, width = 5,   bg = self.j)
		self.screen_lbl22 = Label(self.frame2, height= 1, width = 5,   bg = self.i)
		self.screen_lbl23 = Label(self.frame2, height= 1, width = 5,   bg = self.h)
		self.screen_lbl24 = Label(self.frame2, height= 1, width = 5,   bg = self.g)
		self.screen_lbl25 = Label(self.frame2, height= 1, width = 5,   bg = self.f)
		self.screen_lbl26 = Label(self.frame2, height= 1, width = 5,   bg = self.e)
		self.screen_lbl27 = Label(self.frame2, height= 1, width = 5,   bg = self.d)
		self.screen_lbl28 = Label(self.frame2, height= 1, width = 5,   bg = self.c)
		self.screen_lbl29 = Label(self.frame2, height= 1, width = 5,   bg = self.b)
		self.screen_lbl30 = Label(self.frame2, height= 1, width = 5,   bg = self.a)
		
	
		
		#Frame 2 grid
		self.img_panel2.grid(row=0, column=3, columnspan=2)
		self.screen_lbl1.grid(row=1, column=3, columnspan=2)
		self.screen_lbl2.grid(row=2, column=3 , columnspan=2)
		self.screen_lbl3.grid(row=3, column=3, columnspan=2)
		self.screen_lbl4.grid(row=4, column=3, columnspan=2)
		self.screen_lbl5.grid(row=5, column=3, columnspan=2)
		self.screen_lbl6.grid(row=6, column=3, columnspan=2)
		self.screen_lbl7.grid(row=7, column=3, columnspan=2)
		self.screen_lbl8.grid(row=8, column=3, columnspan=2)
		self.screen_lbl9.grid(row=9, column=3, columnspan=2)
		self.screen_lbl10.grid(row=10, column=3, columnspan=2)
		self.screen_lbl11.grid(row=11, column=3, columnspan=2)
		self.screen_lbl12.grid(row=12, column=3 , columnspan=2)
		self.screen_lbl13.grid(row=13, column=3, columnspan=2)
		self.screen_lbl14.grid(row=14, column=3, columnspan=2)
		self.screen_lbl15.grid(row=15, column=3, columnspan=2)
		self.screen_lbl16.grid(row=16, column=3, columnspan=2)
		self.screen_lbl17.grid(row=17, column=3, columnspan=2)
		self.screen_lbl18.grid(row=18, column=3, columnspan=2)
		self.screen_lbl19.grid(row=19, column=3, columnspan=2)
		self.screen_lbl20.grid(row=20, column=3, columnspan=2)
		self.screen_lbl21.grid(row=11, column=3, columnspan=2)
		self.screen_lbl22.grid(row=12, column=3 , columnspan=2)
		self.screen_lbl23.grid(row=13, column=3, columnspan=2)
		self.screen_lbl24.grid(row=14, column=3, columnspan=2)
		self.screen_lbl25.grid(row=15, column=3, columnspan=2)
		self.screen_lbl26.grid(row=16, column=3, columnspan=2)
		self.screen_lbl27.grid(row=17, column=3, columnspan=2)
		self.screen_lbl28.grid(row=18, column=3, columnspan=2)
		self.screen_lbl29.grid(row=19, column=3, columnspan=2)
		self.screen_lbl30.grid(row=20, column=3, columnspan=2)
		
		self.rootWindow.geometry('1100x680')
			
			
	#Clears the text input box when you click on it	
	def clear_entry_func(self, event):
		self.enter_name
		self.enter_name.set('')
	
	#Terminate the app. Happens when the user does not want to open an account	
	def end_func(self):
		tkinter.messagebox.showinfo('PIGGY BANK', 'Goodbye!')
		self.rootWindow.destroy()

	#Get the current balance
	def get_balance_func(self):
		balance_list = []
		with open(self.username + '.csv', 'r') as f:
			reader = csv.reader(f, delimiter = ',')
			for column in reader:
				balance_list.append(column[0])
		self.current_balance = balance_list[len(balance_list) - 1]
		f.close()
		return self.current_balance		
		
		
	
	#Displays balance to the user, and writes it to the csv file
	def write_new_balance(self, new_balance, x):
		f = open(self.username + '.csv', 'a')
		if x == 1:
			opening_transaction =  str(new_balance) +', deposit,' + str(self.date) + '\n'
			f.write(opening_transaction)
			f.close()
		elif x == 2:
			opening_transaction = str(new_balance) + ', withdrawal,' + str(self.date) + '\n'
			f.write(opening_transaction)
			f.close()
		self.screen_lbl.delete('1.0', END)
		self.screen_lbl.insert(INSERT, '%s your new balance is: $%s\nYou can type deposit, withdraw, or \nbalance above to continue. Then press \nthe matching button' % (self.username_org, new_balance))
	
	#Gets username and gives the user options. This is the first function the user sees
	def user_choices_func(self):
		self.screen_lbl.delete('1.0', END)
		self.username_org = self.name_entry.get()
		self.username = self.username_org.lower()
		if self.username == "ethan" or self.username == "eden":
			self.check_exists_func()
			self.screen_lbl.insert(INSERT, "Hello %s! \nYou can type deposit, withdraw, or \nbalance above to continue. Then press \nthe matching button" % (self.username_org))
			if os.path.exists(self.username+'_goal.txt'):
				self.add_goal_bar_func()
			else:
				self.frame2.grid_remove()
			self.enter_name
			self.enter_name.set('')				
		else:
			self.screen_lbl.insert(INSERT, "Please Enter a correct Name!")
	
	#Double checks to make sure if the user has an account if not this makes the user one	
	def check_exists_func(self):
		if os.path.exists(self.username + ".csv"):	
			return
		else:
			answer = tkinter.messagebox.askquestion('Alert!!!', 'You don\'t have an account.\nWould you like to create one?')
			if answer == 'yes':
				f = open(self.username + '.csv', 'a')
				top_column = 'balance, transaction type, date\n'
				f.write(top_column)
				opening_transaction = '0, deposit,' + str(self.date) + '\n'
				f.write(opening_transaction)
				f.close()
			else:
				self.end_func()
	
	#Gets balance and displays it for the user	
	def view_balance_func(self):
		self.balance = self.name_entry.get()
		self.balance.lower()
		if self.balance == 'balance':
			current_balance = self.get_balance_func()
			self.screen_lbl.delete('1.0', END)
			self.screen_lbl.insert(INSERT, '%s Your balance is: $%s\nYou can type deposit, withdraw, or \nbalance above to continue. Then press \nthe matching button' % (self.username_org, current_balance))
		else:
			tkinter.messagebox.showinfo('Alert!!!', 'Make sure you spell balance correctly!')
	
	#Deposit function for the user
	def deposit_func(self):	
		current_balance = self.get_balance_func()
		current_balance = float(current_balance)
		deposit_amount = self.name_entry.get()
		deposit_amount = float(deposit_amount)
		new_balance = current_balance + deposit_amount
		self.write_new_balance(new_balance, 1)
		if os.path.exists(self.username+'_goal.txt'):
			self.add_goal_bar_func()
		
	#Withdraw function for the user	
	def withdraw_func(self):
		current_balance = self.get_balance_func()
		current_balance = float(current_balance)
		if current_balance > 1:
			withdraw_amount = self.name_entry.get()
			withdraw_amount = float(withdraw_amount)
			new_balance = current_balance - withdraw_amount
			if new_balance < 0: 
				tkinter.messagebox.showinfo('Alert!!!', 'Can\'t withdraw more money than you have.')
				self.screen_lbl.delete('1.0', END)
				self.screen_lbl.insert(INSERT, '\nYou can type deposit, withdraw, or \nbalance above to continue. Then press \nthe matching button')	
			else:
				self.write_new_balance(new_balance, 2)
		else:
			tkinter.messagebox.showinfo('Alert!!!', 'Can\'t withdraw more money than you have.')
			self.screen_lbl.delete('1.0', END)
			self.screen_lbl.insert(INSERT, '\nYou can type deposit, withdraw, or \nbalance above to continue. Then press \nthe matching button')
		if os.path.exists(self.username+'_goal.txt'):
			self.add_goal_bar_func()
		
	#Functions for getting input from user on what action they would like to perform	
	def what_to_do_func(self):
		user_choice = self.name_entry.get().lower()
		if user_choice == 'deposit':
			self.choice = 1
			self.screen_lbl.delete('1.0', END)
			self.screen_lbl.insert(INSERT, 'Type above how much you would like to \ndeposit and press Go?')
		elif user_choice == 'withdraw':
			self.choice = 2
			self.screen_lbl.delete('1.0', END)
			self.screen_lbl.insert(INSERT, 'Type above how much you would like to \nwithdraw and press Go?')
		else:
			tkinter.messagebox.showinfo('Alert!!!', 'Check your spelling!')
	
	#function that uses Go button to send to the corresponding function	
	def go_func(self):
		if self.choice == 1:
			self.deposit_func()
		elif self.choice == 2:
			self.withdraw_func() 
	
	#Export the balance to a file with filedialog to choose file path	
	def export_balance(self):
		rep = filedialog.asksaveasfilename( filetypes=[("comma separtated values",".csv"),("All files","*")])
		shutil.copyfile(self.username+'.csv', rep)
	
	#Goal functions	
	def create_goal_func(self):
		balance = self.get_balance_func()
		self.goal_popup=popupWindow(self.rootWindow)
		self.rootWindow.wait_window(self.goal_popup.top)
		self.value_amount = self.goal_popup.goal_value
		self.diff_amount = float(self.value_amount)  - float(balance)  
		self.screen_lbl.delete('1.0', END)
		if self.diff_amount > 0:
			with open(self.username+'_goal.txt', 'w') as f:
				f.write(str(self.value_amount))
			self.screen_lbl.insert(INSERT,	"%s your new goal is $%s.\nOnly $%s left to go!\n\nYou can type deposit, withdraw, or \nbalance above to continue. Then press \nthe matching button" % (self.username_org, str(self.value_amount), str(self.diff_amount)))
			self.add_goal_bar_func()
		else:
			self.hit_goal_func()
			
	def hit_goal_func(self):
		self.screen_lbl.insert(INSERT, "You hit your goal!")
		self.end_goal_func()
		
	def view_goal_func(self):
		if os.path.exists(self.username+'_goal.txt'):
			f = open(self.username+'_goal.txt')
			goal_amount = f.read()
			balance = self.get_balance_func()
			left_of_goal = float(goal_amount) - float(balance)
			self.screen_lbl.delete('1.0', END)
			self.screen_lbl.insert(INSERT, '%s your Goal is: $%s\nYou only have $%s to go!\nYou can type deposit, withdraw, or \nbalance above to continue. Then press \nthe matching button.' % (self.username_org, goal_amount, left_of_goal))
		else:
			goal_answer = tkinter.messagebox.askquestion('Alert!!!','You don\'t have a goal.\nWould you like to make one?')
			if goal_answer == 'yes':
				self.create_goal_func()
				
		
	def end_goal_func(self):
		os.remove(self.username+"_goal.txt")
		self.frame2.grid_remove()
		self.screen_lbl.delete('1.0', END)
		self.screen_lbl.insert(INSERT, '%s your Goal is ended.\nYou can type deposit, withdraw, or \nbalance above to continue. Then press \nthe matching button.' % (self.username_org))
		
	
			
root = Tk()
root.geometry('1000x680')
root.resizable(width=False, height=False)
Grid.columnconfigure(root, 0, weight=1)
Grid.rowconfigure(root, 0, weight=1)
bank = BankingApp(root)
root.mainloop()


