import tkinter as tk

window = tk.Tk()

window.geometry("720x500")

inputBox = tk.Entry(window, width=25).grid(row=0, column=0)

encodeButton = tk.Button(window, text="Encode", ).grid(row=1, column=0)
decodeButton = tk.Button(window, text="Decode", ).grid(row=1, column=1)

window.mainloop()