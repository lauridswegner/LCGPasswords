import tkinter as tk
from tkinter import messagebox
from tkinter import ttk
from implementation.generator import PasswordGenerator

class GUI(tk.Tk):

    def __init__(self):
        super().__init__()
        """ 
        - create frames, labels, checkboxes and entries
        - pack all elements
        """

        self.passgen = PasswordGenerator()

        self.title("LCG-Password-Generator")
        self.geometry("400x350")

        # Title
        title_label = tk.Label(self, text="LCG-Password-Generator")
        title_label.pack(pady=10)

        # Password display
        self.password_var = tk.StringVar()
        self.password_entry = ttk.Entry(self, textvariable=self.password_var, font=("Helvetica", 14), width=30)
        self.password_entry.pack(pady=10)

        # Password length slider
        length_label = tk.Label(self, text="Password Length: 9")
        length_label.pack()
        self.length_var = tk.IntVar(value=9)
        self.length_slider = ttk.Scale(self, from_=4, to_=20, orient=tk.HORIZONTAL, variable=self.length_var)
        self.length_slider.pack(pady=5)

        # Options
        self.letters_var = tk.BooleanVar(value=True)
        self.numbers_var = tk.BooleanVar()
        self.specialChars_var = tk.BooleanVar()

        self.create_checkbutton("Include Letters", self.letters_var).pack(anchor=tk.W)
        self.create_checkbutton("Include Numbers", self.numbers_var).pack(anchor=tk.W)
        self.create_checkbutton("Include Special Characters", self.specialChars_var).pack(anchor=tk.W)

        # Generate button
        generate_button = ttk.Button(self, text="Generate", command=self.generate)
        generate_button.pack(pady=10)

        # Copy button
        copy_button = ttk.Button(self, text="Copy", command=self.copy_password)
        copy_button.pack(pady=5)

        # Apply update-function to slider
        self.length_slider.bind("<Motion>", lambda e: self.update_length_label(length_label))

    def create_checkbutton(self, text, variable):
        return tk.Checkbutton(self, text=text, variable=variable)

    def generate(self):
        length = int(self.length_slider.get())

        if not (self.letters_var.get() or self.numbers_var.get() or self.specialChars_var.get()):
            messagebox.showerror("Error", "Please select at least one character set.")
            return
        
        password = self.passgen.generate_password(password_length=length,
                                                  charsCheck=self.letters_var.get(),
                                                  numbersCheck=self.numbers_var.get(),
                                                  specialCharsCheck=self.specialChars_var.get())

        self.password_var.set(password)

    def copy_password(self):
        self.clipboard_clear()
        self.clipboard_append(self.password_var.get())
        messagebox.showinfo("Copied", "Password copied to clipboard!")

    def update_length_label(self, label):
        label.config(text=f"Password Length: {int(self.length_slider.get())}")

if __name__ == "__main__":
    gui = GUI()
    gui.mainloop()