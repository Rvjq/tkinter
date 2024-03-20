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

buttonA1 = ctk.CTkButton(master=frame_1, command=button_callback, width=100, height=100, text="A1", fg_color="transparent")
buttonA2 = ctk.CTkButton(master=frame_1, command=button_callback, width=100, height=100, text="A2", fg_color="transparent")
buttonA3 = ctk.CTkButton(master=frame_1, command=button_callback, width=100, height=100, text="A3", fg_color="transparent")
buttonB1 = ctk.CTkButton(master=frame_1, command=button_callback, width=100, height=100, text="B1", fg_color="transparent")
buttonB2 = ctk.CTkButton(master=frame_1, command=button_callback, width=100, height=100, text="B2", fg_color="transparent")
buttonB3 = ctk.CTkButton(master=frame_1, command=button_callback, width=100, height=100, text="B3", fg_color="transparent")
buttonC1 = ctk.CTkButton(master=frame_1, command=button_callback, width=100, height=100, text="C1", fg_color="transparent")
buttonC2 = ctk.CTkButton(master=frame_1, command=button_callback, width=100, height=100, text="C2", fg_color="transparent")
buttonC3 = ctk.CTkButton(master=frame_1, command=button_callback, width=100, height=100, text="C3", fg_color="transparent")

buttonA1.place(x=0, y=0)
buttonA2.place(x=100, y=0)
buttonA3.place(x=200, y=0)
buttonB1.place(x=0, y=100)
buttonB2.place(x=100, y=100)
buttonB3.place(x=200, y=100)
buttonC1.place(x=0, y=200)
buttonC2.place(x=100, y=200)
buttonC3.place(x=200, y=200)

app.mainloop()