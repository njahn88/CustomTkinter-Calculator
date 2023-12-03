from typing import Optional, Tuple, Union
import customtkinter

class Calulator(customtkinter.CTk):
    textbox = None
    arithmeticPressed = False
    previousValue = ""
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

        arithmeticType = ""

        buttonFont = ""
        fontSize = 18

        self.title("Calculator")
        self.geometry("320x350")
        self.resizable(width=False, height=False)

        frame = customtkinter.CTkFrame(master=self, fg_color="#141414")
        frame.pack(pady=20, padx=60, fill="both", expand=True)


        #entry field
        entry = customtkinter.CTkTextbox(master=frame, width=190, height=40, fg_color="transparent", font=(buttonFont, 35))
        entry.grid(row=0, column=0, columnspan=4, pady=(20, 3))

        self.textbox = entry

        #row 1
        button1 = customtkinter.CTkButton(master=frame, width=40, height=40, text="AC", fg_color=lightGrayFgColor, text_color="black", hover_color=lightGrayHoverColor, font=(buttonFont, fontSize), command=lambda: self.ClearValue())
        button1.grid(row=1, column=0, padx=5, pady=3)

        button2 = customtkinter.CTkButton(master=frame, width=40, height=40, text="+/-", fg_color=lightGrayFgColor, text_color="black", hover_color=lightGrayHoverColor, font=(buttonFont, fontSize), command=lambda: self.SignChange())
        button2.grid(row=1, column=1, padx=5, pady=3)

        button3 = customtkinter.CTkButton(master=frame, width=40, height=40, text="%", fg_color=lightGrayFgColor, text_color="black", hover_color=lightGrayHoverColor, font=(buttonFont, fontSize), command=lambda: self.Decimal())
        button3.grid(row=1, column=2, padx=5, pady=3)

        button4 = customtkinter.CTkButton(master=frame, width=40, height=40, text="/", fg_color=orangeFgColor, text_color="white", hover_color=orangeHoverColor, font=(buttonFont, fontSize), command=lambda: self.Arithmetic("Divide"))
        button4.grid(row=1, column=3, padx=5, pady=3)

        #row2
        button1b = customtkinter.CTkButton(master=frame, width=40, height=40, text="7", fg_color=darkGrayFgColor, text_color="white", hover_color=darkGrayHoverColor, font=(buttonFont, fontSize), command=lambda: self.WriteNumber(7))
        button1b.grid(row=2, column=0, padx=5, pady=3)

        button2b = customtkinter.CTkButton(master=frame, width=40, height=40, text="8", fg_color=darkGrayFgColor, text_color="white", hover_color=darkGrayHoverColor, font=(buttonFont, fontSize), command=lambda: self.WriteNumber(8))
        button2b.grid(row=2, column=1, padx=5, pady=3)

        button3b = customtkinter.CTkButton(master=frame, width=40, height=40, text="9", fg_color=darkGrayFgColor, text_color="white", hover_color=darkGrayHoverColor, font=(buttonFont, fontSize), command=lambda: self.WriteNumber(9))
        button3b.grid(row=2, column=2, padx=5, pady=3)

        button4b = customtkinter.CTkButton(master=frame, width=40, height=40, text="X", fg_color=orangeFgColor, text_color="white", hover_color=orangeHoverColor, font=(buttonFont, fontSize), command=lambda: self.Arithmetic("Multiply"))
        button4b.grid(row=2, column=3, padx=5, pady=3)

        #row3
        button1c = customtkinter.CTkButton(master=frame, width=40, height=40, text="4", fg_color=darkGrayFgColor, text_color="white", hover_color=darkGrayHoverColor, font=(buttonFont, fontSize), command=lambda: self.WriteNumber(4))
        button1c.grid(row=3, column=0, padx=5, pady=3)

        button2c = customtkinter.CTkButton(master=frame, width=40, height=40, text="5", fg_color=darkGrayFgColor, text_color="white", hover_color=darkGrayHoverColor, font=(buttonFont, fontSize), command=lambda: self.WriteNumber(5))
        button2c.grid(row=3, column=1, padx=5, pady=3)

        button3c = customtkinter.CTkButton(master=frame, width=40, height=40, text="6", fg_color=darkGrayFgColor, text_color="white", hover_color=darkGrayHoverColor, font=(buttonFont, fontSize), command=lambda: self.WriteNumber(6))
        button3c.grid(row=3, column=2, padx=5, pady=3)

        button4c = customtkinter.CTkButton(master=frame, width=40, height=40, text="-", fg_color=orangeFgColor, text_color="white", hover_color=orangeHoverColor, font=(buttonFont, fontSize), command=lambda: self.Arithmetic("Subtract"))
        button4c.grid(row=3, column=3, padx=5, pady=3)

        #row4
        button1c = customtkinter.CTkButton(master=frame, width=40, height=40, text="1", fg_color=darkGrayFgColor, text_color="white", hover_color=darkGrayHoverColor, font=(buttonFont, fontSize), command=lambda: self.WriteNumber(1))
        button1c.grid(row=4, column=0, padx=5, pady=3)

        button2c = customtkinter.CTkButton(master=frame, width=40, height=40, text="2", fg_color=darkGrayFgColor, text_color="white", hover_color=darkGrayHoverColor, font=(buttonFont, fontSize), command=lambda: self.WriteNumber(2))
        button2c.grid(row=4, column=1, padx=5, pady=3)

        button3c = customtkinter.CTkButton(master=frame, width=40, height=40, text="3", fg_color=darkGrayFgColor, text_color="white", hover_color=darkGrayHoverColor, font=(buttonFont, fontSize), command=lambda: self.WriteNumber(3))
        button3c.grid(row=4, column=2, padx=5, pady=3)

        button4c = customtkinter.CTkButton(master=frame, width=40, height=40, text="+", fg_color=orangeFgColor, text_color="white", hover_color=orangeHoverColor, font=(buttonFont, fontSize), command=lambda: self.Arithmetic("Add"))
        button4c.grid(row=4, column=3, padx=5, pady=3)

        #row4
        button1d = customtkinter.CTkButton(master=frame, width=90, height=40, text="0", fg_color=darkGrayFgColor, text_color="white", hover_color=darkGrayHoverColor, font=(buttonFont, fontSize), command=lambda: self.WriteNumber(0))
        button1d.grid(row=5, column=0, columnspan=2, padx=5, pady=3)

        button2d = customtkinter.CTkButton(master=frame, width=40, height=40, text=".", fg_color=darkGrayFgColor, text_color="white", hover_color=darkGrayHoverColor, font=(buttonFont, fontSize), command=lambda: self.WriteNumber("."))
        button2d.grid(row=5, column=2, padx=5, pady=3)

        button3d = customtkinter.CTkButton(master=frame, width=40, height=40, text="=", fg_color=orangeFgColor, text_color="white", hover_color=orangeHoverColor, font=(buttonFont, fontSize), command=lambda: self.Compute())
        button3d.grid(row=5, column=3, padx=5, pady=3)


    def WriteNumber(self, numberToWrite):
        if(numberToWrite == "."):
            if(len(self.textbox.get("0.0", "end")) == 1 or self.HasDecimal()):
                return
        if(self.arithmeticPressed):
            self.ClearValue()
            self.textbox.insert("0.-1", f"{numberToWrite}")
            self.arithmeticPressed = False
            return
        if(len(self.textbox.get("0.0", "end")) == 1):
            self.textbox.insert("0.0", f"{numberToWrite}")
        else:
            tempText = ""
            for char in self.textbox.get("0.0", "end"):
                if(char == "\n"):
                    break
                tempText += char
            tempText += str(numberToWrite)
            self.ClearValue()
            self.textbox.insert("0.0", f"{tempText}")

    def HasDecimal(self):
        indexCount = 0
        for char in self.textbox.get("0.0", "end"):
            if(char == "." and indexCount != 0):
                return True
            indexCount += 1
        return False

    def ClearValue(self):
        self.textbox.delete("0.0", "end")

    def Arithmetic(self, arithmeticType):
        self.arithmeticPressed = True
        self.arithmeticType = arithmeticType
        try:
            self.previousValue = float(self.textbox.get("0.0", "end"))
        except:
            return

    def Decimal(self):
        try:
            self.previousValue = float(self.textbox.get("0.0", "end"))
            answerToWrite = self.previousValue / 100
        except:
            self.ClearValue()
            self.arithmeticPressed = True
            return
        self.ClearValue()
        self.WriteNumber(answerToWrite)
        self.arithmeticPressed = True

    def SignChange(self):
        try:
            self.previousValue = float(self.textbox.get("0.0", "end"))
            answerToWrite = -self.previousValue
        except:
            self.ClearValue()
            self.arithmeticPressed = True
            return
        self.ClearValue()
        self.WriteNumber(answerToWrite)
        self.arithmeticPressed = True

    def Compute(self):
        if(self.previousValue == ""):
            return
        if(self.arithmeticType == "Add"):
            answerToWrite = self.previousValue + float(self.textbox.get("0.0", "end"))
        elif(self.arithmeticType == "Subtract"):
            answerToWrite = self.previousValue - float(self.textbox.get("0.0", "end"))
        elif(self.arithmeticType == "Multiply"):
            answerToWrite = self.previousValue * float(self.textbox.get("0.0", "end"))
        elif(self.arithmeticType == "Divide"):
            answerToWrite = self.previousValue / float(self.textbox.get("0.0", "end"))
        self.ClearValue()
        self.WriteNumber(round(answerToWrite, 5))
        self.arithmeticPressed = True


calculator = Calulator()
calculator.mainloop()