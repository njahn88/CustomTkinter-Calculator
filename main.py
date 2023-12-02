from typing import Optional, Tuple, Union
import customtkinter

class Calulator(customtkinter.CTk):

    def __init__(self):
        super().__init__()
        customtkinter.set_appearance_mode('dark')
        customtkinter.set_default_color_theme("dark-blue")

        lightGrayFgColor = "#b0b0b0"
        lightGrayHoverColor = "#e0e0de"
        darkGrayFgColor = "#292929"
        darkGrayHoverColor = "#6b6b6b"
        orangeFgColor = "#c77e10"
        orangeHoverColor = "#c48839"

        self.title("Calculator")
        self.geometry("320x350")
        self.resizable(width=False, height=False)

        frame = customtkinter.CTkFrame(master=self, fg_color="#141414")
        frame.pack(pady=20, padx=60, fill="both", expand=True)


        #entry field
        entry = customtkinter.CTkTextbox(master=frame, width=190, height=40, fg_color="transparent")
        entry.grid(row=0, column=0, columnspan=4, pady=(35, 3))

        #row 1
        button1 = customtkinter.CTkButton(master=frame, width=40, height=40, text="AC", fg_color=lightGrayFgColor, text_color="black", hover_color=lightGrayHoverColor)
        button1.grid(row=1, column=0, padx=5, pady=3)

        button2 = customtkinter.CTkButton(master=frame, width=40, height=40, text="+/-", fg_color=lightGrayFgColor, text_color="black", hover_color=lightGrayHoverColor)
        button2.grid(row=1, column=1, padx=5, pady=3)

        button3 = customtkinter.CTkButton(master=frame, width=40, height=40, text="%", fg_color=lightGrayFgColor, text_color="black", hover_color=lightGrayHoverColor)
        button3.grid(row=1, column=2, padx=5, pady=3)

        button4 = customtkinter.CTkButton(master=frame, width=40, height=40, text="/", fg_color=orangeFgColor, text_color="white", hover_color=orangeHoverColor)
        button4.grid(row=1, column=3, padx=5, pady=3)

        #row2
        button1b = customtkinter.CTkButton(master=frame, width=40, height=40, text="7", fg_color=darkGrayFgColor, text_color="white", hover_color=darkGrayHoverColor)
        button1b.grid(row=2, column=0, padx=5, pady=3)

        button2b = customtkinter.CTkButton(master=frame, width=40, height=40, text="8", fg_color=darkGrayFgColor, text_color="white", hover_color=darkGrayHoverColor)
        button2b.grid(row=2, column=1, padx=5, pady=3)

        button3b = customtkinter.CTkButton(master=frame, width=40, height=40, text="9", fg_color=darkGrayFgColor, text_color="white", hover_color=darkGrayHoverColor)
        button3b.grid(row=2, column=2, padx=5, pady=3)

        button4b = customtkinter.CTkButton(master=frame, width=40, height=40, text="X", fg_color=orangeFgColor, text_color="white", hover_color=orangeHoverColor)
        button4b.grid(row=2, column=3, padx=5, pady=3)

        #row3
        button1c = customtkinter.CTkButton(master=frame, width=40, height=40, text="4", fg_color=darkGrayFgColor, text_color="white", hover_color=darkGrayHoverColor)
        button1c.grid(row=3, column=0, padx=5, pady=3)

        button2c = customtkinter.CTkButton(master=frame, width=40, height=40, text="5", fg_color=darkGrayFgColor, text_color="white", hover_color=darkGrayHoverColor)
        button2c.grid(row=3, column=1, padx=5, pady=3)

        button3c = customtkinter.CTkButton(master=frame, width=40, height=40, text="6", fg_color=darkGrayFgColor, text_color="white", hover_color=darkGrayHoverColor)
        button3c.grid(row=3, column=2, padx=5, pady=3)

        button4c = customtkinter.CTkButton(master=frame, width=40, height=40, text="-", fg_color=orangeFgColor, text_color="white", hover_color=orangeHoverColor)
        button4c.grid(row=3, column=3, padx=5, pady=3)

        #row4
        button1c = customtkinter.CTkButton(master=frame, width=40, height=40, text="1", fg_color=darkGrayFgColor, text_color="white", hover_color=darkGrayHoverColor)
        button1c.grid(row=4, column=0, padx=5, pady=3)

        button2c = customtkinter.CTkButton(master=frame, width=40, height=40, text="2", fg_color=darkGrayFgColor, text_color="white", hover_color=darkGrayHoverColor)
        button2c.grid(row=4, column=1, padx=5, pady=3)

        button3c = customtkinter.CTkButton(master=frame, width=40, height=40, text="3", fg_color=darkGrayFgColor, text_color="white", hover_color=darkGrayHoverColor)
        button3c.grid(row=4, column=2, padx=5, pady=3)

        button4c = customtkinter.CTkButton(master=frame, width=40, height=40, text="+", fg_color=orangeFgColor, text_color="white", hover_color=orangeHoverColor)
        button4c.grid(row=4, column=3, padx=5, pady=3)

        #row4
        button1d = customtkinter.CTkButton(master=frame, width=90, height=40, text="0", fg_color=darkGrayFgColor, text_color="white", hover_color=darkGrayHoverColor)
        button1d.grid(row=5, column=0, columnspan=2, padx=5, pady=3)

        button2d = customtkinter.CTkButton(master=frame, width=40, height=40, text=".", fg_color=darkGrayFgColor, text_color="white", hover_color=darkGrayHoverColor)
        button2d.grid(row=5, column=2, padx=5, pady=3)

        button3d = customtkinter.CTkButton(master=frame, width=40, height=40, text="=", fg_color=orangeFgColor, text_color="white", hover_color=orangeHoverColor)
        button3d.grid(row=5, column=3, padx=5, pady=3)


calculator = Calulator()
calculator.mainloop()