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
		label = tk.Label(frame, textvariable=text, font=FONT)
		label.grid(row=row, sticky='E')
		entry = tk.Entry(frame)
		entry.grid(row=row,column=1)
		entry.bind("<Tab>, <Return>",self.focus_next_widget)
		# entry.bind("<Return>", self.focus_next_widget)
		return label, entry

class command:
	def cancel_command(self):
		print("=-= WARNING =-=\n\ncancel_command() not implemented yet\n")
		return None

	def remove_stock_record(self):
		print("=-= WARNING =-=\n\nremove_stock_record() not implemented yet\n")
		return None