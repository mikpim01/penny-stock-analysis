import numpy as np
from helper import *
import tkinter as tk
import pandas as pd


history = pd.read_csv('history_samples/history.csv',sep=',',header=0,skip_blank_lines=True)
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
		my_PL,
		perfect_entry,
		perfect_exit,
		perfect_PL,
		trade_ID]
"""
# cancel_command = False

class rem_GUI(gui,command):
	def __init__(self,master):
		master.title("record")
		self.master.geometry("150x100+1300+100")
		self.label_trade_ID = self.entry_widget(frame=master,row=0,text='trade ID:')
		self.button_remove = tk.Button(master,command=self.remove_stock_record,text='remove',font=FONT)
		self.button_remove.grid(row=1,column=0, columnspan=2,pady=5,padx=5)


class add_GUI(gui,command):
	def __init__(self, master):
		self.master = master
		master.title("record")
		master.geometry("250x500+500+250")

		self.title_frame = tk.Frame(self.master)
		self.title_frame.grid(row=0,sticky='N', pady=30)
		self.frame = tk.Frame(self.master)
		self.frame.grid(row=1)
		self.button_frame = tk.Frame(self.master)
		self.button_frame.grid(row=2,pady=10)

		self.label_title = tk.Label(self.title_frame,text="ADD RECORD:",font=('helvetica',17,'bold'))
		self.label_title.pack(fill=tk.BOTH)

		self.label_ticker, self.entry_ticker = self.entry_widget(self.frame, row=0, text='ticker:')
		self.entry_ticker.focus_set()

		self.label_quarter, self.entry_quarter = self.entry_widget(self.frame, text='quarter:', row=1)
		self.label_year, self.entry_year = self.entry_widget(self.frame, text='year:', row=2)
		self.label_sector, self.entry_sector = self.entry_widget(self.frame, text='sector:', row=3)
		self.label_index, self.entry_index = self.entry_widget(self.frame, text='index:', row=4)
		self.label_float_level, self.entry_float_level = self.entry_widget(self.frame, text='float:', row=5)
		self.label_daily_volume, self.entry_daily_volume = self.entry_widget(self.frame, text='daily volume', row=6)
		self.label_my_entry, self.entry_my_entry = self.entry_widget(self.frame, text='my entry:', row=7)
		self.label_my_exit, self.entry_my_exit = self.entry_widget(self.frame, text='my exit:', row=8)
		self.label_my_PL, self.entry_my_PL = self.entry_widget(self.frame, text='my %P/L:', row=9)
		self.label_perfect_entry, self.entry_perfect_entry = self.entry_widget(self.frame, text='perfect entry:', row=10)
		self.label_perfect_exit, self.entry_perfect_exit = self.entry_widget(self.frame, text='perfect exit:', row=11)
		self.label_perfect_PL, self.entry_perfect_PL = self.entry_widget(self.frame, text='Perfect %P/L:', row=12)
		self.label_trade_ID, self.entry_trade_ID = self.entry_widget(self.frame, text='trade ID:', row=13)

		self.button_cancel = tk.Button(self.button_frame, command=self.master.destroy, text="cancel", font=FONT)
		self.button_cancel.grid(row=0,column=0)
		self.button_add_record = tk.Button(self.button_frame, command=self.add_stock_record, text="add record", font=FONT)
		self.button_add_record.grid(row=0, column=1)
		
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
		
		history.append(ticker,quarter,year,sector,index,float_level,daily_volume,my_entry,my_exit,perfect_entry,perfect_exit,trade_ID)
		print("\n=-= Adding record data to history =-=\n")
		print(history)


def execute_command(text_in):
	if text_in == "quit" or text_in == 'q':
		print("\n=-= Closing Application =-=\n")
		exit()
	elif text_in == "add" or text_in == 'a':
		root = tk.Tk()
		gui = add_GUI(root)
		root.mainloop()
	elif text_in == "rem" or text_in == 'r':
		root = tk.Tk()
		gui = rem_GUI(root)
		root.mainloop()
	elif text_in == "read" or text_in == 'rd':
		print(history)
	elif text_in == "help" or text_in == 'h':
		print("\nadd\nquit\nrem\nread\n")
	else:
		print("\n=-=INVALID COMMAND=-=\n")

def main():
	while True:
		# Get input
		# Act accordingly
		execute_command(str(input("\nEnter command:\t")))

if __name__ == '__main__':
	main()