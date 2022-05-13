from tkinter import *
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg, NavigationToolbar2Tk


canvas_width = 700
canvas_height = 500
brush_size = 3
color = "black"

def paint (event):
    global brush_size
    global color
    x1 = event.x - brush_size
    x2 = event.x + brush_size
    y1 = event.y - brush_size
    y2 = event.y + brush_size
    w.create_oval(x1, y1, x2, y2,
                  fill=color, outline=color)

def medraw(even):
	w.create_line([[0,0],[900,900]], fill = "blue", width=3)
	w.create_polygon([300,20],[400,75],[650,200], fill = "orange")
	w.create_rectangle (150,250,220,320, fill = "pink")
		
def mypolcode():
	x = np.linspace(0,2 * np.pi)
	fig = plt.figure (facecolor = "cyan")
	ax = fig.add_subplot(111)
	#ax.plot(x, )
	plt.xlabel("x-ось абсцисс")
	plt.ylabel("y-ординат")
	return fig

def brish_size_change (new_size):
    global brush_size
    brush_size = new_size

def color_change (new_color):
    global color
    color = new_color

root = Tk()
root.title ("Рисовалка")
frm = Frame(root)
fgr = myplotcode()
canvasAgg = FigureCanvasTkAgg(fgr, master = frm)
canvasAgg.draw()

w = canvasAgg.get_tk_widget()
w.pack(fill=BOTH, expand=1)
frm.pack(fill=BOTH, expand=1)


# w = Canvas (root,
            # width = canvas_width,
            # height = canvas_height,
            # bg = "white")
w.bind("<Configure>", mydraw,"+")
red_btn = Button (text = "Красный", width=10, command=lambda : color_change ("red"))
blue_btn = Button (text = "Голубенький", width=10, command=lambda : color_change ("blue"))
black_btn = Button (text = "Черный", width=10, command=lambda : color_change ("black"))
white_btn = Button (text = "Ластик", width=10, command=lambda : color_change ("white"))

clear_btn = Button (text = "Удалить все", width=10, command=lambda : w.delete("all"))

w.grid(row = 2, column = 0,
       columnspan = 7, padx = 5,
       pady = 5, sticky = E + W + S + N)
w.columnconfigure(6, weight = 1)
w.rowconfigure (2, weight = 1)



toolbar = NavigationToolbar2Tk(canvasAgg, root)
toolbar.update()

root.mainloop()
