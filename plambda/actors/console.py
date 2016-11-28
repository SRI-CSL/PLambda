""" The plambda actor console for debugging running actors.
"""

import os
import sys
import traceback


#python 2 vs python 3. if there is a python 4 I quit.
try:
    import Tkinter as tk
    import tkFileDialog as fdialog
except ImportError:
    import tkinter as tk
    import tkinter.filedialog as fdialog


from ..eval.Interpreter import Interpreter

from ..visitor.Parser import parseFromString

from ..eval.PLambdaException import PLambdaException

from ..util.StringBuffer import StringBuffer


class InputTextArea(tk.Frame):

    def __init__(self, console):
        tk.Frame.__init__(self, borderwidth=1, relief="sunken")
        self.console = console
        self.text = tk.Text(wrap=tk.NONE, background="white", borderwidth=0, highlightthickness=0)
        self.text_sb = tk.Scrollbar(orient="vertical", borderwidth=1, command=self.text.yview)
        self.text.configure(yscrollcommand=self.text_sb.set)
        self.text_sb.pack(in_=self, side="right", fill="y", expand=False)
        self.text.pack(in_=self, side="left", fill="both", expand=True)
        self.text.bind("<Control-b>", lambda e: console.evaluate(self.buffer()))
        self.text.bind("<Command-b>", lambda e: console.evaluate(self.buffer()))
        self.text.bind("<Control-l>", lambda e: console.evaluate(self.line()))
        self.text.bind("<Command-l>", lambda e: console.evaluate(self.line()))
        self.text.bind("<Control-e>", lambda e: console.evaluate(self.selected()))
        self.text.bind("<Command-e>", lambda e: console.evaluate(self.selected()))
        self.text.bind("<Control-s>", lambda e: console.save())
        self.text.bind("<Command-s>", lambda e: console.save())
        self.text.bind("<Control-r>", lambda e: console.load(console.path))
        self.text.bind("<Command-r>", lambda e: console.load(console.path))


    def selected(self):
        if self.text.tag_ranges(tk.SEL):
            return self.text.get(tk.SEL_FIRST, tk.SEL_LAST)
        else:
            return None

    def line(self):
        return self.text.get("insert linestart", "insert lineend")

    def buffer(self):
        return self.text.get(1.0, tk.END)


class OutputTextArea(tk.Frame):
    def __init__(self):
        tk.Frame.__init__(self, borderwidth=1, relief="sunken")
        self.text = tk.Text(wrap=tk.NONE,
                            background="white",
                            borderwidth=0,
                            highlightthickness=0,
                            state=tk.DISABLED)
        self.text_sb = tk.Scrollbar(orient="vertical", borderwidth=1, command=self.text.yview)
        self.text.configure(yscrollcommand=self.text_sb.set)
        self.text_sb.pack(in_=self, side="right", fill="y", expand=False)
        self.text.pack(in_=self, side="left", fill="both", expand=True)

        self.text.tag_config("error", background="white", foreground="red")
        self.text.tag_config("ok", background="white", foreground="black")

    def append(self, text, tag):
        self.text.config(state=tk.NORMAL)
        self.text.insert(tk.END, text, tag)
        self.text.config(state=tk.DISABLED)
        self.text.see(tk.END)


class FileMenu(tk.Menu):
    def __init__(self, console):
        tk.Menu.__init__(self, console.menubar, tearoff=0)
        self.add_command(label="Open", command=console.open, accelerator="Command-O")
        self.add_command(label="Reload",
                         command=lambda: console.load(console.path),
                         accelerator="Command-R")
        self.add_command(label="Save", command=console.save, accelerator="Command-S")
        self.add_command(label="Save As", command=console.saveas, accelerator="Shift-Command-W")
        self.add_command(label="Quit", command=sys.exit, accelerator="Command-Q")
        console.menubar.add_cascade(label="File", menu=self)

