import tkinter as tk
import customtkinter as ctk

sizex = 1000
sizey = 1000

ctk.set_appearance_mode("dark")  # Modes: system (default), light, dark
ctk.set_default_color_theme("dark-blue")  # Themes: blue (default), dark-blue, green

app = ctk.CTk()  # create CTk window like you do with the Tk window
app.geometry(str(sizex)+"x"+str(sizey))
app.wm_iconbitmap('C:\\Users\\rvjq_cesar\\tkinter\\src\\img\\tic-tac-toe.ico')
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

buttonvar = [A1,A2,A3,B1,B2,B3,C1,C2,C3]
buttonx, buttony = 0,0

for i in range(len(buttonvar)):
    if i == 3 or i == 6:
        buttonx = 0
        buttony += 100
        pass

    print(buttonvar[i],buttonx,buttony)

    buttonvar[i].place(x=buttonx, y=buttony)
    buttonx += 100

app.mainloop()