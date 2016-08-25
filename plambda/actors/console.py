import Tkinter as tk

from plambda.eval.Interpreter import Interpreter

class InputTextArea(tk.Frame):
     def __init__(self, console):
         tk.Frame.__init__(self, borderwidth=1, relief="sunken")
         self.console = console
         self.top = tk.Text(wrap="word", background="white", borderwidth=0, highlightthickness=0)
         self.top_sb = tk.Scrollbar(orient="vertical", borderwidth=1, command=self.top.yview)
         self.top.configure(yscrollcommand=self.top_sb.set)
         self.top_sb.pack(in_=self, side="right", fill="y", expand=False)
         self.top.pack(in_=self, side="left", fill="both", expand=True)

         self.top.bind("<Control-l>", console.evaluate)
         self.top.bind("<Command-l>", console.evaluate)

class OutputTextArea(tk.Frame):
     def __init__(self):
         tk.Frame.__init__(self, borderwidth=1, relief="sunken")
         self.top = tk.Text(wrap="word", background="white", borderwidth=0, highlightthickness=0)
         self.top_sb = tk.Scrollbar(orient="vertical", borderwidth=1, command=self.top.yview)
         self.top.configure(yscrollcommand=self.top_sb.set)
         self.top_sb.pack(in_=self, side="right", fill="y", expand=False)
         self.top.pack(in_=self, side="left", fill="both", expand=True)

         self.top.tag_config("error", background="white", foreground="red")
         self.top.tag_config("ok", background="white", foreground="black")
         
     def append(self, text, tag):
          self.top.insert(tk.END, text, tag)


class FileMenu(tk.Menu):
     def __init__(self, console):
          tk.Menu.__init__(self, console.menubar, tearoff=0)
          self.add_command(label="Open", command=console.tbi)
          self.add_command(label="Reload", command=console.tbi)
          self.add_command(label="Save", command=console.tbi)
          self.add_command(label="Save As", command=console.tbi)
          self.add_command(label="Search", command=console.tbi)
          self.add_command(label="Quit", command=console.tbi)
          console.menubar.add_cascade(label="File", menu=self)


class Console(tk.Tk):

     def __init__(self, interpreter):
        tk.Tk.__init__(self)

        self.title("PLambda Console")
        
        self.interpreter = interpreter
        
        self.console_frame = tk.Frame(borderwidth=1, relief="sunken")

        self.toolbar = tk.Frame()


        self.splitpane = tk.PanedWindow(orient=tk.VERTICAL, sashwidth=10, showhandle=True, sashrelief=tk.RAISED)
        self.splitpane.pack(fill=tk.BOTH, expand=1)

        self.top_frame = InputTextArea(self)
        
        self.splitpane.add(self.top_frame)

        self.bottom_frame = OutputTextArea()
        
        self.splitpane.add(self.bottom_frame)

        self.splitpane.pack(in_=self.console_frame, side="left", fill="both", expand=True)

        self.toolbar.pack(in_=self.console_frame, side="top", fill="x")

        self.menubar =  tk.Menu(self)

        self.filemenu =  FileMenu(self)

        self.config(menu=self.menubar)
        
        self.console_frame.pack(side="bottom", fill="both", expand=True)

        self.load("console.lsp")
        
     def evaluate(self, event):
          self.bottom_frame.append("evaluating...\n", "error")
          self.bottom_frame.append("evaluating...\n", "ok")

     def tbi(self):
          self.bottom_frame.append("To be implemented...\n", "error")

     def load(self, path):
          


        
def launch():
     console=Console(Interpreter())
     console.mainloop()
    
        
if __name__ == "__main__":
     launch()

