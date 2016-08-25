import Tkinter as tk

from plambda.eval.Interpreter import Interpreter

class TextArea(tk.Frame):
     def __init__(self):
         tk.Frame.__init__(self, borderwidth=1, relief="sunken")
         self.top = tk.Text(wrap="word", background="white", borderwidth=0, highlightthickness=0)
         self.top_sb = tk.Scrollbar(orient="vertical", borderwidth=1, command=self.top.yview)
         self.top.configure(yscrollcommand=self.top_sb.set)
         self.top_sb.pack(in_=self, side="right", fill="y", expand=False)
         self.top.pack(in_=self, side="left", fill="both", expand=True)


class Console(tk.Tk):
    def __init__(self, interpreter):
        tk.Tk.__init__(self)

        self.interpreter = interpreter
        
        self.console_frame = tk.Frame(borderwidth=1, relief="sunken")

        self.toolbar = tk.Frame()


        self.splitpane = tk.PanedWindow(orient=tk.VERTICAL, sashwidth=10, showhandle=True, sashrelief=tk.RAISED)
        self.splitpane.pack(fill=tk.BOTH, expand=1)

        self.top_frame = TextArea()
        
        self.splitpane.add(self.top_frame)

        self.bottom_frame = TextArea()
        
        self.splitpane.add(self.bottom_frame)

        self.splitpane.pack(in_=self.console_frame, side="left", fill="both", expand=True)

        self.toolbar.pack(in_=self.console_frame, side="top", fill="x")

        self.console_frame.pack(side="bottom", fill="both", expand=True)

def launch():
     console=Console(Interpreter())
     console.mainloop()
    
        
if __name__ == "__main__":
     launch()

