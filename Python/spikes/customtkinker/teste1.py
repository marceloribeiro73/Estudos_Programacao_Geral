import tkinter
import customtkinter

root_tk = tkinter.Tk()
root_tk.geometry("400x240")
root_tk.title("CustomTinker Test")


def button_function():
    print("Button Pressed")


button = customtkinter.CTkButton(master=root_tk,
                                 corner_radius=10,
                                 command=button_function())
button.place(relx=0.5,
             rely=0.5,
             anchor=tkinter.CENTER)

root_tk.mainloop()
