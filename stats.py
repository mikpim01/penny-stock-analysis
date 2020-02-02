import numpy as np
from helper import *
import tkinter as tk



#history = np.genfromtxt('history_samples/history.csv',delimiter=',')
"""
history.csv entry:
		[ticker,
		quarter,
		year,
		sector,
		index,
		float_level,
		daily_volume,
		my_entry,
		my_exit,
		perfect_entry,
		perfect_exit,
		trade_ID]
"""
# cancel_command = False

class rem_GUI(gui,command):
	def __init__(self,master):
		master.title("record")
		master.geometry("150x100+500+250")
		self.label_trade_ID = self.entry_widget(frame=master,row=0,text='trade ID:')
		self.button_remove = tk.Button(master,command=self.remove_stock_record,text='remove',font=FONT)
		self.button_remove.grid(row=1,column=0, columnspan=2,pady=5)


class add_GUI(gui,command):
	def __init__(self, master):
		self.master = master
		master.title("record")
		master.geometry("250x450+500+250")

		self.title_frame = tk.Frame(self.master)
		self.title_frame.grid(row=0,sticky='N', pady=30)
		self.frame = tk.Frame(self.master)
		self.frame.grid(row=1)
		self.button_frame = tk.Frame(self.master)
		self.button_frame.grid(row=2,pady=10)

		self.label_title = tk.Label(self.title_frame,text="ADD RECORD:",font=FONT)
		self.label_title.pack(fill=tk.BOTH)

		self.label_ticker = tk.Label(self.frame, text='ticker:', font=FONT)
		self.label_ticker.grid(row=0, sticky='E')
		self.entry_ticker = tk.Entry(self.frame)
		self.entry_ticker.grid(row=0,column=1)
		self.entry_ticker.focus_set()

		self.label_quarter = tk.Label(self.frame, text='quarter:', font=FONT)
		self.label_quarter.grid(row=1, sticky='E')
		self.entry_quarter = tk.Entry(self.frame)
		self.entry_quarter.grid(row=1,column=1)
		self.entry_quarter.bind("<Tab>",self.focus_next_widget)

		self.label_year = tk.Label(self.frame, text='year:', font=FONT)
		self.label_year.grid(row=2, sticky='E')
		self.entry_year = tk.Entry(self.frame)
		self.entry_year.grid(row=2,column=1)
		self.entry_year.bind("<Tab>",self.focus_next_widget)

		self.label_sector = tk.Label(self.frame, text='sector:', font=FONT)
		self.label_sector.grid(row=3, sticky='E')
		self.entry_sector = tk.Entry(self.frame)
		self.entry_sector.grid(row=3,column=1)
		self.entry_sector.bind("<Tab>",self.focus_next_widget)

		self.label_index = tk.Label(self.frame, text='index:', font=FONT)
		self.label_index.grid(row=4, sticky='E')
		self.entry_index = tk.Entry(self.frame)
		self.entry_index.grid(row=4,column=1)
		self.entry_index.bind("<Tab>",self.focus_next_widget)

		self.label_float_level = tk.Label(self.frame, text='float:', font=FONT)
		self.label_float_level.grid(row=5, sticky='E')
		self.entry_float_level = tk.Entry(self.frame)
		self.entry_float_level.grid(row=5,column=1)
		self.entry_float_level.bind("<Tab>",self.focus_next_widget)

		self.label_daily_volume = tk.Label(self.frame, text='daily volume', font=FONT)
		self.label_daily_volume.grid(row=6, sticky='E')
		self.entry_daily_volume = tk.Entry(self.frame)
		self.entry_daily_volume.grid(row=6,column=1)
		self.entry_daily_volume.bind("<Tab>",self.focus_next_widget)

		self.label_my_entry = tk.Label(self.frame, text='my entry:', font=FONT)
		self.label_my_entry.grid(row=7, sticky='E')
		self.entry_my_entry = tk.Entry(self.frame)
		self.entry_my_entry.grid(row=7,column=1)
		self.entry_my_entry.bind("<Tab>",self.focus_next_widget)

		self.label_my_exit = tk.Label(self.frame, text='my exit:', font=FONT)
		self.label_my_exit.grid(row=8, sticky='E')
		self.entry_my_exit = tk.Entry(self.frame)
		self.entry_my_exit.grid(row=8,column=1)
		self.entry_my_exit.bind("<Tab>",self.focus_next_widget)

		self.label_perfect_entry = tk.Label(self.frame, text='perfect entry:', font=FONT)
		self.label_perfect_entry.grid(row=9, sticky='E')
		self.entry_perfect_entry = tk.Entry(self.frame)
		self.entry_perfect_entry.grid(row=9,column=1)
		self.entry_perfect_entry.bind("<Tab>",self.focus_next_widget)

		self.label_perfect_exit = tk.Label(self.frame, text='perfect exit:', font=FONT)
		self.label_perfect_exit.grid(row=10, sticky='E')
		self.entry_perfect_exit = tk.Entry(self.frame)
		self.entry_perfect_exit.grid(row=10,column=1)
		self.entry_perfect_exit.bind("<Tab>",self.focus_next_widget)

		self.label_trade_ID = tk.Label(self.frame, text='trade ID:', font=FONT)
		self.label_trade_ID.grid(row=11, sticky='E')
		self.entry_trade_ID = tk.Entry(self.frame)
		self.entry_trade_ID.grid(row=11,column=1)
		self.entry_trade_ID.bind("<Tab>",self.focus_next_widget)

		self.button_cancel = tk.Button(self.button_frame, command=self.master.destroy, text="cancel", font=FONT)
		self.button_cancel.grid(row=12)
		self.button_add_record = tk.Button(self.button_frame, command=self.add_stock_record, text="add record", font=FONT)
		self.button_add_record.grid(row=12, column=1)
		
	def add_stock_record(self):

		ticker = self.entry_ticker.get()
		quarter = self.entry_quarter.get()
		year = self.entry_year.get()
		sector = self.entry_sector.get()
		index = self.entry_index.get()
		float_level = self.entry_float_level.get()
		daily_volume = self.entry_daily_volume.get()
		my_entry = self.entry_my_entry.get()
		my_exit = self.entry_my_exit.get()
		perfect_entry = self.entry_perfect_entry.get()
		perfect_exit = self.entry_perfect_exit.get()
		trade_ID = self.entry_trade_ID.get()
		
		print("\n=-= Adding record data to history =-=\n")


def valid(string,description=None):

	global cancel_command

	if string == "cancel" or string == "c":
		cancel_command = True
	else:
		while string == "":
			string = input("\nNo input giself.ven. Try again:\t")


		if description == "quarter":

			while string not in ['Q1','Q2','Q3','Q4','q1','q2','q3','q4']:
				string = input("\ninvalid date given. Try again:\t")
			if string in ['q1','q2','q3','q4']:
				string.replace('q','Q')

		elif description == "y/n":

			while string not in ["yes", "no", 'y', 'n']:
				string = input("\ninvalid answer. type y/n :\t")


	return string

def execute_command(text_in):
	if text_in == "quit" or text_in == 'q':
		print("\n=-= Closing Application =-=\n")
		exit()
	else:
		if text_in == "add" or text_in == 'a':
			root = tk.Tk()
			gui = add_GUI(root)
			root.mainloop()
		elif text_in == "rem" or text_in == 'r':
			root = tk.Tk()
			gui = rem_GUI(root)
			root.mainloop()
		elif text_in == "help" or text_in == 'h':
			print("\nadd\nquit\nrem\n")


def main():
	while True:
		# Get input
		# Act accordingly
		execute_command(str(input("\nEnter command:\t")))

if __name__ == '__main__':
	main()