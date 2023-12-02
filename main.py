from typing import Optional, Tuple, Union
import customtkinter

class Calulator(customtkinter.CTk):
    def __init__(self):
        super().__init__()
        customtkinter.set_appearance_mode('dark')
        customtkinter.set_default_color_theme("dark-blue")

        self.title("Calculator")
        self.geometry("320x350")
        self.resizable(width=False, height=False)

        frame = customtkinter.CTkFrame(master=self, fg_color="#141414")
        frame.pack(pady=20, padx=60, fill="both", expand=True)


        #entry field
        entry = customtkinter.CTkTextbox(master=frame, width=190, height=40, fg_color="transparent")
        entry.grid(row=0, column=0, columnspan=4, pady=(35, 3))

        #row 1
        button1 = customtkinter.CTkButton(master=frame, width=40, height=40, text="AC", fg_color="#b0b0b0", text_color="black", hover_color="#e0e0de")
        button1.grid(row=1, column=0, padx=5, pady=3)

        button2 = customtkinter.CTkButton(master=frame, width=40, height=40, text="+/-", fg_color="#b0b0b0", text_color="black", hover_color="#e0e0de")
        button2.grid(row=1, column=1, padx=5, pady=3)

        button3 = customtkinter.CTkButton(master=frame, width=40, height=40, text="%", fg_color="#b0b0b0", text_color="black", hover_color="#e0e0de")
        button3.grid(row=1, column=2, padx=5, pady=3)

        button4 = customtkinter.CTkButton(master=frame, width=40, height=40, text="/", fg_color="#c77e10", text_color="white", hover_color="#c48839")
        button4.grid(row=1, column=3, padx=5, pady=3)

        #row2
        button1b = customtkinter.CTkButton(master=frame, width=40, height=40, text="7", fg_color="#292929", text_color="white", hover_color="#6b6b6b")
        button1b.grid(row=2, column=0, padx=5, pady=3)

        button2b = customtkinter.CTkButton(master=frame, width=40, height=40, text="8", fg_color="#292929", text_color="white", hover_color="#6b6b6b")
        button2b.grid(row=2, column=1, padx=5, pady=3)

        button3b = customtkinter.CTkButton(master=frame, width=40, height=40, text="9", fg_color="#292929", text_color="white", hover_color="#6b6b6b")
        button3b.grid(row=2, column=2, padx=5, pady=3)

        button4b = customtkinter.CTkButton(master=frame, width=40, height=40, text="X", fg_color="#c77e10", text_color="white", hover_color="#c48839")
        button4b.grid(row=2, column=3, padx=5, pady=3)

        #row3
        button1c = customtkinter.CTkButton(master=frame, width=40, height=40, text="4", fg_color="#292929", text_color="white", hover_color="#6b6b6b")
        button1c.grid(row=3, column=0, padx=5, pady=3)

        button2c = customtkinter.CTkButton(master=frame, width=40, height=40, text="5", fg_color="#292929", text_color="white", hover_color="#6b6b6b")
        button2c.grid(row=3, column=1, padx=5, pady=3)

        button3c = customtkinter.CTkButton(master=frame, width=40, height=40, text="6", fg_color="#292929", text_color="white", hover_color="#6b6b6b")
        button3c.grid(row=3, column=2, padx=5, pady=3)

        button4c = customtkinter.CTkButton(master=frame, width=40, height=40, text="-", fg_color="#c77e10", text_color="white", hover_color="#c48839")
        button4c.grid(row=3, column=3, padx=5, pady=3)

        #row4
        button1c = customtkinter.CTkButton(master=frame, width=40, height=40, text="1", fg_color="#292929", text_color="white", hover_color="#6b6b6b")
        button1c.grid(row=4, column=0, padx=5, pady=3)

        button2c = customtkinter.CTkButton(master=frame, width=40, height=40, text="2", fg_color="#292929", text_color="white", hover_color="#6b6b6b")
        button2c.grid(row=4, column=1, padx=5, pady=3)

        button3c = customtkinter.CTkButton(master=frame, width=40, height=40, text="3", fg_color="#292929", text_color="white", hover_color="#6b6b6b")
        button3c.grid(row=4, column=2, padx=5, pady=3)

        button4c = customtkinter.CTkButton(master=frame, width=40, height=40, text="+", fg_color="#c77e10", text_color="white", hover_color="#c48839")
        button4c.grid(row=4, column=3, padx=5, pady=3)

        #row4
        button1d = customtkinter.CTkButton(master=frame, width=90, height=40, text="0", fg_color="#292929", text_color="white", hover_color="#6b6b6b")
        button1d.grid(row=5, column=0, columnspan=2, padx=5, pady=3)

        button2d = customtkinter.CTkButton(master=frame, width=40, height=40, text=".", fg_color="#292929", text_color="white", hover_color="#6b6b6b")
        button2d.grid(row=5, column=2, padx=5, pady=3)

        button3d = customtkinter.CTkButton(master=frame, width=40, height=40, text="=", fg_color="#c77e10", text_color="white", hover_color="#c48839")
        button3d.grid(row=5, column=3, padx=5, pady=3)


calculator = Calulator()
calculator.mainloop()