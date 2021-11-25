import dataStructures
import tkinter as tk


#constants
winDim = (500,600)
mrgin = 25


#predefined functions
def find_button_command():
	global data_entry
	print(data_entry.get())

#main
window = tk.Tk()
window.geometry(f'{winDim[0]}x{winDim[1]}')


#widgets
data_entry = tk.Entry()
title = tk.Label(text="Data Structures !")
find_button = tk.Button(window, text="Get the structures...", command=find_button_command) 


#frames
result_frames = [tk.Frame(master=window, bg="white",width=150, height=150) for _ in range(3)]
frame_labels = [tk.Label(master=frame,text=txt) for txt,frame in zip(("Queue","Stack","List"),result_frames)]

#widget placement
title.place(x=winDim[0]//3, y=mrgin)
data_entry.place(x=mrgin, y=winDim[1]//6)
find_button.place(x=mrgin, y=winDim[1]//4)
[frame.place(x=winDim[0]-(150 + mrgin), y=offset) for frame,offset in zip(result_frames,[0 + mrgin, 200 + mrgin,400 + mrgin])]
[frame_label.place(x=0, y=0) for frame_label in frame_labels]


window.mainloop()