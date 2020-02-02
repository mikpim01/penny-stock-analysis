import tkinter as tk

FONT=('helvetica',13)

class gui:
		
	def clear_entry(self, event):
	    event.widget.delete(0,"end")
	    return None
	def focus_next_widget(self, event):
	    event.widget.tk_focusNext().focus()
	    return("break")

	def entry_widget(self,frame,row,text):

		text = tk.StringVar(value=text)
		self.label = tk.Label(frame, textvariable=text, font=FONT)
		self.label.grid(row=row, sticky='E')
		self.entry = tk.Entry(frame)
		self.entry.grid(row=row,column=1)
		self.entry.bind("<Tab>",self.focus_next_widget)

class command:
	def cancel_command(self):
		print("=-= WARNING =-=\n\ncancel_command() not implemented yet\n")
		return None

	def remove_stock_record():
		print("=-= WARNING =-=\n\nremove_stock_record() not implemented yet\n")
		return None