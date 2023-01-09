import tkinter as tk

class MainApplication(tk.Frame):
    def __init__(self, parent, *args, **kwargs):
        tk.Frame.__init__(self, parent, *args, **kwargs)

        self.var = tk.IntVar()
        tk.Label(self, textvariable=self.var).pack()
        
        self.callback()     #This starts the recursion loop
    
    def __del__(self):
        self.after_cancel(self.after_id)

    def callback(self):
        self.var.set(self.var.get()+1)
        self.after_id = self.after(500, self.callback)