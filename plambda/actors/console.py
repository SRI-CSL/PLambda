import Tkinter as tk

import os, sys, traceback

from plambda.eval.Interpreter import Interpreter

from plambda.visitor.Parser import parseFromString

from plambda.eval.PLambdaException import PLambdaException


class InputTextArea(tk.Frame):
     def __init__(self, console):
         tk.Frame.__init__(self, borderwidth=1, relief="sunken")
         self.console = console
         self.top = tk.Text(wrap=tk.NONE, background="white", borderwidth=0, highlightthickness=0)
         self.top_sb = tk.Scrollbar(orient="vertical", borderwidth=1, command=self.top.yview)
         self.top.configure(yscrollcommand=self.top_sb.set)
         self.top_sb.pack(in_=self, side="right", fill="y", expand=False)
         self.top.pack(in_=self, side="left", fill="both", expand=True)

         self.top.bind("<Control-b>", lambda e: console.evaluate(self.buffer(), e))
         self.top.bind("<Command-b>", lambda e: console.evaluate(self.buffer(), e))

         self.top.bind("<Control-l>", lambda e: console.evaluate(self.line(), e))
         self.top.bind("<Command-l>", lambda e: console.evaluate(self.line(), e))

         self.top.bind("<Control-e>", lambda e: console.evaluate(self.selected(), e))
         self.top.bind("<Command-e>", lambda e: console.evaluate(self.selected(), e))

     def selected(self):
          if self.top.tag_ranges(tk.SEL):
               return self.top.get(tk.SEL_FIRST, tk.SEL_LAST)
          else:
               None

     def line(self):
          return self.top.get("insert linestart", "insert lineend")

     def buffer(self):
          return self.top.get(1.0, tk.END)

          
class OutputTextArea(tk.Frame):
     def __init__(self):
         tk.Frame.__init__(self, borderwidth=1, relief="sunken")
         self.top = tk.Text(wrap=tk.NONE, background="white", borderwidth=0, highlightthickness=0, state=tk.DISABLED)
         self.top_sb = tk.Scrollbar(orient="vertical", borderwidth=1, command=self.top.yview)
         self.top.configure(yscrollcommand=self.top_sb.set)
         self.top_sb.pack(in_=self, side="right", fill="y", expand=False)
         self.top.pack(in_=self, side="left", fill="both", expand=True)

         self.top.tag_config("error", background="white", foreground="red")
         self.top.tag_config("ok", background="white", foreground="black")
         
     def append(self, text, tag):
          self.top.config(state=tk.NORMAL)
          self.top.insert(tk.END, text, tag)
          self.top.config(state=tk.DISABLED)


class FileMenu(tk.Menu):
     def __init__(self, console):
          tk.Menu.__init__(self, console.menubar, tearoff=0)
          self.add_command(label="Open", command=console.tbi, accelerator="Command-O")
          self.add_command(label="Reload", command=console.tbi, accelerator="Command-R")
          self.add_command(label="Save", command=console.tbi, accelerator="Command-S")
          self.add_command(label="Save As", command=console.tbi, accelerator="Shift-Command-W")
          self.add_command(label="Search", command=console.tbi, accelerator="Command-F")
          self.add_command(label="Quit", command=console.tbi, accelerator="Command-W")
          console.menubar.add_cascade(label="File", menu=self)

class EditMenu(tk.Menu):
     def __init__(self, console):
          tk.Menu.__init__(self, console.menubar, tearoff=0)
          self.add_command(label="Cut", command=console.tbi, accelerator="Command-X")
          self.add_command(label="Copy", command=console.tbi, accelerator="Command-C")
          self.add_command(label="Paste", command=console.tbi, accelerator="Command-V")
          console.menubar.add_cascade(label="Edit", menu=self)

class EvaluateMenu(tk.Menu):
     def __init__(self, console):
          tk.Menu.__init__(self, console.menubar, tearoff=0)
          self.add_command(label="Buffer",
                           command=lambda : console.evaluate(console.top_frame.buffer(), None),
                           accelerator="Command-B")
          self.add_command(label="Selected",
                           command=lambda : console.evaluate(console.top_frame.selected(), None),
                           accelerator="Command-E")
          self.add_command(label="Line",
                           command=lambda : console.evaluate(console.top_frame.line(), None),
                           accelerator="Command-L")
          console.menubar.add_cascade(label="Evaluate", menu=self)


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

        self.editmenu =  EditMenu(self)

        self.evaluatemenu =  EvaluateMenu(self)

        self.config(menu=self.menubar)
        
        self.console_frame.pack(side="bottom", fill="both", expand=True)

        self.load("console.lsp")
        
     def evaluate(self, text, event):
          if self.interpreter is None:
               self.bottom_frame.append("Interpreter is None\n", "error")
          elif text is None:
               self.bottom_frame.append("Text to evaluate is None\n", "error")
          else:
               try:
                    code = parseFromString(text)
                    for c in code:
                         if c is not None:
                              value = self.interpreter.evaluate(c)
                              self.bottom_frame.append(str(value), "ok")
               except PLambdaException as e:
                    self.bottom_frame.append(str(e), "error")
               except Exception as e:
                    print 'PLambda.rep Exception: ', e
                    traceback.print_exc(file=sys.stderr)
               self.bottom_frame.append('\n', "ok")

     def tbi(self):
          self.bottom_frame.append("To be implemented...\n", "error")

     def load(self, fname):
          path = os.path.abspath(fname)
          if os.path.exists(path):
               with open (path, "r") as fp:
                   for line  in fp.readlines():
                        self.top_frame.top.insert(tk.END, line)
               self.path = path
               self.bottom_frame.append("{0} loaded\n".format(path), "ok")
          else:
               self.bottom_frame.append("{0} not found\n".format(path), "error")
               


        
def launch():
     console=Console(Interpreter())
     console.mainloop()
    
        
if __name__ == "__main__":
     launch()

