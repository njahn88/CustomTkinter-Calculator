import customtkinter

customtkinter.set_appearance_mode('dark')
customtkinter.set_default_color_theme("dark-blue")

root = customtkinter.CTk()
root.geometry("500x350")

frame = customtkinter.CTkFrame(master=root, fg_color="#141414")
frame.pack(pady=20, padx=60, fill="both", expand=True)
frame.columnconfigure((0, 1, 2, 3), weight=1)

#row 1
button1 = customtkinter.CTkButton(master=frame, width=40, height=40, corner_radius=20, text="AC", fg_color="#b0b0b0", text_color="black", hover_color="#e0e0de")
button1.grid(row=0, column=0, padx=20)

button2 = customtkinter.CTkButton(master=frame, width=40, height=40, corner_radius=20, text="+/-", fg_color="#b0b0b0", text_color="black", hover_color="#e0e0de")
button2.grid(row=0, column=1, padx=20)

button3 = customtkinter.CTkButton(master=frame, width=40, height=40, corner_radius=20, text="%", fg_color="#b0b0b0", text_color="black", hover_color="#e0e0de")
button3.grid(row=0, column=2, padx=20)

button4 = customtkinter.CTkButton(master=frame, width=40, height=40, corner_radius=20, text="/", fg_color="#c77e10", text_color="white", hover_color="#c48839")
button4.grid(row=0, column=3, padx=20)

#row2
button1b = customtkinter.CTkButton(master=frame, width=40, height=40, corner_radius=20, text="7", fg_color="#292929", text_color="black", hover_color="#6b6b6b")
button1b.grid(row=1, column=0, padx=20)

button2b = customtkinter.CTkButton(master=frame, width=40, height=40, corner_radius=20, text="8", fg_color="#292929", text_color="black", hover_color="#6b6b6b")
button2b.grid(row=1, column=1, padx=20)

button3b = customtkinter.CTkButton(master=frame, width=40, height=40, corner_radius=20, text="9", fg_color="#292929", text_color="black", hover_color="#6b6b6b")
button3b.grid(row=1, column=2, padx=20)

button4b = customtkinter.CTkButton(master=frame, width=40, height=40, corner_radius=20, text="X", fg_color="#c77e10", text_color="white", hover_color="#c48839")
button4b.grid(row=1, column=3, padx=20)


root.mainloop()