class EvaluateMenu(tk.Menu):
    def __init__(self, console):
        tk.Menu.__init__(self, console.menubar, tearoff=0)
        self.add_command(label="Buffer",
                         command=lambda: console.evaluate(console.top_frame.buffer(), None),
                         accelerator="Command-B")
        self.add_command(label="Selected",
                         command=lambda: console.evaluate(console.top_frame.selected(), None),
                         accelerator="Command-E")
        self.add_command(label="Line",
                         command=lambda: console.evaluate(console.top_frame.line(), None),
                         accelerator="Command-L")
        console.menubar.add_cascade(label="Evaluate", menu=self)

class ViewMenu(tk.Menu):
    def __init__(self, console):
        tk.Menu.__init__(self, console.menubar, tearoff=0)
        self.add_command(label="Definitions", command=console.definitions, accelerator="Command-D")
        self.add_command(label="UIDs", command=console.uids, accelerator="Command-U")
        self.add_command(label="Code", command=console.code)
        console.menubar.add_cascade(label="View", menu=self)


class Console(tk.Tk):

    def __init__(self, interpreter):
        tk.Tk.__init__(self)
        self.title("PLambda Console")
        self.interpreter = interpreter
        self.console_frame = tk.Frame(borderwidth=1, relief="sunken")
        self.toolbar = tk.Frame()
        self.splitpane = tk.PanedWindow(orient=tk.VERTICAL,
                                        sashwidth=10,
                                        showhandle=True,
                                        sashrelief=tk.RAISED)
        self.splitpane.pack(fill=tk.BOTH, expand=1)
        self.top_frame = InputTextArea(self)
        self.splitpane.add(self.top_frame)
        self.bottom_frame = OutputTextArea()
        self.splitpane.add(self.bottom_frame)
        self.splitpane.pack(in_=self.console_frame, side="left", fill="both", expand=True)
        self.toolbar.pack(in_=self.console_frame, side="top", fill="x")
        self.menubar = tk.Menu(self)
        self.filemenu = FileMenu(self)
        self.evaluatemenu = EvaluateMenu(self)
        self.viewmenu = ViewMenu(self)
        self.config(menu=self.menubar)
        self.console_frame.pack(side="bottom", fill="both", expand=True)
        self.load("console.lsp")

    def evaluate(self, text):
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
                        self.bottom_frame.append('\n', "ok")
            except PLambdaException as e:
                self.bottom_frame.append(str(e), "error")
                self.bottom_frame.append('\n', "ok")
            except Exception as e:
                sys.stderr.write('PLambda.rep Exception: {0}\n'.format(str(e)))
                traceback.print_exc(file=sys.stderr)
                self.bottom_frame.append('\n', "ok")

    def tbi(self):
        self.bottom_frame.append("To be implemented...\n", "error")

    def load(self, fname):
        if not fname:
            return
        path = os.path.abspath(fname)
        if os.path.exists(path):
            with open(path, "r") as fp:
                self.top_frame.text.delete(1.0, tk.END)
                for line  in fp.readlines():
                    self.top_frame.text.insert(tk.END, line)
                    self.path = path
                    self.bottom_frame.append("{0} loaded\n".format(path), "ok")
        else:
            self.bottom_frame.append("{0} not found\n".format(path), "error")

    def save(self, path=None):
        if path is None:
            path = self.path
        if path is None:
            self.bottom_frame.append("No file set, use 'Save as'\n", "error")
        else:
            with open(path, 'w') as fp:
                fp.write(self.top_frame.buffer())
                self.bottom_frame.append("{0} saved\n".format(path), "ok")

    def open(self):
        path = fdialog.askopenfilename(initialdir=os.getcwd())
        if path:
            self.load(path)

    def saveas(self):
        path = fdialog.asksaveasfilename(initialdir=os.getcwd())
        if path:
            self.save(path)

    def uids(self):
        self.intdump(self.interpreter.showUIDs)

    def definitions(self):
        self.intdump(self.interpreter.showDefinitions)

    def code(self):
        self.intdump(self.interpreter.showCode)

    def intdump(self, func):
        self.bottom_frame.append(str(func(StringBuffer())), "ok")


def launch():
    console = Console(Interpreter())
    console.mainloop()


if __name__ == "__main__":
    launch()
