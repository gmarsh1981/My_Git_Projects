from tkinter import *
import subprocess, sys
import tkinter.messagebox
from tkinter import filedialog
import os
import PS_Script as ps 
import csv

class FolderSizes(object):
	def __init__(self, rootWindow):
		self.rootWindow  = rootWindow
		self.rootWindow.title('Check Folder Sizes')
			
		self.filePath_var = StringVar()
		self.filePath_var.set("ENTER FILE PATH:")
		
				
		#Frame
		self.frame = Frame(self.rootWindow)
		self.frame.grid(row=0, column=0, sticky=N+W+S+E)
		#Frame1
		self.frame1 = Frame(self.rootWindow)
		self.frame1.grid(row=0, column=4, sticky=N+W+S+E)
		
		for i in range(5):
			Grid.rowconfigure(self.frame, i, weight=1)
		for i in range(3):
			Grid.columnconfigure(self.frame, i , weight=1)
		
		self.v = IntVar()
		
		#Elements
		self.username_entry_textbox = Text(self.frame, height=0, width=0, font = ('Consolas','16'), fg='green', bg='black')
		self.username_entry_textbox.insert(INSERT, 'ENTER USERNAMES:')
		self.username_entry_textbox.bind('<Button-1>', self.clear_entry_func)
		self.username_entry_scroll = Scrollbar(self.frame, command=self.username_entry_textbox.yview)
		self.username_entry_textbox['yscrollcommand'] = self.username_entry_scroll.set
		
		self.filePath_entry = Entry(self.frame, textvariable = self.filePath_var, font = ('Consolas','16'), fg='green', bg='black')
		self. filePath_entry.bind('<Button-1>', self.clear_filePath_entry_func)
		
		self.go_btn = Button(self.frame, text='GO', font=('Arial Rounded MT Bold','24'), command=self.get_data_func)
		
		self.RadTB = Radiobutton(self.frame1, text = 'TB', variable = self.v, value = 100)
		self.RadGB = Radiobutton(self.frame1, text = 'GB', variable = self.v, value = 10)
		self.RadMB = Radiobutton(self.frame1, text = 'MB', variable = self.v, value = 1)
		
		self.result_textbox = Text(self.frame, height=0, width=0, font = ('Consolas','16'), fg='green', bg='black')
		self.result_scroll = Scrollbar(self.frame, command=self.result_textbox.yview)
		self.result_textbox['yscrollcommand'] = self.result_scroll.set
		
		#Grid
		self.username_entry_textbox.grid(row=0, columnspan=2, sticky=N+S+E+W)
		self.username_entry_scroll.grid(row=0, column=2, sticky=N+S)
		self.filePath_entry.grid(row=1, columnspan=2, sticky=N+S+E+W)
		self.go_btn.grid(row=2, columnspan=2, sticky=E+W)
		self.RadTB.grid(row=0, columnspan=2, sticky=E+W)
		self.RadGB.grid(row=1, columnspan=2, sticky=E+W)
		self.RadMB.grid(row=2, columnspan=2, sticky=E+W)
		self.result_textbox.grid(row = 4, columnspan=2, sticky=N+S+E+W)
		self.result_scroll.grid(row=4, column=2, sticky=N+S)
		
		
	def clear_entry_func(self, event):
		self.username_entry_textbox.delete('1.0', END)
		
	def clear_filePath_entry_func(self, event):
		self.filePath_var.set("")
		self.filePath = filedialog.askdirectory()
		self.filePath = self.filePath.replace('/', '\\')
		self.filePath_var.set(self.filePath)
		j = open('filepath.txt', 'w')
		j.write(self.filePath)
		j.close
		
		
	def get_data_func(self):
		self.result_textbox.insert(INSERT, 'Getting infromation...')
		self.username = self.username_entry_textbox.get('1.0', END)
		if self.username == '' or self.filePath == '':
			tkinter.messagebox.showinfo('Alert!!!', 'Make sure you fill out both username and folder loaction')
		else:
			username_list = self.username.split()
			f = open('usernames.csv', 'w')
			for name in username_list:
				info = 'Ludwigsd\\' +name+ ',\n'
				f.write(info)
			f.close()
		self.radio = self.v.get()	
		ps.get_PS_data_func(self.radio)
		self.display_result_func()
	
		
	def display_result_func(self):
		f = open('Foldersize.csv', 'r')
		results = csv.reader(f, delimiter = ',')
		results_list = []
		for row in results:
			results_list.append(row)
		results_list.remove(results_list[0])	
		self.result_textbox.delete('1.0', END)
		for i in range(len(results_list)):
			result = ' '.join(results_list[i])
			if self.radio == 1:
				self.result_textbox.insert(INSERT, '%sMB\n' % (result))
			elif self.radio == 10:
				self.result_textbox.insert(INSERT, '%sGB\n' % (result))
			elif self.radio == 100:
				self.result_textbox.insert(INSERT, '%sTB\n' % (result))
		f.close()		
		self.cleanup_func()

	def cleanup_func(self):
		os.remove("Foldersize.csv")
		os.remove("usernames.csv")
		os.remove("filepath.txt")
		
root = Tk()
root.geometry('800x600')
Grid.columnconfigure(root, 0, weight=1)
Grid.rowconfigure(root, 0, weight=1)
root.resizable(height=True, width=True)
folders = FolderSizes(root)
root = mainloop()


