import tkinter as tk
from tkinter import filedialog
import pyttsx3

def convert():
    text = text_entry.get("1.0", tk.END).strip()
    
    if text:
        engine = pyttsx3.init()
        
        output_file = filedialog.asksaveasfilename(defaultextension=".mp3", filetypes=(("MP3 Files", "*.mp3"), ("All Files", "*.*")))
        if output_file:
            engine.save_to_file(text, output_file)
            engine.runAndWait()
            status_label.config(text="Audiobook generated successfully.")
        else:
            status_label.config(text="No output file selected.")
    else:
        status_label.config(text="No text entered.")

 
 

# Create the GUI window
t= tk.Tk()
t.title("Text-to-Audiobook Converter")
t.iconbitmap("python.ico")

text_label=tk.Label(t,text="AUDIO BOOK",bg="green",fg="white",font="Arial 20")
text_label.pack()


# Create and configure the text entry widget
text_entry = tk.Text(t, height=10, width=50)
text_entry.pack(pady=20)



# Create and configure the convert button
convert_button = tk.Button(t, text="Convert to Audiobook", command=convert)
convert_button.pack()


# Create the status label
status_label = tk.Label(t, text="")
status_label.pack()

# Start the GUI event loop
t.mainloop()
