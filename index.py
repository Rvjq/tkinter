import tkinter as tk
import customtkinter as ctk

sizex = 1000
sizey = 1000

ctk.set_appearance_mode("dark")  # Modes: system (default), light, dark
ctk.set_default_color_theme("dark-blue")  # Themes: blue (default), dark-blue, green

app = ctk.CTk()  # create CTk window like you do with the Tk window
app.geometry(str(sizex)+"x"+str(sizey))
app.title("Tic-Tac-Toe")

def button_callback ():
    print("Hey!")

frame_1 = ctk.CTkFrame(master=app, width=300,height=300)
frame_1.pack(pady=50, padx=50, expand=True)

label_1 = ctk.CTkFrame(master=frame_1, width=300, height=10)
label_1.place(x=0,y=100.5)

#Mass creation of buttons to be placed later!
buttons = ['A1','A2','A3','B1','B2','B3','C1','C2','C3']
A1,A2,A3,B1,B2,B3,C1,C2,C3 = [ctk.CTkButton(master=frame_1, command=button_callback, width=100, height=100, text=x, fg_color="transparent") for x in buttons]

#Mass button placement
A1.place(x=0, y=0)
A2.place(x=100, y=0)
A3.place(x=200, y=0)
B1.place(x=0, y=100)
B2.place(x=100, y=100)
B3.place(x=200, y=100)
C1.place(x=0, y=200)
C2.place(x=100, y=200)
C3.place(x=200, y=200)

app.mainloop()