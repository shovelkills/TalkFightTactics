import tkinter as tk
import tkinter.ttk as ttk

from numpy.core.defchararray import title


class GUI:
	def __init__(self, rootOfTk):
		self.mainMenuFrame = tk.Frame(rootOfTk)
		rootOfTk.geometry("640x480")
		rootOfTk.resizable(False, False)
		self.mainMenuFrame.grid(row=0, column=0)
		titleLabel = ttk.Label(text='Talk Fight Tactics')
		titleLabel.pack(ipadx=10, ipady=10)
		speakButton = ttk.Button(rootOfTk, text="Start", command=self.talk)

		self.speakFrame = tk.Frame(rootOfTk)
		titleLabel = ttk.Label(text='Talk Fight Tactics')
		titleLabel.pack(ipadx=10, ipady=10)
		modelLabel = ttk.Label(text='Current Mode')
		modelLabel.pack(ipadx=10, ipady=10)
		commandLabel = ttk.Label(text='Current Command')
		commandLabel.pack(ipadx=10, ipady=10)
		closeButton = ttk.Button(rootOfTk, text="End App")

	def talk(self):
		self.mainMenuFrame.grid_remove()
		self.speakFrame.grid()



if __name__ == "__main__":
	root = tk.Tk()
	GUI(root)
	root.title("Talk Fight Tactics")
	root.mainloop()