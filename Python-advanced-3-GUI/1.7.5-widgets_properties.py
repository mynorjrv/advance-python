import tkinter as tk

window = tk.Tk()
label_1 = tk.Label(window, height=3, text="arrow", cursor="arrow")
label_1.pack()
label_2 = tk.Label(window, height=3, text="clock", cursor="boat")
label_2.pack()
label_3 = tk.Label(window, height=3, text="heart", cursor="bogosity")
label_3.pack()
window.mainloop()
